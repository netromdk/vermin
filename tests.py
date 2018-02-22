import unittest
import sys
from minpy import detect_min_versions_source as detect

def current_version():
  return float(sys.version_info.major)

class MinpyTests(unittest.TestCase):
  def __assertOnlyIn(self, value, data):
    """Assert only value is in data but ignores None values."""
    self.assertEqual(len(data) - data.count(None), 1)
    self.assertIn(value, data)

  def test_printv2(self):
    self.__assertOnlyIn(2.0, detect("print 'hello'"))

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    self.__assertOnlyIn(current_version(), detect("print('hello')"))

  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    self.__assertOnlyIn(2.0, detect("print 'hello'\nprint('hello')"))

  def test_formatv3(self):
    self.__assertOnlyIn(3.0, detect("'hello {}!'.format('world')"))
