from .testutils import MinpyTest, detect

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

  def test_sentinel_of_multiprocessing_Process(self):
    self.assertOnlyIn(3.3, detect("from multiprocessing import Process\np = Process()\np.sentinel"))

  def test_skipped_of_unittest_TestResult(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestResult\np = TestResult()\np.skipped"))

  def test_buffer_of_unittest_TestResult(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestResult\np = TestResult()\np.buffer"))

  def test_failfast_of_unittest_TestResult(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestResult\np = TestResult()\np.failfast"))

  def test_fold_of_datetime_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\np = datetime()\np.fold"))

  def test_TYPE_CHECKING_of_typing(self):
    self.assertOnlyIn(3.5, detect("from typing import TYPE_CHECKING"))

  def test_algorithms_of_hashlib(self):
    self.assertOnlyIn(2.7, detect("from hashlib import algorithms"))

  def test_algorithms_available_of_hashlib(self):
    self.assertOnlyIn((2.7, 3.2), detect("from hashlib import algorithms_available"))

  def test_algorithms_guaranteed_of_hashlib(self):
    self.assertOnlyIn((2.7, 3.2), detect("from hashlib import algorithms_guaranteed"))

  def test_reverse_pointer_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn(3.5,
                      detect("from ipaddress import IPv4Address\n"
                             "addr = IPv4Address('127.0.0.1')\n"
                             "addr.reverse_pointer"))

  def test_is_global_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn(3.4,
                      detect("from ipaddress import IPv4Address\n"
                             "addr = IPv4Address('127.0.0.1')\n"
                             "addr.is_global"))

  def test_is_global_of_ipaddress_IPv6Address(self):
    self.assertOnlyIn(3.4,
                      detect("from ipaddress import IPv6Address\n"
                             "addr = IPv6Address(':::1')\n"
                             "addr.is_global"))
