from .testutils import VerminTest, detect, current_version, current_major_version, visit, Parser

class VerminLanguageTests(VerminTest):
  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn((2, 0), detect("print 'hello'"))

    source = "print 'hello'"
    parser = Parser(source)
    (node, mins, novermin) = parser.detect()
    v = current_version()
    if v >= 3.4:
      self.assertEqual(node, None)
      self.assertOnlyIn((2, 0), mins)
    elif v >= 3.0 and v < 3.4:
      self.assertEqual(node, None)
      self.assertEqual(mins, [(0, 0), (0, 0)])
    else:  # < 3.0
      visitor = visit(source)
      self.assertTrue(visitor.printv2())
      self.assertEqual([(2, 0), (0, 0)], visitor.minimum_versions())

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    visitor = visit("print('hello')")
    if current_version() < 3.0:
      self.assertTrue(visitor.printv2())
      self.assertFalse(visitor.printv3())
    else:
      self.assertFalse(visitor.printv2())
      self.assertTrue(visitor.printv3())
    self.assertIn((current_major_version(), 0), visitor.minimum_versions())

  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn((2, 0), detect("print 'hello'\nprint('hello')"))

  def test_format(self):
    visitor = visit("'hello {}!'.format('world')")
    self.assertTrue(visitor.format27())
    self.assertOnlyIn(((2, 7), (3, 0)), visitor.minimum_versions())

    # Ensure regular str formatting is ~2, ~3.
    visitor = visit("'%x' % 66")
    self.assertFalse(visitor.format27())
    self.assertFalse(visitor.bytesv3())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_longv2(self):
    visitor = visit("v = long(42)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

    visitor = visit("isinstance(42, long)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

  def test_bytesv3(self):
    v = current_version()

    # py2: type(b'hello') = <type 'str'>
    if v >= 2.0 and v < 3.0:
      visitor = visit("s = b'hello'")
      self.assertFalse(visitor.bytesv3())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # py3: type(b'hello') = <type 'bytes'>
    elif v >= 3.0:
      visitor = visit("s = b'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())
      visitor = visit("s = B'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_fstrings(self):
    if current_version() >= 3.6:
      visitor = visit("name = 'world'\nf'hello {name}'")
      self.assertTrue(visitor.fstrings())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_fstrings_self_doc(self):
    if current_version() >= 3.8:
      visitor = visit("name = 'world'\nf'hello {name=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_coroutines_async(self):
    if current_version() >= 3.5:
      visitor = visit("async def func():\n\tpass")
      self.assertTrue(visitor.coroutines())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_coroutines_await(self):
    if current_version() >= 3.5:
      visitor = visit("async def func():\n\tawait something()")
      self.assertTrue(visitor.coroutines())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_async_generator(self):
    if current_version() >= 3.6:
      visitor = visit("async def func():\n"
                      "  yield 42\n"
                      "  await something()")
      self.assertTrue(visitor.async_generator())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

      visitor = visit("async def func():\n"
                      "  yield 42\n"
                      "  async def func2():\n"
                      "    await other()")
      self.assertFalse(visitor.async_generator())

    # 3.7 = await in comprehension.
    if current_version() >= 3.7:
      visitor = visit("async def func():\n"
                      "  yield 42\n"
                      "  d = [v for v in await other()]")
      self.assertFalse(visitor.async_generator())
      self.assertTrue(visitor.await_in_comprehension())

  def test_async_comprehension(self):
    if current_version() >= 3.7:
      self.assertOnlyIn((3, 7), detect("[i async for i in aiter() if i % 2]"))

  def test_await_in_comprehension(self):
    if current_version() >= 3.7:
      visitor = visit("[await fun() for fun in funcs if await condition()]")
      self.assertTrue(visitor.await_in_comprehension())
      self.assertOnlyIn((3, 7), visitor.minimum_versions())

  def test_continue_in_finally(self):
    if current_version() >= 3.8:
      visitor = visit("try: pass\nfinally: continue")
      self.assertTrue(visitor.continue_in_finally())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit("for i in range(3):\n"
                      "  try:\n"
                      "    pass\n"
                      "  finally:\n"
                      "    continue")
      self.assertTrue(visitor.continue_in_finally())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit("for i in range(3):\n"
                      "  try:\n"
                      "    pass\n"
                      "  finally:\n"
                      "    for j in []:\n"
                      "      continue")  # Skip due to inline for-loop.
      self.assertFalse(visitor.continue_in_finally())

      visitor = visit("for i in range(3):\n"
                      "  try:\n"
                      "    pass\n"
                      "  finally:\n"
                      "    while i < 2:\n"
                      "      continue")  # Skip due to inline while-loop.
      self.assertFalse(visitor.continue_in_finally())

      visitor = visit("for i in range(3):\n"
                      "  try:\n"
                      "    pass\n"
                      "  finally:\n"
                      "    for j in []:\n"
                      "      continue\n"  # Skip due to inline for-loop.
                      "    while i < 2:\n"
                      "      continue\n"  # Skip due to inline while-loop.
                      "    continue")  # Accept this one.
      self.assertTrue(visitor.continue_in_finally())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_named_expressions(self):
    if current_version() >= 3.8:
      visitor = visit("a = 1\nif (b := a) == 1:\n\tprint(b)")
      self.assertTrue(visitor.named_expressions())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_kw_only_args(self):
    if current_version() >= 3.0:
      visitor = visit("def foo(a, *, b): return a + b")
      self.assertTrue(visitor.kw_only_args())
      self.assertOnlyIn((3, 0), visitor.minimum_versions())

  def test_pos_only_args(self):
    if current_version() >= 3.8:
      visitor = visit("def foo(a, /, b): return a + b")
      self.assertTrue(visitor.pos_only_args())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_yield_from(self):
    if current_version() >= 3.3:
      visitor = visit("def foo(x): yield from range(x)")
      self.assertTrue(visitor.yield_from())
      self.assertOnlyIn((3, 3), visitor.minimum_versions())

  def test_raise_cause(self):
    if current_version() >= 3.3:
      visitor = visit("raise Exception() from None")
      self.assertTrue(visitor.raise_cause())
      self.assertOnlyIn((3, 3), visitor.minimum_versions())

  def test_dict_comprehension(self):
    visitor = visit("{key: value for ld in lod for key, value in ld.items()}")
    self.assertTrue(visitor.dict_comprehension())
    self.assertEqual([(2, 7), (3, 0)], visitor.minimum_versions())

  def test_infix_matrix_multiplication(self):
    if current_version() >= 3.5:
      visitor = visit("M @ N")
      self.assertTrue(visitor.infix_matrix_multiplication())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_str_from_type(self):
    visitor = visit("\"\".zfill(1)")
    self.assertIn("str.zfill", visitor.members())
    visitor = visit("str().zfill(1)")
    self.assertIn("str.zfill", visitor.members())

  def test_unicode_from_type(self):
    if current_version() < 3.0:
      visitor = visit("u\"\".isdecimal()")
      self.assertIn("unicode.isdecimal", visitor.members())
      visitor = visit("unicode().isdecimal()")
      self.assertIn("unicode.isdecimal", visitor.members())

  def test_list_from_type(self):
    visitor = visit("[].clear()")
    self.assertIn("list.clear", visitor.members())
    visitor = visit("list().clear()")
    self.assertIn("list.clear", visitor.members())

  def test_dict_from_type(self):
    visitor = visit("{}.pop()")
    self.assertIn("dict.pop", visitor.members())
    visitor = visit("dict().pop()")
    self.assertIn("dict.pop", visitor.members())

  def test_set_from_type(self):
    visitor = visit("{1}.isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())
    visitor = visit("set().isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())

  def test_frozenset_from_type(self):
    visitor = visit("frozenset().isdisjoint()")
    self.assertIn("frozenset.isdisjoint", visitor.members())

  def test_int_from_type(self):
    visitor = visit("(1).bit_length()")
    self.assertIn("int.bit_length", visitor.members())
    visitor = visit("int().bit_length()")
    self.assertIn("int.bit_length", visitor.members())

  def test_long_from_type(self):
    if current_version() < 3.0:
      visitor = visit("(1L).bit_length()")
      self.assertIn("long.bit_length", visitor.members())
      visitor = visit("long().bit_length()")
      self.assertIn("long.bit_length", visitor.members())

  def test_float_from_type(self):
    visitor = visit("(4.2).hex()")
    self.assertIn("float.hex", visitor.members())
    visitor = visit("float().hex()")
    self.assertIn("float.hex", visitor.members())

  def test_bytes_from_type(self):
    if current_version() >= 3.0:
      visitor = visit("b'hello'.hex()")
      self.assertIn("bytes.hex", visitor.members())
      visitor = visit("bytes().hex()")
      self.assertIn("bytes.hex", visitor.members())

  def test_with_statement(self):
      visitor = visit("with func():\n  pass")
      self.assertTrue(visitor.with_statement())
      self.assertOnlyIn([(2, 5), (3, 0)], visitor.minimum_versions())

  def test_generalized_unpacking(self):
    if current_version() >= 3.0:
      visitor = visit("(*range(4), 4)")  # tuple
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*range(4), 4]")  # list
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

    if current_version() >= 3.5:
      visitor = visit("{*range(4), 4}")  # set
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{'x': 1, **{'y': 2}}")  # dict
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("function(*arguments, argument)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("function(**kw_arguments, **more_arguments)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("function(**{'x': 42}, arg=84)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_bytes_format(self):
    if current_version() >= 3.5:
      visitor = visit("b'%x' % 10")
      self.assertTrue(visitor.bytes_format())
      self.assertOnlyIn(((2, 6), (3, 5)), visitor.minimum_versions())

  def test_bytearray_format(self):
    if current_version() >= 3.5:
      visitor = visit("bytearray(b'%x') % 10")
      self.assertTrue(visitor.bytearray_format())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_bytes_directives(self):
    if current_version() >= 3.0:
      visitor = visit("b'%b %x'")
      self.assertOnlyIn(("b", "x"), visitor.bytes_directives())
      visitor = visit("b'%4b'")
      self.assertOnlyIn(("b",), visitor.bytes_directives())
      visitor = visit("b'%4b'")
      self.assertOnlyIn(("b",), visitor.bytes_directives())
      visitor = visit("b'%#4b'")
      self.assertOnlyIn(("b",), visitor.bytes_directives())
      visitor = visit("b'%04b'")
      self.assertOnlyIn(("b",), visitor.bytes_directives())
      visitor = visit("b'%.4f'")
      self.assertOnlyIn(("f",), visitor.bytes_directives())
      visitor = visit("b'%-4f'")
      self.assertOnlyIn(("f",), visitor.bytes_directives())
      visitor = visit("b'%  f'")
      self.assertOnlyIn(("f",), visitor.bytes_directives())
      visitor = visit("b'%+f'")
      self.assertOnlyIn(("f",), visitor.bytes_directives())
