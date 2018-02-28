from testutils import MinpyTest, detect

class MinpyConstantMemberTests(MinpyTest):
  def test_flags_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("from sys import flags"))

  def test_supports_unicode_filenames_of_os_path(self):
    self.assertOnlyIn((2.3, 3.0), detect("from os.path import supports_unicode_filenames"))

  def test_supports_bytes_environ_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import supports_bytes_environ"))

  def test_environb_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import environb"))

  def test_PRIO_PROCESS_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import PRIO_PROCESS"))

  def test_PRIO_PGRP_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import PRIO_PGRP"))

  def test_PRIO_USER_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import PRIO_USER"))

  def test_F_LOCK_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import F_LOCK"))

  def test_F_TLOCK_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import F_TLOCK"))

  def test_F_ULOCK_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import F_ULOCK"))

  def test_F_TEST_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import F_TEST"))

  def test_O_CLOEXEC_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import O_CLOEXEC"))

  def test_O_PATH_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import O_PATH"))

  def test_O_TMPFILE_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import O_TMPFILE"))

  def test_POSIX_FADV_NORMAL_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_NORMAL"))

  def test_POSIX_FADV_SEQUENTIAL_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_SEQUENTIAL"))

  def test_POSIX_FADV_RANDOM_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_RANDOM"))

  def test_POSIX_FADV_NOREUSE_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_NOREUSE"))

  def test_POSIX_FADV_WILLNEED_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_WILLNEED"))

  def test_POSIX_FADV_DONTNEED_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import POSIX_FADV_DONTNEED"))

  def test_SF_NODISKIO_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import SF_NODISKIO"))

  def test_SF_MNOWAIT_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import SF_MNOWAIT"))

  def test_SF_SYNC_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import SF_SYNC"))

  def test_float_info_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("from sys import float_info"))

  def test_float_repr_style_of_sys(self):
    self.assertOnlyIn((2.7, 3.0), detect("from sys import float_repr_style"))

  def test_long_info_of_sys(self):
    self.assertOnlyIn(2.7, detect("from sys import long_info"))

  def test_py3kwarning_of_sys(self):
    self.assertOnlyIn(2.6, detect("from sys import py3kwarning"))

  def test_subversion_of_sys(self):
    self.assertOnlyIn(2.5, detect("from sys import subversion"))

  def test_api_version_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("from sys import api_version"))

  def test_version_info_of_sys(self):
    self.assertOnlyIn((2.0, 3.0), detect("from sys import version_info"))
