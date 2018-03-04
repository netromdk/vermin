from testutils import MinpyTest, detect

class MinpyModuleTests(MinpyTest):
  def test_argparse(self):
    self.assertOnlyIn((2.7, 3.2), detect("import argparse"))
    self.assertOnlyIn((2.7, 3.2), detect("from argparse import *"))

  def test_abc(self):
    self.assertOnlyIn((2.6, 3.0), detect("import abc"))

  def test_multiprocessing(self):
    self.assertOnlyIn((2.6, 3.0), detect("import multiprocessing"))

  def test_md5(self):
    self.assertOnlyIn(2.0, detect("import md5"))

  def test__winreg(self):
    self.assertOnlyIn(2.0, detect("import _winreg"))

  def test_winreg(self):
    self.assertOnlyIn(3.0, detect("import winreg"))

  def test_ConfigParser(self):
    self.assertOnlyIn(2.0, detect("import ConfigParser"))

  def test_configparser(self):
    self.assertOnlyIn(3.0, detect("import configparser"))

  def test_copy_reg(self):
    self.assertOnlyIn(2.0, detect("import copy_reg"))

  def test_copyreg(self):
    self.assertOnlyIn(3.0, detect("import copyreg"))

  def test_Queue(self):
    self.assertOnlyIn(2.0, detect("import Queue"))

  def test_queue(self):
    self.assertOnlyIn(3.0, detect("import queue"))

  def test_SocketServer(self):
    self.assertOnlyIn(2.0, detect("import SocketServer"))

  def test_socketserver(self):
    self.assertOnlyIn(3.0, detect("import socketserver"))

  def test_markupbase(self):
    self.assertOnlyIn(2.0, detect("import markupbase"))

  def test__markupbase(self):
    self.assertOnlyIn(3.0, detect("import _markupbase"))

  def test_repr(self):
    self.assertOnlyIn(2.0, detect("import repr"))

  def test_reprlib(self):
    self.assertOnlyIn(3.0, detect("import reprlib"))

  def test_dbm_io(self):
    self.assertOnlyIn(3.0, detect("import dbm.io"))

  def test_dbm_ndbm(self):
    self.assertOnlyIn(3.0, detect("import dbm.ndbm"))

  def test_dbm_os(self):
    self.assertOnlyIn(3.0, detect("import dbm.os"))

  def test_dbm_struct(self):
    self.assertOnlyIn(3.0, detect("import dbm.struct"))

  def test_dbm_sys(self):
    self.assertOnlyIn(3.0, detect("import dbm.sys"))

  def test_dbm_whichdb(self):
    self.assertOnlyIn(3.0, detect("import dbm.whichdb"))

  def test_html(self):
    self.assertOnlyIn(3.0, detect("import html"))

  def test_HTMLParser(self):
    self.assertOnlyIn(2.2, detect("import HTMLParser"))

  def test_htmlentitydefs(self):
    self.assertOnlyIn(2.0, detect("import htmlentitydefs"))

  def test_http(self):
    self.assertOnlyIn(3.0, detect("import http"))

  def test_tkinter(self):
    self.assertOnlyIn(3.0, detect("import tkinter"))

  def test_urllib2(self):
    self.assertOnlyIn(2.0, detect("import urllib2"))

  def test_xmlrpc(self):
    self.assertOnlyIn(3.0, detect("import xmlrpc"))

  def test_sets(self):
    self.assertOnlyIn(2.0, detect("import sets"))

  def test_new(self):
    self.assertOnlyIn(2.0, detect("import new"))

  def test___builtin__(self):
    self.assertOnlyIn(2.0, detect("import __builtin__"))

  def test_builtins(self):
    self.assertOnlyIn(3.0, detect("import builtins"))

  def test_string_letters(self):
    self.assertOnlyIn(2.0, detect("import string.letters"))

  def test_string_lowercase(self):
    self.assertOnlyIn(2.0, detect("import string.lowercase"))

  def test_string_uppercase(self):
    self.assertOnlyIn(2.0, detect("import string.uppercase"))

  def test_ast(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ast"))

  def test_unittest(self):
    self.assertOnlyIn((2.1, 3.0), detect("import unittest"))

  def test_secrets(self):
    self.assertOnlyIn(3.6, detect("import secrets"))

  def test_asyncio(self):
    self.assertOnlyIn(3.4, detect("import asyncio"))

  def test_typing(self):
    self.assertOnlyIn(3.5, detect("import typing"))

  def test_tracemalloc(self):
    self.assertOnlyIn(3.4, detect("import tracemalloc"))

  def test_hashlib(self):
    self.assertOnlyIn((2.5, 3.0), detect("import hashlib"))

  def test_faulthandler(self):
    self.assertOnlyIn(3.3, detect("import faulthandler"))

  def test_ipaddress(self):
    self.assertOnlyIn(3.3, detect("import ipaddress"))
