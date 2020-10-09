import unittest
import sys
import os
from tempfile import NamedTemporaryFile

from vermin import SourceVisitor, Parser

def current_major_version():
  return float(sys.version_info.major)

def current_version():
  return current_major_version() + float(sys.version_info.minor) / 10.0

class VerminTest(unittest.TestCase):
  def __init__(self, methodName):
    super(VerminTest, self).__init__(methodName)

    # Allow test diffs of any size (instead of 640 char max).
    self.maxDiff = None

  """General test case class for all Vermin tests."""
  def assertOnlyIn(self, values, data):
    """Assert only value(s) is in data but ignores None and 0 values."""
    size = 1
    multiple = isinstance(values, list) or isinstance(values, tuple)
    if multiple:
      # Unless it's a tuple of ints, then it's a version and not a multiple.
      if all(isinstance(x, int) for x in values):
        multiple = False
      else:
        size = len(values)
    self.assertEqual(len(data) - data.count(None) - data.count(0) - data.count((0, 0)), size,
                     msg="ONLY looking for '{}' in '{}'".format(values, data))
    if multiple:
      for value in values:
        self.assertIn(value, data, msg="ONLY looking for '{}' in '{}'".format(value, data))
    else:
      self.assertIn(values, data, msg="ONLY looking for '{}' in '{}'".format(values, data))

  def assertContainsDict(self, dictionary, data):
    """Assert data contains all keys and values of dictionary input."""
    for key in dictionary:
      self.assertTrue(key in data, msg="Data doesn't have key '{}'".format(key))
      value = dictionary[key]
      value2 = data[key]
      self.assertEqual(value, value2,
                       msg="key={}, value={} != target={}".format(key, value, value2))

  def assertEmpty(self, data):
    self.assertTrue(len(data) == 0,
                    msg="Input not empty! size={}, '{}'".format(len(data), data))

  def assertEqualItems(self, expected, actual):
    """Assert that two sequences contain the same elements, regardless of the ordering.
`assertItemsEqual()` is a 2.7 unittest function. In 3.2 it's called `assertCountEqual()`. This
override is made to work for all versions, also 3.0-3.1."""
    v = current_version()
    if v >= 3.2:
      self.assertCountEqual(expected, actual)
    if v >= 2.7 and v < 3.0:  # pragma: no cover
      self.assertItemsEqual(expected, actual)
    else:
      self.assertEqual(sorted(expected), sorted(actual))

def visit(source, fstring_self_doc=False):
  parser = Parser(source)
  (node, novermin) = parser.parse()
  visitor = SourceVisitor()
  visitor.set_no_lines(novermin)
  visitor.set_fstring_self_doc_enabled(fstring_self_doc)
  visitor.tour(node)
  return visitor

class ScopedTemporaryFile:
  """Creates a temporary file that is automatically removed when this instance goes out of scope.
The difference to NamedTemporaryFile is that it isn't deleted when closing the file.
  """

  def __init__(self, suffix=".py"):
    self.__fp = NamedTemporaryFile(suffix=suffix, delete=False)

  def __del__(self):
    os.remove(self.path())

  def __enter__(self):
    return self

  def __exit__(self, _exc_type, _exc_val, _exc_tb):
    return False

  def write(self, data, newline=False):
    self.__fp.write(data)
    if newline:
      self.__fp.write(b"\n")

  def writeln(self, data):
    self.write(data, newline=True)

  def close(self):
    self.__fp.close()

  def path(self):
    return self.__fp.name
