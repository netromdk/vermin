from vermin import BUILTIN_GENERIC_ANNOTATION_TYPES, dotted_name

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
    elif v >= 3.0 and v < 3.4:  # pragma: no cover
      self.assertEqual(node, None)
      self.assertEqual(mins, [(0, 0), (0, 0)])
    # < 3.0
    else:  # pragma: no cover
      visitor = visit(source)
      self.assertTrue(visitor.printv2())
      self.assertEqual([(2, 0), (0, 0)], visitor.minimum_versions())

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    visitor = visit("print('hello')")
    if current_version() < 3.0:  # pragma: no cover
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

    visitor = visit("v = 1\nv += long(42)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

    visitor = visit("isinstance(42, long)")
    self.assertTrue(visitor.longv2())
    self.assertOnlyIn((2, 0), visitor.minimum_versions())

  def test_bytesv3(self):
    v = current_version()

    # py2: type(b'hello') = <type 'str'>
    if v >= 2.0 and v < 3.0:  # pragma: no cover
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

      visitor = visit("f'{f\"{3.1415:.1f}\":*^20}'")
      self.assertTrue(visitor.fstrings())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

      visitor = visit("f'''{\n3\n}'''")
      self.assertTrue(visitor.fstrings())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_fstrings_named_expr(self):
    if current_version() >= 3.8:
      visitor = visit("f'{(x:=1)}'")
      self.assertTrue(visitor.fstrings())
      self.assertTrue(visitor.named_expressions())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

    if current_version() >= 3.6:
      visitor = visit("f'{x:=10}'")
      self.assertTrue(visitor.fstrings())
      self.assertFalse(visitor.named_expressions())
      self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_fstrings_self_doc(self):
    enabled = False
    if enabled and current_version() >= 3.8:  # pragma: no cover
      def visit_fstring_self_doc(source):
        return visit(source=source, fstring_self_doc=True)

      # NOTE: The built-in AST cannot distinguish `f'{a=}'` from `f'a={a}'` because it optimizes
      # some information away. Therefore, this test will be seen as a self-doc f-string, which is
      # why fstring self-doc detection has been disabled for now.
      visitor = visit_fstring_self_doc("a = 1\nf'a={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("name = 'world'\nf'hello {name=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("name = 'world'\nf'hello={name}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("a = 1\nf'={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("a = 1\nf'{a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("a = 1\nb = 2\nf'={b}={a}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("a = 1\nb = 2\nf'{b=}={a}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a =}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a= }'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ a = }'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{1+1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{1+b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a+b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a+1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a-1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a/1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a//1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a*1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{not a=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{1 in []=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{1 not in []=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{None is None=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{None is not True=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{10 % 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{10 ^ 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{10 | 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{10 & 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{10 ** 5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{-5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{+5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{~5=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x << y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x >> y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x @ y=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a or b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{a and b=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{(1,2,3)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{[1,2,3]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ {1,2,3}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ {1:1, 2:2}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{[x for x in [1,2,3]]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{(x for x in [1,2,3])=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ {x for x in [1,2,3]}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{ {x:1 for x in [1,2,3]}=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0==1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0<1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0>1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0<=1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0>=1=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{0==1!=2=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{3.14=:10.10}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{3.14=!s:10.10}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x=!s}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x=!r}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x=!a}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x=:.2f}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{x=!a:^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{f\"{3.1415=:.1f}\":*^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'alpha a {pi=} w omega'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'''{\n3\n=}'''")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{f(a=4)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{f(a=\"3=\")=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{C()=!r:*^20}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{user=!s}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{delta.days=:,d}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{user=!s}  {delta.days=:,d}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{delta.days:,d}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("f'{cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("f'{cos(radians(theta))=:.3f}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'={cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("f'{theta}  {cos(radians(theta)):.3f}'")
      self.assertFalse(visitor.fstrings_self_doc())

      visitor = visit_fstring_self_doc("f'{cos(radians(theta)):.3f} {theta=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{(a+b)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{(a+((b-(c*d))/e))=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{d[\"foo\"]=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'i:{i=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{1 if True else 2=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'{(d[a], None) if 42 != 84 else (1,2,3)=}'")
      self.assertTrue(visitor.fstrings_self_doc())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = visit_fstring_self_doc("f'expr={ {x: y for x, y in [(1, 2) ]} = }'")
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
    if current_version() < 3.0:  # pragma: no cover
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
    if current_version() < 3.0:  # pragma: no cover
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
    if current_version() >= 3.5:
      visitor = visit("(*range(4), 4)")  # tuple
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(4, *range(4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(*range(4),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(*(1,),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(*(1, 2),)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(0, *(1, 2))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(*(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(0, *(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("(*(1, 2), *(3, 4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*range(4), 4]")  # list
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[4, *range(4)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*range(4)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*[1]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*[1, 2]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[0, *[1, 2]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*[1, 2], 3]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[0, *[1, 2], 3]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*[1, 2], *[3, 4]]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*range(4), 4}")  # set
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{4, *range(4)}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*range(4)}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*{1}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*{1, 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{0, *{1, 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*{1, 2}, 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{0, *{1, 2}, 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{*{1, 2}, *{3, 4}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{'x': 1, **{'y': 2}}")  # dict
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{**{'y': 2}, 'x': 1}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{**{1: 1}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{**{1: 1, 2: 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{0: 0, **{1: 1, 2: 2}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{**{1: 1, 2: 2}, 3: 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{0: 0, **{1: 1, 2: 2}, 3: 3}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("{**{1: 1, 2: 2}, **{3: 3, 4: 4}}")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("[*{1,2,3}, *(1,2,3), *[1,2,3], *range(3)]")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("print(*(1,))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = visit("print(*(1, 2))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = visit("print(0, *(1, 2))")
      self.assertFalse(visitor.generalized_unpacking())

      visitor = visit("print(*(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("print(0, *(1, 2), 3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("print(*(1, 2), *(3, 4))")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("dict(**{'b': 1, 'c': 2}, d=3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("dict(a=0, **{'b': 1, 'c': 2}, d=3)")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("dict(**{'b': 1, 'c': 2}, **{'d': 3, 'e': 4})")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("foo(0, *(1, 2), 3, a=1, **{'b': 2, 'c': 3})")
      self.assertTrue(visitor.generalized_unpacking())
      self.assertOnlyIn((3, 5), visitor.minimum_versions())

      visitor = visit("foo(0, *(1, 2), a=1, **{'b': 2, 'c': 3}, d=4)")
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

    visitor = visit("dict(**{'b': 1})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = visit("dict(**{'b': 1, 'c': 2})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = visit("dict(a=0, **{'b': 1, 'c': 2})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = visit("foo(0, *(1, 2), a=1, **{'b': 2, 'c': 3})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = visit("function(arg=84, **{'x': 42})")
    self.assertFalse(visitor.generalized_unpacking())

    visitor = visit("d = {'a': 'b'}\ndict(**d)")
    self.assertFalse(visitor.generalized_unpacking())

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

  def test_detect_raise_members(self):
    visitor = visit("raise ModuleNotFoundError")
    self.assertOnlyIn("ModuleNotFoundError", visitor.members())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_detect_except_members(self):
    visitor = visit("try: pass\nexcept ModuleNotFoundError: pass")
    self.assertOnlyIn("ModuleNotFoundError", visitor.members())
    self.assertOnlyIn((3, 6), visitor.minimum_versions())

  def test_dict_union(self):
    visitor = visit("{'a':1} | {'b':2}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {'a':1}\nb = {'b':2}\na | b")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {'a':1}\na | {'b':2}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {'a':1}\n{'b':2} | a")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("dict() | dict()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = dict()\nb = dict()\na | b")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = dict()\na | dict()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = dict()\ndict() | a")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("{} | dict() | {}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("(lambda: {})() | {}")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("(lambda: {} | dict())()")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("{} | (1,{},'a')[1]")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("{} | (1,{},'a')[0]")
    self.assertFalse(visitor.dict_union())
    visitor = visit("{} | [1,{},'a'][1]")
    self.assertTrue(visitor.dict_union())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("[1,(lambda:{1:2})(),3][1] | {2:3}")
    self.assertTrue(visitor.dict_union())

  def test_dict_union_merge(self):
    visitor = visit("a = {'a':1}\na |= {'b':2}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {'a':1}\nb = {'b':2}\na |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = dict()\na |= dict()")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = dict()\nb = dict()\na |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {}\nfor b in ({}, {}, {}):\n\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {}\nfor b in [{}, {}, {}]:\n\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {}\nb = {}\nfor c in (b,):\n\ta |= c")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = {}\na |= (lambda:{})()")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("a = 1\nfor a in [{}]:\n\tfor b in ({},):\n\t\ta |= b")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    # "os.environ" and "os.environb" were modified to also support "|=".
    visitor = visit("from os import environ\nos.environ |= {'var':'val'}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())
    visitor = visit("from os import environb\nos.environb |= {'var':'val'}")
    self.assertTrue(visitor.dict_union_merge())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

  def test_builtin_generic_type_annotation(self):
    # For each type, either use directly if builtin or import and then use.
    # Examples:
    # -  from re import Match
    #    Match[str]
    # -  tuple[str]
    for typ in BUILTIN_GENERIC_ANNOTATION_TYPES:
      names = [typ]
      src = ""
      if "." in typ:
        names = typ.split(".")
        src = "from {} import {}\n".format(dotted_name(names[:-1]), names[-1])
      src += "{}[str]".format(names[-1])
      visitor = visit(src)
      self.assertTrue(visitor.builtin_generic_type_annotations(), msg=src)
      self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("class A: pass\nA[str]")
    self.assertFalse(visitor.builtin_generic_type_annotations())

    # Ignore user-defined types that clash with builtin types.
    visitor = visit("class dict: pass\ndict[str]")
    self.assertFalse(visitor.builtin_generic_type_annotations())

    visitor = visit("dict[str, list[int]]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("tuple[int, ...]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("from collections import ChainMap\nChainMap[str, list[str]]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("l = list[str]()")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("import types\nisinstance(list[str], types.GenericAlias)")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    visitor = visit("l = list\nl[-1]")
    self.assertTrue(visitor.builtin_generic_type_annotations())
    self.assertOnlyIn((3, 9), visitor.minimum_versions())

    # Not a result because a list instance rather than list type is used.
    visitor = visit("l = [1,2,3]\nl[-1]")
    self.assertFalse(visitor.builtin_generic_type_annotations())
