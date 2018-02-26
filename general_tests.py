from testutils import MinpyTest, current_version
from minpy import SourceVisitor, parse_source, parse_detect_source

def visit(source):
  visitor = SourceVisitor()
  visitor.visit(parse_source(source))
  return visitor

class MinpyGeneralTests(MinpyTest):
  def test_printv2(self):
    source = "print 'hello'"
    (node, mins) = parse_detect_source(source)
    v = current_version()
    if v >= 3.4:
      self.assertEqual(node, None)
      self.assertOnlyIn(2.0, mins)
    elif v >= 3.0 and v < 3.4:
      self.assertEqual(node, None)
      self.assertEqual(mins, [None, None])
    else:  # < 3.0
      visitor = visit(source)
      self.assertTrue(visitor.printv2())

  def test_printv3(self):
    visitor = visit("print('hello')")
    if current_version() >= 3.0:
      self.assertTrue(visitor.printv3())
    else:
      self.assertTrue(visitor.printv2())

  def test_format(self):
    visitor = visit("print('{}'.format(42))")
    self.assertTrue(visitor.format())

  def test_modules(self):
    visitor = visit("import ast\nimport sys\nfrom os import *")
    self.assertOnlyIn(("ast", "sys", "os"), visitor.modules())

  def test_member_class(self):
    visitor = visit("from abc import ABC")
    self.assertOnlyIn("ABC", visitor.members())
    visitor = visit("import abc.ABC")
    self.assertOnlyIn("ABC", visitor.members())
    visitor = visit("import abc\nclass a(abc.ABC): pass")
    self.assertOnlyIn("ABC", visitor.members())

  def test_member_function(self):
    visitor = visit("from sys import exc_clear")
    self.assertOnlyIn("exc_clear", visitor.members())

  def test_member_import_star(self):
    visitor = visit("from abc import *\nclass a(ABC): pass")
    self.assertOnlyIn("ABC", visitor.members())
    visitor = visit("from sys import *\nprint(exc_clear())")
    self.assertOnlyIn("exc_clear", visitor.members())

  def test_member_constant(self):
    visitor = visit("from sys import version_info")
    self.assertOnlyIn("version_info", visitor.members())

  def test_member_kwargs(self):
    visitor = visit("from os import open\nfd = open(dir_fd = None)")
    self.assertOnlyIn([("open", "dir_fd")], visitor.kwargs())
