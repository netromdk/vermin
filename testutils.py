import unittest
import sys

# Export as short function name for tests.
from minpy import detect_min_versions_source as detect  # noqa:401

def current_version():
  return float(sys.version_info.major)

class MinpyTest(unittest.TestCase):
  """General test case class for all Minpy tests."""
  def assertOnlyIn(self, values, data):
    """Assert only value(s) is in data but ignores None values."""
    size = 1
    multiple = isinstance(values, list) or isinstance(values, tuple)
    if multiple:
      size = len(values)
    self.assertEqual(len(data) - data.count(None), size,
                     msg="ONLY looking for '{}' in '{}'".format(values, data))
    if multiple:
      for value in values:
        self.assertIn(value, data, msg="ONLY looking for '{}' in '{}'".format(value, data))
    else:
      self.assertIn(values, data, msg="ONLY looking for '{}' in '{}'".format(values, data))
