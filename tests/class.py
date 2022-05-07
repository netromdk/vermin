from .testutils import VerminTest

class VerminClassMemberTests(VerminTest):
  def test_ConfigParser_of_ConfigParser(self):
    self.assertOnlyIn((2, 3), self.detect("from ConfigParser import ConfigParser"))

  def test_RawConfigParser_of_ConfigParser(self):
    self.assertOnlyIn((2, 3), self.detect("from ConfigParser import RawConfigParser"))

  def test_SafeConfigParser_of_ConfigParser(self):
    self.assertOnlyIn((2, 3), self.detect("from ConfigParser import SafeConfigParser"))

  def test_LifoQueue_of_Queue(self):
    self.assertOnlyIn((2, 6), self.detect("from Queue import LifoQueue"))

  def test_PriorityQueue_of_Queue(self):
    self.assertOnlyIn((2, 6), self.detect("from Queue import PriorityQueue"))

  def test_ABC_of_abc(self):
    self.assertOnlyIn((3, 4), self.detect("from abc import ABC"))

  def test_BooleanOptionalAction_of_argparse(self):
    self.assertOnlyIn((3, 9), self.detect("from argparse import BooleanOptionalAction"))

  def test_BufferedProtocol_of_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("from asyncio import BufferedProtocol"))

  def test_MultiLoopChildWatcher_of_asyncio(self):
    self.assertOnlyIn((3, 8), self.detect("from asyncio import MultiLoopChildWatcher"))

  def test_ThreadedChildWatcher_of_asyncio(self):
    self.assertOnlyIn((3, 8), self.detect("from asyncio import ThreadedChildWatcher"))

  def test_PidfdChildWatcher_of_asyncio(self):
    self.assertOnlyIn((3, 9), self.detect("from asyncio import PidfdChildWatcher"))

  def test_Calendar_of_calendar(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from calendar import Calendar"))

  def test_HTMLCalendar_of_calendar(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from calendar import HTMLCalendar"))

  def test_LocaleHTMLCalendar_of_calendar(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from calendar import LocaleHTMLCalendar"))

  def test_LocaleTextCalendar_of_calendar(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from calendar import LocaleTextCalendar"))

  def test_TextCalendar_of_calendar(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from calendar import TextCalendar"))

  def test_IncrementalEncoder_of_codecs(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from codecs import IncrementalEncoder"))

  def test_NNTP_SSL_of_nntplib(self):
    self.assertOnlyIn((3, 2), self.detect("from nntplib import NNTP_SSL"))

  def test_DirEntry_of_os(self):
    self.assertOnlyIn((3, 5), self.detect("from os import DirEntry"))

  def test_PathLike_of_os(self):
    self.assertOnlyIn((3, 6), self.detect("from os import PathLike"))

  def test_sched_param_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import sched_param"))

  def test_terminal_size_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import terminal_size"))

  def test_PickleBuffer_of_pickle(self):
    self.assertOnlyIn((3, 8), self.detect("from pickle import PickleBuffer"))

  def test_Popen4_of_popen2(self):
    self.assertOnlyIn((2, 0), self.detect("from popen2 import Popen4"))

  def test_POP3_SSL_of_poplib(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from poplib import POP3_SSL"))

  def test_Stats_of_pstats(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from pstats import Stats"))

  def test_PycInvalidationMode_of_py_compile(self):
    self.assertOnlyIn((3, 7), self.detect("from py_compile import PycInvalidationMode"))

  def test_SimpleQueue_of_queue(self):
    self.assertOnlyIn((3, 7), self.detect("from queue import SimpleQueue"))

  def test_SystemRandom_of_random(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from random import SystemRandom"))

  def test_DevpollSelector_of_selectors(self):
    self.assertOnlyIn((3, 5), self.detect("from selectors import DevpollSelector"))

  def test_Barrier_of_multiprocessing(self):
    self.assertOnlyIn((3, 3), self.detect("from multiprocessing import Barrier"))

  def test_IsolatedAsyncioTestCase_of_unittest(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest import IsolatedAsyncioTestCase"))

  def test_TextTestResult_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from unittest import TextTestResult"))

  def test_AsyncMock_of_unittest_mock(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest.mock import AsyncMock"))
    self.assertTrue(self.config.add_backport("mock"))
    self.assertOnlyIn(((3, 6)), self.detect("from unittest.mock import AsyncMock"))

  def test_DefragResult_of_urllib_parse(self):
    self.assertOnlyIn((3, 2), self.detect("from urllib.parse import DefragResult"))

  def test_DefragResultBytes_of_urllib_parse(self):
    self.assertOnlyIn((3, 2), self.detect("from urllib.parse import DefragResultBytes"))

  def test_ParseResultBytes_of_urllib_parse(self):
    self.assertOnlyIn((3, 2), self.detect("from urllib.parse import ParseResultBytes"))

  def test_SplitResultBytes_of_urllib_parse(self):
    self.assertOnlyIn((3, 2), self.detect("from urllib.parse import SplitResultBytes"))

  def test_DataHandler_of_urllib_request(self):
    self.assertOnlyIn((3, 4), self.detect("from urllib.request import DataHandler"))

  def test_HTTPPasswordMgrWithPriorAuth_of_urllib_request(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from urllib.request import HTTPPasswordMgrWithPriorAuth"))

  def test_HTTPCookieProcessor_of_urllib2(self):
    self.assertOnlyIn((2, 4), self.detect("from urllib2 import HTTPCookieProcessor"))

  def test_HTTPErrorProcessor_of_urllib2(self):
    self.assertOnlyIn((2, 4), self.detect("from urllib2 import HTTPErrorProcessor"))

  def test_SafeUUID_of_uuid(self):
    self.assertOnlyIn((3, 7), self.detect("from uuid import SafeUUID"))

  def test_timezone_of_datetime(self):
    self.assertOnlyIn((3, 2), self.detect("from datetime import timezone"))

  def test_Collection_of_typing(self):
    self.assertOnlyIn((3, 6), self.detect("from typing import Collection"))

  def test_ContextManager_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import ContextManager"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from typing import ContextManager"))

  def test_Coroutine_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import Coroutine"))

  def test_Counter_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import Counter"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from typing import Counter"))

  def test_Deque_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import Deque"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from typing import Deque"))

  def test_ForwardRef_of_typing(self):
    self.assertOnlyIn((3, 7), self.detect("from typing import ForwardRef"))

  def test_OrderedDict_of_typing(self):
    self.assertOnlyIn((3, 7), self.detect("from typing import OrderedDict"))

  def test_AsyncContextManager_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import AsyncContextManager"))

  def test_ChainMap_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import ChainMap"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn((3, 3), self.detect("from typing import ChainMap"))

  def test_AsyncGenerator_of_typing(self):
    self.assertOnlyIn((3, 6), self.detect("from typing import AsyncGenerator"))

  def test_Protocol_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import Protocol"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 8)), self.detect("from typing import Protocol"))

  def test_SupportsBytes_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import SupportsBytes"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn((3, 2), self.detect("from typing import SupportsBytes"))

  def test_SupportsIndex_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import SupportsIndex"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from typing import SupportsIndex"))

  def test_SupportsRound_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import SupportsRound"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn((3, 2), self.detect("from typing import SupportsRound"))

  def test_Awaitable_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import Awaitable"))

  def test_AsyncIterable_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import AsyncIterable"))

  def test_AsyncIterator_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import AsyncIterator"))

  def test_GenericAlias_of_types(self):
    self.assertOnlyIn((3, 9), self.detect("from types import GenericAlias"))

  def test_MappingProxyType_of_types(self):
    self.assertOnlyIn((3, 3), self.detect("from types import MappingProxyType"))

  def test_SimpleNamespace_of_types(self):
    self.assertOnlyIn((3, 3), self.detect("from types import SimpleNamespace"))

  def test_DomainFilter_of_tracemalloc(self):
    self.assertOnlyIn((3, 6), self.detect("from tracemalloc import DomainFilter"))

  def test_Counter_of_collections(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from collections import Counter"))

  def test_deque_of_collections(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from collections import deque"))

  def test_defaultdict_of_collections(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from collections import defaultdict"))

  def test_namedtuple_of_collections(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from collections import namedtuple"))

  def test_OrderedDict_of_collections(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from collections import OrderedDict"))

  def test_UserDict_of_collections(self):
    self.assertOnlyIn((3, 0), self.detect("from collections import UserDict"))

  def test_UserList_of_collections(self):
    self.assertOnlyIn((3, 0), self.detect("from collections import UserList"))

  def test_UserString_of_collections(self):
    self.assertOnlyIn((3, 0), self.detect("from collections import UserString"))

  def test_ChainMap_of_collections(self):
    self.assertOnlyIn((3, 3), self.detect("from collections import ChainMap"))

  def test_Collection_of_collections_abc(self):
    self.assertOnlyIn((3, 6), self.detect("from collections.abc import Collection"))

  def test_Reversible_of_collections_abc(self):
    self.assertOnlyIn((3, 6), self.detect("from collections.abc import Reversible"))

  def test_Generator_of_collections_abc(self):
    self.assertOnlyIn((3, 5), self.detect("from collections.abc import Generator"))

  def test_Coroutine_of_collections_abc(self):
    self.assertOnlyIn((3, 5), self.detect("from collections.abc import Coroutine"))

  def test_AsyncIterable_of_collections_abc(self):
    self.assertOnlyIn((3, 5), self.detect("from collections.abc import AsyncIterable"))

  def test_AsyncIterator_of_collections_abc(self):
    self.assertOnlyIn((3, 5), self.detect("from collections.abc import AsyncIterator"))

  def test_AsyncGenerator_of_collections_abc(self):
    self.assertOnlyIn((3, 6), self.detect("from collections.abc import AsyncGenerator"))

  def test_AbstractContextManager_of_contextlib(self):
    self.assertOnlyIn((3, 6), self.detect("from contextlib import AbstractContextManager"))

  def test_AbstractAsyncContextManager_of_contextlib(self):
    self.assertOnlyIn((3, 7), self.detect("from contextlib import AbstractAsyncContextManager"))

  def test_ContextDecorator_of_contextlib(self):
    self.assertOnlyIn((3, 2), self.detect("from contextlib import ContextDecorator"))

  def test_ExitStack_of_contextlib(self):
    self.assertOnlyIn((3, 3), self.detect("from contextlib import ExitStack"))

  def test_AsyncExitStack_of_contextlib(self):
    self.assertOnlyIn((3, 7), self.detect("from contextlib import AsyncExitStack"))

  def test_AsyncContextDecorator_of_contextlib(self):
    self.assertOnlyIn((3, 10), self.detect("from contextlib import AsyncContextDecorator"))

  def test_unix_dialect_of_csv(self):
    self.assertOnlyIn((3, 2), self.detect("from csv import unix_dialect"))

  def test_c_longdouble_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from ctypes import c_longdouble"))

  def test_c_bool_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from ctypes import c_bool"))

  def test_c_ssize_t_of_ctypes(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ctypes import c_ssize_t"))

  def test_HtmlDiff_of_difflib(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from difflib import HtmlDiff"))

  def test_Signature_of_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("from inspect import Signature"))

  def test_Parameter_of_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("from inspect import Parameter"))

  def test_BoundArguments_of_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("from inspect import BoundArguments"))

  def test_LoggerAdapter_of_logging(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from logging import LoggerAdapter"))

  def test_NullHandler_of_logging(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from logging import NullHandler"))

  def test_StreamHandler_of_logging(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from logging import StreamHandler"))

  def test_QueueHandler_of_logging_handlers(self):
    self.assertOnlyIn((3, 2), self.detect("from logging.handlers import QueueHandler"))

  def test_QueueListener_of_logging_handlers(self):
    self.assertOnlyIn((3, 2), self.detect("from logging.handlers import QueueListener"))

  def test_WatchedFileHandler_of_logging_handlers(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from logging.handlers import WatchedFileHandler"))

  def test_ModuleInfo_of_pkgutil(self):
    self.assertOnlyIn((3, 6), self.detect("from pkgutil import ModuleInfo"))

  def test_CGIXMLRPCRequestHandler_of_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 3), self.detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler"))

  def test_MemoryBIO_of_ssl(self):
    self.assertOnlyIn((3, 5), self.detect("from ssl import MemoryBIO"))

  def test_Options_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import Options"))

  def test_SSLContext_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import SSLContext"))

  def test_SSLSession_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import SSLSession"))

  def test_SSLObject_of_ssl(self):
    self.assertOnlyIn((3, 5), self.detect("from ssl import SSLObject"))

  def test_AlertDescription_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import AlertDescription"))

  def test_SSLErrorNumber_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import SSLErrorNumber"))

  def test_TLSVersion_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import TLSVersion"))

  def test_Formatter_of_string(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from string import Formatter"))

  def test_Template_of_string(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from string import Template"))

  def test_Struct_of_struct(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from struct import Struct"))

  def test_CompletedProcess_of_subprocess(self):
    self.assertOnlyIn((3, 5), self.detect("from subprocess import CompletedProcess"))

  def test_EnvironmentVarGuard_of_test_support(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from test.support import EnvironmentVarGuard"))

  def test_TransientResource_of_test_support(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from test.support import TransientResource"))

  def test_WarningsRecorder_of_test_support(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from test.support import WarningsRecorder"))

  def test_Barrier_of_threading(self):
    self.assertOnlyIn((3, 2), self.detect("from threading import Barrier"))

  def test_local_of_threading(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from threading import local"))

  def test_struct_time_of_time(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from time import struct_time"))

  def test_FrameSummary_of_traceback(self):
    self.assertOnlyIn((3, 5), self.detect("from traceback import FrameSummary"))

  def test_StackSummary_of_traceback(self):
    self.assertOnlyIn((3, 5), self.detect("from traceback import StackSummary"))

  def test_TracebackException_of_traceback(self):
    self.assertOnlyIn((3, 5), self.detect("from traceback import TracebackException"))

  def test_catch_warnings_of_warnings(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from warnings import catch_warnings"))

  def test_WeakSet_of_weakref(self):
    self.assertOnlyIn(((2, 7), (3, 0)), self.detect("from weakref import WeakSet"))

  def test_WeakMethod_of_weakref(self):
    self.assertOnlyIn((3, 4), self.detect("from weakref import WeakMethod"))

  def test_finalize_of_weakref(self):
    self.assertOnlyIn((3, 4), self.detect("from weakref import finalize"))

  def test_IISCGIHandler_of_wsgiref_handlers(self):
    self.assertOnlyIn((3, 2), self.detect("from wsgiref.handlers import IISCGIHandler"))

  def test_C14NWriterTarget_of_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8), self.detect("from xml.etree.ElementTree import C14NWriterTarget"))

  def test_XMLPullParser_of_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4), self.detect("from xml.etree.ElementTree import XMLPullParser"))

  def test_LexicalHandler_of_xml_sax_handler(self):
    self.assertOnlyIn((3, 10), self.detect("from xml.sax.handler import LexicalHandler"))

  def test_MultiCall_of_xmlrpclib(self):
    self.assertOnlyIn((2, 4), self.detect("from xmlrpclib import MultiCall"))

  def test_MIMENonMultipart_of_email_mime_nonmultipart(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.mime.nonmultipart import MIMENonMultipart"))

  def test_MIMEMultipart_of_email_mime_multipart(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect(
      "from email.mime.multipart import MIMEMultipart"))

  def test_MIMEApplication_of_email_mime_application(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from email.mime.application import MIMEApplication"))

  def test_FeedParser_of_email_parser(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from email.parser import FeedParser"))

  def test_BytesFeedParser_of_email_parser(self):
    self.assertOnlyIn((3, 2), self.detect("from email.parser import BytesFeedParser"))

  def test_BytesParser_of_email_parser(self):
    self.assertOnlyIn((3, 2), self.detect("from email.parser import BytesParser"))

  def test_BytesHeaderParser_of_email_parser(self):
    self.assertOnlyIn((3, 3), self.detect("from email.parser import BytesHeaderParser"))

  def test_EmailPolicy_of_email_policy(self):
    self.assertOnlyIn((3, 3), self.detect("from email.policy import EmailPolicy"))

  def test_DecodedGenerator_of_email_generator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from email.generator import DecodedGenerator"))

  def test_BytesGenerator_of_email_generator(self):
    self.assertOnlyIn((3, 2), self.detect("from email.generator import BytesGenerator"))

  def test_Flag_of_enum(self):
    self.assertOnlyIn((3, 6), self.detect("from enum import Flag"))

  def test_IntFlag_of_enum(self):
    self.assertOnlyIn((3, 6), self.detect("from enum import IntFlag"))

  def test_auto_of_enum(self):
    self.assertOnlyIn((3, 6), self.detect("from enum import auto"))

  def test_FTP_TLS_of_ftplib(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ftplib import FTP_TLS"))

  def test_partialmethod_of_functools(self):
    self.assertOnlyIn((3, 4), self.detect("from functools import partialmethod"))

  def test_HTTPStatus_of_http(self):
    self.assertOnlyIn((3, 5), self.detect("from http import HTTPStatus"))

  def test_ThreadingHTTPServer_of_http_server(self):
    self.assertOnlyIn((3, 7), self.detect("from http.server import ThreadingHTTPServer"))

  def test_HTTPConnection_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import HTTPConnection"))

  def test_HTTPResponse_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import HTTPResponse"))

  def test_HTTPSConnection_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import HTTPSConnection"))

  def test_IMAP4_stream_of_imaplib(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from imaplib import IMAP4_stream"))

  def test_NullImporter_of_imp(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from imp import NullImporter"))

  def test_FileLoader_of_importlib_abc(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.abc import FileLoader"))

  def test_MetaPathFinder_of_importlib_abc(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.abc import MetaPathFinder"))

  def test_PathEntryFinder_of_importlib_abc(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.abc import PathEntryFinder"))

  def test_ResourceReader_of_importlib_abc(self):
    self.assertOnlyIn((3, 7), self.detect("from importlib.abc import ResourceReader"))

  def test_Traversable_of_importlib_abc(self):
    self.assertOnlyIn((3, 9), self.detect("from importlib.abc import Traversable"))

  def test_TraversableReader_of_importlib_abc(self):
    self.assertOnlyIn((3, 9), self.detect("from importlib.abc import TraversableReader"))

  def test_TraversableResources_of_importlib_abc(self):
    self.assertOnlyIn((3, 9), self.detect("from importlib.abc import TraversableResources"))

  def test_WindowsRegistryFinder_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.machinery import WindowsRegistryFinder"))

  def test_FileFinder_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.machinery import FileFinder"))

  def test_SourceFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.machinery import SourceFileLoader"))

  def test_SourcelessFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.machinery import SourcelessFileLoader"))

  def test_ExtensionFileLoader_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib.machinery import ExtensionFileLoader"))

  def test_ModuleSpec_of_importlib_machinery(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib.machinery import ModuleSpec"))

  def test_EntryPoints_of_importlib_metadata(self):
    self.assertOnlyIn((3, 10), self.detect("from importlib.metadata import EntryPoints"))

  def test_LazyLoader_of_importlib_util(self):
    self.assertOnlyIn((3, 5), self.detect("from importlib.util import LazyLoader"))

  def test_Bytecode_of_dis(self):
    self.assertOnlyIn((3, 4), self.detect("from dis import Bytecode"))

  def test_Instruction_of_dis(self):
    self.assertOnlyIn((3, 4), self.detect("from dis import Instruction"))

  def test_DocTest_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import DocTest"))

  def test_DocTestFinder_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import DocTestFinder"))

  def test_DocTestParser_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import DocTestParser"))

  def test_DocTestRunner_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import DocTestRunner"))

  def test_Example_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import Example"))

  def test_OutputChecker_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import OutputChecker"))

  def test_UID_of_plistlib(self):
    self.assertOnlyIn((3, 8), self.detect("from plistlib import UID"))

  def test_NormalDist_of_statistics(self):
    self.assertOnlyIn((3, 8), self.detect("from statistics import NormalDist"))

  def test_TypedDict_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import TypedDict"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 8)), self.detect("from typing import TypedDict"))

  def test_ParamSpec_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import ParamSpec"))

  def test_SMTP_SSL_of_smtplib(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from smtplib import SMTP_SSL"))

  def test_LMTP_of_smtplib(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from smtplib import LMTP"))

  def test_Path_of_zipfile(self):
    self.assertOnlyIn((3, 8), self.detect("from zipfile import Path"))

  def test_zipimporter_of_zipimport(self):
    self.assertOnlyIn(((2, 7), (3, 0)), self.detect("from zipimport import zipimporter"))

  def test_FunctionProfile_of_pstats(self):
    self.assertOnlyIn((3, 9), self.detect("from pstats import FunctionProfile"))

  def test_StatsProfile_of_pstats(self):
    self.assertOnlyIn((3, 9), self.detect("from pstats import StatsProfile"))
