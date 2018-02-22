import unittest
import sys
from minpy import detect_min_versions_source as detect

def current_version():
  return float(sys.version_info.major)

class MinpyTests(unittest.TestCase):
  def __assertOnlyIn(self, values, data):
    """Assert only value(s) is in data but ignores None values."""
    size = 1
    multiple = isinstance(values, list) or isinstance(values, tuple)
    if multiple:
      size = len(values)
    self.assertEqual(len(data) - data.count(None), size)
    if multiple:
      for value in values:
        self.assertIn(value, data)
    else:
      self.assertIn(values, data)

  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.__assertOnlyIn(2.0, detect("print 'hello'"))

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    self.__assertOnlyIn(current_version(), detect("print('hello')"))

  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.__assertOnlyIn(2.0, detect("print 'hello'\nprint('hello')"))

  def test_format(self):
    vers = detect("'hello {}!'.format('world')")
    self.__assertOnlyIn((2.7, 3.0), vers)

  def test_module_argparse(self):
    self.__assertOnlyIn((2.7, 3.2), detect("import argparse"))
    self.__assertOnlyIn((2.7, 3.2), detect("from argparse import *"))

  def test_module_abc(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import abc"))

  def test_module_multiprocessing(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import multiprocessing"))

  def test_member_ABC_of_abc(self):
    self.__assertOnlyIn(3.4, detect("import abc.ABC"))
    self.__assertOnlyIn(3.4, detect("from abc import ABC"))
