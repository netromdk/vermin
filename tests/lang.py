from vermin import BUILTIN_GENERIC_ANNOTATION_TYPES, DICT_UNION_SUPPORTED_TYPES,\
  DICT_UNION_MERGE_SUPPORTED_TYPES, dotted_name, Parser

from .testutils import VerminTest, current_version

class VerminLanguageTests(VerminTest):
  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= (3, 4):
      self.assertOnlyIn((2, 0), self.detect("print 'hello'"))

    source = "print 'hello'"
    parser = Parser(source)
    (node, mins, _novermin) = parser.detect(self.config)
    v = current_version()
    if v >= (3, 4):
      self.assertEqual(node, None)
      self.assertOnlyIn((2, 0), mins)
    elif (3, 0) <= v < (3, 4):  # pragma: no cover
      self.assertEqual(node, None)
      self.assertEqual(mins, [(0, 0), (0, 0)])
    # < 3.0
    else:  # pragma: no cover
      visitor = self.visit(source)
      self.assertTrue(visitor.printv2())
      self.assertEqual([(2, 0), (0, 0)], visitor.minimum_versions())

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    visitor = self.visit("print('hello')")
    v = current_version()
    if v < (3, 0):  # pragma: no cover
      self.assertTrue(visitor.printv2())
      self.assertFalse(visitor.printv3())
    else:
      self.assertFalse(visitor.printv2())
      self.assertTrue(visitor.printv3())
    self.assertIn((v.major, 0), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 4)
  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    self.assertOnlyIn((2, 0), self.detect("print 'hello'\nprint('hello')"))

  def test_format(self):
    visitor = self.visit("'hello {}!'.format('world')")
    self.assertTrue(visitor.format27())
    self.assertOnlyIn(((2, 7), (3, 0)), visitor.minimum_versions())

    # Ensure regular str formatting is ~2, ~3.
    visitor = self.visit("'%x' % 66")
    self.assertFalse(visitor.format27())
    self.assertFalse(visitor.bytesv3())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_longv2(self):
    visitor = self.visit("v = long(42)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

    visitor = self.visit("v = 1\nv += long(42)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

    visitor = self.visit("isinstance(42, long)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

  def test_bytesv3(self):
    v = current_version()

    # py2: type(b'hello') = <type 'str'>
    if (2, 0) <= v < (3, 0):  # pragma: no cover
      visitor = self.visit("s = b'hello'")
      self.assertFalse(visitor.bytesv3())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # py3: type(b'hello') = <type 'bytes'>
    elif v >= (3, 0):
      visitor = self.visit("s = b'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())
      visitor = self.visit("s = B'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_fstrings(self):
    visitor = self.visit("name = 'world'\nf'hello {name}'")
    self.assertTrue(visitor.fstrings())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

    visitor = self.visit("f'{f\"{3.1415:.1f}\":*^20}'")
    self.assertTrue(visitor.fstrings())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

    visitor = self.visit("f'''{\n3\n}'''")
    self.assertTrue(visitor.fstrings())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_fstrings_named_expr(self):
    if current_version() >= (3, 8):
      visitor = self.visit("f'{(x:=1)}'")
      self.assertTrue(visitor.fstrings())
      self.assertTrue(visitor.named_expressions())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

    if current_version() >= (3, 6):
      visitor = self.visit("f'{x:=10}'")
      self.assertTrue(visitor.fstrings())
      self.assertFalse(visitor.named_expressions())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 8)
  def test_fstrings_self_doc(self):
    enabled = False
    if enabled:  # pragma: no cover
      self.config.enable_feature("fstring-self-doc")

      # NOTE: The built-in AST cannot distinguish `f'{a=}'` from `f'a={a}'` because it optimizes
      # some information away. Therefore, this test will be seen as a self-doc f-string, which is
      # why fstring self-doc detection has been disabled for now.
      visitor = self.visit("a = 1\nf'a={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("name = 'world'\nf'hello {name=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("name = 'world'\nf'hello={name}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("a = 1\nf'={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("a = 1\nf'{a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("a = 1\nb = 2\nf'={b}={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("a = 1\nb = 2\nf'{b=}={a}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a =}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a= }'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ a = }'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{1+1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{1+b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a+b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a+1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a-1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a/1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a//1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a*1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{not a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{1 in []=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{1 not in []=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{None is None=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{None is not True=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{10 % 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{10 ^ 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{10 | 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{10 & 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{10 ** 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{-5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{+5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{~5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x << y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x >> y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x @ y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a or b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{a and b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{(1,2,3)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{[1,2,3]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ {1,2,3}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ {1:1, 2:2}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{[x for x in [1,2,3]]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{(x for x in [1,2,3])=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ {x for x in [1,2,3]}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{ {x:1 for x in [1,2,3]}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0==1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0<1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0>1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0<=1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0>=1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{0==1!=2=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{3.14=:10.10}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{3.14=!s:10.10}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x=!s}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x=!r}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x=!a}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x=:.2f}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{x=!a:^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{f\"{3.1415=:.1f}\":*^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'alpha a {pi=} w omega'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'''{\n3\n=}'''")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{f(a=4)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{f(a=\"3=\")=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{C()=!r:*^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{user=!s}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{delta.days=:,d}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{user=!s}  {delta.days=:,d}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{delta.days:,d}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("f'{cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("f'{cos(radians(theta))=:.3f}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'={cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("f'{theta}  {cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = self.visit("f'{cos(radians(theta)):.3f} {theta=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{(a+b)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{(a+((b-(c*d))/e))=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{d[\"foo\"]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'i:{i=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{1 if True else 2=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'{(d[a], None) if 42 != 84 else (1,2,3)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("f'expr={ {x: y for x, y in [(1, 2) ]} = }'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_coroutines_async(self):
    visitor = self.visit("async def func():\n\tpass")
    self.assertTrue(visitor.coroutines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_coroutines_await(self):
    visitor = self.visit("async def func():\n\tawait something()")
    self.assertTrue(visitor.coroutines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_async_generator(self):
    if current_version() >= (3, 6):
      visitor = self.visit("async def func():\n"
                           "  yield 42\n"
                           "  await something()")
      self.assertTrue(visitor.async_generator())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

      visitor = self.visit("async def func():\n"
                           "  yield 42\n"
                           "  async def func2():\n"
                           "    await other()")
      self.assertFalse(visitor.async_generator())

    # 3.7 = await in comprehension.
    if current_version() >= (3, 7):
      visitor = self.visit("async def func():\n"
                           "  yield 42\n"
                           "  d = [v for v in await other()]")
      self.assertFalse(visitor.async_generator())
      self.assertTrue(visitor.await_in_comprehension())

  @VerminTest.skipUnlessVersion(3, 7)
  def test_async_comprehension(self):
    self.assertOnlyIn((3, 7), self.detect("[i async for i in aiter() if i % 2]"))

  @VerminTest.skipUnlessVersion(3, 7)
  def test_await_in_comprehension(self):
    visitor = self.visit("[await fun() for fun in funcs if await condition()]")
    self.assertTrue(visitor.await_in_comprehension())
    self.assertOnlyIn((3, 7), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_async_for(self):
    self.assertOnlyIn((3, 6), self.detect("async def foo():\n\tasync for a in []:pass"))

  @VerminTest.skipUnlessVersion(3, 8)
  def test_continue_in_finally(self):
    visitor = self.visit("try: pass\nfinally: continue")
    self.assertTrue(visitor.continue_in_finally())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

    visitor = self.visit("for i in range(3):\n"
                         "  try:\n"
                         "    pass\n"
                         "  finally:\n"
                         "    continue")
    self.assertTrue(visitor.continue_in_finally())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

    visitor = self.visit("for i in range(3):\n"
                         "  try:\n"
                         "    pass\n"
                         "  finally:\n"
                         "    for j in []:\n"
                         "      continue")  # Skip due to inline for-loop.
    self.assertFalse(visitor.continue_in_finally())

    visitor = self.visit("for i in range(3):\n"
                         "  try:\n"
                         "    pass\n"
                         "  finally:\n"
                         "    while i < 2:\n"
                         "      continue")  # Skip due to inline while-loop.
    self.assertFalse(visitor.continue_in_finally())

    visitor = self.visit("for i in range(3):\n"
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

  @VerminTest.skipUnlessVersion(3, 8)
  def test_named_expressions(self):
    visitor = self.visit("a = 1\nif (b := a) == 1:\n\tprint(b)")
    self.assertTrue(visitor.named_expressions())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3)
  def test_kw_only_args(self):
    visitor = self.visit("def foo(a, *, b): return a + b")
    self.assertTrue(visitor.kw_only_args())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 8)
  def test_pos_only_args(self):
    visitor = self.visit("def foo(a, /, b): return a + b")
    self.assertTrue(visitor.pos_only_args())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 3)
  def test_yield_from(self):
    visitor = self.visit("def foo(x): yield from range(x)")
    self.assertTrue(visitor.yield_from())
    self.assertOnlyIn((3, 3), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 0)
  def test_raise_cause(self):
    visitor = self.visit("raise Exception() from ValueError")
    self.assertTrue(visitor.raise_cause())
    self.assertFalse(visitor.raise_from_none())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 3)
  def test_raise_from_none(self):
    visitor = self.visit("raise Exception() from None")
    self.assertTrue(visitor.raise_cause())
    self.assertTrue(visitor.raise_from_none())
    self.assertOnlyIn((3, 3), visitor.minimum_versions())

  def test_dict_comprehension(self):
    visitor = self.visit("{key: value for ld in lod for key, value in ld.items()}")
    self.assertTrue(visitor.dict_comprehension())
    self.assertEqual([(2, 7), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_infix_matrix_multiplication(self):
    visitor = self.visit("M @ N")
    self.assertTrue(visitor.infix_matrix_multiplication())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_str_from_type(self):
    visitor = self.visit("\"\".zfill(1)")
    self.assertIn("str.zfill", visitor.members())
    visitor = self.visit("str().zfill(1)")
    self.assertIn("str.zfill", visitor.members())

  # pragma: no cover
  @VerminTest.skipUnlessLowerVersion(3)
  def test_unicode_from_type(self):
    visitor = self.visit("u\"\".isdecimal()")
    self.assertIn("unicode.isdecimal", visitor.members())
    visitor = self.visit("unicode().isdecimal()")
    self.assertIn("unicode.isdecimal", visitor.members())

  def test_list_from_type(self):
    visitor = self.visit("[].clear()")
    self.assertIn("list.clear", visitor.members())
    visitor = self.visit("list().clear()")
    self.assertIn("list.clear", visitor.members())

  def test_dict_from_type(self):
    visitor = self.visit("{}.pop()")
    self.assertIn("dict.pop", visitor.members())
    visitor = self.visit("dict().pop()")
    self.assertIn("dict.pop", visitor.members())

  def test_set_from_type(self):
    visitor = self.visit("{1}.isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())
    visitor = self.visit("set().isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())

  def test_frozenset_from_type(self):
    visitor = self.visit("frozenset().isdisjoint()")
    self.assertIn("frozenset.isdisjoint", visitor.members())

  def test_int_from_type(self):
    visitor = self.visit("(1).bit_length()")
    self.assertIn("int.bit_length", visitor.members())
    visitor = self.visit("int().bit_length()")
    self.assertIn("int.bit_length", visitor.members())

  # pragma: no cover
  @VerminTest.skipUnlessLowerVersion(3)
  def test_long_from_type(self):
    visitor = self.visit("(1L).bit_length()")
    self.assertIn("long.bit_length", visitor.members())
    visitor = self.visit("long().bit_length()")
    self.assertIn("long.bit_length", visitor.members())

  def test_float_from_type(self):
    visitor = self.visit("(4.2).hex()")
    self.assertIn("float.hex", visitor.members())
    visitor = self.visit("float().hex()")
    self.assertIn("float.hex", visitor.members())

  @VerminTest.skipUnlessVersion(3)
  def test_bytes_from_type(self):
    visitor = self.visit("b'hello'.hex()")
    self.assertIn("bytes.hex", visitor.members())
    visitor = self.visit("bytes().hex()")
    self.assertIn("bytes.hex", visitor.members())

  def test_with_statement(self):
    visitor = self.visit("with func():\n  pass")
    self.assertTrue(visitor.with_statement())
    self.assertOnlyIn([(2, 5), (3, 0)], visitor.minimum_versions())

  def test_generalized_unpacking(self):
    if current_version() >= (3, 5):
      visitor = self.visit("(*range(4), 4)")  # tuple
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(4, *range(4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(*range(4),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(*(1,),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(*(1, 2),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(0, *(1, 2))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(*(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(0, *(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("(*(1, 2), *(3, 4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*range(4), 4]")  # list
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[4, *range(4)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*range(4)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*[1]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*[1, 2]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[0, *[1, 2]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*[1, 2], 3]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[0, *[1, 2], 3]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*[1, 2], *[3, 4]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*range(4), 4}")  # set
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{4, *range(4)}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*range(4)}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*{1}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*{1, 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{0, *{1, 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*{1, 2}, 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{0, *{1, 2}, 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{*{1, 2}, *{3, 4}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{'x': 1, **{'y': 2}}")  # dict
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{**{'y': 2}, 'x': 1}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{**{1: 1}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{**{1: 1, 2: 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{0: 0, **{1: 1, 2: 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{**{1: 1, 2: 2}, 3: 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{0: 0, **{1: 1, 2: 2}, 3: 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("{**{1: 1, 2: 2}, **{3: 3, 4: 4}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("[*{1,2,3}, *(1,2,3), *[1,2,3], *range(3)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("print(*(1,))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = self.visit("print(*(1, 2))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = self.visit("print(0, *(1, 2))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = self.visit("print(*(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("print(0, *(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("print(*(1, 2), *(3, 4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("dict(**{'b': 1, 'c': 2}, d=3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("dict(a=0, **{'b': 1, 'c': 2}, d=3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("dict(**{'b': 1, 'c': 2}, **{'d': 3, 'e': 4})")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("foo(0, *(1, 2), 3, a=1, **{'b': 2, 'c': 3})")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("foo(0, *(1, 2), a=1, **{'b': 2, 'c': 3}, d=4)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("function(*arguments, argument)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("function(**kw_arguments, **more_arguments)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("function(**{'x': 42}, arg=84)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("z = *x, y")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = self.visit("*x, y = *u, *v")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

    visitor = self.visit("dict(**{'b': 1})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = self.visit("dict(**{'b': 1, 'c': 2})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = self.visit("dict(a=0, **{'b': 1, 'c': 2})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = self.visit("foo(0, *(1, 2), a=1, **{'b': 2, 'c': 3})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = self.visit("function(arg=84, **{'x': 42})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = self.visit("d = {'a': 'b'}\ndict(**d)")
    self.assertFalse(visitor.generalized_unpacking())

  @VerminTest.skipUnlessVersion(3)
  @VerminTest.parameterized_args([
    ["*x, y = [1, 2, 3]"],
    ["a, *b = 'hello'"],
    ["([x, *y], z) = ((1, 2), 3)"],
    ["for *x, in [[1]]: pass"],
    ["for a, *b in [(1, 2, 3), (4, 5, 6, 7)]: pass"],
    ["[x for *x, in [[1]]]"],
    ["{x for *x, in [[1]]}"],
    ["(x for *x, in [[1]])"],
  ])
  def test_unpacking_assignment(self, source):
    # Starred expressions are allowed as assignments targets 3.0+, but generalized unpacking from
    # 3.5+.
    visitor = self.visit(source)
    self.assertTrue(visitor.unpacking_assignment(), msg=source)
    self.assertFalse(visitor.generalized_unpacking(), msg=source)
    self.assertOnlyIn((3, 0), visitor.minimum_versions(), msg=source)

  @VerminTest.skipUnlessVersion(3, 5)
  def test_bytes_format(self):
    visitor = self.visit("b'%x' % 10")
    self.assertTrue(visitor.bytes_format())
    self.assertOnlyIn(((2, 6), (3, 5)), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_bytearray_format(self):
    visitor = self.visit("bytearray(b'%x') % 10")
    self.assertTrue(visitor.bytearray_format())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3)
  def test_bytes_directives(self):
    visitor = self.visit("b'%b %x'")
    self.assertOnlyIn(("b", "x"), visitor.bytes_directives())
    visitor = self.visit("b'%4b'")
    self.assertOnlyIn(("b",), visitor.bytes_directives())
    visitor = self.visit("b'%4b'")
    self.assertOnlyIn(("b",), visitor.bytes_directives())
    visitor = self.visit("b'%#4b'")
    self.assertOnlyIn(("b",), visitor.bytes_directives())
    visitor = self.visit("b'%04b'")
    self.assertOnlyIn(("b",), visitor.bytes_directives())
    visitor = self.visit("b'%.4f'")
    self.assertOnlyIn(("f",), visitor.bytes_directives())
    visitor = self.visit("b'%-4f'")
    self.assertOnlyIn(("f",), visitor.bytes_directives())
    visitor = self.visit("b'%  f'")
    self.assertOnlyIn(("f",), visitor.bytes_directives())
    visitor = self.visit("b'%+f'")
    self.assertOnlyIn(("f",), visitor.bytes_directives())

  def test_detect_raise_members(self):
    visitor = self.visit("raise ModuleNotFoundError")
    self.assertOnlyIn("ModuleNotFoundError", visitor.members())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_detect_except_members(self):
    visitor = self.visit("try: pass\nexcept ModuleNotFoundError: pass")
    self.assertOnlyIn("ModuleNotFoundError", visitor.members())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_dict_union(self):
    visitor = self.visit("{'a':1} | {'b':2}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {'a':1}\nb = {'b':2}\na | b")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {'a':1}\na | {'b':2}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {'a':1}\n{'b':2} | a")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("dict() | dict()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = dict()\nb = dict()\na | b")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = dict()\na | dict()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = dict()\ndict() | a")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("{} | dict() | {}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("(lambda: {})() | {}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("(lambda: {} | dict())()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("{} | (1,{},'a')[1]")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("{} | (1,{},'a')[0]")
    self.assertFalse(visitor.dict_union())
    visitor = self.visit("{} | [1,{},'a'][1]")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("[1,(lambda:{1:2})(),3][1] | {2:3}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    # Builtin types were modified to support "|".
    visitor = self.visit("from types import MappingProxyType\nm=MappingProxyType({})\nm|{}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from types import MappingProxyType\nm=MappingProxyType({})\n{}|m")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from types import MappingProxyType\nMappingProxyType({})|{}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from types import MappingProxyType\n{}|MappingProxyType({})")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from types import MappingProxyType as MPT\nMPT({})|{}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from types import MappingProxyType as MPT\n{}|MPT({})")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    for typ in DICT_UNION_SUPPORTED_TYPES:
      names = typ.split(".")
      src = "from {} import {} as X\nX() | dict()".format(dotted_name(names[:-1]), names[-1])
      visitor = self.visit(src)
      self.assertTrue(visitor.dict_union(), msg=src)
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_dict_union_merge(self):
    visitor = self.visit("a = {'a':1}\na |= {'b':2}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {'a':1}\nb = {'b':2}\na |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = dict()\na |= dict()")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = dict()\nb = dict()\na |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {}\nfor b in ({}, {}, {}):\n\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {}\nfor b in [{}, {}, {}]:\n\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {}\nb = {}\nfor c in (b,):\n\ta |= c")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = {}\na |= (lambda:{})()")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("a = 1\nfor a in [{}]:\n\tfor b in ({},):\n\t\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    # Builtin types were modified to also support "|=".
    visitor = self.visit("from os import environ\nos.environ |= {'var':'val'}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from os import environ\ne=os.environ\ne |= {}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = self.visit("from os import environ as e\ne |= {}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    for typ in DICT_UNION_MERGE_SUPPORTED_TYPES:
      names = typ.split(".")
      src = "from {} import {} as X\nx = X()\nx |= dict()".\
        format(dotted_name(names[:-1]), names[-1])
      visitor = self.visit(src)
      self.assertTrue(visitor.dict_union_merge(), msg=src)
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_builtin_generic_type_annotation(self):
    # For each type, either use directly if builtin or import and then use. And the fully-qualified
    # variant.
    # Examples:
    # -  from re import Match
    #    Match[str]
    # -  import re
    #    re.Match[str]
    # -  tuple[str]
    for typ in BUILTIN_GENERIC_ANNOTATION_TYPES:
      names = [typ]
      src = ""
      if "." in typ:
        names = typ.split(".")
        src = "from {} import {}\n".format(dotted_name(names[:-1]), names[-1])
      src += "{}[str]".format(names[-1])
      visitor = self.visit(src)
      self.assertTrue(visitor.builtin_generic_type_annotations(), msg=src)
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      if len(names) > 1:
        src = "import {}\n{}[str]".format(dotted_name(names[:-1]), dotted_name(names))
        visitor = self.visit(src)
        self.assertTrue(visitor.builtin_generic_type_annotations(), msg=src)
        self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("class A: pass\nA[str]")
    self.assertFalse(visitor.builtin_generic_type_annotations())

    # Ignore user-defined types that clash with builtin types.
    visitor = self.visit("class dict: pass\ndict[str]")
    self.assertFalse(visitor.builtin_generic_type_annotations())

    visitor = self.visit("dict[str, list[int]]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("tuple[int, ...]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("from collections import ChainMap\nChainMap[str, list[str]]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("l = list[str]()")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("import types\nisinstance(list[str], types.GenericAlias)")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("l = list\nl[-1]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    # Not a result because a list instance rather than list type is used.
    visitor = self.visit("l = [1,2,3]\nl[-1]")
    self.assertFalse(visitor.builtin_generic_type_annotations())

    visitor = self.visit("""import collections
collections.ChainMap[str]
""")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = self.visit("""import collections.abc
collections.abc.Reversible[int]
""")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_function_decorators(self):
    visitor = self.visit("def foo(): pass")
    self.assertFalse(visitor.function_decorators())

    visitor = self.visit("@f\ndef foo(): pass")
    self.assertTrue(visitor.function_decorators())
    self.assertOnlyIn(((2, 4), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@button_0.clicked.connect\ndef foo(): pass")
    self.assertTrue(visitor.function_decorators())
    self.assertOnlyIn(((2, 4), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@eval('buttons[1].clicked.connect')\ndef foo(): pass")
    self.assertTrue(visitor.function_decorators())
    self.assertOnlyIn(((2, 4), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@x.y(func)\ndef foo(): pass")
    self.assertTrue(visitor.function_decorators())
    self.assertOnlyIn(((2, 4), (3, 0)), visitor.minimum_versions())

  def test_class_decorators(self):
    visitor = self.visit("class A: pass")
    self.assertFalse(visitor.class_decorators())

    visitor = self.visit("@f\nclass A: pass")
    self.assertTrue(visitor.class_decorators())
    self.assertOnlyIn(((2, 6), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@button_0.clicked.connect\nclass A: pass")
    self.assertTrue(visitor.class_decorators())
    self.assertOnlyIn(((2, 6), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@eval('buttons[1].clicked.connect')\nclass A: pass")
    self.assertTrue(visitor.class_decorators())
    self.assertOnlyIn(((2, 6), (3, 0)), visitor.minimum_versions())

    visitor = self.visit("@x.y(func)\nclass A: pass")
    self.assertTrue(visitor.class_decorators())
    self.assertOnlyIn(((2, 6), (3, 0)), visitor.minimum_versions())

  def test_relaxed_decorators(self):
    visitor = self.visit("@f\ndef foo(): pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@button_0.clicked.connect\ndef foo(): pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@eval('buttons[1].clicked.connect')\ndef foo(): pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@_(buttons[0].clicked.connect)\ndef foo(): pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@functools.wraps(func)\ndef foo(): pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@f\nclass foo: pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@button_0.clicked.connect\nclass foo: pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@eval('buttons[1].clicked.connect')\nclass foo: pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@_(buttons[0].clicked.connect)\nclass foo: pass")
    self.assertFalse(visitor.relaxed_decorators())

    visitor = self.visit("@functools.wraps(func)\nclass foo: pass")
    self.assertFalse(visitor.relaxed_decorators())

    if current_version() >= (3, 6):
      visitor = self.visit("@f\nasync def foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("@button_0.clicked.connect\nasync def foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("@eval('buttons[1].clicked.connect')\nasync def foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("@_(buttons[0].clicked.connect)\nasync def foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("@functools.wraps(func)\nasync def foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

    if current_version() >= (3, 9):
      visitor = self.visit("@[bax][0]\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@[bax][0]  # novm\ndef foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("# novm\n@[bax][0]\ndef foo(): pass")
      self.assertFalse(visitor.relaxed_decorators())

      visitor = self.visit("@x[0]()\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@(lambda x: 1)\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\n@not_relaxed\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@non_relaxed\n@buttons[1].clicked.connect\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit(
        "@non_relaxed\n@buttons[1].clicked.connect\n@not_relaxed\ndef foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@[bax][0]\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@x[0]()\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@(lambda x: 1)\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\n@not_relaxed\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@non_relaxed\n@buttons[1].clicked.connect\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit(
        "@non_relaxed\n@buttons[1].clicked.connect\n@not_relaxed\nclass foo: pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@[bax][0]\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@x[0]()\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@(lambda x: 1)\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@buttons[1].clicked.connect\n@not_relaxed\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit("@non_relaxed\n@buttons[1].clicked.connect\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

      visitor = self.visit(
        "@non_relaxed\n@buttons[1].clicked.connect\n@not_relaxed\nasync def foo(): pass")
      self.assertTrue(visitor.relaxed_decorators())
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_module_dir_func(self):
    visitor = self.visit("def __dir__(): pass", path="__init__.py")
    self.assertTrue(visitor.module_dir_func())

    visitor = self.visit("def __dir__(): pass")
    self.assertFalse(visitor.module_dir_func())

    visitor = self.visit("def __dir__(a): pass", path="__init__.py")
    self.assertFalse(visitor.module_dir_func())

    visitor = self.visit("def __dir__(a, b=1): pass", path="__init__.py")
    self.assertFalse(visitor.module_dir_func())

    visitor = self.visit("def __dir__(b=1): pass", path="__init__.py")
    self.assertFalse(visitor.module_dir_func())

    visitor = self.visit("""def foo():
  def __dir__(): pass
""", path="__init__.py")
    self.assertFalse(visitor.module_dir_func())

  def test_module_getattr_func(self):
    visitor = self.visit("def __getattr__(name): pass", path="__init__.py")
    self.assertTrue(visitor.module_getattr_func())

    visitor = self.visit("def __getattr__(a): pass", path="__init__.py")
    self.assertTrue(visitor.module_getattr_func())

    visitor = self.visit("def __getattr__(name): pass")
    self.assertFalse(visitor.module_getattr_func())

    visitor = self.visit("def __getattr__(n, b=2): pass", path="__init__.py")
    self.assertFalse(visitor.module_getattr_func())

    visitor = self.visit("def __getattr__(): pass", path="__init__.py")
    self.assertFalse(visitor.module_getattr_func())

    visitor = self.visit("""def foo():
  def __getattr__(name): pass
""", path="__init__.py")
    self.assertFalse(visitor.module_getattr_func())
