from .testutils import VerminTest, current_version

class VerminCommentsExclusionsTests(VerminTest):
  def test_import(self):
    visitor = self.visit("# novm\nimport email.parser.FeedParser")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Comment "novm" or "novermin" on its own refers to the next line.
    self.assertIn(2, visitor.no_lines())

    visitor = self.visit("# novermin\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing at end of line w/o spacing.
    visitor = self.visit("import email.parser.FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  #novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser#novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing multiple comment segments.
    visitor = self.visit("import email.parser.FeedParser  # noqa # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # novm # noqa")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # noqa # novermin # nolint")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser "
                         "# type: ignore[attr-defined] # novm # pylint: disable=no-member")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing multiple comment segments on its own refers to the next line.
    visitor = self.visit("# noqa # novm # nolint\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# noqa # novermin # nolint\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# type: ignore[attr-defined] # novm # pylint: disable=no-member\n"
                         "import email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Detect comments on line that are indented, i.e. col != 0 but the comment is alone on the line.
    visitor = self.visit("if 1:\n # novermin\n import email.parser.FeedParser")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if 1:\n\t# novermin\n\timport email.parser.FeedParser")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if 1:\n\tif 1:\n\t\t# novermin\n\t\timport email.parser.FeedParser")
    self.assertIn(4, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_from_import(self):
    visitor = self.visit("# novm\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# novermin\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("from email.parser import FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("from email.parser import FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_function(self):
    visitor = self.visit("# novm\ndef foo():\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("def foo(): # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_async_function(self):
    visitor = self.visit("# novm\nasync def foo():\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("async def foo():  #novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_class(self):
    visitor = self.visit("# novm\nclass foo():\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("class foo(): # novm\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_if(self):
    visitor = self.visit("# novm\nif True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_for(self):
    visitor = self.visit("# novm\nfor a in [1,2,3]:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("for a in [1,2,3]:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_async_for(self):
    visitor = self.visit("""async def foo():
  # novm
  async for a in [1,2,3]:
    all([])
""")
    self.assertIn(3, visitor.no_lines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())
    visitor = self.visit("""async def foo():
  async for a in [1,2,3]:  # novm
    all([])
""")
    self.assertIn(2, visitor.no_lines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_while(self):
    visitor = self.visit("# novm\nwhile True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("while True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_boolop(self):
    visitor = self.visit("# novm\nFalse or all([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("False or all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_call(self):
    visitor = self.visit("# novm\nall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_assign(self):
    visitor = self.visit("""import ssl
tls_version = ssl.PROTOCOL_TLSv1
if hasattr(ssl, "PROTOCOL_TLS"):
  tls_version = ssl.PROTOCOL_TLS  # novermin
""")
    self.assertIn(4, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_augassign(self):
    visitor = self.visit("""import ssl
tls_version = ssl.PROTOCOL_TLSv1
if hasattr(ssl, "PROTOCOL_TLS"):
  tls_version += ssl.PROTOCOL_TLS  # novermin
""")
    self.assertIn(4, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_annassign(self):
    visitor = self.visit("""a : int = 1  # novermin
""")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_coroutines_await(self):
    self.config.set_verbose(2)
    visitor = self.visit("""async def func():
  await something()  # novermin
""")
    self.assertIn(2, visitor.no_lines())
    # Since both `async def` and `await` require 3.5, and `await` must be in an `async def`, the
    # verbose (2) output text is inspected.
    self.assertTrue(visitor.coroutines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())
    self.assertNotIn("await", visitor.output_text())

  @VerminTest.skipUnlessVersion(3, 8)
  def test_namedexpr(self):
    visitor = self.visit("""import ssl
(a := ssl.PROTOCOL_TLS)  # novermin
""")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 3)
  def test_yield_from(self):
    visitor = self.visit("""def foo(x):
  yield from range(x)  # novermin
""")
    self.assertIn(2, visitor.no_lines())
    self.assertFalse(visitor.yield_from())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_yield(self):
    visitor = self.visit("""import ssl
yield ssl.PROTOCOL_TLS  # novermin
""")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_raise(self):
    visitor = self.visit("""import ssl
raise ssl.PROTOCOL_TLS  # novermin
""")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_excepthandler(self):
    visitor = self.visit("""import ssl
try:
  pass
except TypeError:  # novermin
  ssl.PROTOCOL_TLS
""")
    self.assertIn(4, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_with(self):
    visitor = self.visit("""import ssl
with 1 as a:  # novermin
  ssl.PROTOCOL_TLS
""")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_async_with(self):
    visitor = self.visit("""import ssl
async def foo():
  async with 1 as a:  # novermin
    ssl.PROTOCOL_TLS
""")
    self.assertIn(3, visitor.no_lines())
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_subscript(self):
    visitor = self.visit("""import ssl
l = [1, 2, 3]
l[1:ssl.PROTOCOL_TLS.value]  # novermin
""")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_newline_before_novm(self):
    # Earlier, it wasn't checking for both `NL` and `NEWLINE` tokens to denote newlines, only the
    # later.
    visitor = self.visit("""import ssl
l = [1, 2, 3]
for a in l:

  # novm
  l[1:ssl.PROTOCOL_TLS.value]
""")
    self.assertIn(6, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_function_decorator(self):
    visitor = self.visit("""@staticmethod  # novm
def foo(): pass
""")
    self.assertFalse(visitor.function_decorators())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""@staticmethod #novm
@staticmethod #novm
def foo(): pass
""")
    self.assertFalse(visitor.function_decorators())
    self.assertEqual({1, 2}, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # When not all function decorators are excluded, the function decorator version requirement is
    # still in effect.
    visitor = self.visit("""@staticmethod
@staticmethod #novm
def foo(): pass
""")
    self.assertTrue(visitor.function_decorators())
    self.assertEqual({2}, visitor.no_lines())
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

    visitor = self.visit("""@staticmethod #novm
@staticmethod
def foo(): pass
""")
    self.assertEqual({1}, visitor.no_lines())

    # The line numbers were not as precise before 3.8, so excluding the first decorator would
    # exclude the whole function, too.
    if current_version() < (3, 8):
      self.assertFalse(visitor.function_decorators())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    else:
      self.assertTrue(visitor.function_decorators())
      self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

  def test_class_decorator(self):
    visitor = self.visit("""@somedeco  # novm
class Foo: pass
""")
    self.assertFalse(visitor.class_decorators())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""@somedeco #novm
@somedeco #novm
class Foo: pass
""")
    self.assertFalse(visitor.class_decorators())
    self.assertEqual({1, 2}, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # When not all class decorators are excluded, the class decorator version requirement is still
    # in effect.
    visitor = self.visit("""@somedeco
@somedeco #novm
class Foo: pass
""")
    self.assertTrue(visitor.class_decorators())
    self.assertEqual({2}, visitor.no_lines())
    self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

    visitor = self.visit("""@somedeco #novm
@somedeco
class Foo: pass
""")
    self.assertEqual({1}, visitor.no_lines())

    # The line numbers were not as precise before 3.8, so excluding the first decorator would
    # exclude the whole class, too.
    if current_version() < (3, 8):
      self.assertFalse(visitor.class_decorators())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    else:
      self.assertTrue(visitor.class_decorators())
      self.assertEqual([(2, 6), (3, 0)], visitor.minimum_versions())

  def test_multiline(self):
    visitor = self.visit('''foo = """
{}
""".format('bar') #novm
''')
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('''foo = """{}""".format('bar') #novm
''')
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('''foo = """{}
""".format('bar') #novm
''')
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""foo = '''
{}
'''.format('bar') #novm
""")
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""foo = '''{}'''.format('bar') #novm
""")
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""foo = '''{}
'''.format('bar') #novm
""")
    self.assertFalse(visitor.format27())
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('''#novm
foo = """
{}
""".format('bar')
''')
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('''#novm
foo = """{}""".format('bar')
''')
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit('''#novm
foo = """{}
""".format('bar')
''')
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""#novm
foo = '''
{}
'''.format('bar')
""")
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""#novm
foo = '''{}'''.format('bar')
""")
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("""#novm
foo = '''{}
'''.format('bar')
""")
    self.assertFalse(visitor.format27())
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_not_parsing_comments(self):
    self.config.set_parse_comments(False)

    visitor = self.visit("# novm\nimport email.parser.FeedParser")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # novm")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 10)
  def test_pattern_matching(self):
    visitor = self.visit("""
def http_error(status):
  match status:  #novm
    case 400:
      return "Bad request"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"
""")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_ifexp(self):
    visitor = self.visit("1 if True else 2  #novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_nonlocal(self):
    visitor = self.visit("""
def foo():
  a = 1
  def bar():
    nonlocal a  #novm
""")
    self.assertIn(5, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
