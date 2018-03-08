import unittest
import sys

# Export as short function name for tests.
from vermin import detect_min_versions_source as detect  # noqa:401

def current_major_version():
  return float(sys.version_info.major)

def current_version():
  return current_major_version() + float(sys.version_info.minor) / 10.0

class VerminTest(unittest.TestCase):
  """General test case class for all Vermin tests."""
  def assertOnlyIn(self, values, data):
    """Assert only value(s) is in data but ignores None and 0 values."""
    size = 1
    multiple = isinstance(values, list) or isinstance(values, tuple)
    if multiple:
      size = len(values)
    self.assertEqual(len(data) - data.count(None) - data.count(0), size,
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
