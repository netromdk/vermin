from .testutils import VerminTest, detect

class VerminClassMemberTests(VerminTest):
  def test_ABC_of_abc(self):
    self.assertOnlyIn(3.4, detect("from abc import ABC"))

  def test_PathLike_of_os(self):
    self.assertOnlyIn(3.6, detect("from os import PathLike"))

  def test_terminal_size_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import terminal_size"))

  def test_Barrier_of_multiprocessing(self):
    self.assertOnlyIn(3.3, detect("from multiprocessing import Barrier"))

  def test_TextTestResult_of_unittest(self):
    self.assertOnlyIn((2.7, 3.0), detect("from unittest import TextTestResult"))

  def test_timezone_of_datetime(self):
    self.assertOnlyIn(3.2, detect("from datetime import timezone"))

  def test_Collection_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import Collection"))

  def test_Deque_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import Deque"))

  def test_ContextManager_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import ContextManager"))

  def test_Counter_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import Counter"))

  def test_ChainMap_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import ChainMap"))

  def test_AsyncGenerator_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import AsyncGenerator"))

  def test_Text_of_typing(self):
    self.assertOnlyIn(3.6, detect("from typing import Text"))

  def test_ClassVar_of_typing(self):
    self.assertOnlyIn(3.5, detect("from typing import ClassVar"))

  def test_DomainFilter_of_tracemalloc(self):
    self.assertOnlyIn(3.6, detect("from tracemalloc import DomainFilter"))

  def test_Counter_of_collections(self):
    self.assertOnlyIn((2.7, 3.1), detect("from collections import Counter"))

  def test_deque_of_collections(self):
    self.assertOnlyIn((2.4, 3.0), detect("from collections import deque"))

  def test_defaultdict_of_collections(self):
    self.assertOnlyIn((2.5, 3.0), detect("from collections import defaultdict"))

  def test_namedtuple_of_collections(self):
    self.assertOnlyIn((2.6, 3.0), detect("from collections import namedtuple"))

  def test_OrderedDict_of_collections(self):
    self.assertOnlyIn((2.7, 3.1), detect("from collections import OrderedDict"))

  def test_UserDict_of_collections(self):
    self.assertOnlyIn(3.0, detect("from collections import UserDict"))

  def test_UserList_of_collections(self):
    self.assertOnlyIn(3.0, detect("from collections import UserList"))

  def test_UserString_of_collections(self):
    self.assertOnlyIn(3.0, detect("from collections import UserString"))

  def test_AbstractContextManager_of_contextlib(self):
    self.assertOnlyIn(3.6, detect("from contextlib import AbstractContextManager"))

  def test_ContextDecorator_of_contextlib(self):
    self.assertOnlyIn(3.2, detect("from contextlib import ContextDecorator"))

  def test_ExitStack_of_contextlib(self):
    self.assertOnlyIn(3.3, detect("from contextlib import ExitStack"))

  def test_unix_dialect_of_csv(self):
    self.assertOnlyIn(3.2, detect("from csv import unix_dialect"))

  def test_c_longdouble_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("from ctypes import c_longdouble"))

  def test_c_bool_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("from ctypes import c_bool"))

  def test_c_ssize_t_of_ctypes(self):
    self.assertOnlyIn((2.7, 3.2), detect("from ctypes import c_ssize_t"))

  def test_HtmlDiff_of_difflib(self):
    self.assertOnlyIn((2.4, 3.0), detect("from difflib import HtmlDiff"))

  def test_Signature_of_inspect(self):
    self.assertOnlyIn(3.3, detect("from inspect import Signature"))

  def test_Parameter_of_inspect(self):
    self.assertOnlyIn(3.3, detect("from inspect import Parameter"))

  def test_BoundArguments_of_inspect(self):
    self.assertOnlyIn(3.3, detect("from inspect import BoundArguments"))

  def test_JSONDecodeError_of_json(self):
    self.assertOnlyIn(3.5, detect("from json import JSONDecodeError"))

  def test_LoggerAdapter_of_logging(self):
    self.assertOnlyIn((2.6, 3.0), detect("from logging import LoggerAdapter"))

  def test_ModuleInfo_of_pkgutil(self):
    self.assertOnlyIn(3.6, detect("from pkgutil import ModuleInfo"))

  def test_CGIXMLRPCRequestHandler_of_SimpleXMLRPCServer(self):
    self.assertOnlyIn(2.3, detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler"))

  def test_SSLContext_of_ssl(self):
    self.assertOnlyIn((2.7, 3.2), detect("from ssl import SSLContext"))

  def test_SSLSession_of_ssl(self):
    self.assertOnlyIn(3.6, detect("from ssl import SSLSession"))

  def test_SSLMemoryBIO_of_ssl(self):
    self.assertOnlyIn(3.6, detect("from ssl import SSLMemoryBIO"))

  def test_SSLObject_of_ssl(self):
    self.assertOnlyIn(3.6, detect("from ssl import SSLObject"))

  def test_CompletedProcess_of_subprocess(self):
    self.assertOnlyIn(3.5, detect("from subprocess import CompletedProcess"))

  def test_catch_warnings_of_warnings(self):
    self.assertOnlyIn((2.6, 3.0), detect("from warnings import catch_warnings"))

  def test_WeakSet_of_weakref(self):
    self.assertOnlyIn((2.7, 3.0), detect("from weakref import WeakSet"))

  def test_WeakMethod_of_weakref(self):
    self.assertOnlyIn(3.4, detect("from weakref import WeakMethod"))

  def test_finalize_of_weakref(self):
    self.assertOnlyIn(3.4, detect("from weakref import finalize"))

  def test_IISCGIHandler_of_wsgiref_handlers(self):
    self.assertOnlyIn(3.2, detect("from wsgiref.handlers import IISCGIHandler"))

  def test_ElementTree_of_xml_etree(self):
    self.assertOnlyIn((2.5, 3.0), detect("from xml.etree import ElementTree"))

  def test_XMLPullParser_of_xml_etree_ElementTree(self):
    self.assertOnlyIn(3.4, detect("from xml.etree.ElementTree import XMLPullParser"))

  def test_MultiCall_of_xmlrpclib(self):
    self.assertOnlyIn(2.4, detect("from xmlrpclib import MultiCall"))

  def test_MIMENonMultipart_of_email_mime_nonmultipart(self):
    self.assertOnlyIn((2.2, 3.0), detect("from email.mime.nonmultipart import MIMENonMultipart"))

  def test_MIMEMultipart_of_email_mime_multipart(self):
    self.assertOnlyIn((2.2, 3.0), detect("from email.mime.multipart import MIMEMultipart"))

  def test_MIMEApplication_of_email_mime_application(self):
    self.assertOnlyIn((2.5, 3.0), detect("from email.mime.application import MIMEApplication"))

  def test_FeedParser_of_email_parser(self):
    self.assertOnlyIn((2.4, 3.0), detect("from email.parser import FeedParser"))

  def test_BytesFeedParser_of_email_parser(self):
    self.assertOnlyIn(3.2, detect("from email.parser import BytesFeedParser"))

  def test_BytesParser_of_email_parser(self):
    self.assertOnlyIn(3.2, detect("from email.parser import BytesParser"))

  def test_BytesHeaderParser_of_email_parser(self):
    self.assertOnlyIn(3.3, detect("from email.parser import BytesHeaderParser"))

  def test_EmailPolicy_of_email_policy(self):
    self.assertOnlyIn(3.6, detect("from email.policy import EmailPolicy"))

  def test_DecodedGenerator_of_email_generator(self):
    self.assertOnlyIn((2.2, 3.0), detect("from email.generator import DecodedGenerator"))

  def test_BytesGenerator_of_email_generator(self):
    self.assertOnlyIn(3.2, detect("from email.generator import BytesGenerator"))

  def test_WindowsRegistryFinder_of_importlib_machinery(self):
    self.assertOnlyIn(3.3, detect("from importlib.machinery import WindowsRegistryFinder"))

  def test_FileFinder_of_importlib_machinery(self):
    self.assertOnlyIn(3.3, detect("from importlib.machinery import FileFinder"))

  def test_SourceFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn(3.3, detect("from importlib.machinery import SourceFileLoader"))

  def test_SourcelessFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn(3.3, detect("from importlib.machinery import SourcelessFileLoader"))

  def test_ExtensionFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn(3.3, detect("from importlib.machinery import ExtensionFileLoader"))

  def test_ModuleSpec_of_importlib_machinery(self):
    self.assertOnlyIn(3.4, detect("from importlib.machinery import ModuleSpec"))
