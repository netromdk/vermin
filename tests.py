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

  def test_module_ast(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import ast"))

  ### Members ###

  ##### Classes #####

  def test_member_ABC_of_abc(self):
    self.__assertOnlyIn(3.4, detect("import abc.ABC"))
    self.__assertOnlyIn(3.4, detect("from abc import ABC"))

  ##### Functions #####

  def test_member_exc_clear_of_sys(self):
    self.__assertOnlyIn(2.3, detect("import sys.exc_clear"))

  def test_member_used_in_context_of_star_import(self):
    self.__assertOnlyIn(2.3, detect("from sys import *\nvar=exc_clear"))
    self.__assertOnlyIn(2.3, detect("from sys import *\nprint(exc_clear)"))

  def test_member_getcheckinterval_of_sys(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import sys.getcheckinterval"))

  def test_member_getdefaultencoding_of_sys(self):
    self.__assertOnlyIn((2.0, 3.0), detect("import sys.getdefaultencoding"))

  def test_member_getdlopenflags_of_sys(self):
    self.__assertOnlyIn((2.2, 3.0), detect("import sys.getdlopenflags"))

  def test_member_getfilesystemencoding_of_sys(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import sys.getfilesystemencoding"))

  def test_member_getsizeof_of_sys(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import sys.getsizeof"))

  def test_member_getprofile_of_sys(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import sys.getprofile"))

  def test_member_gettrace_of_sys(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import sys.gettrace"))

  def test_member_getwindowsversion_of_sys(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import sys.getwindowsversion"))

  def test_member_commonpath_of_os_path(self):
    self.__assertOnlyIn(3.5, detect("import os.path.commonpath"))

  def test_member_getctime_of_os_path(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import os.path.getctime"))

  def test_member_ismount_of_os_path(self):
    self.__assertOnlyIn(3.4, detect("import os.path.ismount"))

  def test_member_lexists_of_os_path(self):
    self.__assertOnlyIn((2.4, 3.0), detect("import os.path.lexists"))

  def test_member_realpath_of_os_path(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import os.path.realpath"))

  def test_member_getpgid_of_os(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import os.getpgid"))

  def test_member_getresgid_of_os(self):
    self.__assertOnlyIn((2.7, 3.0), detect("import os.getresgid"))

  def test_member_getresuid_of_os(self):
    self.__assertOnlyIn((2.7, 3.0), detect("import os.getresuid"))

  def test_member_getsid_of_os(self):
    self.__assertOnlyIn((2.4, 3.0), detect("import os.getsid"))

  def test_member_initgroups_of_os(self):
    self.__assertOnlyIn((2.7, 3.0), detect("import os.initgroups"))

  def test_member_setgroups_of_os(self):
    self.__assertOnlyIn((2.2, 3.0), detect("import os.setgroups"))

  def test_member_setresgid_of_os(self):
    self.__assertOnlyIn((2.7, 3.0), detect("import os.setresgid"))

  def test_member_setresuid_of_os(self):
    self.__assertOnlyIn((2.7, 3.0), detect("import os.setresuid"))

  ##### Variables #####

  def test_member_flags_of_sys(self):
    self.__assertOnlyIn((2.6, 3.0), detect("import sys.flags"))

  def test_member_supports_unicode_filenames_of_sys(self):
    self.__assertOnlyIn((2.3, 3.0), detect("import sys.supports_unicode_filenames"))
