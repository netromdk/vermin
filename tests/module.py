from .testutils import VerminTest, detect

class VerminModuleTests(VerminTest):
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

  def test_Tkinter(self):
    self.assertOnlyIn(2.0, detect("import Tkinter"))

  def test_urllib2(self):
    self.assertOnlyIn(2.0, detect("import urllib2"))

  def test_xmlrpc(self):
    self.assertOnlyIn(3.0, detect("import xmlrpc"))

  def test_sets(self):
    self.assertOnlyIn(2.3, detect("import sets"))

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

  def test_unittest_mock(self):
    self.assertOnlyIn(3.3, detect("import unittest.mock"))

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

  def test___future__(self):
    self.assertOnlyIn((2.1, 3.0), detect("import __future__"))

  def test_atexit(self):
    self.assertOnlyIn((2.0, 3.0), detect("import atexit"))

  def test_bz2(self):
    self.assertOnlyIn((2.3, 3.0), detect("import bz2"))

  def test_cgitb(self):
    self.assertOnlyIn((2.2, 3.0), detect("import cgitb"))

  def test_collections(self):
    self.assertOnlyIn((2.4, 3.0), detect("import collections"))

  def test_contextlib(self):
    self.assertOnlyIn((2.5, 3.0), detect("import contextlib"))

  def test_cookielib(self):
    self.assertOnlyIn(2.4, detect("import cookielib"))

  def test_http_cookiejar(self):
    self.assertOnlyIn(3.0, detect("import http.cookiejar"))

  def test_cProfile(self):
    self.assertOnlyIn((2.5, 3.0), detect("import cProfile"))

  def test_csv(self):
    self.assertOnlyIn((2.3, 3.0), detect("import csv"))

  def test_ctypes(self):
    self.assertOnlyIn((2.5, 3.0), detect("import ctypes"))

  def test_datetime(self):
    self.assertOnlyIn((2.3, 3.0), detect("import datetime"))

  def test_decimal(self):
    self.assertOnlyIn((2.4, 3.0), detect("import decimal"))

  def test_difflib(self):
    self.assertOnlyIn((2.1, 3.0), detect("import difflib"))

  def test_DocXMLRPCServer(self):
    self.assertOnlyIn(2.3, detect("import DocXMLRPCServer"))

  def test_xmlrpc_server(self):
    self.assertOnlyIn(3.0, detect("import xmlrpc.server"))

  def test_xmlrpc_client(self):
    self.assertOnlyIn(3.0, detect("import xmlrpc.client"))

  def test_dummy_thread(self):
    self.assertOnlyIn(2.3, detect("import dummy_thread"))

  def test__dummy_thread(self):
    self.assertOnlyIn(3.0, detect("import _dummy_thread"))

  def test_dummy_threading(self):
    self.assertOnlyIn(2.3, detect("import dummy_threading"))

  def test_email(self):
    self.assertOnlyIn((2.2, 3.0), detect("import email"))

  def test_email_header(self):
    self.assertOnlyIn((2.2, 3.0), detect("import email.header"))

  def test_email_charset(self):
    self.assertOnlyIn((2.2, 3.0), detect("import email.charset"))

  def test_email_policy(self):
    self.assertOnlyIn(3.3, detect("import email.policy"))

  def test_email_contentmanager(self):
    self.assertOnlyIn(3.6, detect("import email.contentmanager"))

  def test_email_headerregistry(self):
    self.assertOnlyIn(3.6, detect("import email.headerregistry"))

  def test_fractions(self):
    self.assertOnlyIn((2.6, 3.0), detect("import fractions"))

  def test_functools(self):
    self.assertOnlyIn((2.5, 3.0), detect("import functools"))

  def test_future_builtins(self):
    self.assertOnlyIn(2.6, detect("import future_builtins"))

  def test_heapq(self):
    self.assertOnlyIn((2.3, 3.0), detect("import heapq"))

  def test_hmac(self):
    self.assertOnlyIn((2.2, 3.0), detect("import hmac"))

  def test_hotshot(self):
    self.assertOnlyIn(2.2, detect("import hotshot"))

  def test_importlib(self):
    self.assertOnlyIn((2.7, 3.1), detect("import importlib"))

  def test_inspect(self):
    self.assertOnlyIn((2.1, 3.0), detect("import inspect"))

  def test_io(self):
    self.assertOnlyIn((2.6, 3.0), detect("import io"))

  def test_itertools(self):
    self.assertOnlyIn((2.3, 3.0), detect("import itertools"))

  def test_json(self):
    self.assertOnlyIn((2.6, 3.0), detect("import json"))

  def test_logging(self):
    self.assertOnlyIn((2.3, 3.0), detect("import logging"))

  def test_modulefinder(self):
    self.assertOnlyIn((2.3, 3.0), detect("import modulefinder"))

  def test_msilib(self):
    self.assertOnlyIn((2.5, 3.0), detect("import msilib"))

  def test_numbers(self):
    self.assertOnlyIn((2.6, 3.0), detect("import numbers"))

  def test_optparse(self):
    self.assertOnlyIn((2.3, 3.0), detect("import optparse"))

  def test_ossaudiodev(self):
    self.assertOnlyIn((2.3, 3.0), detect("import ossaudiodev"))

  def test_pickletools(self):
    self.assertOnlyIn((2.3, 3.0), detect("import pickletools"))

  def test_pkgutil(self):
    self.assertOnlyIn((2.3, 3.0), detect("import pkgutil"))

  def test_platform(self):
    self.assertOnlyIn((2.3, 3.0), detect("import platform"))

  def test_pydoc(self):
    self.assertOnlyIn((2.1, 3.0), detect("import pydoc"))

  def test_runpy(self):
    self.assertOnlyIn((2.5, 3.0), detect("import runpy"))

  def test_shlex(self):
    self.assertOnlyIn((2.0, 3.0), detect("import shlex"))

  def test_SimpleXMLRPCServer(self):
    self.assertOnlyIn(2.2, detect("import SimpleXMLRPCServer"))

  def test_spwd(self):
    self.assertOnlyIn((2.5, 3.0), detect("import spwd"))

  def test_sqlite3(self):
    self.assertOnlyIn((2.5, 3.0), detect("import sqlite3"))

  def test_ssl(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ssl"))

  def test_stringprep(self):
    self.assertOnlyIn((2.3, 3.0), detect("import stringprep"))

  def test_subprocess(self):
    self.assertOnlyIn((2.4, 3.0), detect("import subprocess"))

  def test_sysconfig(self):
    self.assertOnlyIn((2.7, 3.2), detect("import sysconfig"))

  def test_tarfile(self):
    self.assertOnlyIn((2.3, 3.0), detect("import tarfile"))

  def test_textwrap(self):
    self.assertOnlyIn((2.3, 3.0), detect("import textwrap"))

  def test_timeit(self):
    self.assertOnlyIn((2.3, 3.0), detect("import timeit"))

  def test_uuid(self):
    self.assertOnlyIn((2.5, 3.0), detect("import uuid"))

  def test_warnings(self):
    self.assertOnlyIn((2.1, 3.0), detect("import warnings"))

  def test_weakref(self):
    self.assertOnlyIn((2.1, 3.0), detect("import weakref"))

  def test_wsgiref(self):
    self.assertOnlyIn((2.5, 3.0), detect("import wsgiref"))

  def test_xmlrpclib(self):
    self.assertOnlyIn(2.2, detect("import xmlrpclib"))

  def test_zipimport(self):
    self.assertOnlyIn((2.3, 3.0), detect("import zipimport"))

  def test_lzma(self):
    self.assertOnlyIn(3.3, detect("import lzma"))

  def test_venv(self):
    self.assertOnlyIn(3.3, detect("import venv"))
