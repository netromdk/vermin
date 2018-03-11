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
