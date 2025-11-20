from vermin import BUILTIN_GENERIC_ANNOTATION_TYPES, DICT_UNION_SUPPORTED_TYPES, \
  DICT_UNION_MERGE_SUPPORTED_TYPES, dotted_name, Parser, InvalidVersionException

from .testutils import VerminTest, current_version

class VerminLanguageTests(VerminTest):
  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= (3, 4):
      self.assertOnlyIn((2, 0), self.detect("print 'hello'"))

    source = "print 'hello'"
    parser = Parser(source)
    (node, mins, _novermin, _err_msg) = parser.detect(self.config)
    v = current_version()
    if v >= (3, 4):
      self.assertEqual(node, None)
      self.assertOnlyIn((2, 0), mins)
    elif (3, 0) <= v < (3, 4):  # pragma: no cover
      self.assertEqual(node, None)
      self.assertEqual(mins, [(0, 0), (0, 0)])

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    visitor = self.visit("print('hello')")
    v = current_version()
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

    # "{0}" is py 2.6. "{{}}" simply yields "{}" as a string value.
    visitor = self.visit("'{{}} {0}'.format('test')")
    self.assertFalse(visitor.format27())
    self.assertOnlyIn(((2, 6), (3, 0)), visitor.minimum_versions())

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
    self.assertOnlyIn((3, 7), self.detect("[i async for i in iter() if i % 2]"))
    self.assertOnlyIn((3, 10), self.detect("[i async for i in aiter() if i % 2]"))

  @VerminTest.skipUnlessVersion(3, 7)
  def test_await_in_comprehension(self):
    visitor = self.visit("[await fun() for fun in funcs if await condition()]")
    self.assertTrue(visitor.await_in_comprehension())
    self.assertOnlyIn((3, 7), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_async_for(self):
    self.assertOnlyIn((3, 5), self.detect("async def foo():\n\tasync for a in []:pass"))

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

  def test_kw_only_args(self):
    visitor = self.visit("def foo(a, *, b): return a + b")
    self.assertTrue(visitor.kw_only_args())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 8)
  def test_pos_only_args(self):
    visitor = self.visit("def foo(a, /, b): return a + b")
    self.assertTrue(visitor.pos_only_args())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_nonlocal_stmt(self):
    visitor = self.visit("def foo():\n\tlong = 1\n\tdef bar():\n\t\tnonlocal long")
    self.assertTrue(visitor.nonlocal_stmt())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

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

  def test_set_literals(self):
    visitor = self.visit("{1}")
    self.assertTrue(visitor.set_literals())
    self.assertEqual([(2, 7), (3, 0)], visitor.minimum_versions())

  def test_set_comprehension(self):
    visitor = self.visit("{key for ld in lod for key, value in ld.items()}")
    self.assertTrue(visitor.set_comprehension())
    self.assertEqual([(2, 7), (3, 0)], visitor.minimum_versions())

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

  def test_float_from_type(self):
    visitor = self.visit("(4.2).hex()")
    self.assertIn("float.hex", visitor.members())
    visitor = self.visit("float().hex()")
    self.assertIn("float.hex", visitor.members())

  def test_bytes_from_type(self):
    visitor = self.visit("b'hello'.hex()")
    self.assertIn("bytes.hex", visitor.members())
    visitor = self.visit("bytes().hex()")
    self.assertIn("bytes.hex", visitor.members())

  @VerminTest.parameterized_args([
    ["with func():\n  pass"],
    ["with a as (b, c): pass"],
    ["with a as b:\n\twith c as d:\n\t\tpass"],
  ])
  def test_with_statement(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.with_statement())
    self.assertFalse(visitor.multi_withitem())
    self.assertFalse(visitor.with_parentheses())
    self.assertOnlyIn([(2, 5), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 3)  # See `visit_With` for reason for only testing on 3.3+.
  @VerminTest.parameterized_args([
    ["with a, b: pass"],
    ["with a, b as c: pass"],
    ["with a as b, c: pass"],
    ["with a as b, c as d: pass"],
  ])
  def test_multi_withitem(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertFalse(visitor.with_parentheses())
    self.assertOnlyIn([(2, 7), (3, 1)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 9)
  @VerminTest.parameterized_args([
    ["with (a, b): pass"],
    ["with (a, b as c): pass"],
    ["with (a as b, c): pass"],
    ["with (a as b, c as d): pass"],
    ["""with \
  (a, b): pass"""],
    ["""with \
  (a, b as c): pass"""],
    ["""with \
  (\
  a, b): pass"""],
    ["""with \
  (\
  a, b as c): pass"""],
    ["""with \
  \
  (a, b): pass"""],
    ["""with \
  \
  (a, b as c): pass"""],
  ])
  def test_with_parentheses(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertTrue(visitor.with_parentheses())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 9)
  def test_with_parentheses_first_match(self):
    self.config.set_verbose(3)  # show lines
    visitor = self.visit("""with (a as b, c as d): pass
with a as b, c as d: pass""")
    self.assertTrue(visitor.with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertTrue(visitor.with_parentheses())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    self.assertEqual(visitor.output_text(), """L1: `with` requires 2.5, 3.0
L1: multiple context expressions in a `with` statement require 2.7, 3.1
L1: multiple context expressions in a `with` statement with parentheses require !2, 3.9
L2: `with` requires 2.5, 3.0
L2: multiple context expressions in a `with` statement require 2.7, 3.1
""")

  @VerminTest.skipUnlessVersion(3, 9)
  def test_with_parentheses_second_match(self):
    self.config.set_verbose(3)  # show lines
    visitor = self.visit("""with a as b, c as d: pass
with (a as b, c as d): pass""")
    self.assertTrue(visitor.with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertTrue(visitor.with_parentheses())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    self.assertEqual(visitor.output_text(), """L1: `with` requires 2.5, 3.0
L1: multiple context expressions in a `with` statement require 2.7, 3.1
L2: `with` requires 2.5, 3.0
L2: multiple context expressions in a `with` statement require 2.7, 3.1
L2: multiple context expressions in a `with` statement with parentheses require !2, 3.9
""")

  @VerminTest.skipUnlessVersion(3, 5)
  @VerminTest.parameterized_args([
    ["""async def foo():
  async with func(): pass"""],
    ["""async def foo():
  async with a as (b, c): pass"""],
    ["""async def foo():
  async with a as b:
    with c as d: pass"""],
  ])
  def test_async_with_statement(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.async_with_statement())
    self.assertFalse(visitor.multi_withitem())
    self.assertFalse(visitor.with_parentheses())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  @VerminTest.parameterized_args([
    ["""async def foo():
  async with a, b: pass"""],
    ["""async def foo():
  async with a, b as c: pass"""],
    ["""async def foo():
  async with a as b, c: pass"""],
    ["""async def foo():
  async with a as b, c as d: pass"""],
  ])
  def test_async_multi_withitem(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.async_with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertFalse(visitor.with_parentheses())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 9)
  @VerminTest.parameterized_args([
    ["""async def foo():
  async with (a, b): pass"""],
    ["""async def foo():
  async with (a, b as c): pass"""],
    ["""async def foo():
  async with (a as b, c): pass"""],
    ["""async def foo():
  async with (a as b, c as d): pass"""],
    ["""async def foo():
  async with \
  (a, b): pass"""],
    ["""async def foo():
  async with \
  (a, b as c): pass"""],
    ["""async def foo():
  async with \
  (\
  a, b): pass"""],
    ["""async def foo():
  async with \
  (\
  a, b as c): pass"""],
    ["""async def foo():
  async with \
  \
  (a, b): pass"""],
    ["""async def foo():
  async with \
  \
  (a, b as c): pass"""],
  ])
  def test_async_with_parentheses(self, source):
    visitor = self.visit(source)
    self.assertTrue(visitor.async_with_statement())
    self.assertTrue(visitor.multi_withitem())
    self.assertTrue(visitor.with_parentheses())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

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

  def test_ellipsis_in_slices(self):
    visitor = self.visit('x[...]')
    self.assertFalse(visitor.ellipsis_out_of_slices())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('x[a, ..., b]')
    self.assertFalse(visitor.ellipsis_out_of_slices())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_ellipsis_out_of_slices(self):
    visitor = self.visit('...')
    self.assertTrue(visitor.ellipsis_out_of_slices())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

    visitor = self.visit('x[[...]]')
    self.assertTrue(visitor.ellipsis_out_of_slices())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 12)
  def test_type_alias_statement(self):
    visitor = self.visit('type X = int')
    self.assertTrue(visitor.type_alias_statement())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    visitor = self.visit('type Point = tuple[float, float]')
    self.assertTrue(visitor.type_alias_statement())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    visitor = self.visit('type(X)')
    self.assertFalse(visitor.type_alias_statement())

    # Plain syntax errors.
    visitor = self.visit('type "X = int"')
    self.assertEqual([(0, 0), (0, 0)], visitor)

    visitor = self.visit('type "Point = tuple[float, float]"')
    self.assertEqual([(0, 0), (0, 0)], visitor)

    visitor = self.visit('type "Po_int = tuple[float, float]"')
    self.assertEqual([(0, 0), (0, 0)], visitor)

  def test_type_alias_statement_invalid_syntax(self):
    """Prior to 3.12 it would yield SyntaxError: invalid syntax for type alias statements."""
    cv = current_version()
    if cv.major == 3 and cv.minor <= 11:
      self.assertOnlyIn((3, 12), self.detect("type X = int"))
      self.assertOnlyIn((3, 12), self.detect("type Point = tuple[float, float]"))

      # Plain syntax errors.
      self.assertEqual([(0, 0), (0, 0)], self.detect("type 'X = int'"))
      self.assertEqual([(0, 0), (0, 0)], self.detect("type 'Point = tuple[float, float]'"))
      self.assertEqual([(0, 0), (0, 0)], self.detect("type 'Po_int = tuple[float, float]'"))

  @VerminTest.skipUnlessVersion(3, 12)
  def test_type_alias_statement_class_scope_lambda(self):
    # Type alias not in a class scope.
    visitor = self.visit("type Alias = lambda: T")
    self.assertTrue(visitor.type_alias_statement())
    self.assertFalse(visitor.type_alias_statement_class_scope_lambda())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())
    visitor = self.visit("type Alias = [l for l in [lambda: T]]")
    self.assertTrue(visitor.type_alias_statement())
    self.assertFalse(visitor.type_alias_statement_class_scope_lambda())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    # Type alias with lambda not in a class scope but with a nested one without.
    visitor = self.visit("""
type Alias = lambda: T
class A[T]:
  type Alias = T
""")
    self.assertTrue(visitor.type_alias_statement())
    self.assertFalse(visitor.type_alias_statement_class_scope_lambda())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    # Type alias in a class scope.
    visitor = self.visit("""
class A[T]:
  type Alias = lambda: T
""")
    self.assertTrue(visitor.type_alias_statement())
    self.assertTrue(visitor.type_alias_statement_class_scope_lambda())
    self.assertOnlyIn((3, 13), visitor.minimum_versions())
    visitor = self.visit("""
class A[T]:
  type Alias = [l for l in [lambda: T]]
""")
    self.assertTrue(visitor.type_alias_statement())
    self.assertTrue(visitor.type_alias_statement_class_scope_lambda())
    self.assertOnlyIn((3, 13), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 14)
  def test_template_string_literal(self):
    visitor = self.visit("t'hello'")
    self.assertTrue(visitor.template_string_literal())
    self.assertOnlyIn((3, 14), visitor.minimum_versions())

    visitor = self.visit("t'hello {var}'")
    self.assertTrue(visitor.template_string_literal())
    self.assertOnlyIn((3, 14), visitor.minimum_versions())

    visitor = self.visit("""
from string.templatelib import Interpolation

def lower_upper(template):
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(str(part.value).upper())
        else:
            parts.append(part.lower())
    return ''.join(parts)

name = 'Wenslydale'
template = t'Mister {name}'
assert lower_upper(template) == 'mister WENSLYDALE'
""")
    self.assertTrue(visitor.template_string_literal())
    self.assertOnlyIn((3, 14), visitor.minimum_versions())

    visitor = self.visit("""
attributes = {'src': 'test.jpg', 'alt': 'test test'}
template = t'<img {attributes}>'
assert html(template) == '<img src="test.jpg" alt="test test" />'
""")
    self.assertTrue(visitor.template_string_literal())
    self.assertOnlyIn((3, 14), visitor.minimum_versions())

    # f-strings are not t-strings
    visitor = self.visit("f'hello'")
    self.assertFalse(visitor.template_string_literal())

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

    # Issue 69 example where `file` would get incorrectly seen as Python 2's builtin function
    # instead of a name defined in the for-loop. The fix is to only look for members in the type
    # branch of exception handlers.
    visitor = self.visit("""
for file in ['foo']:
  try:
    1 / 0
  except ZeroDivisionError:
    print(file)
""")
    self.assertNotIn("file", visitor.members())

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

    # The following annotations are only requiring 3.9 when evaluated, which doesn't happen at
    # definition time.

    # Spot test without annotations evaluation enabled first.
    self.config.set_eval_annotations(False)
    visitor = self.visit("dict[str, list[int]]")
    self.assertFalse(visitor.builtin_generic_type_annotations())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Instruct to eval annotations even though they aren't directly since that is
    # what this test is about.
    self.config.set_eval_annotations(True)

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

  def test_issue_66_annotations(self):
    self.assertOnlyIn((3, 7), self.detect("""
from __future__ import annotations

def foo() -> list[int]:
    return [0]

foo()"""))

    self.config.set_eval_annotations(True)
    self.assertOnlyIn((3, 9), self.detect("""
from __future__ import annotations
import typing

def foo() -> list[int]:
    return [0]

typing.get_type_hints(foo)"""))

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

  def test_for_target_ignore_user_def(self):
    # unpacking assignment requires !2, 3.0
    self.assertEqual([None, (3, 0)], self.detect("""
for a, (*file, c[d+e::f(g)], h.i) in []:
  file()
"""))

    # The user-def passed out of scope, so match `file` as 2, !3.
    self.assertEqual([(2, 0), None], self.detect("""
for a, file, b in []:
  pass
file()
"""))

  def test_with_items_ignore_user_def(self):
    # See `visit_With` for reason for only testing on 3.3+ for first and third test case of this
    # function.

    # Multiple context expressions in a `with` statement is 2.7, 3.1.
    if current_version() >= (3, 3):
      self.assertEqual([(2, 7), (3, 1)], self.detect("""
with False as a, True as file, 42 as b:
  file()
"""))

    self.assertEqual([(2, 5), (3, 0)], self.detect("""
with ctx() as (file,):
  file()
"""))

    # The user-def passed out of scope, so match `file` as 2, !3 -> 2.7, !3 due to
    # multiple context expressions in a `with` statement.
    if current_version() >= (3, 3):
      self.assertEqual([(2, 7), None], self.detect("""
with False as a, True as file, 42 as b:
  pass
file()
"""))

  def test_except_handler_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
try:
  1 / 0
except ZeroDivisionError as file:
  file()
"""))

    # The user-def passed out of scope, so match `file` as 2, !3.
    self.assertEqual([(2, 0), None], self.detect("""
try:
  1 / 0
except ZeroDivisionError as file:
  pass
file()
"""))

  def test_func_name_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
def file():
  file()
"""))

  def test_func_arg_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
def foo(a, file, b):
  file()
"""))

    # The user-def passed out of scope, so match `file` as 2, !3.
    self.assertEqual([(2, 0), None], self.detect("""
def foo(a, file, b):
  pass
file()
"""))

  @VerminTest.skipUnlessVersion(3, 8)
  def test_func_posonlyarg_ignore_user_def(self):
    self.assertEqual([None, (3, 8)], self.detect("""
def foo(file, /, a="Hello"):
  file()
"""))

    # The user-def passed out of scope, and exception because `file` requries 2, !3 and posonlyargs
    # requires !2, 3.8.
    with self.assertRaises(InvalidVersionException):
      self.visit("""
def foo(file, /, a="Hello"):
  pass
file()
""")

  def test_func_kwonlyarg_ignore_user_def(self):
    self.assertEqual([None, (3, 0)], self.detect("""
def foo(a, *, file="Hello"):
  file()
"""))

    # The user-def passed out of scope, and exception because `file` requries 2, !3 and kwonlyargs
    # requires !2, 3.
    with self.assertRaises(InvalidVersionException):
      self.visit("""
def foo(a, *, file="Hello"):
  pass
file()
""")

  def test_func_vararg_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
def foo(*file):
  file()
"""))

  def test_func_kwarg_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
def foo(**file):
  file()
"""))

  def test_lambda_arg_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
(lambda file: file())(print)
"""))

  def test_class_name_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
class file:
  def __init__(self):
    file()
"""))

  def test_assign_target_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
file = None
file()
"""))

    # unpacking assignment requires !2, 3.0
    self.assertEqual([None, (3, 0)], self.detect("""
a, (*file, c[d+e::f(g)], h.i) = [], []
file()
"""))

  def test_aug_assign_target_ignore_user_def(self):
    # Semantically, this AugAssign cannot be without an initial Assign but this tests that AugAssign
    # adds the user-def and not the Assign.
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
file += 1
file()
"""))

  @VerminTest.skipUnlessVersion(3, 6)
  def test_ann_assign_target_ignore_user_def(self):
    # variable annotations requires !2, 3.6
    self.assertEqual([None, (3, 6)], self.detect("""
file: int = 42
file()
"""))

  def test_import_as_target_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
import sys as file
file()
"""))

  def test_import_from_as_target_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
from sys import exit as file
file()
"""))

  @VerminTest.skipUnlessVersion(3, 8)
  def test_named_expr_assign_target_ignore_user_def(self):
    # named expressions requires !2, 3.8
    self.assertEqual([None, (3, 8)], self.detect("""
(file := 42)
file()
"""))

  def test_comprehension_assign_target_ignore_user_def(self):
    self.assertEqual([(0, 0), (0, 0)], self.detect("""
[file() for file in [lambda: None]]
"""))

    # set comprehension requires 2.7, 3.0
    self.assertEqual([(2, 7), (3, 0)], self.detect("""
{file() for file in [lambda: None]}
"""))

    # dict comprehension requires 2.7, 3.0
    self.assertEqual([(2, 7), (3, 0)], self.detect("""
{file(): 1 for file in [lambda: None]}
"""))

    self.assertEqual([(0, 0), (0, 0)], self.detect("""
(file() for file in [lambda: None])
"""))

    self.assertEqual([(0, 0), (0, 0)], self.detect("""
[file() for a, file in [1]]
"""))

    if current_version() >= (3,):
      self.assertEqual([None, (3, 0)], self.detect("""
[file() for a, *file in [1]]
"""))

    # After comprehension, `file` rules apply.
    self.assertEqual([(2, 0), None], self.detect("""
[file() for a, file in [1]], file()
"""))

    # After comprehension, `file` rules apply but unpacking assignment requires !2, 3.
    with self.assertRaises(InvalidVersionException):
      self.visit("""
[file() for a, *file in [1]], file()
""")

    # `file` rules apply because the target is bound in the inner-most comprehension and not the
    # outer-most one.
    self.assertEqual([(2, 0), None], self.detect("""
[file() for w, x[[file for file in [1]][0]] in [(1, 1)]]
"""))

  def test_bare_except_handler(self):
    # Support having a bare except handler: `node.type` in `visit_ExceptHandler`.
    try:
      self.visit("""
try:
  pass
except:
  pass
""")
    except AttributeError:
      self.fail("Crashed while parsing bare except handler.")

  @VerminTest.skipUnlessVersion(3, 10)
  def test_pattern_matching(self):
    visitor = self.visit("""
def http_error(status):
  match status:
    case 400:
      return "Bad request"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"
""")
    self.assertTrue(visitor.pattern_matching())

  def test_union_types_enabled(self):
    self.config.enable_feature("union-types")
    visitor = self.visit("int | float")
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    visitor = self.visit("a = 1 | 0")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = {'x':1}
b = {'y':2}
a | b
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit('isinstance("", int | str)')
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    visitor = self.visit("issubclass(bool, int | float)")
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    visitor = self.visit("""
a = str
a |= "test"
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = "test"
a |= int
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = str
a |= int
""")
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    visitor = self.visit("""
class Foo: pass
class Bar: pass
a = Foo() | Bar()
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
class Foo: pass
foo = Foo()
class Bar: pass
bar = Bar()
a = foo | bar
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
class Foo: pass
class Bar: pass
a = Foo | Bar
""")
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    visitor = self.visit("""
class Foo: pass
class Bar: pass
a = Foo
a |= Bar
""")
    self.assertTrue(visitor.union_types())
    self.assertOnlyIn((3, 10), visitor.minimum_versions())

    # Issue 103: Don't judge `|` operator applied to values, and not types, as a union of types.
    visitor = self.visit("""
index = 0
c_bitmap = [42]
exec_result = [42]
global_byte = c_bitmap[index]
local_byte = exec_result[index]
if (global_byte | local_byte) != global_byte:
  pass
""")
    self.assertFalse(visitor.union_types())

    if current_version() >= (3, 10):
      # Issue 159: Attributes can also be used for union types.
      visitor = self.visit("""
def function(argument: ipaddress.IPv4Interface | ipaddress.IPv6Interface):
    if isinstance(argument, ipaddress.IPv4Address):
        print("We got an IPv4")
    elif isinstance(argument, ipaddress.IPv6Address):
        print("We got an IPv6")
    else:
        print(f"We got type {type(argument)}")
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())
      visitor = self.visit("""
def function(argument: ipaddress.IPv4Interface | None):
    pass
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())
      visitor = self.visit("""
def function(argument: None | ipaddress.IPv4Interface):
    pass
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())
      visitor = self.visit("""
def function(argument: str | ipaddress.IPv4Interface):
    pass
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      # Issue 109: When not evaluating annotations, returns annotations must not be visited.
      self.config.set_eval_annotations(False)
      visitor = self.visit("""
from __future__ import annotations
def b(s: str) -> str | None:  # <-- don't visit returns node.
  return s
""")
      self.assertFalse(visitor.union_types())
      visitor = self.visit("""
from __future__ import annotations
a: str | None = None
def b(s: str) -> str | None:  # <-- don't visit returns node.
  return s
b(a or '')
""")
      self.assertFalse(visitor.union_types())

      visitor = self.visit("""
def square(number) -> int | float:
  return number ** 2
""")
      self.assertFalse(visitor.union_types())

      # Issue 109: When evaluating annotations, visit returns annotations.
      self.config.set_eval_annotations(True)
      visitor = self.visit("""
from __future__ import annotations
def b(s: str) -> str | None:  # <-- visit returns node.
  return s
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())
      visitor = self.visit("""
from __future__ import annotations
a: str | None = None
def b(s: str) -> str | None:  # <-- visit returns node.
  return s
b(a or '')
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("""
def square(number) -> int | float:
  return number ** 2
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      self.config.set_eval_annotations(False)
      visitor = self.visit("""
def square(number: int | float):
  return number ** 2
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("""
def square(number: int | float) -> int | float:
  return number ** 2
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      self.config.set_eval_annotations(False)
      visitor = self.visit("a: int | float = 1")
      self.assertFalse(visitor.union_types())
      self.assertTrue(visitor.maybe_annotations())
      # variable annotations requires !2, 3.6
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

      self.config.set_eval_annotations(True)
      visitor = self.visit("a: int | float = 1")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      self.config.set_eval_annotations(False)
      visitor = self.visit("""
a = int
b = str
c: a | b = 1
""")
      self.assertFalse(visitor.union_types())
      self.assertTrue(visitor.maybe_annotations())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

      self.config.set_eval_annotations(True)
      visitor = self.visit("""
a = int
b = str
c: a | b = 1
""")
      self.assertTrue(visitor.union_types())
      self.assertFalse(visitor.maybe_annotations())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("a: int | None")
      self.assertTrue(visitor.union_types())
      self.assertFalse(visitor.maybe_annotations())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("a: None | int")
      self.assertTrue(visitor.union_types())
      self.assertFalse(visitor.maybe_annotations())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("a: None | None")
      self.assertTrue(visitor.union_types())
      self.assertFalse(visitor.maybe_annotations())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("""
def foo(n: int | None):
  return n
""")
      self.assertTrue(visitor.union_types())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

      visitor = self.visit("""
a = int
b = None
c: a | b = 1  # though in this case `b` is a Name and not Constant.
""")
      self.assertTrue(visitor.union_types())
      self.assertFalse(visitor.maybe_annotations())
      self.assertOnlyIn((3, 10), visitor.minimum_versions())

  def test_union_types_disabled(self):
    self.assertFalse(self.config.has_feature("union-types"))

    # --- Normally true but false because the feature is disabled. ---

    visitor = self.visit("int | float")
    self.assertFalse(visitor.union_types())

    visitor = self.visit('isinstance("", int | str)')
    self.assertFalse(visitor.union_types())

    visitor = self.visit("issubclass(bool, int | float)")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = str
a |= int
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
class Foo: pass
class Bar: pass
a = Foo | Bar
""")
    self.assertFalse(visitor.union_types())

    if current_version() >= (3, 10):
      # Issue 159: Attributes can also be used for union types.
      visitor = self.visit("""
def function(argument: ipaddress.IPv4Interface | ipaddress.IPv6Interface):
    if isinstance(argument, ipaddress.IPv4Address):
        print("We got an IPv4")
    elif isinstance(argument, ipaddress.IPv6Address):
        print("We got an IPv6")
    else:
        print(f"We got type {type(argument)}")
""")
      self.assertFalse(visitor.union_types())

    # --- False in all cases, disabled or not. ---

    visitor = self.visit("a = 1 | 0")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = {'x':1}
b = {'y':2}
a | b
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = str
a |= "test"
""")
    self.assertFalse(visitor.union_types())

    visitor = self.visit("""
a = "test"
a |= int
""")
    self.assertFalse(visitor.union_types())

    # Issue 103: Don't judge `|` operator applied to values, and not types, as a union of types.
    visitor = self.visit("""
index = 0
c_bitmap = [42]
exec_result = [42]
global_byte = c_bitmap[index]
local_byte = exec_result[index]
if (global_byte | local_byte) != global_byte:
  pass
""")
    self.assertFalse(visitor.union_types())

  def test_super_no_args(self):
    # Without arguments, it's v3.0.
    visitor = self.visit("""
class Foo:
  def test(self):
    super()
""")
    self.assertTrue(visitor.super_no_args())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

    # With arguments, the mininmum of super() is v2.2/3.0.
    visitor = self.visit("""
class Foo:
  def test(self):
    super(Foo, self)
""")
    self.assertFalse(visitor.super_no_args())
    self.assertOnlyIn(((2, 2), (3, 0)), visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 11)
  def test_except_star(self):
    visitor = self.visit("""
try:
  pass
except* OSError as ex:
  pass
""")
    self.assertTrue(visitor.except_star())
    self.assertOnlyIn((3, 11), visitor.minimum_versions())

    visitor = self.visit("""
try:
  pass
except  *  OSError as ex:
  pass
""")
    self.assertTrue(visitor.except_star())
    self.assertOnlyIn((3, 11), visitor.minimum_versions())

    visitor = self.visit("""
def foo():
  try:
    pass
  except* OSError as ex:
    pass
""")
    self.assertTrue(visitor.except_star())
    self.assertOnlyIn((3, 11), visitor.minimum_versions())

    visitor = self.visit("""
try:
  pass
except OSError as ex:
  pass
""")
    self.assertFalse(visitor.except_star())

  def test_False_constant(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("False"))

  def test_True_constant(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("True"))

  def test_issue_168_keyword_values(self):
    visitor = self.visit("""
ret = subparser.add_parser("qemu")
ret.add_argument("--efi", action=argparse.BooleanOptionalAction, help="...")
""")

    # `argparse.BooleanOptionalAction` requires !2, 3.9 but the keyword values weren't visited
    # before.
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_metaclass_class_keyword(self):
    visitor = self.visit("""
class Foo(metaclass="foo"):
  pass
""")
    self.assertTrue(visitor.metaclass_class_keyword())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())

    visitor = self.visit("""
class Foo(other="foo"):
  pass
""")
    self.assertFalse(visitor.metaclass_class_keyword())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("class Foo: pass")
    self.assertFalse(visitor.metaclass_class_keyword())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Py2 variant not using keyword.
    visitor = self.visit("""
class Foo:
  __metaclass__ = "foo"
""")
    self.assertFalse(visitor.metaclass_class_keyword())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 12)
  def test_generic_class_keyword(self):
    visitor = self.visit("""
class Foo[T]:
  pass
""")
    self.assertTrue(visitor.generic_class())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    visitor = self.visit("""
class Car[Tire]:
  def __init__(self, tire: Tire):
    self.tire = tire

  def change_tire(self, tire: Tire):
    self.tire = tire
""")
    self.assertTrue(visitor.generic_class())
    self.assertOnlyIn((3, 12), visitor.minimum_versions())

    visitor = self.visit("""
class Foo:
  pass
""")
    self.assertFalse(visitor.generic_class())
