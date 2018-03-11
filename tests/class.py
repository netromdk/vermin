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
