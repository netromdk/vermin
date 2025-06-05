from .testutils import VerminTest

class VerminModuleTests(VerminTest):
  def test_argparse(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import argparse"))
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from argparse import *"))
    self.assertTrue(self.config.add_backport("argparse"))
    self.assertOnlyIn(((2, 3), (3, 1)), self.detect("import argparse"))

  def test_abc(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import abc"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import abc as ABC"))

  def test_multiprocessing(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import multiprocessing"))

  def test_md5(self):
    self.assertOnlyIn((2, 0), self.detect("import md5"))

  def test__winreg(self):
    self.assertOnlyIn((2, 0), self.detect("import _winreg"))

  def test_winreg(self):
    self.assertOnlyIn((3, 0), self.detect("import winreg"))

  def test_BaseHTTPServer(self):
    self.assertOnlyIn((2, 0), self.detect("import BaseHTTPServer"))

  def test_ConfigParser(self):
    self.assertOnlyIn((2, 0), self.detect("import ConfigParser"))

  def test_configparser(self):
    self.assertOnlyIn((3, 0), self.detect("import configparser"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import configparser"))

  def test_copy_reg(self):
    self.assertOnlyIn((2, 0), self.detect("import copy_reg"))

  def test_copyreg(self):
    self.assertOnlyIn((3, 0), self.detect("import copyreg"))

  def test_Queue(self):
    self.assertOnlyIn((2, 0), self.detect("import Queue"))

  def test_queue(self):
    self.assertOnlyIn((3, 0), self.detect("import queue"))

  def test_SocketServer(self):
    self.assertOnlyIn((2, 0), self.detect("import SocketServer"))

  def test_socketserver(self):
    self.assertOnlyIn((3, 0), self.detect("import socketserver"))

  def test_markupbase(self):
    self.assertOnlyIn((2, 0), self.detect("import markupbase"))

  def test__markupbase(self):
    self.assertOnlyIn((3, 0), self.detect("import _markupbase"))

  def test__thread(self):
    self.assertOnlyIn((3, 0), self.detect("import _thread"))

  def test_random(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import random"))

  def test_repr(self):
    self.assertOnlyIn((2, 0), self.detect("import repr"))

  def test_reprlib(self):
    self.assertOnlyIn((3, 0), self.detect("import reprlib"))

  def test_dbm_io(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.io"))

  def test_dbm_ndbm(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.ndbm"))

  def test_dbm_os(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.os"))

  def test_dbm_struct(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.struct"))

  def test_dbm_sqlite3(self):
    self.assertOnlyIn((3, 13), self.detect("import dbm.sqlite3"))

  def test_dbm_sys(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.sys"))

  def test_dbm_whichdb(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.whichdb"))

  def test_dbm_gnu(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.gnu"))

  def test_dbm_dumb(self):
    self.assertOnlyIn((3, 0), self.detect("import dbm.dumb"))

  def test_html(self):
    self.assertOnlyIn((3, 0), self.detect("import html"))

  def test_HTMLParser(self):
    self.assertOnlyIn((2, 2), self.detect("import HTMLParser"))

  def test_htmlentitydefs(self):
    self.assertOnlyIn((2, 0), self.detect("import htmlentitydefs"))

  def test_http(self):
    self.assertOnlyIn((3, 0), self.detect("import http"))

  def test_tkinter(self):
    self.assertOnlyIn((3, 0), self.detect("import tkinter"))

  def test_Tkinter(self):
    self.assertOnlyIn((2, 0), self.detect("import Tkinter"))

  def test_tomllib(self):
    self.assertOnlyIn((3, 11), self.detect("import tomllib"))

  def test_urllib2(self):
    self.assertOnlyIn((2, 0), self.detect("import urllib2"))

  def test_xmlrpc(self):
    self.assertOnlyIn((3, 0), self.detect("import xmlrpc"))

  def test_sets(self):
    self.assertOnlyIn((2, 3), self.detect("import sets"))

  def test_socket(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import socket"))

  def test_new(self):
    self.assertOnlyIn((2, 0), self.detect("import new"))

  def test___builtin__(self):
    self.assertOnlyIn((2, 0), self.detect("import __builtin__"))

  def test_builtins(self):
    self.assertOnlyIn((3, 0), self.detect("import builtins"))

  def test_ast(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ast"))

  def test__ast(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import _ast"))

  def test_unittest(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import unittest"))

  def test_unittest_mock(self):
    self.assertOnlyIn((3, 3), self.detect("import unittest.mock"))

  def test_secrets(self):
    self.assertOnlyIn((3, 6), self.detect("import secrets"))

  def test_asyncio(self):
    self.assertOnlyIn((3, 4), self.detect("import asyncio"))
    self.assertTrue(self.config.add_backport("asyncio"))
    self.assertOnlyIn((3, 3), self.detect("import asyncio"))

  def test_asyncore(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import asyncore"))

  def test_atexit(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import atexit"))

  def test_audioop(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import audioop"))

  def test_typing(self):
    self.assertOnlyIn((3, 5), self.detect("import typing"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import typing"))

  def test_tracemalloc(self):
    self.assertOnlyIn((3, 4), self.detect("import tracemalloc"))

  def test_hashlib(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import hashlib"))

  def test_faulthandler(self):
    self.assertOnlyIn((3, 3), self.detect("import faulthandler"))
    self.assertTrue(self.config.add_backport("faulthandler"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import faulthandler"))

  def test_ipaddress(self):
    self.assertOnlyIn((3, 3), self.detect("import ipaddress"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)), self.detect("import ipaddress"))

  def test___future__(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import __future__"))

  def test_bisect(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import bisect"))

  def test_bz2(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import bz2"))

  def test_calendar(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import calendar"))

  def test_cgitb(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import cgitb"))

  def test_collections(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import collections"))

  def test_collections_abc(self):
    self.assertOnlyIn((3, 3), self.detect("import collections.abc"))

  def test_compileall(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import compileall"))

  def test_contextlib(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import contextlib"))

  def test_cookielib(self):
    self.assertOnlyIn((2, 4), self.detect("import cookielib"))

  def test_http_cookiejar(self):
    self.assertOnlyIn((3, 0), self.detect("import http.cookiejar"))

  def test_http_server(self):
    self.assertOnlyIn((3, 0), self.detect("import http.server"))

  def test_cProfile(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import cProfile"))

  def test_csv(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import csv"))

  def test_ctypes(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import ctypes"))

  def test_datetime(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import datetime"))

  def test_decimal(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import decimal"))

  def test_difflib(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import difflib"))

  def test_DocXMLRPCServer(self):
    self.assertOnlyIn((2, 3), self.detect("import DocXMLRPCServer"))

  def test_xmlrpc_server(self):
    self.assertOnlyIn((3, 0), self.detect("import xmlrpc.server"))

  def test_xmlrpc_client(self):
    self.assertOnlyIn((3, 0), self.detect("import xmlrpc.client"))

  def test_dummy_thread(self):
    self.assertOnlyIn((2, 3), self.detect("import dummy_thread"))

  def test__dummy_thread(self):
    self.assertOnlyIn((3, 0), self.detect("import _dummy_thread"))

  def test_dummy_threading(self):
    self.assertOnlyIn((2, 3), self.detect("import dummy_threading"))

  def test_email(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email"))

  def test_email_header(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email.header"))

  def test_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import email.errors"))

  def test_email_message(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email.message"))

  def test_email_parser(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email.parser"))

  def test_email_utils(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email.utils"))

  def test_email_charset(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import email.charset"))

  def test_email_policy(self):
    self.assertOnlyIn((3, 3), self.detect("import email.policy"))

  def test_email_contentmanager(self):
    self.assertOnlyIn((3, 4), self.detect("import email.contentmanager"))

  def test_email_headerregistry(self):
    self.assertOnlyIn((3, 3), self.detect("import email.headerregistry"))

  def test_encodings_idna(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import encodings.idna"))

  def test_encodings_utf_8_sig(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import encodings.utf_8_sig"))

  def test_fractions(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import fractions"))

  def test_functools(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import functools"))

  def test_future_builtins(self):
    self.assertOnlyIn((2, 6), self.detect("import future_builtins"))

  def test_heapq(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import heapq"))

  def test_hmac(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import hmac"))

  def test_hotshot(self):
    self.assertOnlyIn((2, 2), self.detect("import hotshot"))

  def test_imghdr(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import imghdr"))

  def test_imp(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import imp"))

  def test_importlib(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import importlib"))
    self.assertTrue(self.config.add_backport("importlib"))
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import importlib"))

  def test_inspect(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import inspect"))

  def test_io(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import io"))

  def test_itertools(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import itertools"))

  def test_json(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import json"))

  def test_locale(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import locale"))

  def test_logging(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import logging"))

  def test_logging_config(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import logging.config"))

  def test_logging_handlers(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import logging.handlers"))

  def test_modulefinder(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import modulefinder"))

  def test_msilib(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import msilib"))

  def test_numbers(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import numbers"))

  def test_optparse(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import optparse"))

  def test_ossaudiodev(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import ossaudiodev"))

  def test_pickletools(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import pickletools"))

  def test_pkgutil(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import pkgutil"))

  def test_platform(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import platform"))

  def test_popen2(self):
    self.assertOnlyIn((2, 0), self.detect("import popen2"))

  def test_pyclbr(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import pyclbr"))

  def test_pydoc(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import pydoc"))

  def test_runpy(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import runpy"))

  def test_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 2), self.detect("import SimpleXMLRPCServer"))

  def test_spwd(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import spwd"))

  def test_sqlite3(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import sqlite3"))

  def test_ssl(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ssl"))

  def test_stringprep(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import stringprep"))

  def test_subprocess(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import subprocess"))

  def test_sysconfig(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import sysconfig"))

  def test_tarfile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import tarfile"))

  def test_textwrap(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import textwrap"))

  def test_timeit(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import timeit"))

  def test_uuid(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import uuid"))

  def test_warnings(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import warnings"))

  def test_weakref(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import weakref"))

  def test_wsgiref(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import wsgiref"))

  def test_wsgiref_types(self):
    self.assertOnlyIn((3, 11), self.detect("import wsgiref.types"))

  def test_xml_dom(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.dom"))

  def test_xml_dom_minidom(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.dom.minidom"))

  def test_xml_dom_pulldom(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.dom.pulldom"))

  def test_xml_etree_ElementTree(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import xml.etree.ElementTree"))

  def test_xml_etree_ElementInclude(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import xml.etree.ElementInclude"))

  def test_xml_parsers_expat(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.parsers.expat"))

  def test_xml_sax(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.sax"))

  def test_xml_sax_handler(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.sax.handler"))

  def test_xml_sax_saxutils(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.sax.saxutils"))

  def test_xml_sax_xmlreader(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import xml.sax.xmlreader"))

  def test_xmlrpclib(self):
    self.assertOnlyIn((2, 2), self.detect("import xmlrpclib"))

  def test_zipimport(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import zipimport"))

  def test_lzma(self):
    self.assertOnlyIn((3, 3), self.detect("import lzma"))

  def test_venv(self):
    self.assertOnlyIn((3, 3), self.detect("import venv"))

  def test_pathlib(self):
    self.assertOnlyIn((3, 4), self.detect("import pathlib"))

  def test_pdb(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("import pdb"))

  def test_contextvars(self):
    self.assertOnlyIn((3, 7), self.detect("import contextvars"))
    self.assertTrue(self.config.add_backport("contextvars"))
    self.assertOnlyIn((3, 5), self.detect("import contextvars"))

  def test_dataclasses(self):
    self.assertOnlyIn((3, 7), self.detect("import dataclasses"))
    self.assertTrue(self.config.add_backport("dataclasses"))
    self.assertOnlyIn((3, 6), self.detect("import dataclasses"))

  def test_importlib_resources(self):
    self.assertOnlyIn((3, 7), self.detect("import importlib.resources"))

  def test_importlib_resources_abc(self):
    self.assertOnlyIn((3, 11), self.detect("import importlib.resources.abc"))

  def test_concurrent_futures(self):
    self.assertOnlyIn((3, 2), self.detect("import concurrent.futures"))

  def test_importlib_metadata(self):
    self.assertOnlyIn((3, 8), self.detect("import importlib.metadata"))

  def test_multiprocessing_pool(self):
    self.assertOnlyIn((3, 0), self.detect("import multiprocessing.pool"))

  def test_multiprocessing_shared_memory(self):
    self.assertOnlyIn((3, 8), self.detect("import multiprocessing.shared_memory"))

  def test_statistics(self):
    self.assertOnlyIn((3, 4), self.detect("import statistics"))
    self.assertTrue(self.config.add_backport("statistics"))
    self.assertOnlyIn(((2, 6), (3, 4)), self.detect("import statistics"))

  def test_ensurepip(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import ensurepip"))

  def test_enum(self):
    self.assertOnlyIn((3, 4), self.detect("import enum"))
    self.assertTrue(self.config.add_backport("enum"))
    self.assertOnlyIn(((2, 4), (3, 3)), self.detect("import enum"))

  def test_selectors(self):
    self.assertOnlyIn((3, 4), self.detect("import selectors"))

  def test_zipapp(self):
    self.assertOnlyIn((3, 5), self.detect("import zipapp"))

  def test_urlparse(self):
    self.assertOnlyIn((2, 0), self.detect("import urlparse"))

  def test_urllib_parse(self):
    self.assertOnlyIn((3, 0), self.detect("import urllib.parse"))

  def test_zoneinfo(self):
    self.assertOnlyIn((3, 9), self.detect("import zoneinfo"))

  def test_graphlib(self):
    self.assertOnlyIn((3, 9), self.detect("import graphlib"))

  def test_test_support_socket_helper(self):
    self.assertOnlyIn((3, 9), self.detect("import test.support.socket_helper"))

  def test_test_support_bytecode_helper(self):
    self.assertOnlyIn((3, 9), self.detect("import test.support.bytecode_helper"))

  def test_test_support_threading_helper(self):
    self.assertOnlyIn((3, 10), self.detect("import test.support.threading_helper"))

  def test_test_support_os_helper(self):
    self.assertOnlyIn((3, 10), self.detect("import test.support.os_helper"))

  def test_test_support_import_helper(self):
    self.assertOnlyIn((3, 10), self.detect("import test.support.import_helper"))

  def test_test_support_warnings_helper(self):
    self.assertOnlyIn((3, 10), self.detect("import test.support.warnings_helper"))
