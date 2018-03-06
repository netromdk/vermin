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
