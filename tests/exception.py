from .testutils import VerminTest, detect

class VerminExceptionMemberTests(VerminTest):
  def test_SSLZeroReturnError_of_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("from ssl import SSLZeroReturnError"))

  def test_SSLWantReadError_of_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("from ssl import SSLWantReadError"))

  def test_SSLWantWriteError_of_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("from ssl import SSLWantWriteError"))

  def test_SSLSyscallError_of_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("from ssl import SSLSyscallError"))

  def test_SubprocessError_of_subprocess(self):
    self.assertOnlyIn(3.3, detect("from subprocess import SubprocessError"))

  def test_TimeoutExpired_of_subprocess(self):
    self.assertOnlyIn(3.3, detect("from subprocess import TimeoutExpired"))

  def test_HeaderError_of_tarfile(self):
    self.assertOnlyIn((2.6, 3.0), detect("from tarfile import HeaderError"))

  def test_BadZipFile_of_zipfile(self):
    self.assertOnlyIn(3.2, detect("from zipfile import BadZipFile"))

  def test_NoBoundaryInMultipartDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0), detect("from email.errors import NoBoundaryInMultipartDefect"))

  def test_StartBoundaryNotFoundDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0), detect("from email.errors import StartBoundaryNotFoundDefect"))

  def test_FirstHeaderLineIsContinuationDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0),
                      detect("from email.errors import FirstHeaderLineIsContinuationDefect"))

  def test_MisplacedEnvelopeHeaderDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0), detect("from email.errors import MisplacedEnvelopeHeaderDefect"))

  def test_MalformedHeaderDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0), detect("from email.errors import MalformedHeaderDefect"))

  def test_MultipartInvariantViolationDefect_of_email_errors(self):
    self.assertOnlyIn((2.4, 3.0),
                      detect("from email.errors import MultipartInvariantViolationDefect"))

  def test_CloseBoundaryNotFoundDefect_of_email_errors(self):
    self.assertOnlyIn(3.3, detect("from email.errors import CloseBoundaryNotFoundDefect"))

  def test_MissingHeaderBodySeparatorDefect_of_email_errors(self):
    self.assertOnlyIn(3.3, detect("from email.errors import MissingHeaderBodySeparatorDefect"))
