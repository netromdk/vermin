from os.path import abspath
from multiprocessing import cpu_count

from minpy import SourceVisitor, parse_source, parse_detect_source, detect_min_versions_source,\
  combine_versions, InvalidVersionException, detect_paths, process_paths

from .testutils import MinpyTest, current_version

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
      self.assertEqual(mins, [0, 0])
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

  def test_longv2(self):
    visitor = visit("n = long(42)")
    self.assertTrue(visitor.longv2())
    visitor = visit("isinstance(42, long)")
    self.assertTrue(visitor.longv2())

  def test_bytesv3(self):
    if current_version() >= 3.0:
      visitor = visit("s = b'hello'")
      self.assertTrue(visitor.bytesv3())
      visitor = visit("s = B'hello'")
      self.assertTrue(visitor.bytesv3())

  def test_fstrings(self):
    if current_version() >= 3.6:
      visitor = visit("name = 'world'\nf'hello {name}'")
      self.assertTrue(visitor.fstrings())

  def test_strftime_directives(self):
    visitor = visit("from datetime import datetime\ndatetime.now().strftime('%A %d. %B %Y')")
    self.assertOnlyIn(("%A", "%d", "%B", "%Y"), visitor.strftime_directives())
    visitor = visit("from datetime import datetime\ndatetime.strptime('2018', '%Y')")
    self.assertOnlyIn("%Y", visitor.strftime_directives())

  def test_modules(self):
    visitor = visit("import ast\nimport sys, argparse\nfrom os import *")
    self.assertOnlyIn(("ast", "sys", "argparse", "os"), visitor.modules())

  def test_member_class(self):
    visitor = visit("from abc import ABC")
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

  def test_detect_minpy_min_versions(self):
    paths = detect_paths([abspath("minpy")])
    (mins, incomp) = process_paths(paths, cpu_count())
    self.assertOnlyIn((2.7, 3.0), mins)

  def test_combine_versions(self):
    with self.assertRaises(AssertionError):
      combine_versions([None], [None, None])
    self.assertEqual([2.0, 3.1], combine_versions([2.0, 3.0], [2.0, 3.1]))
    self.assertEqual([2.1, 3.0], combine_versions([2.1, 3.0], [2.0, 3.0]))
    self.assertEqual([None, 3.0], combine_versions([2.0, 3.0], [None, 3.0]))
    self.assertEqual([2.0, None], combine_versions([2.0, None], [2.0, 3.0]))
    self.assertEqual([None, None], combine_versions([2.0, 3.0], [None, None]))
    self.assertEqual([None, None], combine_versions([None, None], [2.0, 3.0]))
    with self.assertRaises(InvalidVersionException):
      combine_versions([2.0, None], [None, 3.0])
    with self.assertRaises(InvalidVersionException):
      combine_versions([None, 3.0], [2.0, None])
    self.assertEqual([0, 3.0], combine_versions([0, 3.0], [0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([0, 3.0], [2.0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 3.0], [0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 0], [2.0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 3.0], [2.0, 0]))

  def test_detect_min_version(self):
    self.assertEqual([2.6, 3.0], detect_min_versions_source("import abc"))

    # (2.6, 3.0) vs. (2.7, 3.2) = (2.7, 3.2)
    self.assertEqual([2.7, 3.2], detect_min_versions_source("import abc, argparse"))

    # (2.6, 3.0) vs. (None, 3.4) = (None, 3.4)
    self.assertEqual([None, 3.4], detect_min_versions_source("import abc\nfrom abc import ABC"))

    # (2.0, None) vs. (2.0, 3.0) = (2.0, None)
    self.assertEqual([2.0, None],
                     detect_min_versions_source("import repr\nfrom sys import getdefaultencoding"))

    # (2.0, None) vs. (None, 3.0) = both exclude the other major version -> exception!
    with self.assertRaises(InvalidVersionException):
      print(detect_min_versions_source("import copy_reg, http"))
