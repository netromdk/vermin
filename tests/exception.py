from .testutils import VerminTest

class VerminExceptionMemberTests(VerminTest):
  def test_QueueShutDown_of_asyncio(self):
    self.assertOnlyIn((3, 13), self.detect("from asyncio import QueueShutDown"))

  def test_SSLCertVerificationError_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import SSLCertVerificationError"))

  def test_SSLZeroReturnError_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLZeroReturnError"))

  def test_SSLWantReadError_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLWantReadError"))

  def test_SSLWantWriteError_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLWantWriteError"))

  def test_SSLSyscallError_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLSyscallError"))

  def test_SubprocessError_of_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect("from subprocess import SubprocessError"))

  def test_TimeoutExpired_of_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect("from subprocess import TimeoutExpired"))

  def test_HeaderError_of_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from tarfile import HeaderError"))

  def test_LinkFallbackError_of_tarfile(self):
    self.assertOnlyIn((3, 9), self.detect("from tarfile import LinkFallbackError"))

  def test_BadZipFile_of_zipfile(self):
    self.assertOnlyIn((3, 2), self.detect("from zipfile import BadZipFile"))

  def test_NoBoundaryInMultipartDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.errors import NoBoundaryInMultipartDefect"))

  def test_StartBoundaryNotFoundDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.errors import StartBoundaryNotFoundDefect"))

  def test_FirstHeaderLineIsContinuationDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.errors import FirstHeaderLineIsContinuationDefect"))

  def test_MisplacedEnvelopeHeaderDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.errors import MisplacedEnvelopeHeaderDefect"))

  def test_MalformedHeaderDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
      "from email.errors import MalformedHeaderDefect"))

  def test_MultipartInvariantViolationDefect_of_email_errors(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.errors import MultipartInvariantViolationDefect"))

  def test_CloseBoundaryNotFoundDefect_of_email_errors(self):
    self.assertOnlyIn((3, 3), self.detect("from email.errors import CloseBoundaryNotFoundDefect"))

  def test_MissingHeaderBodySeparatorDefect_of_email_errors(self):
    self.assertOnlyIn((3, 3), self.detect(
      "from email.errors import MissingHeaderBodySeparatorDefect"))

  def test_InterpolationMissingOptionError_of_ConfigParser(self):
    self.assertOnlyIn((2, 3), self.detect(
      "from ConfigParser import InterpolationMissingOptionError"))

  def test_InterpolationSyntaxError_of_ConfigParser(self):
    self.assertOnlyIn((2, 3), self.detect("from ConfigParser import InterpolationSyntaxError"))

  def test_MultilineContinuationError_of_configparser(self):
    self.assertOnlyIn((3, 13), self.detect("from configparser import MultilineContinuationError"))

  def test_UnnamedSectionDisabledError_of_configparser(self):
    self.assertOnlyIn((3, 14), self.detect("from configparser import UnnamedSectionDisabledError"))

  def test_InvalidWriteError_of_configparser(self):
    self.assertOnlyIn((3, 14), self.detect("from configparser import InvalidWriteError"))

  def test_COMError_of_ctypes(self):
    self.assertOnlyIn((3, 14), self.detect("from ctypes import COMError"))

  def test_BrokenExecutor_of_concurrent_futures(self):
    self.assertOnlyIn((3, 7), self.detect("from concurrent.futures import BrokenExecutor"))

  def test_InvalidStateError_of_concurrent_futures(self):
    self.assertOnlyIn((3, 8), self.detect("from concurrent.futures import InvalidStateError"))

  def test_BrokenInterpreterPool_of_concurrent_futures_interpreter(self):
    self.assertOnlyIn((3, 14), self.detect("""
from concurrent.futures.interpreter import BrokenInterpreterPool
"""))

  def test_ExecutionFailed_of_concurrent_futures_interpreter(self):
    self.assertOnlyIn((3, 14), self.detect("""
from concurrent.futures.interpreter import ExecutionFailed
"""))

  def test_BrokenThreadPool_of_concurrent_futures_thread(self):
    self.assertOnlyIn((3, 7), self.detect("from concurrent.futures.thread import BrokenThreadPool"))

  def test_BrokenProcessPool_of_concurrent_futures_process(self):
    self.assertOnlyIn((3, 3), self.detect(
      "from concurrent.futures.process import BrokenProcessPool"))

  def test_BadGzipFile_of_gzip(self):
    self.assertOnlyIn((3, 8), self.detect("from gzip import BadGzipFile"))

  def test_HTMLParseError_of_htmllib(self):
    self.assertOnlyIn((2, 4), self.detect("from htmllib import HTMLParseError"))

  def test_BadStatusLine_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import BadStatusLine"))

  def test_CannotSendHeader_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import CannotSendHeader"))

  def test_CannotSendRequest_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import CannotSendRequest"))

  def test_HTTPException_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import HTTPException"))

  def test_ImproperConnectionState_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import ImproperConnectionState"))

  def test_IncompleteRead_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import IncompleteRead"))

  def test_InvalidURL_of_httplib(self):
    self.assertOnlyIn((2, 3), self.detect("from httplib import InvalidURL"))

  def test_NotConnected_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import NotConnected"))

  def test_ResponseNotReady_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import ResponseNotReady"))

  def test_UnimplementedFileMode_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import UnimplementedFileMode"))

  def test_UnknownProtocol_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import UnknownProtocol"))

  def test_UnknownTransferEncoding_of_httplib(self):
    self.assertOnlyIn((2, 0), self.detect("from httplib import UnknownTransferEncoding"))

  def test_JSONDecodeError_of_json(self):
    self.assertOnlyIn((3, 5), self.detect("from json import JSONDecodeError"))

  def test_UnsupportedOperation_of_pathlib(self):
    self.assertOnlyIn((3, 13), self.detect("from pathlib import UnsupportedOperation"))

  def test_ShutDown_of_queue(self):
    self.assertOnlyIn((3, 13), self.detect("from queue import ShutDown"))

  def test_PatternError_of_re(self):
    self.assertOnlyIn((3, 13), self.detect("from re import PatternError"))

  def test_SGMLParseError_of_sgmllib(self):
    self.assertOnlyIn((2, 1), self.detect("from sgmllib import SGMLParseError"))

  def test_Error_of_shutil(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from shutil import Error"))

  def test_SameFileError_of_shutil(self):
    self.assertOnlyIn((3, 4), self.detect("from shutil import SameFileError"))

  def test_SMTPNotSupportedError_of_smtplib(self):
    self.assertOnlyIn((3, 5), self.detect("from smtplib import SMTPNotSupportedError"))

  def test_timeout_of_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from socket import timeout"))

  def test_BrokenBarrierError_of_threading(self):
    self.assertOnlyIn((3, 2), self.detect("from threading import BrokenBarrierError"))

  def test_SkipTest_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from unittest import SkipTest"))

  def test_ContentTooShortError_of_urllib(self):
    self.assertOnlyIn((2, 5), self.detect("from urllib import ContentTooShortError"))

  def test_DOMException_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import DOMException"))

  def test_DomstringSizeErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import DomstringSizeErr"))

  def test_HierarchyRequestErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import HierarchyRequestErr"))

  def test_IndexSizeErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import IndexSizeErr"))

  def test_InuseAttributeErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import InuseAttributeErr"))

  def test_InvalidAccessErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import InvalidAccessErr"))

  def test_InvalidCharacterErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import InvalidCharacterErr"))

  def test_InvalidModificationErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import InvalidModificationErr"))

  def test_InvalidStateErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import InvalidStateErr"))

  def test_NamespaceErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NamespaceErr"))

  def test_NoDataAllowedErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NoDataAllowedErr"))

  def test_NoModificationAllowedErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NoModificationAllowedErr"))

  def test_NotFoundErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NotFoundErr"))

  def test_NotSupportedErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NotSupportedErr"))

  def test_SyntaxErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import SyntaxErr"))

  def test_WrongDocumentErr_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import WrongDocumentErr"))
