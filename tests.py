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
    self.assertEqual(len(data) - data.count(None), size,
                     msg="ONLY looking for '{}' in '{}'".format(values, data))
    if multiple:
      for value in values:
        self.assertIn(value, data, msg="ONLY looking for '{}' in '{}'".format(value, data))
    else:
      self.assertIn(values, data, msg="ONLY looking for '{}' in '{}'".format(values, data))

  ### Language ###

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

  ### Modules ###

  def test_module_argparse(self):
    self.__assertOnlyIn((2.7, 3.2), detect("import argparse"))
    self.__assertOnlyIn((2.7, 3.2), detect("from argparse import *"))

  def test_module_abc(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import abc"))

  def test_module_multiprocessing(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import multiprocessing"))

  def test_module_md5(self):
    self.__assertOnlyIn(2.0, detect("import md5"))

  def test_module__winreg(self):
    self.__assertOnlyIn(2.0, detect("import _winreg"))

  def test_module_winreg(self):
    self.__assertOnlyIn(3.0, detect("import winreg"))

  def test_module_ConfigParser(self):
    self.__assertOnlyIn(2.0, detect("import ConfigParser"))

  def test_module_configparser(self):
    self.__assertOnlyIn(3.0, detect("import configparser"))

  def test_module_copy_reg(self):
    self.__assertOnlyIn(2.0, detect("import copy_reg"))

  def test_module_copyreg(self):
    self.__assertOnlyIn(3.0, detect("import copyreg"))

  def test_module_Queue(self):
    self.__assertOnlyIn(2.0, detect("import Queue"))

  def test_module_queue(self):
    self.__assertOnlyIn(3.0, detect("import queue"))

  def test_module_SocketServer(self):
    self.__assertOnlyIn(2.0, detect("import SocketServer"))

  def test_module_socketserver(self):
    self.__assertOnlyIn(3.0, detect("import socketserver"))

  def test_module_markupbase(self):
    self.__assertOnlyIn(2.0, detect("import markupbase"))

  def test_module__markupbase(self):
    self.__assertOnlyIn(3.0, detect("import _markupbase"))

  def test_module_repr(self):
    self.__assertOnlyIn(2.0, detect("import repr"))

  def test_module_reprlib(self):
    self.__assertOnlyIn(3.0, detect("import reprlib"))

  def test_module_dbm_io(self):
    self.__assertOnlyIn(3.0, detect("import dbm.io"))

  def test_module_dbm_ndbm(self):
    self.__assertOnlyIn(3.0, detect("import dbm.ndbm"))

  def test_module_dbm_os(self):
    self.__assertOnlyIn(3.0, detect("import dbm.os"))

  def test_module_dbm_struct(self):
    self.__assertOnlyIn(3.0, detect("import dbm.struct"))

  def test_module_dbm_sys(self):
    self.__assertOnlyIn(3.0, detect("import dbm.sys"))

  def test_module_dbm_whichdb(self):
    self.__assertOnlyIn(3.0, detect("import dbm.whichdb"))

  def test_module_html(self):
    self.__assertOnlyIn(3.0, detect("import html"))

  def test_module_HTMLParser(self):
    self.__assertOnlyIn(2.2, detect("import HTMLParser"))

  def test_module_htmlentitydefs(self):
    self.__assertOnlyIn(2.0, detect("import htmlentitydefs"))

  def test_module_http(self):
    self.__assertOnlyIn(3.0, detect("import http"))

  def test_module_tkinter(self):
    self.__assertOnlyIn(3.0, detect("import tkinter"))

  def test_module_urllib2(self):
    self.__assertOnlyIn(2.0, detect("import urllib2"))

  def test_module_xmlrpc(self):
    self.__assertOnlyIn(3.0, detect("import xmlrpc"))

  def test_module_sets(self):
    self.__assertOnlyIn(2.0, detect("import sets"))

  def test_module_new(self):
    self.__assertOnlyIn(2.0, detect("import new"))

  def test_module___builtin__(self):
    self.__assertOnlyIn(2.0, detect("import __builtin__"))

  def test_module_builtins(self):
    self.__assertOnlyIn(3.0, detect("import builtins"))

  def test_module_string_letters(self):
    self.__assertOnlyIn(2.0, detect("import string.letters"))

  def test_module_string_lowercase(self):
    self.__assertOnlyIn(2.0, detect("import string.lowercase"))

  def test_module_string_uppercase(self):
    self.__assertOnlyIn(2.0, detect("import string.uppercase"))

  ### Members ###

  def test_member_ABC_of_abc(self):
    self.__assertOnlyIn(3.4, detect("import abc.ABC"))
    self.__assertOnlyIn(3.4, detect("from abc import ABC"))
