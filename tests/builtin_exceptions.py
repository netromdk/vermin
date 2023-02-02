from .testutils import VerminTest

class VerminBuiltinExceptionsMemberTests(VerminTest):
  def test_BaseException(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("BaseException()"))
    self.assertOnlyIn((2, 5), self.detect("from exceptions import BaseException"))

  def test_BytesWarning(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("BytesWarning()"))
    self.assertOnlyIn((2, 6), self.detect("from exceptions import BytesWarning"))

  def test_UnicodeWarning(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("UnicodeWarning()"))
    self.assertOnlyIn((2, 5), self.detect("from exceptions import UnicodeWarning"))

  def test_UnicodeError(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("UnicodeError()"))
    self.assertOnlyIn((2, 0), self.detect("from exceptions import UnicodeError"))

  def test_GeneratorExit(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("GeneratorExit()"))
    self.assertOnlyIn((2, 5), self.detect("from exceptions import GeneratorExit"))

  def test_ImportWarning(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("ImportWarning()"))
    self.assertOnlyIn((2, 5), self.detect("from exceptions import ImportWarning"))

  def test_StopIteration(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("StopIteration()"))
    self.assertOnlyIn((2, 2), self.detect("from exceptions import StopIteration"))

  def test_UnboundLocalError(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("UnboundLocalError()"))
    self.assertOnlyIn((2, 0), self.detect("from exceptions import UnboundLocalError"))

  def test_UnicodeDecodeError(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("UnicodeDecodeError()"))
    self.assertOnlyIn((2, 3), self.detect("from exceptions import UnicodeDecodeError"))

  def test_UnicodeEncodeError(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("UnicodeEncodeError()"))
    self.assertOnlyIn((2, 3), self.detect("from exceptions import UnicodeEncodeError"))

  def test_UnicodeTranslateError(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("UnicodeTranslateError()"))
    self.assertOnlyIn((2, 3), self.detect("from exceptions import UnicodeTranslateError"))

  def test_WindowsError(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("WindowsError()"))
    self.assertOnlyIn((2, 0), self.detect("from exceptions import WindowsError"))

  def test_ReferenceError(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("ReferenceError()"))
    self.assertOnlyIn((2, 2), self.detect("from exceptions import ReferenceError"))

  def test_ExceptionGroup(self):
    self.assertOnlyIn((3, 11), self.detect("ExceptionGroup()"))

  def test_BaseExceptionGroup(self):
    self.assertOnlyIn((3, 11), self.detect("BaseExceptionGroup()"))

  def test_BlockingIOError(self):
    self.assertOnlyIn((3, 3), self.detect("BlockingIOError()"))

  def test_BrokenPipeError(self):
    self.assertOnlyIn((3, 3), self.detect("BrokenPipeError()"))

  def test_ChildProcessError(self):
    self.assertOnlyIn((3, 3), self.detect("ChildProcessError()"))

  def test_ConnectionAbortedError(self):
    self.assertOnlyIn((3, 3), self.detect("ConnectionAbortedError()"))

  def test_ConnectionError(self):
    self.assertOnlyIn((3, 3), self.detect("ConnectionError()"))

  def test_ConnectionRefusedError(self):
    self.assertOnlyIn((3, 3), self.detect("ConnectionRefusedError()"))

  def test_ConnectionResetError(self):
    self.assertOnlyIn((3, 3), self.detect("ConnectionResetError()"))

  def test_EncodingWarning(self):
    self.assertOnlyIn((3, 10), self.detect("EncodingWarning()"))

  def test_FileExistsError(self):
    self.assertOnlyIn((3, 3), self.detect("FileExistsError()"))

  def test_FileNotFoundError(self):
    self.assertOnlyIn((3, 3), self.detect("FileNotFoundError()"))

  def test_InterruptedError(self):
    self.assertOnlyIn((3, 3), self.detect("InterruptedError()"))

  def test_IsADirectoryError(self):
    self.assertOnlyIn((3, 3), self.detect("IsADirectoryError()"))

  def test_ModuleNotFoundError(self):
    self.assertOnlyIn((3, 6), self.detect("ModuleNotFoundError()"))

  def test_NotADirectoryError(self):
    self.assertOnlyIn((3, 3), self.detect("NotADirectoryError()"))

  def test_PermissionError(self):
    self.assertOnlyIn((3, 3), self.detect("PermissionError()"))

  def test_ProcessLookupError(self):
    self.assertOnlyIn((3, 3), self.detect("ProcessLookupError()"))

  def test_RecursionError(self):
    self.assertOnlyIn((3, 5), self.detect("RecursionError()"))

  def test_ResourceWarning(self):
    self.assertOnlyIn((3, 2), self.detect("ResourceWarning()"))

  def test_StopAsyncIteration(self):
    self.assertOnlyIn((3, 5), self.detect("StopAsyncIteration()"))

  def test_TimeoutError(self):
    self.assertOnlyIn((3, 3), self.detect("TimeoutError()"))
