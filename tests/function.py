from .testutils import VerminTest

class VerminFunctionMemberTests(VerminTest):
  def test_exc_clear_of_sys(self):
    self.assertOnlyIn((2, 3), self.detect("from sys import exc_clear"))

  def test_exception_of_sys(self):
    self.assertOnlyIn((3, 11), self.detect("from sys import exception"))

  def test_getcheckinterval_of_sys(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from sys import getcheckinterval"))

  def test_getdlopenflags_of_sys(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from sys import getdlopenflags"))

  def test_getfilesystemencoding_of_sys(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from sys import getfilesystemencoding"))

  def test_getsizeof_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import getsizeof"))

  def test_getprofile_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import getprofile"))

  def test_gettrace_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import gettrace"))

  def test_getwindowsversion_of_sys(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from sys import getwindowsversion"))

  def test_commonpath_of_os_path(self):
    self.assertOnlyIn((3, 5), self.detect("from os.path import commonpath"))

  def test_getctime_of_os_path(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os.path import getctime"))

  def test_ismount_of_os_path(self):
    self.assertOnlyIn((3, 4), self.detect("from os.path import ismount"))

  def test_lexists_of_os_path(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from os.path import lexists"))

  def test_realpath_of_os_path(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from os.path import realpath"))

  def test_relpath_of_os_path(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from os.path import relpath"))

  def test_getpgid_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import getpgid"))

  def test_getresgid_of_os(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from os import getresgid"))

  def test_getresuid_of_os(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from os import getresuid"))

  def test_getsid_of_os(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from os import getsid"))

  def test_initgroups_of_os(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from os import initgroups"))

  def test_setgroups_of_os(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from os import setgroups"))

  def test_setresgid_of_os(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from os import setresgid"))

  def test_setresuid_of_os(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from os import setresuid"))

  def test_fsencode_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import fsencode"))

  def test_fsdecode_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import fsdecode"))

  def test_fspath_of_os(self):
    self.assertOnlyIn((3, 6), self.detect("from os import fspath"))

  def test_getenvb_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import getenvb"))

  def test_get_exec_path_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import get_exec_path"))

  def test_getgrouplist_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import getgrouplist"))

  def test_getpriority_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import getpriority"))

  def test_setpriority_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import setpriority"))

  def test_get_blocking_of_os(self):
    self.assertOnlyIn((3, 5), self.detect("from os import get_blocking"))

  def test_set_blocking_of_os(self):
    self.assertOnlyIn((3, 5), self.detect("from os import set_blocking"))

  def test_lockf_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import lockf"))

  def test_login_tty_of_os(self):
    self.assertOnlyIn((3, 11), self.detect("from os import login_tty"))

  def test_pipe2_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import pipe2"))

  def test_posix_fallocate_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import posix_fallocate"))

  def test_posix_fadvise_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import posix_fadvise"))

  def test_pread_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import pread"))

  def test_pwrite_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import pwrite"))

  def test_sendfile_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import sendfile"))

  def test_readv_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import readv"))

  def test_writev_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import writev"))

  def test_splice_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import splice"))

  def test_eventfd_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import eventfd"))

  def test_eventfd_read_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import eventfd_read"))

  def test_eventfd_write_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import eventfd_write"))

  def test_get_terminal_size_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import get_terminal_size"))

  def test_get_inheritable_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import get_inheritable"))

  def test_set_inheritable_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import set_inheritable"))

  def test_get_handle_inheritable_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import get_handle_inheritable"))

  def test_set_handle_inheritable_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import set_handle_inheritable"))

  def test_starmap_of_multiprocessing_Pool(self):
    self.assertOnlyIn((3, 3), self.detect(
        "from multiprocessing import Pool\np = Pool()\np.starmap()"))

  def test_starmap_async_of_multiprocessing_Pool(self):
    self.assertOnlyIn((3, 3), self.detect(
      "from multiprocessing import Pool\np = Pool()\np.starmap_async()"))

  def test_wait_of_multiprocessing_connection(self):
    self.assertOnlyIn((3, 3), self.detect(
        "from multiprocessing import connection\nconnection.wait()"))

  def test_get_all_start_methods_of_multiprocessing(self):
    self.assertOnlyIn((3, 4), self.detect("from multiprocessing import get_all_start_methods"))

  def test_get_start_method_of_multiprocessing(self):
    self.assertOnlyIn((3, 4), self.detect("from multiprocessing import get_start_method"))
    self.assertOnlyIn((3, 4), self.detect("import multiprocessing as mp\nmp.get_start_method"))

  def test_set_start_method_of_multiprocessing(self):
    self.assertOnlyIn((3, 4), self.detect("from multiprocessing import set_start_method"))

  def test_get_context_of_multiprocessing(self):
    self.assertOnlyIn((3, 4), self.detect("from multiprocessing import get_context"))

  def test_enterAsyncContext_of_unittest_IsolatedAsyncioTestCase(self):
    self.assertOnlyIn((3, 11),
                      self.detect("""
from unittest import IsolatedAsyncioTestCase
IsolatedAsyncioTestCase.enterAsyncContext()
"""))

  def test_assertIs_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertIs()"))

  def test_assertIsNot_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertIsNot()"))

  def test_assertIsNone_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertIsNone()"))

  def test_assertIsNotNone_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertIsNotNone()"))

  def test_assertIn_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertIn()"))

  def test_assertNotIn_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertNotIn()"))

  def test_assertIsInstance_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\nTestCase.assertIsInstance()"))

  def test_assertNotIsInstance_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\nTestCase.assertNotIsInstance()"))

  def test_assertRaisesRegexp_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertRaisesRegexp()"))

  def test_assertGreater_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertGreater()"))

  def test_assertGreaterEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertGreaterEqual()"))

  def test_assertLess_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertLess()"))

  def test_assertLessEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertLessEqual()"))

  def test_assertRegexpMatches_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertRegexpMatches()"))

  def test_assertNotRegexpMatches_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 5)), self.detect(
      "from unittest import TestCase\nTestCase.assertNotRegexpMatches()"))

  def test_assertItemsEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from unittest import TestCase\nTestCase.assertItemsEqual()"))

  def test_assertDictContainsSubset_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
      "from unittest import TestCase\nTestCase.assertDictContainsSubset()"))

  def test_addTypeEqualityFunc_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.addTypeEqualityFunc()"))

  def test_assertMultilineEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertMultilineEqual()"))

  def test_assertSequenceEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertSequenceEqual()"))

  def test_assertListEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertListEqual()"))

  def test_assertTupleEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertTupleEqual()"))

  def test_assertRegex_of_unittest_TestCase(self):
    self.assertOnlyIn((3, 2), self.detect("from unittest import TestCase\nTestCase.assertRegex()"))

  def test_assertNotRegex_of_unittest_TestCase(self):
    self.assertOnlyIn((3, 2), self.detect(
        "from unittest import TestCase\nTestCase.assertNotRegex()"))

  def test_assertSetEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertSetEqual()"))

  def test_assertDictEqual_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.assertDictEqual()"))

  def test_addCleanup_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.addCleanup()"))

  def test_doCleanups_of_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\nTestCase.doCleanups()"))

  def test_enterClassContext_of_unittest_TestCase(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from unittest import TestCase\nTestCase.enterClassContext()"))

  def test_enterContext_of_unittest_TestCase(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from unittest import TestCase\nTestCase.enterContext()"))

  def test_discover_of_unittest_TestLoader(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestLoader\nTestLoader.discover()"))

  def test_startTestRun_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestResult\nTestResult.startTestRun()"))

  def test_stopTestRun_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestResult\nTestResult.stopTestRun()"))

  def test_addModuleCleanup_of_unittest(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest import addModuleCleanup"))

  def test_doModuleCleanups_of_unittest(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest import doModuleCleanups"))

  def test_enterModuleContext_of_unittest(self):
    self.assertOnlyIn((3, 11), self.detect("from unittest import enterModuleContext"))

  def test_total_seconds_of_datetime_timedelta(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
        "from datetime import timedelta\ntimedelta.total_seconds()"))

  def test_timestamp_of_datetime_datetime(self):
    self.assertOnlyIn((3, 3), self.detect("from datetime import datetime\ndatetime.timestamp()"))

  def test_pbkdf2_hmac_of_hashlib(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import hashlib\nhashlib.pbkdf2_hmac()"))

  def test_scrypt_of_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.scrypt()"))

  def test_open_of_bz2(self):
    self.assertOnlyIn((3, 3), self.detect("import bz2\nbz2.open()"))

  def test_peek_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.peek()"))

  def test_fileno_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.fileno()"))

  def test_readable_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.readable()"))

  def test_seekable_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.seekable()"))

  def test_writable_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.writable()"))
    self.assertOnlyIn((3, 3), self.detect("import bz2\nf = bz2.BZ2File()\nf.writable()"))
    self.assertOnlyIn((3, 3), self.detect("import bz2\nf = bz2.BZ2File\nf.writable"))

  def test_read1_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.read1()"))

  def test_readinto_of_bz2_BZ2File(self):
    self.assertOnlyIn((3, 3), self.detect("from bz2 import BZ2File\nf = BZ2File()\nf.readinto()"))

  def test_count_of_collections_deque(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from collections import deque\nd = deque()\nd.count()"))

  def test_remove_of_collections_deque(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from collections import deque\nd = deque()\nd.remove()"))

  def test_reverse_of_collections_deque(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from collections import deque\nd = deque()\nd.reverse()"))

  def test_copy_of_collections_deque(self):
    self.assertOnlyIn((3, 5), self.detect("from collections import deque\nd = deque()\nd.copy()"))

  def test_index_of_collections_deque(self):
    self.assertOnlyIn((3, 5), self.detect("from collections import deque\nd = deque()\nd.index()"))

  def test_insert_of_collections_deque(self):
    self.assertOnlyIn((3, 5), self.detect("from collections import deque\nd = deque()\nd.insert()"))

  def test_move_to_end_of_collections_OrderedDict(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from collections import OrderedDict\n"
                                  "d = OrderedDict()\n"
                                  "d.move_to_end()"))

  def test_subtract_of_collections_Counter(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from collections import Counter\n"
                                  "c = Counter()\n"
                                  "c.subtract()"))

  def test_total_of_collections_Counter(self):
    self.assertOnlyIn((3, 10), self.detect("""
from collections import Counter
c = Counter()
c.total()
"""))

  def test_suppress_of_contextlib(self):
    self.assertOnlyIn((3, 4), self.detect("import contextlib\ncontextlib.suppress()"))

  def test_redirect_stdout_of_contextlib(self):
    self.assertOnlyIn((3, 4), self.detect("import contextlib\ncontextlib.redirect_stdout()"))

  def test_redirect_stderr_of_contextlib(self):
    self.assertOnlyIn((3, 5), self.detect("import contextlib\ncontextlib.redirect_stderr()"))

  def test_field_size_limit_of_csv(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import csv\ncsv.field_size_limit()"))

  def test_find_msvcrt_of_ctypes_util(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import ctypes.util\nctypes.util.find_msvcrt()"))

  def test_get_errno_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.get_errno()"))

  def test_get_last_error_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.get_last_error()"))

  def test_set_errno_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.set_errno()"))

  def test_set_last_error_of_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.set_last_error()"))

  def test_from_buffer_of_ctypes__CData(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from ctypes import _CData\n_CData.from_buffer()"))

  def test_from_buffer_copy_of_ctypes__CData(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from ctypes import _CData\n_CData.from_buffer_copy()"))

  def test_canonical_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.canonical()"))

  def test_compare_signal_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.compare_signal()"))

  def test_compare_total_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.compare_total()"))

  def test_compare_total_mag_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.compare_total_mag()"))

  def test_conjugate_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.conjugate()"))

  def test_copy_abs_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.copy_abs()"))

  def test_copy_negate_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.copy_negate()"))

  def test_copy_sign_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.copy_sign()"))

  def test_exp_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.exp()"))

  def test_from_float_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
        "from decimal import Decimal\nDecimal.from_float()"))

  def test_fma_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.fma()"))

  def test_is_canonical_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.is_canonical()"))

  def test_is_finite_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_finite()"))

  def test_is_infinite_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from decimal import Decimal\nDecimal.is_infinite()"))

  def test_is_nan_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from decimal import Decimal\nDecimal.is_nan()"))

  def test_is_normal_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_normal()"))

  def test_is_qnan_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_qnan()"))

  def test_is_signed_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_signed()"))

  def test_is_snan_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_snan()"))

  def test_is_subnormal_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.is_subnormal()"))

  def test_is_zero_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.is_zero()"))

  def test_ln_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.ln()"))

  def test_log10_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.log10()"))

  def test_logb_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.logb()"))

  def test_logical_and_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.logical_and()"))

  def test_logical_invert_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.logical_invert()"))

  def test_logical_or_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.logical_or()"))

  def test_logical_xor_of_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.logical_xor()"))

  def test_max_mag_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.max_mag()"))

  def test_min_mag_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.min_mag()"))

  def test_next_minus_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.next_minus()"))

  def test_next_plus_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from decimal import Decimal\nDecimal.next_plus()"))

  def test_next_toward_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.next_toward()"))

  def test_number_class_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.number_class()"))

  def test_radix_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from decimal import Decimal\nDecimal.radix()"))

  def test_rotate_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from decimal import Decimal\nDecimal.rotate()"))

  def test_scaleb_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from decimal import Decimal\nDecimal.scaleb()"))

  def test_shift_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from decimal import Decimal\nDecimal.shift()"))

  def test_to_integral_exact_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.to_integral_exact()"))

  def test_to_integral_value_decimal_Decimal(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from decimal import Decimal\nDecimal.to_integral_value()"))

  def test_as_integer_ratio_decimal_Decimal(self):
    self.assertOnlyIn((3, 6), self.detect(
      "from decimal import Decimal\nDecimal.as_integer_ratio()"))

  def test_localcontext_decimal(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import decimal\ndecimal.localcontext()"))

  def test_create_decimal_from_float_decimal_Context(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
      "from decimal import Context\nContext.create_decimal_from_float()"))

  def test_clear_traps_decimal_Context(self):
    self.assertOnlyIn((3, 3), self.detect("from decimal import Context\nContext.clear_traps()"))

  def test_context_diff_difflib(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import difflib\ndifflib.context_diff()"))

  def test_unified_diff_difflib(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import difflib\ndifflib.unified_diff()"))

  def test_diff_bytes_difflib(self):
    self.assertOnlyIn((3, 5), self.detect("import difflib\ndifflib.diff_bytes()"))

  def test_get_grouped_opcodes_difflib_SequenceMatcher(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from difflib import SequenceMatcher\n"
                                  "SequenceMatcher.get_grouped_opcodes()"))

  def test_cmp_to_key_from_functools(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import functools\nfunctools.cmp_to_key()"))

  def test_reduce_from_functools(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import functools\nfunctools.reduce()"))

  def test_heappushpop_from_heapq(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import heapq\nheapq.heappushpop()"))

  def test_merge_from_heapq(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import heapq\nheapq.merge()"))

  def test_nlargest_from_heapq(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import heapq\nheapq.nlargest()"))

  def test_nsmallest_from_heapq(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import heapq\nheapq.nsmallest()"))

  def test_compare_digest_from_hmac(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("import hmac\nhmac.compare_digest()"))

  def test_hmac_digest(self):
    self.assertOnlyIn((3, 7), self.detect("import hmac\nhmac.digest()"))

  def test_isgenerator_from_inspect(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import inspect\ninspect.isgenerator()"))

  def test_isgeneratorfunction_from_inspect(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import inspect\ninspect.isgeneratorfunction()"))

  def test_isabstract_from_inspect(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import inspect\ninspect.isabstract()"))

  def test_isdatadescriptor_from_inspect(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import inspect\ninspect.isdatadescriptor()"))

  def test_isgetsetdescriptor_from_inspect(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import inspect\ninspect.isgetsetdescriptor()"))

  def test_ismemberdescriptor_from_inspect(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import inspect\ninspect.ismemberdescriptor()"))

  def test_cleandoc_from_inspect(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import inspect\ninspect.cleandoc()"))

  def test_getcallargs_from_inspect(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import inspect\ninspect.getcallargs()"))

  def test_iscoroutine_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.iscoroutine()"))

  def test_iscoroutinefunction_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.iscoroutinefunction()"))

  def test_isawaitable_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.isawaitable()"))

  def test_isasyncgen_from_inspect(self):
    self.assertOnlyIn((3, 6), self.detect("import inspect\ninspect.isasyncgen()"))

  def test_isasyncgenfunction_from_inspect(self):
    self.assertOnlyIn((3, 6), self.detect("import inspect\ninspect.isasyncgenfunction()"))

  def test_signature_from_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("import inspect\ninspect.signature()"))

  def test_apply_defaults_from_inspect_BoundArguments(self):
    self.assertOnlyIn((3, 5), self.detect("from inspect import BoundArguments\n"
                                          "ba = BoundArguments()\n"
                                          "ba.apply_defaults()"))

  def test_getclosurevars_from_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("import inspect\ninspect.getclosurevars()"))

  def test_unwrap_from_inspect(self):
    self.assertOnlyIn((3, 4), self.detect("import inspect\ninspect.unwrap()"))

  def test_getattr_static_from_inspect(self):
    self.assertOnlyIn((3, 2), self.detect("import inspect\ninspect.getattr_static()"))

  def test_getgeneratorstate_from_inspect(self):
    self.assertOnlyIn((3, 2), self.detect("import inspect\ninspect.getgeneratorstate()"))

  def test_getgeneratorlocals_from_inspect(self):
    self.assertOnlyIn((3, 3), self.detect("import inspect\ninspect.getgeneratorlocals()"))

  def test_getmembers_static_from_inspect(self):
    self.assertOnlyIn((3, 11), self.detect("import inspect\ninspect.getmembers_static()"))

  def test_getcoroutinestate_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.getcoroutinestate()"))

  def test_getcoroutinelocals_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.getcoroutinelocals()"))

  def test_get_annotations_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("import inspect\ninspect.get_annotations()"))

  def test_detach_from_io_BufferedIOBase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from io import BufferedIOBase\n"
                                  "bb = BufferedIOBase()\n"
                                  "bb.detach()"))

  def test_readinto1_from_io_BufferedIOBase(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from io import BufferedIOBase\n"
                                  "bb = BufferedIOBase()\n"
                                  "bb.readinto1()"))

  def test_readinto1_from_io_BytesIO(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from io import BytesIO\n"
                                  "bb = BytesIO()\n"
                                  "bb.readinto1()"))

  def test_getbuffer_from_io_BytesIO(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from io import BytesIO\n"
                                  "bb = BytesIO()\n"
                                  "bb.getbuffer()"))

  def test_detach_from_io_TextIOBase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from io import TextIOBase\n"
                                  "bb = TextIOBase()\n"
                                  "bb.detach()"))

  def test_combinations_from_itertools(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import itertools\nitertools.combinations()"))

  def test_combinations_with_replacement_from_itertools(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("import itertools\nitertools.combinations_with_replacement()"))

  def test_compress_from_itertools(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import itertools\nitertools.compress()"))

  def test_groupby_from_itertools(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import itertools\nitertools.groupby()"))

  def test_izip_longest_from_itertools(self):
    self.assertOnlyIn((2, 6), self.detect("import itertools\nitertools.izip_longest()"))

  def test_pairwise_from_itertools(self):
    self.assertOnlyIn((3, 10), self.detect("import itertools\nitertools.pairwise()"))

  def test_permutations_from_itertools(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import itertools\nitertools.permutations()"))

  def test_product_from_itertools(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import itertools\nitertools.product()"))

  def test_tee_from_itertools(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import itertools\nitertools.tee()"))

  def test_accumulate_from_itertools(self):
    self.assertOnlyIn((3, 2), self.detect("import itertools\nitertools.accumulate()"))

  def test_getChild_from_logging_Logger(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
      "from logging import Logger\nLogger.getChild()"))

  def test_hasHandlers_from_logging_Logger(self):
    self.assertOnlyIn((3, 2), self.detect("from logging import Logger\nLogger.hasHandlers()"))

  def test__log_from_logging_LoggerAdapter(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter()._log()"))

  def test_getLevelNamesMapping_from_logging(self):
    self.assertOnlyIn((3, 11), self.detect("import logging\nlogging.getLevelNamesMapping()"))

  def test_getLogRecordFactory_from_logging(self):
    self.assertOnlyIn((3, 2), self.detect("import logging\nlogging.getLogRecordFactory()"))

  def test_setLogRecordFactory_from_logging(self):
    self.assertOnlyIn((3, 2), self.detect("import logging\nlogging.setLogRecordFactory()"))

  def test_optimize_from_pickletools(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import pickletools\npickletools.optimize()"))

  def test_get_data_from_pkgutil(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import pkgutil\npkgutil.get_data()"))

  def test_resolve_name_from_pkgutil(self):
    self.assertOnlyIn((3, 9), self.detect("import pkgutil\npkgutil.resolve_name()"))

  def test_python_branch_from_platform(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import platform\nplatform.python_branch()"))

  def test_python_implementation_from_platform(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import platform\nplatform.python_implementation()"))

  def test_python_revision_from_platform(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import platform\nplatform.python_revision()"))

  def test_linux_distribution_from_platform(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import platform\nplatform.linux_distribution()"))

  def test_run_path_from_runpy(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import runpy\nrunpy.run_path()"))

  def test_split_from_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import shlex\nshlex.split()"))

  def test_join_from_shlex(self):
    self.assertOnlyIn((3, 8), self.detect("import shlex\nshlex.join()"))

  def test_push_source_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import shlex\nshlex.shlex().push_source()"))

  def test_pop_source_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import shlex\nshlex.shlex().pop_source()"))

  def test_quote_from_shlex(self):
    self.assertOnlyIn((3, 3), self.detect("import shlex\nshlex.quote()"))

  def test_register_introspection_functions_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                                  "srv = SimpleXMLRPCServer()\n"
                                  "srv.register_introspection_functions()"))
    self.assertOnlyIn((3, 0),
                      self.detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                                  "srv = SimpleXMLRPCServer()\n"
                                  "srv.register_introspection_functions()"))

  def test_serialize_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().serialize()"))

  def test_getlimit_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().getlimit()"))

  def test_setlimit_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().setlimit()"))

  def test_set_progress_handler_from_sqlite3_Connection(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from sqlite3 import Connection\n"
                                  "conn = Connection()\n"
                                  "conn.set_progress_handler()"))

  def test_enable_load_extension_from_sqlite3_Connection(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from sqlite3 import Connection\n"
                                  "conn = Connection()\n"
                                  "conn.enable_load_extension()"))

  def test_load_extension_from_sqlite3_Connection(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from sqlite3 import Connection\n"
                                  "conn = Connection()\n"
                                  "conn.load_extension()"))

  def test_iter_dump_from_sqlite3_Connection(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from sqlite3 import Connection\n"
                                  "conn = Connection()\n"
                                  "conn.iter_dump()"))

  def test_set_trace_callback_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from sqlite3 import Connection\n"
                                  "conn = Connection()\n"
                                  "conn.set_trace_callback()"))

  def test_keys_from_sqlite3_Row(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from sqlite3 import Row\n"
                                  "conn = Row()\n"
                                  "conn.keys()"))

  def test_create_default_context_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import ssl\nssl.create_default_context()"))

  def test__https_verify_certificates_from_ssl(self):
    self.assertOnlyIn((2, 7), self.detect("import ssl\nssl._https_verify_certificates()"))

  def test_RAND_bytes_from_ssl(self):
    self.assertOnlyIn((3, 3), self.detect("import ssl\nssl.RAND_bytes()"))

  def test_RAND_pseudo_bytes_from_ssl(self):
    self.assertOnlyIn((3, 3), self.detect("import ssl\nssl.RAND_pseudo_bytes()"))

  def test_match_hostname_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import ssl\nssl.match_hostname()"))

  def test_get_default_verify_paths_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import ssl\nssl.get_default_verify_paths()"))

  def test_enum_certificates_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import ssl\nssl.enum_certificates()"))

  def test_enum_crls_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("import ssl\nssl.enum_crls()"))

  def test_set_alpn_protocols_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 5)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.set_alpn_protocols()"))

  def test_cert_store_stats_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.cert_store_stats()"))

  def test_load_default_certs_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.load_default_certs()"))

  def test_get_ca_certs_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.get_ca_certs()"))

  def test_get_ciphers_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.get_ciphers()"))

  def test_set_npn_protocols_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.set_npn_protocols()"))

  def test_load_dh_params_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.load_dh_params()"))

  def test_set_ecdh_curve_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.set_ecdh_curve()"))

  def test_set_servername_callback_from_ssl_SSLContext(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.set_servername_callback()"))

  def test_verify_client_post_handshake_from_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ssl import SSLSocket\n"
                                  "sock = SSLSocket()\n"
                                  "sock.verify_client_post_handshake()"))

  def test_check_call_from_subprocess(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import subprocess\nsubprocess.check_call()"))

  def test_check_output_from_subprocess(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import subprocess\nsubprocess.check_output()"))

  def test_send_signal_from_subprocess_Popen(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from subprocess import Popen\nPopen.send_signal()"))

  def test_terminate_from_subprocess_Popen(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from subprocess import Popen\nPopen.terminate()"))

  def test_kill_from_subprocess_Popen(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from subprocess import Popen\nPopen.kill()"))

  def test_run_from_subprocess(self):
    self.assertOnlyIn((3, 5), self.detect("import subprocess\nsubprocess.run()"))

  def test_extractall_from_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect(
        "from tarfile import TarFile\nTarFile.extractall()"))

  def test_fromtarfile_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarInfo\nTarInfo.fromtarfile()"))

  def test_shorten_from_textwrap(self):
    self.assertOnlyIn((3, 4), self.detect("import textwrap\ntextwrap.shorten()"))

  def test_indent_from_textwrap(self):
    self.assertOnlyIn((3, 3), self.detect("import textwrap\ntextwrap.indent()"))

  def test_timeit_from_timeit(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import timeit\ntimeit.timeit()"))

  def test_repeat_from_timeit(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import timeit\ntimeit.repeat()"))

  def test_info_patchlevel_from_tkinter(self):
    self.assertOnlyIn((3, 11), self.detect("import tkinter\ntkinter.info_patchlevel()"))

  def test_warnpy3k_from_warnings(self):
    self.assertOnlyIn((2, 6), self.detect("import warnings\nwarnings.warnpy3k()"))

  def test_iterkeyrefs_from_weakref_WeakKeyDictionary(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from weakref import WeakKeyDictionary\n"
                                  "wkd = WeakKeyDictionary()\n"
                                  "wkd.iterkeyrefs()"))

  def test_keyrefs_from_weakref_WeakKeyDictionary(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from weakref import WeakKeyDictionary\n"
                                  "wkd = WeakKeyDictionary()\n"
                                  "wkd.keyrefs()"))

  def test_itervaluerefs_from_weakref_WeakValueDictionary(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from weakref import WeakValueDictionary\n"
                                  "wkd = WeakValueDictionary()\n"
                                  "wkd.itervaluerefs()"))

  def test_valuerefs_from_weakref_WeakValueDictionary(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from weakref import WeakValueDictionary\n"
                                  "wkd = WeakValueDictionary()\n"
                                  "wkd.valuerefs()"))

  def test_read_environ_from_wsgiref_handlers(self):
    self.assertOnlyIn((3, 2), self.detect(
        "import wsgiref.handlers\nwsgiref.handlers.read_environ()"))

  def test_fromstringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree import ElementTree\n"
                                  "tree = ElementTree()\n"
                                  "tree.fromstringlist()"))

  def test_register_namespace_from_xml_etree_ElementTree(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree import ElementTree\n"
                                  "tree = ElementTree()\n"
                                  "tree.register_namespace()"))

  def test_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree import ElementTree\n"
                                  "tree = ElementTree()\n"
                                  "tree.tostringlist()"))

  def test_extend_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import Element\n"
                                  "elm = Element()\n"
                                  "elm.extend()"))

  def test_iter_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import Element\n"
                                  "elm = Element()\n"
                                  "elm.iter()"))

  def test_iterfind_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import Element\n"
                                  "elm = Element()\n"
                                  "elm.iterfind()"))

  def test_itertext_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import Element\n"
                                  "elm = Element()\n"
                                  "elm.itertext()"))

  def test_indent_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from xml.etree.ElementTree import indent\n"
                                  "indent()"))

  def test_iterfind_from_xml_etree_ElementTree_ElementTree(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import ElementTree\n"
                                  "tree = ElementTree()\n"
                                  "tree.iterfind()"))

  def test_doctype_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from xml.etree.ElementTree import TreeBuilder\n"
                                  "tree = TreeBuilder()\n"
                                  "tree.doctype()"))

  def test_comment_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree.ElementTree import TreeBuilder\n"
                                  "tree = TreeBuilder()\n"
                                  "tree.comment()"))

  def test_start_ns_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree.ElementTree import TreeBuilder\n"
                                  "tree = TreeBuilder()\n"
                                  "tree.start_ns()"))

  def test_end_ns_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree.ElementTree import TreeBuilder\n"
                                  "tree = TreeBuilder()\n"
                                  "tree.end_ns()"))

  def test_canonicalize_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree import ElementTree\n"
                                  "tree = ElementTree()\n"
                                  "tree.canonicalize()"))

  def test_open_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.open()"))

  def test_extract_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.extract()"))

  def test_extractall_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.extractall()"))

  def test_mkdir_from_zipfile_ZipFile(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.mkdir()"))

  def test_setpassword_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.setpassword()"))

  def test_from_file_from_zipfile_ZipInfo(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zipfile import ZipInfo\n"
                                  "zf = ZipInfo()\n"
                                  "zf.from_file()"))

  def test_is_dir_from_zipfile_ZipInfo(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zipfile import ZipInfo\n"
                                  "zf = ZipInfo()\n"
                                  "zf.is_dir()"))

  def test_get_filename_from_zipimport_zipimporter(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from zipimport import zipimporter\n"
                                  "zi = zipimporter()\n"
                                  "zi.get_filename()"))

  def test_create_module_from_zipimport_zipimporter(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from zipimport import zipimporter\n"
                                  "zi = zipimporter()\n"
                                  "zi.create_module()"))

  def test_exec_module_from_zipimport_zipimporter(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from zipimport import zipimporter\n"
                                  "zi = zipimporter()\n"
                                  "zi.exec_module()"))

  def test_find_spec_from_zipimport_zipimporter(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from zipimport import zipimporter\n"
                                  "zi = zipimporter()\n"
                                  "zi.find_spec()"))

  def test_invalidate_caches_from_zipimport_zipimporter(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from zipimport import zipimporter\n"
                                  "zi = zipimporter()\n"
                                  "zi.invalidate_caches()"))

  def test_Tcl_from_Tkinter(self):
    self.assertOnlyIn((2, 4), self.detect("import Tkinter\nTkinter.Tcl()"))

  def test_mksalt_from_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.mksalt()"))

  def test_formatdate_from_email_utils(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import email.utils\nemail.utils.formatdate()"))

  def test_localtime_from_email_utils(self):
    self.assertOnlyIn((3, 3), self.detect("import email.utils\nemail.utils.localtime()"))

  def test_parsedate_to_datetime_from_email_utils(self):
    self.assertOnlyIn((3, 3), self.detect(
      "import email.utils\nemail.utils.parsedate_to_datetime()"))

  def test_format_datetime_from_email_utils(self):
    self.assertOnlyIn((3, 3), self.detect("import email.utils\nemail.utils.format_datetime()"))

  def test_copysign_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.copysign()"))

  def test_fsum_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.fsum()"))

  def test_isinf_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.isinf()"))

  def test_isnan_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.isnan()"))

  def test_trunc_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.trunc()"))

  def test_exp2_from_math(self):
    self.assertOnlyIn((3, 11), self.detect("import math\nmath.exp2()"))

  def test_expm1_from_math(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import math\nmath.expm1()"))

  def test_log1p_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.log1p()"))

  def test_asinh_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.asinh()"))

  def test_acosh_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.acosh()"))

  def test_atanh_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.atanh()"))

  def test_erf_from_math(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import math\nmath.erf()"))

  def test_erfc_from_math(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import math\nmath.erfc()"))

  def test_gamma_from_math(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import math\nmath.gamma()"))

  def test_lgamma_from_math(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import math\nmath.lgamma()"))

  def test_gcd_from_math(self):
    self.assertOnlyIn((3, 5), self.detect("import math\nmath.gcd()"))

  def test_isclose_from_math(self):
    self.assertOnlyIn((3, 5), self.detect("import math\nmath.isclose()"))

  def test_isfinite_from_math(self):
    self.assertOnlyIn((3, 2), self.detect("import math\nmath.isfinite()"))

  def test_log2_from_math(self):
    self.assertOnlyIn((3, 3), self.detect("import math\nmath.log2()"))

  def test_dist_from_math(self):
    self.assertOnlyIn((3, 8), self.detect("import math\nmath.dist()"))

  def test_cbrt_from_math(self):
    self.assertOnlyIn((3, 11), self.detect("import math\nmath.cbrt()"))

  def test_comb_from_math(self):
    self.assertOnlyIn((3, 8), self.detect("import math\nmath.comb()"))

  def test_isqrt_from_math(self):
    self.assertOnlyIn((3, 8), self.detect("import math\nmath.isqrt()"))

  def test_perm_from_math(self):
    self.assertOnlyIn((3, 8), self.detect("import math\nmath.perm()"))

  def test_prod_from_math(self):
    self.assertOnlyIn((3, 8), self.detect("import math\nmath.prod()"))

  def test_remainder_from_math(self):
    self.assertOnlyIn((3, 7), self.detect("import math\nmath.remainder()"))

  def test_home_from_path(self):
    self.assertOnlyIn((3, 5), self.detect("from pathlib import Path\np=Path('foo')\np.home()"))

  def test_expanduser_from_path(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from pathlib import Path\np=Path('foo')\np.expanduser()"))

  def test_read_bytes_from_path(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from pathlib import Path\np=Path('foo')\np.read_bytes()"))

  def test_is_mount_from_path(self):
    self.assertOnlyIn((3, 7), self.detect("from pathlib import Path\np=Path('foo')\np.is_mount()"))

  def test_read_text_from_path(self):
    self.assertOnlyIn((3, 5), self.detect("from pathlib import Path\np=Path('foo')\np.read_text()"))

  def test_samefile_from_path(self):
    self.assertOnlyIn((3, 5), self.detect("from pathlib import Path\np=Path('foo')\np.samefile()"))

  def test_write_bytes_from_path(self):
    self.assertOnlyIn((3, 5), self.detect(
        "from pathlib import Path\np=Path('foo')\np.write_bytes()"))

  def test_write_text_from_path(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from pathlib import Path\np=Path('foo')\np.write_text()"))

  def test_link_to_from_path(self):
    self.assertOnlyIn((3, 8), self.detect("from pathlib import Path\np=Path('foo')\np.link_to()"))

  def test_hardlink_to_from_path(self):
    self.assertOnlyIn((3, 10), self.detect("""
from pathlib import Path
p=Path('foo')
p.hardlink_to()
"""))

  def test_readlink_from_path(self):
    self.assertOnlyIn((3, 9), self.detect("from pathlib import Path\np=Path('foo')\np.readlink()"))

  def test_is_relative_to_from_pathlib_PurePath(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from pathlib import PurePath\n"
                                  "p = PurePath()\n"
                                  "p.is_relative_to()"))

  def test_with_stem_from_pathlib_PurePath(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from pathlib import PurePath\n"
                                  "p = PurePath()\n"
                                  "p.with_stem()"))

  def test_all_suffixes_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib import machinery\nmachinery.all_suffixes()"))

  def test_find_spec_of_importlib_machinery_PathFinder(self):
    self.assertOnlyIn((3, 4), self.detect(
      "from importlib.machinery import PathFinder\nPathFinder.find_spec()"))

  def test_find_spec_of_importlib_machinery_FileFinder(self):
    self.assertOnlyIn((3, 4), self.detect(
      "from importlib.machinery import FileFinder\nFileFinder.find_spec()"))

  def test_create_module_of_importlib_machinery_ExtensionFileLoader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from importlib.machinery import ExtensionFileLoader\n"
                                  "ExtensionFileLoader.create_module()"))

  def test_exec_module_of_importlib_machinery_ExtensionFileLoader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from importlib.machinery import ExtensionFileLoader\n"
                                  "ExtensionFileLoader.exec_module()"))

  def test_get_filename_of_importlib_machinery_ExtensionFileLoader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.machinery import ExtensionFileLoader\n"
                                  "ExtensionFileLoader.get_filename()"))

  def test_cache_from_source_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.cache_from_source"))

  def test_source_from_cache_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.source_from_cache"))

  def test_decode_source_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.decode_source"))

  def test_resolve_name_of_importlib_util(self):
    self.assertOnlyIn((3, 3), self.detect("from importlib import util\nutil.resolve_name"))

  def test_find_spec_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.find_spec"))

  def test_module_from_spec_of_importlib_util(self):
    self.assertOnlyIn((3, 5), self.detect("from importlib import util\nutil.module_from_spec"))

  def test_spec_from_loader_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.spec_from_loader"))

  def test_spec_from_file_location_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect(
        "from importlib import util\nutil.spec_from_file_location"))

  def test_source_hash_of_importlib_util(self):
    self.assertOnlyIn((3, 7), self.detect("from importlib import util\nutil.source_hash"))

  def test_pthread_getcpuclockid_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import pthread_getcpuclockid"))

  def test_clock_getres_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import clock_getres"))

  def test_clock_gettime_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import clock_gettime"))

  def test_clock_gettime_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import clock_gettime_ns"))

  def test_clock_settime_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import clock_settime"))

  def test_clock_settime_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import clock_settime_ns"))

  def test_get_clock_info_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import get_clock_info"))

  def test_monotonic_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import monotonic"))

  def test_monotonic_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import monotonic_ns"))

  def test_perf_counter_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import perf_counter"))

  def test_perf_counter_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import perf_counter_ns"))

  def test_process_time_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import process_time"))

  def test_process_time_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import process_time_ns"))

  def test_thread_time_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import thread_time"))

  def test_thread_time_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import thread_time_ns"))

  def test_time_ns_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import time_ns"))

  def test__check_future_of_asyncio_Task(self):
    self.assertOnlyIn((3, 11), self.detect("from asyncio import Task\nTask()._check_future()"))

  def test_run_of_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("import asyncio\nasyncio.run()"))

  def test_run_coroutine_threadsafe_of_asyncio(self):
    self.assertOnlyIn((3, 5), self.detect("import asyncio\nasyncio.run_coroutine_threadsafe()"))

  def test_create_task_of_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("import asyncio\nasyncio.create_task()"))

  def test_current_task_of_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("import asyncio\nasyncio.current_task()"))

  def test_all_tasks_of_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("import asyncio\nasyncio.all_tasks()"))

  def test_parse_intermixed_args_of_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from argparse import ArgumentParser\n"
                                  "ap = ArgumentParser()\nap.parse_intermixed_args()"))

  def test_parse_known_intermixed_args_of_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from argparse import ArgumentParser\n"
                                  "ap = ArgumentParser()\nap.parse_known_intermixed_args()"))

  def test_byteswap_of_audioop(self):
    self.assertOnlyIn((3, 4), self.detect("import audioop\naudioop.byteswap()"))

  def test_a85encode_of_base64(self):
    self.assertOnlyIn((3, 4), self.detect("import base64\nbase64.a85encode()"))

  def test_a85decode_of_base64(self):
    self.assertOnlyIn((3, 4), self.detect("import base64\nbase64.a85decode()"))

  def test_decodebytes_of_base64(self):
    self.assertOnlyIn((3, 1), self.detect("import base64\nbase64.decodebytes()"))

  def test_encodebytes_of_base64(self):
    self.assertOnlyIn((3, 1), self.detect("import base64\nbase64.encodebytes()"))

  def test_bpformat_of_bdb_Breakpoint(self):
    self.assertOnlyIn((3, 2), self.detect(
        "from bdb import Breakpoint\nbp=Breakpoint()\nbp.bpformat()"))

  def test_get_bpbynumber_of_bdb_Bdb(self):
    self.assertOnlyIn((3, 2), self.detect("from bdb import Bdb\nbp=Bdb()\nbp.get_bpbynumber()"))

  def test_clearBreakpoints_from_bdb_Breakpoint(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from bdb import Breakpoint\n"
                                  "Breakpoint().clearBreakpoints()"))

  def test_itermonthdays3_of_calendar_Calendar(self):
    self.assertOnlyIn((3, 7), self.detect(
      "from calendar import Calendar\nc=Calendar()\nc.itermonthdays3()"))

  def test_itermonthdays4_of_calendar_Calendar(self):
    self.assertOnlyIn((3, 7), self.detect(
      "from calendar import Calendar\nc=Calendar()\nc.itermonthdays4()"))

  def test_isfinite_of_cmath(self):
    self.assertOnlyIn((3, 2), self.detect("import cmath\ncmath.isfinite()"))

  def test_isclose_of_cmath(self):
    self.assertOnlyIn((3, 5), self.detect("import cmath\ncmath.isclose()"))

  def test_compile_file_of_compileall(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import compileall\ncompileall.compile_file()"))

  def test_nullcontext_of_contextlib(self):
    self.assertOnlyIn((3, 7), self.detect("import contextlib\ncontextlib.nullcontext()"))

  def test_aclosing_of_contextlib(self):
    self.assertOnlyIn((3, 10), self.detect("import contextlib\ncontextlib.aclosing()"))

  def test_chdir_of_contextlib(self):
    self.assertOnlyIn((3, 11), self.detect("import contextlib\ncontextlib.chdir()"))

  def test_writeheader_of_csv_DictWriter(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from csv import DictWriter\n"
                                                    "DictWriter.writeheader()"))

  def test_update_lines_cols_of_curses(self):
    self.assertOnlyIn((3, 5), self.detect("import curses\ncurses.update_lines_cols()"))

  def test_unget_wch_of_curses(self):
    self.assertOnlyIn((3, 3), self.detect("import curses\ncurses.unget_wch()"))

  def test_has_extended_color_support_of_curses(self):
    self.assertOnlyIn((3, 10), self.detect("import curses\ncurses.has_extended_color_support()"))

  def test_fromisoformat_of_datetime_date(self):
    self.assertOnlyIn((3, 7), self.detect("from datetime import date\ndate.fromisoformat()"))

  def test_fromisoformat_of_datetime_time(self):
    self.assertOnlyIn((3, 7), self.detect("from datetime import time\ntime.fromisoformat()"))

  def test_fromisoformat_of_datetime_datetime(self):
    self.assertOnlyIn((3, 7), self.detect(
      "from datetime import datetime\ndatetime.fromisoformat()"))

  def test_fromisocalendar_of_datetime_date(self):
    self.assertOnlyIn((3, 8), self.detect("from datetime import date\ndate.fromisocalendar()"))

  def test_fromisocalendar_of_datetime_datetime(self):
    self.assertOnlyIn((3, 8), self.detect(
        "from datetime import datetime\ndatetime.fromisocalendar()"))

  def test_code_info_of_dis(self):
    self.assertOnlyIn((3, 2), self.detect("import dis\ndis.code_info()"))

  def test_show_code_of_dis(self):
    self.assertOnlyIn((3, 2), self.detect("import dis\ndis.show_code()"))

  def test_get_instructions_of_dis(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.get_instructions()"))

  def test_stack_effect_of_dis(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.stack_effect()"))

  def test_as_integer_ratio_of_franctions_Fraction(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from fractions import Fraction\n"
                                  "Fraction(42).as_integer_ratio()"))
    self.assertOnlyIn((3, 8),
                      self.detect("from fractions import Fraction\n"
                                  "f=Fraction(42)\nf.as_integer_ratio()"))

  def test_pgettext_of_gettext(self):
    self.assertOnlyIn((3, 8), self.detect("import gettext\ngettext.pgettext()"))

  def test_dpgettext_of_gettext(self):
    self.assertOnlyIn((3, 8), self.detect("import gettext\ngettext.dpgettext()"))

  def test_npgettext_of_gettext(self):
    self.assertOnlyIn((3, 8), self.detect("import gettext\ngettext.npgettext()"))

  def test_dnpgettext_of_gettext(self):
    self.assertOnlyIn((3, 8), self.detect("import gettext\ngettext.dnpgettext()"))

  def test_compress_of_gzip(self):
    self.assertOnlyIn((3, 2), self.detect("import gzip\ngzip.compress()"))

  def test_decompress_of_gzip(self):
    self.assertOnlyIn((3, 2), self.detect("import gzip\ngzip.decompress()"))

  def test_peek_of_gzip_GzipFile(self):
    self.assertOnlyIn((3, 2), self.detect("from gzip import GzipFile\nGzipFile.peek()"))

  def test_madvise_of_mmap_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("from mmap import mmap\nmmap.madvise()"))

  def test_add_dll_directory_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("import os\nos.add_dll_directory()"))

  def test_memfd_create_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("import os\nos.memfd_create()"))

  def test_getxattr_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import getxattr"))

  def test_setxattr_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import setxattr"))

  def test_removexattr_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import removexattr"))

  def test_listxattr_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import listxattr"))

  def test_reducer_override_from_pickle_Pickler(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import Pickler\n"
                                  "p=Pickler('foo')\n"
                                  "p.reducer_override(None, None)"))

  def test_dump_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import dump"))

  def test_dumps_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import dumps"))

  def test_load_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import load"))

  def test_loads_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import loads"))

  def test_create_server_of_socket(self):
    self.assertOnlyIn((3, 8), self.detect("from socket import create_server"))

  def test_has_dualstack_ipv6_of_socket(self):
    self.assertOnlyIn((3, 8), self.detect("from socket import has_dualstack_ipv6"))

  def test_fromshare_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import fromshare"))

  def test_share_of_socket_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import socket\n"
                                          "socket().share"))

  def test_close_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import close"))

  def test_CMSG_LEN_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CMSG_LEN"))

  def test_CMSG_SPACE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CMSG_SPACE"))

  def test_sethostname_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import sethostname"))

  def test_if_nameindex_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import if_nameindex"))

  def test_if_nametoindex_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import if_nametoindex"))

  def test_if_indextoname_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import if_indextoname"))

  def test_detach_of_socket_socket(self):
    self.assertOnlyIn((3, 2), self.detect("from socket import socket\n"
                                          "socket().detach"))

  def test_get_inheritable_of_socket_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import socket\n"
                                          "socket().get_inheritable"))

  def test_set_inheritable_of_socket_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import socket\n"
                                          "socket().set_inheritable"))

  def test_getblocking_of_socket_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import socket\n"
                                          "socket().getblocking"))

  def test_recvmsg_of_socket_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import socket\n"
                                          "socket().recvmsg"))

  def test_recvmsg_into_of_socket_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import socket\n"
                                          "socket().recvmsg_into"))

  def test_sendmsg_of_socket_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import socket\n"
                                          "socket().sendmsg"))

  def test_sendmsg_afalg_of_socket_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import socket\n"
                                          "socket().sendmsg_afalg"))

  def test_sendfile_of_socket_socket(self):
    self.assertOnlyIn((3, 5), self.detect("from socket import socket\n"
                                          "socket().sendfile"))

  def test_fmean_of_statistics(self):
    self.assertOnlyIn((3, 8), self.detect("from statistics import fmean"))

  def test_geometric_mean_of_statistics(self):
    self.assertOnlyIn((3, 8), self.detect("from statistics import geometric_mean"))

  def test_harmonic_mean_of_statistics(self):
    self.assertOnlyIn((3, 6), self.detect("from statistics import harmonic_mean"))

  def test_multimode_of_statistics(self):
    self.assertOnlyIn((3, 8), self.detect("from statistics import multimode"))

  def test_quantiles_of_statistics(self):
    self.assertOnlyIn((3, 8), self.detect("from statistics import quantiles"))

  def test_covariance_of_statistics(self):
    self.assertOnlyIn((3, 10), self.detect("from statistics import covariance"))

  def test_correlation_of_statistics(self):
    self.assertOnlyIn((3, 10), self.detect("from statistics import correlation"))

  def test_linear_regression_of_statistics(self):
    self.assertOnlyIn((3, 10), self.detect("from statistics import linear_regression"))

  def test_unraisablehook_of_sys(self):
    self.assertOnlyIn((3, 8), self.detect("from sys import unraisablehook"))

  def test_excepthook_of_threading(self):
    self.assertOnlyIn((3, 8), self.detect("from threading import excepthook"))

  def test_get_native_id_of_threading(self):
    self.assertOnlyIn((3, 8), self.detect("from threading import get_native_id"))

  def test_get_ident_of_threading(self):
    self.assertOnlyIn((3, 3), self.detect("from threading import get_ident"))

  def test_main_thread_of_threading(self):
    self.assertOnlyIn((3, 4), self.detect("from threading import main_thread"))

  def test_generate_tokens_of_tokenize(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from tokenize import generate_tokens"))

  def test_untokenize_of_tokenize(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from tokenize import untokenize"))

  def test_open_of_tokenize(self):
    self.assertOnlyIn((3, 2), self.detect("from tokenize import open"))

  def test_assert_never_of_typing(self):
    self.assertOnlyIn((3, 11), self.detect("from typing import assert_never"))

  def test_assert_type_of_typing(self):
    self.assertOnlyIn((3, 11), self.detect("from typing import assert_type"))

  def test_clear_overloads_of_typing(self):
    self.assertOnlyIn((3, 11), self.detect("from typing import clear_overloads"))

  def test_get_origin_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import get_origin"))

  def test_get_overloads_of_typing(self):
    self.assertOnlyIn((3, 11), self.detect("from typing import get_overloads"))

  def test_get_args_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import get_args"))

  def test_is_typeddict_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import is_typeddict"))

  def test_reveal_type_of_typing(self):
    self.assertOnlyIn((3, 11), self.detect("from typing import reveal_type"))

  def test_is_normalized_of_unicodedata(self):
    self.assertOnlyIn((3, 8), self.detect("from unicodedata import is_normalized"))

  def test_addaudithook_of_sys(self):
    self.assertOnlyIn((3, 8), self.detect("from sys import addaudithook"))

  def test_audit_of_sys(self):
    self.assertOnlyIn((3, 8), self.detect("from sys import audit"))

  def test_copy_file_range_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import copy_file_range"))

  def test_posix_spawn_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import posix_spawn"))

  def test_posix_spawnp_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import posix_spawnp"))

  def test_register_at_fork_of_os(self):
    self.assertOnlyIn((3, 7), self.detect("from os import register_at_fork"))

  def test_S_ISDOOR_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_ISDOOR"))

  def test_S_ISPORT_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_ISPORT"))

  def test_S_ISWHT_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_ISWHT"))

  def test_filemode_of_stat(self):
    self.assertOnlyIn((3, 3), self.detect("from stat import filemode"))

  def test_ehlo_or_helo_if_needed_of_smtplib_SMTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from smtplib import SMTP\nSMTP.ehlo_or_helo_if_needed"))

  def test_auth_of_smtplib_SMTP(self):
    self.assertOnlyIn((3, 5), self.detect("from smtplib import SMTP\nSMTP.auth"))

  def test_send_message_of_smtplib_SMTP(self):
    self.assertOnlyIn((3, 2), self.detect("from smtplib import SMTP\nSMTP.send_message"))

  def test_dictConfig_from_logging_config(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
        "import logging.config\nlogging.config.dictConfig()"))

  def test_captured_stdout_from_test_support(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import test.support\ntest.support.captured_stdout()"))

  def test_catch_threading_exception_from_test_support(self):
    self.assertOnlyIn((3, 8), self.detect(
        "import test.support\ntest.support.catch_threading_exception()"))

  def test_catch_unraisable_exception_from_test_support(self):
    self.assertOnlyIn((3, 8), self.detect(
        "import test.support\ntest.support.catch_unraisable_exception()"))

  def test_check__all___from_test_support(self):
    self.assertOnlyIn((3, 6), self.detect("import test.support\ntest.support.check__all__()"))

  def test_check_py3k_warnings_from_test_support(self):
    self.assertOnlyIn((2, 7), self.detect(
      "import test.support\ntest.support.check_py3k_warnings()"))

  def test_check_syntax_warning_from_test_support(self):
    self.assertOnlyIn((3, 8), self.detect(
        "import test.support\ntest.support.check_syntax_warning()"))

  def test_check_warnings_from_test_support(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import test.support\ntest.support.check_warnings()"))

  def test_detect_api_mismatch_from_test_support(self):
    self.assertOnlyIn((3, 5), self.detect(
      "import test.support\ntest.support.detect_api_mismatch()"))

  def test_flush_std_streams_from_test_support(self):
    self.assertOnlyIn((3, 11), self.detect(
      "import test.support\ntest.support.flush_std_streams()"))

  def test_import_fresh_module_from_test_support(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
        "import test.support\ntest.support.import_fresh_module()"))

  def test_import_module_from_test_support(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
        "import test.support\ntest.support.import_module()"))

  def test_seal_from_unittest_mock(self):
    self.assertOnlyIn((3, 7), self.detect("import unittest.mock\nunittest.mock.seal()"))
    self.assertTrue(self.config.add_backport("mock"))
    self.assertOnlyIn(((3, 6)), self.detect("import unittest.mock\nunittest.mock.seal()"))

  def test_quoteattr_from_xml_sax_saxutils(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect(
        "import xml.sax.saxutils\nxml.sax.saxutils.quoteattr()"))

  def test_unescape_from_xml_sax_saxutils(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect(
        "import xml.sax.saxutils\nxml.sax.saxutils.unescape()"))

  def test_set_from_ConfigParser_SafeConfigParser(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from ConfigParser import SafeConfigParser\n"
                                  "SafeConfigParser().set()"))

  def test_GetArgv_from_EasyDialogs(self):
    self.assertOnlyIn((2, 0), self.detect("import EasyDialogs\nEasyDialogs.GetArgv()"))

  def test_join_from_Queue_Queue(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from Queue import Queue\n"
                                  "Queue().join()"))

  def test_task_done_from_Queue_Queue(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from Queue import Queue\n"
                                  "Queue().task_done()"))

  def test_do_GET_from_SimpleHTTPServer_SimpleHTTPRequestHandler(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleHTTPServer import SimpleHTTPRequestHandler\n"
                                  "SimpleHTTPRequestHandler().do_GET()"))

  def test_server_close_from_SocketServer_BaseServer(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from SocketServer import BaseServer\n"
                                  "BaseServer().server_close()"))

  def test_shutdown_from_SocketServer_BaseServer(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from SocketServer import BaseServer\n"
                                  "BaseServer().shutdown()"))

  def test_get_native_id_from__thread(self):
    self.assertOnlyIn((3, 8), self.detect("import _thread\n_thread.get_native_id()"))

  def test_CreateKeyEx_from__winreg(self):
    self.assertOnlyIn((2, 7), self.detect("import _winreg\n_winreg.CreateKeyEx()"))

  def test_DeleteKeyEx_from__winreg(self):
    self.assertOnlyIn((2, 7), self.detect("import _winreg\n_winreg.DeleteKeyEx()"))

  def test_ExpandEnvironmentStrings_from__winreg(self):
    self.assertOnlyIn((2, 6), self.detect("import _winreg\n_winreg.ExpandEnvironmentStrings()"))

  def test_get_cache_token_from_abc(self):
    self.assertOnlyIn((3, 4), self.detect("import abc\nabc.get_cache_token()"))

  def test_update_abstractmethods_from_abc(self):
    self.assertOnlyIn((3, 10), self.detect("import abc\nabc.update_abstractmethods()"))

  def test_frombytes_from_array_array(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from array import array\n"
                                  "array().frombytes()"))

  def test_tobytes_from_array_array(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from array import array\n"
                                  "array().tobytes()"))

  def test_get_source_segment_from_ast(self):
    self.assertOnlyIn((3, 8), self.detect("import ast\nast.get_source_segment()"))

  def test_is_active_from_asyncio_AbstractChildWatcher(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import AbstractChildWatcher\n"
                                  "AbstractChildWatcher().is_active()"))

  def test_get_loop_from_asyncio_Future(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Future\n"
                                  "Future().get_loop()"))

  def test_cancelled_from_asyncio_Handle(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Handle\n"
                                  "Handle().cancelled()"))

  def test_is_reading_from_asyncio_ReadTransport(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import ReadTransport\n"
                                  "ReadTransport().is_reading()"))

  def test_get_loop_from_asyncio_Server(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Server\n"
                                  "Server().get_loop()"))

  def test_is_serving_from_asyncio_Server(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Server\n"
                                  "Server().is_serving()"))

  def test_serve_forever_from_asyncio_Server(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Server\n"
                                  "Server().serve_forever()"))

  def test_start_serving_from_asyncio_Server(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Server\n"
                                  "Server().start_serving()"))

  def test_readuntil_from_asyncio_StreamReader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from asyncio import StreamReader\n"
                                  "StreamReader().readuntil()"))

  def test_is_closing_from_asyncio_StreamWriter(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import StreamWriter\n"
                                  "StreamWriter().is_closing()"))

  def test_start_tls_from_asyncio_StreamWriter(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from asyncio import StreamWriter\n"
                                  "StreamWriter().start_tls()"))

  def test_wait_closed_from_asyncio_StreamWriter(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import StreamWriter\n"
                                  "StreamWriter().wait_closed()"))

  def test_get_coro_from_asyncio_Task(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import Task\n"
                                  "Task().get_coro()"))

  def test_get_name_from_asyncio_Task(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import Task\n"
                                  "Task().get_name()"))

  def test_set_name_from_asyncio_Task(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import Task\n"
                                  "Task().set_name()"))

  def test_when_from_asyncio_TimerHandle(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import TimerHandle\n"
                                  "TimerHandle().when()"))

  def test_get_write_buffer_limits_from_asyncio_WriteTransport(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import WriteTransport\n"
                                  "WriteTransport().get_write_buffer_limits()"))

  def test_get_running_loop_from_asyncio(self):
    self.assertOnlyIn((3, 7), self.detect("import asyncio\nasyncio.get_running_loop()"))

  def test_isfuture_from_asyncio(self):
    self.assertOnlyIn((3, 5), self.detect("import asyncio\nasyncio.isfuture()"))

  def test_connect_accepted_socket_from_asyncio_loop(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from asyncio import loop\n"
                                  "loop().connect_accepted_socket()"))

  def test_create_future_from_asyncio_loop(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from asyncio import loop\n"
                                  "loop().create_future()"))

  def test_get_exception_handler_from_asyncio_loop(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from asyncio import loop\n"
                                  "loop().get_exception_handler()"))

  def test_sendfile_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "loop().sendfile()"))

  def test_shutdown_asyncgens_from_asyncio_loop(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from asyncio import loop\n"
                                  "loop().shutdown_asyncgens()"))

  def test_sock_recv_into_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "loop().sock_recv_into()"))

  def test_sock_recvfrom_from_asyncio_loop(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from asyncio import loop\n"
                                  "loop().sock_recvfrom()"))

  def test_sock_recvfrom_into_from_asyncio_loop(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from asyncio import loop\n"
                                  "loop().sock_recvfrom_into()"))

  def test_sock_sendto_from_asyncio_loop(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from asyncio import loop\n"
                                  "loop().sock_sendto()"))

  def test_sock_sendfile_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "loop().sock_sendfile()"))

  def test_start_tls_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "loop().start_tls()"))

  def test_shutdown_default_executor_from_asyncio_loop(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from asyncio import loop\n"
                                  "loop().shutdown_default_executor()"))

  def test_to_thread_from_asyncio(self):
    self.assertOnlyIn((3, 9), self.detect("from asyncio import to_thread"))

  def test_b85decode_from_base64(self):
    self.assertOnlyIn((3, 4), self.detect("import base64\nbase64.b85decode()"))

  def test_b85encode_from_base64(self):
    self.assertOnlyIn((3, 4), self.detect("import base64\nbase64.b85encode()"))

  def test_b32hexencode_from_base64(self):
    self.assertOnlyIn((3, 10), self.detect("import base64\nbase64.b32hexencode()"))

  def test_b32hexdecode_from_base64(self):
    self.assertOnlyIn((3, 10), self.detect("import base64\nbase64.b32hexdecode()"))

  def test_getfirst_from_cgi_FieldStorage(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from cgi import FieldStorage\n"
                                  "FieldStorage().getfirst()"))

  def test_getlist_from_cgi_FieldStorage(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from cgi import FieldStorage\n"
                                  "FieldStorage().getlist()"))

  def test_isinf_from_cmath(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import cmath\ncmath.isinf()"))

  def test_isnan_from_cmath(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import cmath\ncmath.isnan()"))

  def test_phase_from_cmath(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import cmath\ncmath.phase()"))

  def test_polar_from_cmath(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import cmath\ncmath.polar()"))

  def test_rect_from_cmath(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import cmath\ncmath.rect()"))

  def test_decode_from_codecs(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import codecs\ncodecs.decode()"))

  def test_encode_from_codecs(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import codecs\ncodecs.encode()"))

  def test_getincrementaldecoder_from_codecs(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect(
      "import codecs\ncodecs.getincrementaldecoder()"))

  def test_getincrementalencoder_from_codecs(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect(
      "import codecs\ncodecs.getincrementalencoder()"))

  def test_iterdecode_from_codecs(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import codecs\ncodecs.iterdecode()"))

  def test_iterencode_from_codecs(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import codecs\ncodecs.iterencode()"))

  def test_namereplace_errors_from_codecs(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.namereplace_errors()"))

  def test_unregister_from_codecs(self):
    self.assertOnlyIn((3, 10), self.detect("import codecs\ncodecs.unregister()"))

  def test___getnewargs___from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().__getnewargs__()"))

  def test___rmod___from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().__rmod__()"))

  def test_casefold_from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().casefold()"))

  def test_format_map_from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().format_map()"))

  def test_isprintable_from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().isprintable()"))

  def test_maketrans_from_collections_UserString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections import UserString\n"
                                  "UserString().maketrans()"))

  def test_clear_from_collections_abc_MutableSequence(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from collections.abc import MutableSequence\n"
                                  "MutableSequence().clear()"))

  def test_copy_from_collections_abc_MutableSequence(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from collections.abc import MutableSequence\n"
                                  "MutableSequence().copy()"))

  def test_read_dict_from_configparser_ConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_dict()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_dict()"))

  def test_read_file_from_configparser_ConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_file()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_file()"))

  def test_read_string_from_configparser_ConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_string()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser().read_string()"))

  def test_read_dict_from_configparser_RawConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_dict()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_dict()"))

  def test_read_file_from_configparser_RawConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_file()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_file()"))

  def test_read_string_from_configparser_RawConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_string()"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import RawConfigParser\n"
                                  "RawConfigParser().read_string()"))

  def test_get_wch_from_curses_window(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from curses import window\n"
                                  "window().get_wch()"))

  def test_strptime_from_datetime_datetime(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from datetime import datetime\n"
                                  "datetime().strptime()"))

  def test_DocFileSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import doctest\ndoctest.DocFileSuite()"))

  def test_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import doctest\ndoctest.DocTestSuite()"))

  def test_debug_from_doctest(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import doctest\ndoctest.debug()"))

  def test_debug_src_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import doctest\ndoctest.debug_src()"))

  def test_register_optionflag_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
      "import doctest\ndoctest.register_optionflag()"))

  def test_script_from_examples_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import doctest\ndoctest.script_from_examples()"))

  def test_set_unittest_reportflags_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import doctest\ndoctest.set_unittest_reportflags()"))

  def test_testfile_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import doctest\ndoctest.testfile()"))

  def test_testsource_from_doctest(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import doctest\ndoctest.testsource()"))

  def test_clone_from_email_generator_Generator(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.generator import Generator\n"
                                  "Generator().clone()"))

  def test_flatten_from_email_generator_Generator(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.generator import Generator\n"
                                  "Generator().flatten()"))

  def test_get_content_disposition_from_email_message_EmailMessage(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from email.message import EmailMessage\n"
                                  "EmailMessage().get_content_disposition()"))

  def test___bytes___from_email_message_Message(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.message import Message\n"
                                  "Message().__bytes__()"))

  def test_as_bytes_from_email_message_Message(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.message import Message\n"
                                  "Message().as_bytes()"))

  def test_del_param_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().del_param()"))

  def test_get_charset_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_charset()"))

  def test_get_content_charset_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_content_charset()"))

  def test_get_content_disposition_from_email_message_Message(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from email.message import Message\n"
                                  "Message().get_content_disposition()"))

  def test_get_content_maintype_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_content_maintype()"))

  def test_get_content_subtype_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_content_subtype()"))

  def test_get_content_type_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_content_type()"))

  def test_get_default_type_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().get_default_type()"))

  def test_replace_header_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().replace_header()"))

  def test_set_charset_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().set_charset()"))

  def test_set_default_type_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().set_default_type()"))

  def test_set_param_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().set_param()"))

  def test_set_type_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().set_type()"))

  def test_message_from_binary_file_from_email(self):
    self.assertOnlyIn((3, 2), self.detect("import email\nemail.message_from_binary_file()"))

  def test_message_from_bytes_from_email(self):
    self.assertOnlyIn((3, 2), self.detect("import email\nemail.message_from_bytes()"))

  def test_clear_cache_from_filecmp(self):
    self.assertOnlyIn((3, 4), self.detect("import filecmp\nfilecmp.clear_cache()"))

  def test_fileno_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import fileinput\nfileinput.fileno()"))

  def test_hook_compressed_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect(
      "import fileinput\nfileinput.hook_compressed()"))

  def test_hook_encoded_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import fileinput\nfileinput.hook_encoded()"))

  def test_filter_from_fnmatch(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import fnmatch\nfnmatch.filter()"))

  def test_mlsd_from_ftplib_FTP(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ftplib import FTP\n"
                                  "FTP().mlsd()"))

  def test_ccc_from_ftplib_FTP_TLS(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ftplib import FTP_TLS\n"
                                  "FTP_TLS().ccc()"))

  def test_freeze_from_gc(self):
    self.assertOnlyIn((3, 7), self.detect("import gc\ngc.freeze()"))

  def test_get_count_from_gc(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import gc\ngc.get_count()"))

  def test_get_freeze_count_from_gc(self):
    self.assertOnlyIn((3, 7), self.detect("import gc\ngc.get_freeze_count()"))

  def test_get_objects_from_gc(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import gc\ngc.get_objects()"))

  def test_get_referents_from_gc(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import gc\ngc.get_referents()"))

  def test_get_referrers_from_gc(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import gc\ngc.get_referrers()"))

  def test_get_stats_from_gc(self):
    self.assertOnlyIn((3, 4), self.detect("import gc\ngc.get_stats()"))

  def test_is_tracked_from_gc(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import gc\ngc.is_tracked()"))

  def test_is_finalized_from_gc(self):
    self.assertOnlyIn((3, 9), self.detect("import gc\ngc.is_finalized()"))

  def test_unfreeze_from_gc(self):
    self.assertOnlyIn((3, 7), self.detect("import gc\ngc.unfreeze()"))

  def test_gnu_getopt_from_getopt(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import getopt\ngetopt.gnu_getopt()"))

  def test_lgettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().lgettext()"))

  def test_lngettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().lngettext()"))

  def test_ngettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().ngettext()"))

  def test_npgettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().npgettext()"))

  def test_pgettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().pgettext()"))

  def test_ungettext_from_gettext_GNUTranslations(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from gettext import GNUTranslations\n"
                                  "GNUTranslations().ungettext()"))

  def test_lgettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().lgettext()"))

  def test_lngettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().lngettext()"))

  def test_ngettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().ngettext()"))

  def test_npgettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().npgettext()"))

  def test_output_charset_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().output_charset()"))

  def test_pgettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().pgettext()"))

  def test_set_output_charset_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().set_output_charset()"))

  def test_ungettext_from_gettext_NullTranslations(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from gettext import NullTranslations\n"
                                  "NullTranslations().ungettext()"))

  def test_bind_textdomain_codeset_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import gettext\ngettext.bind_textdomain_codeset()"))

  def test_dngettext_from_gettext(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import gettext\ngettext.dngettext()"))

  def test_ldgettext_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import gettext\ngettext.ldgettext()"))

  def test_ldngettext_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import gettext\ngettext.ldngettext()"))

  def test_lgettext_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import gettext\ngettext.lgettext()"))

  def test_lngettext_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import gettext\ngettext.lngettext()"))

  def test_ngettext_from_gettext(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import gettext\ngettext.ngettext()"))

  def test_escape_from_glob(self):
    self.assertOnlyIn((3, 4), self.detect("import glob\nglob.escape()"))

  def test_iglob_from_glob(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import glob\nglob.iglob()"))

  def test_blake2b_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.blake2b()"))

  def test_blake2s_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.blake2s()"))

  def test_file_digest_from_hashlib(self):
    self.assertOnlyIn((3, 11), self.detect("import hashlib\nhashlib.file_digest()"))

  def test_sha3_224_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.sha3_224()"))

  def test_sha3_256_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.sha3_256()"))

  def test_sha3_384_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.sha3_384()"))

  def test_sha3_512_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.sha3_512()"))

  def test_shake_128_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.shake_128()"))

  def test_shake_256_from_hashlib(self):
    self.assertOnlyIn((3, 6), self.detect("import hashlib\nhashlib.shake_256()"))

  def test_escape_from_html(self):
    self.assertOnlyIn((3, 2), self.detect("import html\nhtml.escape()"))

  def test_unescape_from_html(self):
    self.assertOnlyIn((3, 4), self.detect("import html\nhtml.unescape()"))

  def test_set_debuglevel_from_http_client_HTTPConnection(self):
    self.assertOnlyIn((3, 1),
                      self.detect("from http.client import HTTPConnection\n"
                                  "HTTPConnection().set_debuglevel()"))

  def test_set_tunnel_from_http_client_HTTPConnection(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.client import HTTPConnection\n"
                                  "HTTPConnection().set_tunnel()"))

  def test_readinto_from_http_client_HTTPResponse(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from http.client import HTTPResponse\n"
                                  "HTTPResponse().readinto()"))

  def test_flush_headers_from_http_server_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from http.server import BaseHTTPRequestHandler\n"
                                  "BaseHTTPRequestHandler().flush_headers()"))

  def test_handle_expect_100_from_http_server_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.server import BaseHTTPRequestHandler\n"
                                  "BaseHTTPRequestHandler().handle_expect_100()"))

  def test_send_response_only_from_http_server_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.server import BaseHTTPRequestHandler\n"
                                  "BaseHTTPRequestHandler().send_response_only()"))

  def test_set_tunnel_from_httplib_HTTPConnection(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from httplib import HTTPConnection\n"
                                  "HTTPConnection().set_tunnel()"))

  def test_getheaders_from_httplib_HTTPResponse(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from httplib import HTTPResponse\n"
                                  "HTTPResponse().getheaders()"))

  def test_deleteacl_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().deleteacl()"))

  def test_enable_from_imaplib_IMAP4(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().enable()"))

  def test_getannotation_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().getannotation()"))

  def test_getquota_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().getquota()"))

  def test_getquotaroot_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().getquotaroot()"))

  def test_login_cram_md5_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().login_cram_md5()"))

  def test_myrights_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().myrights()"))

  def test_namespace_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().namespace()"))

  def test_proxyauth_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().proxyauth()"))

  def test_setannotation_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().setannotation()"))

  def test_setquota_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().setquota()"))

  def test_starttls_from_imaplib_IMAP4(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().starttls()"))

  def test_thread_from_imaplib_IMAP4(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().thread()"))

  def test_unselect_from_imaplib_IMAP4(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().unselect()"))

  def test_acquire_lock_from_imp(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import imp\nimp.acquire_lock()"))

  def test_cache_from_source_from_imp(self):
    self.assertOnlyIn((3, 2), self.detect("import imp\nimp.cache_from_source()"))

  def test_get_tag_from_imp(self):
    self.assertOnlyIn((3, 2), self.detect("import imp\nimp.get_tag()"))

  def test_release_lock_from_imp(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import imp\nimp.release_lock()"))

  def test_source_from_cache_from_imp(self):
    self.assertOnlyIn((3, 2), self.detect("import imp\nimp.source_from_cache()"))

  def test_exec_module_from_importlib_abc_InspectLoader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import InspectLoader\n"
                                  "InspectLoader().exec_module()"))

  def test_source_to_code_from_importlib_abc_InspectLoader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import InspectLoader\n"
                                  "InspectLoader().source_to_code()"))

  def test_create_module_from_importlib_abc_Loader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import Loader\n"
                                  "Loader().create_module()"))

  def test_exec_module_from_importlib_abc_Loader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import Loader\n"
                                  "Loader().exec_module()"))

  def test_module_repr_from_importlib_abc_Loader(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib.abc import Loader\n"
                                  "Loader().module_repr()"))

  def test_find_spec_from_importlib_abc_MetaPathFinder(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import MetaPathFinder\n"
                                  "MetaPathFinder().find_spec()"))

  def test_find_spec_from_importlib_abc_PathEntryFinder(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import PathEntryFinder\n"
                                  "PathEntryFinder().find_spec()"))

  def test_exec_module_from_importlib_abc_SourceLoader(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from importlib.abc import SourceLoader\n"
                                  "SourceLoader().exec_module()"))

  def test_path_stats_from_importlib_abc_SourceLoader(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib.abc import SourceLoader\n"
                                  "SourceLoader().path_stats()"))

  def test_find_loader_from_importlib(self):
    self.assertOnlyIn((3, 3), self.detect("import importlib\nimportlib.find_loader()"))

  def test_invalidate_caches_from_importlib(self):
    self.assertOnlyIn((3, 3), self.detect("import importlib\nimportlib.invalidate_caches()"))

  def test_create_module_from_importlib_machinery_BuiltinImporter(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from importlib.machinery import BuiltinImporter\n"
                                  "BuiltinImporter().create_module()"))

  def test_exec_module_from_importlib_machinery_BuiltinImporter(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from importlib.machinery import BuiltinImporter\n"
                                  "BuiltinImporter().exec_module()"))

  def test_reload_from_importlib(self):
    self.assertOnlyIn((3, 4), self.detect("import importlib\nimportlib.reload()"))

  def test_files_from_importlib_resources(self):
    self.assertOnlyIn((3, 9), self.detect(
      "import importlib.resources\nimportlib.resources.files()"))

  def test_as_file_from_importlib_resources(self):
    self.assertOnlyIn((3, 9), self.detect("import importlib.resources\n"
                                          "importlib.resources.as_file()"))

  def test_from_callable_from_inspect_Signature(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from inspect import Signature\n"
                                  "Signature().from_callable()"))

  def test_reconfigure_from_io_TextIOWrapper(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from io import TextIOWrapper\n"
                                  "TextIOWrapper().reconfigure()"))

  def test_open_code_from_io(self):
    self.assertOnlyIn((3, 8), self.detect("import io\nio.open_code()"))

  def test_text_encoding_from_io(self):
    self.assertOnlyIn((3, 10), self.detect("import io\nio.text_encoding()"))

  def test___format___from_ipaddress_IPv4Address(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from ipaddress import IPv4Address\n"
                                  "IPv4Address().__format__()"))

  def test_subnet_of_from_ipaddress_IPv4Network(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from ipaddress import IPv4Network\n"
                                  "IPv4Network().subnet_of()"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)),
                      self.detect("from ipaddress import IPv4Network\n"
                                  "IPv4Network().subnet_of()"))

  def test_supernet_of_from_ipaddress_IPv4Network(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from ipaddress import IPv4Network\n"
                                  "IPv4Network().supernet_of()"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)),
                      self.detect("from ipaddress import IPv4Network\n"
                                  "IPv4Network().supernet_of()"))

  def test___format___from_ipaddress_IPv6Address(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from ipaddress import IPv6Address\n"
                                  "IPv6Address().__format__()"))

  def test_lazycache_from_linecache(self):
    self.assertOnlyIn((3, 5), self.detect("import linecache\nlinecache.lazycache()"))

  def test_currency_from_locale(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import locale\nlocale.currency()"))

  def test_delocalize_from_locale(self):
    self.assertOnlyIn((3, 5), self.detect("import locale\nlocale.delocalize()"))

  def test_localize_from_locale(self):
    self.assertOnlyIn((3, 10), self.detect("import locale\nlocale.localize()"))

  def test_format_string_from_locale(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import locale\nlocale.format_string()"))

  def test_getencoding_from_locale(self):
    self.assertOnlyIn((3, 11), self.detect("import locale\nlocale.getencoding()"))

  def test_getpreferredencoding_from_locale(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import locale\nlocale.getpreferredencoding()"))

  def test_getEffectiveLevel_from_logging_LoggerAdapter(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter().getEffectiveLevel()"))

  def test_hasHandlers_from_logging_LoggerAdapter(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter().hasHandlers()"))

  def test_isEnabledFor_from_logging_LoggerAdapter(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter().isEnabledFor()"))

  def test_setLevel_from_logging_LoggerAdapter(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter().setLevel()"))

  def test_setStream_from_logging_StreamHandler(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from logging import StreamHandler\n"
                                  "StreamHandler().setStream()"))

  def test_rotate_from_logging_handlers_BaseRotatingHandler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import BaseRotatingHandler\n"
                                  "BaseRotatingHandler().rotate()"))

  def test_rotation_filename_from_logging_handlers_BaseRotatingHandler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import BaseRotatingHandler\n"
                                  "BaseRotatingHandler().rotation_filename()"))

  def test_enqueue_sentinel_from_logging_handlers_QueueListener(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import QueueListener\n"
                                  "QueueListener().enqueue_sentinel()"))

  def test_reopenIfNeeded_from_logging_handlers_WatchedFileHandler(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from logging.handlers import WatchedFileHandler\n"
                                  "WatchedFileHandler().reopenIfNeeded()"))

  def test_get_bytes_from_mailbox_Mailbox(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from mailbox import Mailbox\n"
                                  "Mailbox().get_bytes()"))

  def test_factorial_from_math(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import math\nmath.factorial()"))

  def test_lcm_from_math(self):
    self.assertOnlyIn((3, 9), self.detect("import math\nmath.lcm()"))

  def test_nextafter_from_math(self):
    self.assertOnlyIn((3, 9), self.detect("import math\nmath.nextafter()"))

  def test_ulp_from_math(self):
    self.assertOnlyIn((3, 9), self.detect("import math\nmath.ulp()"))

  def test_read_windows_registry_from_mimetypes_MimeTypes(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from mimetypes import MimeTypes\n"
                                  "MimeTypes().read_windows_registry()"))

  def test_Close_from_msilib_Database(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from msilib import Database\n"
                                  "Database().Close()"))

  def test_getwch_from_msvcrt(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import msvcrt\nmsvcrt.getwch()"))

  def test_getwche_from_msvcrt(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import msvcrt\nmsvcrt.getwche()"))

  def test_putwch_from_msvcrt(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import msvcrt\nmsvcrt.putwch()"))

  def test_ungetwch_from_msvcrt(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import msvcrt\nmsvcrt.ungetwch()"))

  def test_wait_for_from_multiprocessing_Condition(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from multiprocessing import Condition\n"
                                  "Condition().wait_for()"))

  def test_close_from_multiprocessing_Process(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from multiprocessing import Process\n"
                                  "Process().close()"))

  def test_kill_from_multiprocessing_Process(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from multiprocessing import Process\n"
                                  "Process().kill()"))

  def test_Barrier_from_multiprocessing_managers_SyncManager(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from multiprocessing.managers import SyncManager\n"
                                  "SyncManager().Barrier()"))

  def test_wait_for_from_multiprocessing_managers_SyncManager_Condition(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from multiprocessing.managers.SyncManager import Condition\n"
                                  "Condition().wait_for()"))

  def test_parent_process_from_multiprocessing(self):
    self.assertOnlyIn((3, 8), self.detect(
        "import multiprocessing\nmultiprocessing.parent_process()"))

  def test_close_from_multiprocessing_SimpleQueue(self):
    self.assertOnlyIn((3, 9), self.detect(
      "from multiprocessing import SimpleQueue\n"
      "multiprocessing.SimpleQueue().close()"))

  def test_get_default_domain_from_nis(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import nis\nnis.get_default_domain()"))

  def test_description_from_nntplib_NNTP(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().description()"))

  def test_descriptions_from_nntplib_NNTP(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().descriptions()"))

  def test_getcapabilities_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().getcapabilities()"))

  def test_login_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().login()"))

  def test_over_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().over()"))

  def test_starttls_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().starttls()"))

  def test___eq___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__eq__()"))

  def test___floordiv___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__floordiv__()"))

  def test___ge___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__ge__()"))

  def test___gt___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__gt__()"))

  def test___iadd___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__iadd__()"))

  def test___iand___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__iand__()"))

  def test___iconcat___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__iconcat__()"))

  def test___idiv___from_operator(self):
    self.assertOnlyIn((2, 5), self.detect("import operator\noperator.__idiv__()"))

  def test___ifloordiv___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__ifloordiv__()"))

  def test___ilshift___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__ilshift__()"))

  def test___imatmul___from_operator(self):
    self.assertOnlyIn((3, 5), self.detect("import operator\noperator.__imatmul__()"))

  def test___imod___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__imod__()"))

  def test___imul___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__imul__()"))

  def test___index___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__index__()"))

  def test___ior___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__ior__()"))

  def test___ipow___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__ipow__()"))

  def test___irepeat___from_operator(self):
    self.assertOnlyIn((2, 5), self.detect("import operator\noperator.__irepeat__()"))

  def test___irshift___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__irshift__()"))

  def test___isub___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__isub__()"))

  def test___itruediv___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__itruediv__()"))

  def test___ixor___from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.__ixor__()"))

  def test___le___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__le__()"))

  def test___lt___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__lt__()"))

  def test___matmul___from_operator(self):
    self.assertOnlyIn((3, 5), self.detect("import operator\noperator.__matmul__()"))

  def test___ne___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__ne__()"))

  def test___pow___from_operator(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import operator\noperator.__pow__()"))

  def test___repeat___from_operator(self):
    self.assertOnlyIn((2, 0), self.detect("import operator\noperator.__repeat__()"))

  def test___truediv___from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.__truediv__()"))

  def test_attrgetter_from_operator(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import operator\noperator.attrgetter()"))

  def test_eq_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.eq()"))

  def test_floordiv_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.floordiv()"))

  def test_ge_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.ge()"))

  def test_gt_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.gt()"))

  def test_iadd_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.iadd()"))

  def test_iand_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.iand()"))

  def test_iconcat_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.iconcat()"))

  def test_idiv_from_operator(self):
    self.assertOnlyIn((2, 5), self.detect("import operator\noperator.idiv()"))

  def test_ifloordiv_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.ifloordiv()"))

  def test_ilshift_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.ilshift()"))

  def test_imatmul_from_operator(self):
    self.assertOnlyIn((3, 5), self.detect("import operator\noperator.imatmul()"))

  def test_imod_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.imod()"))

  def test_imul_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.imul()"))

  def test_index_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.index()"))

  def test_ior_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.ior()"))

  def test_ipow_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.ipow()"))

  def test_irepeat_from_operator(self):
    self.assertOnlyIn((2, 5), self.detect("import operator\noperator.irepeat()"))

  def test_irshift_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.irshift()"))

  def test_is__from_operator(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import operator\noperator.is_()"))

  def test_is_not_from_operator(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import operator\noperator.is_not()"))

  def test_isub_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.isub()"))

  def test_itemgetter_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.itemgetter()"))

  def test_itruediv_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.itruediv()"))

  def test_ixor_from_operator(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import operator\noperator.ixor()"))

  def test_le_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.le()"))

  def test_length_hint_from_operator(self):
    self.assertOnlyIn((3, 4), self.detect("import operator\noperator.length_hint()"))

  def test_lt_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.lt()"))

  def test_matmul_from_operator(self):
    self.assertOnlyIn((3, 5), self.detect("import operator\noperator.matmul()"))

  def test_methodcaller_from_operator(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import operator\noperator.methodcaller()"))

  def test_ne_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.ne()"))

  def test_pow_from_operator(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import operator\noperator.pow()"))

  def test_repeat_from_operator(self):
    self.assertOnlyIn((2, 0), self.detect("import operator\noperator.repeat()"))

  def test_truediv_from_operator(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import operator\noperator.truediv()"))

  def test_WCOREDUMP_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.WCOREDUMP()"))

  def test_WIFCONTINUED_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.WIFCONTINUED()"))

  def test_chflags_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.chflags()"))

  def test_chroot_from_os(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import os\nos.chroot()"))

  def test_closerange_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.closerange()"))

  def test_cpu_count_from_os(self):
    self.assertOnlyIn((3, 4), self.detect("import os\nos.cpu_count()"))

  def test_fchdir_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.fchdir()"))

  def test_fchmod_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.fchmod()"))

  def test_fchown_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.fchown()"))

  def test_fwalk_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.fwalk()"))

  def test_getcwdu_from_os(self):
    self.assertOnlyIn((2, 3), self.detect("import os\nos.getcwdu()"))

  def test_getloadavg_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.getloadavg()"))

  def test_getrandom_from_os(self):
    self.assertOnlyIn((3, 6), self.detect("import os\nos.getrandom()"))

  def test_lchflags_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.lchflags()"))

  def test_lchmod_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import os\nos.lchmod()"))

  def test_lchown_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.lchown()"))

  def test_major_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.major()"))

  def test_makedev_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.makedev()"))

  def test_minor_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.minor()"))

  def test_mknod_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.mknod()"))

  def test_popen2_from_os(self):
    self.assertOnlyIn((2, 0), self.detect("import os\nos.popen2()"))

  def test_popen3_from_os(self):
    self.assertOnlyIn((2, 0), self.detect("import os\nos.popen3()"))

  def test_popen4_from_os(self):
    self.assertOnlyIn((2, 0), self.detect("import os\nos.popen4()"))

  def test_preadv_from_os(self):
    self.assertOnlyIn((3, 7), self.detect("import os\nos.preadv()"))

  def test_pwritev_from_os(self):
    self.assertOnlyIn((3, 7), self.detect("import os\nos.pwritev()"))

  def test_replace_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.replace()"))
    self.assertEqual([(0, 0), (0, 0)], self.detect("""import os
s = "some string"
s.replace()
"""))

  def test_scandir_from_os(self):
    self.assertOnlyIn((3, 5), self.detect("import os\nos.scandir()"))

  def test_close_from_os_scandir(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from os import scandir\n"
                                  "scandir().close()"))

  def test_sched_get_priority_max_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_get_priority_max()"))

  def test_sched_get_priority_min_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_get_priority_min()"))

  def test_sched_getaffinity_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_getaffinity()"))

  def test_sched_getparam_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_getparam()"))

  def test_sched_getscheduler_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_getscheduler()"))

  def test_sched_rr_get_interval_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_rr_get_interval()"))

  def test_sched_setaffinity_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_setaffinity()"))

  def test_sched_setparam_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_setparam()"))

  def test_sched_setscheduler_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_setscheduler()"))

  def test_sched_yield_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sched_yield()"))

  def test_sync_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.sync()"))

  def test_truncate_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.truncate()"))

  def test_urandom_from_os(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import os\nos.urandom()"))

  def test_wait3_from_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import os\nos.wait3()"))

  def test_wait4_from_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import os\nos.wait4()"))

  def test_waitid_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nos.waitid()"))

  def test_walk_from_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import os\nos.walk()"))

  def test_pidfd_open_from_os(self):
    self.assertOnlyIn((3, 9), self.detect("import os\nos.pidfd_open()"))

  def test_waitstatus_to_exitcode_from_os(self):
    self.assertOnlyIn((3, 9), self.detect("import os\nos.waitstatus_to_exitcode()"))

  def test_win32_edition_from_platform(self):
    self.assertOnlyIn((3, 8), self.detect("import platform\nplatform.win32_edition()"))

  def test_win32_is_iot_from_platform(self):
    self.assertOnlyIn((3, 8), self.detect("import platform\nplatform.win32_is_iot()"))

  def test_freedesktop_os_release_from_platform(self):
    self.assertOnlyIn((3, 10), self.detect("import platform\nplatform.freedesktop_os_release()"))

  def test_capa_from_poplib_POP3(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from poplib import POP3\n"
                                  "POP3().capa()"))

  def test_stls_from_poplib_POP3(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from poplib import POP3\n"
                                  "POP3().stls()"))

  def test_utf8_from_poplib_POP3(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from poplib import POP3\n"
                                  "POP3().utf8()"))

  def test_format_from_pprint_PrettyPrinter(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from pprint import PrettyPrinter\n"
                                  "PrettyPrinter().format()"))

  def test_pp_from_pprint(self):
    self.assertOnlyIn((3, 8), self.detect("import pprint\npprint.pp()"))

  def test_choices_from_random(self):
    self.assertOnlyIn((3, 6), self.detect("import random\nrandom.choices()"))

  def test_getrandbits_from_random(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import random\nrandom.getrandbits()"))

  def test_getstate_from_random(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import random\nrandom.getstate()"))

  def test_jumpahead_from_random(self):
    self.assertOnlyIn((2, 1), self.detect("import random\nrandom.jumpahead()"))

  def test_sample_from_random(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import random\nrandom.sample()"))

  def test_setstate_from_random(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("import random\nrandom.setstate()"))

  def test_triangular_from_random(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import random\nrandom.triangular()"))

  def test_randbytes_from_random(self):
    self.assertOnlyIn((3, 9), self.detect("import random\nrandom.randbytes()"))

  def test_fullmatch_from_re_Pattern(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from re import Pattern\n"
                                  "Pattern().fullmatch()"))

  def test_finditer_from_re(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import re\nre.finditer()"))

  def test_fullmatch_from_re(self):
    self.assertOnlyIn((3, 4), self.detect("import re\nre.fullmatch()"))

  def test_append_history_file_from_readline(self):
    self.assertOnlyIn((3, 5), self.detect("import readline\nreadline.append_history_file()"))

  def test_clear_history_from_readline(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import readline\nreadline.clear_history()"))

  def test_get_completer_from_readline(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import readline\nreadline.get_completer()"))

  def test_get_completion_type_from_readline(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import readline\nreadline.get_completion_type()"))

  def test_get_current_history_length_from_readline(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect(
        "import readline\nreadline.get_current_history_length()"))

  def test_get_history_item_from_readline(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import readline\nreadline.get_history_item()"))

  def test_remove_history_item_from_readline(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import readline\nreadline.remove_history_item()"))

  def test_replace_history_item_from_readline(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import readline\nreadline.replace_history_item()"))

  def test_set_auto_history_from_readline(self):
    self.assertOnlyIn((3, 6), self.detect("import readline\nreadline.set_auto_history()"))

  def test_set_completion_display_matches_hook_from_readline(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import readline\nreadline.set_completion_display_matches_hook()"))

  def test_set_pre_input_hook_from_readline(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect(
        "import readline\nreadline.set_pre_input_hook()"))

  def test_set_startup_hook_from_readline(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import readline\nreadline.set_startup_hook()"))

  def test_prlimit_from_resource(self):
    self.assertOnlyIn((3, 4), self.detect("import resource\nresource.prlimit()"))

  def test_devpoll_from_select(self):
    self.assertOnlyIn((3, 3), self.detect("import select\nselect.devpoll()"))

  def test_close_from_select_devpoll(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from select import devpoll\n"
                                  "devpoll().close()"))

  def test_fileno_from_select_devpoll(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from select import devpoll\n"
                                  "devpoll().fileno()"))

  def test_epoll_from_select(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import select\nselect.epoll()"))

  def test_kevent_from_select(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import select\nselect.kevent()"))

  def test_kqueue_from_select(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import select\nselect.kqueue()"))

  def test_modify_from_select_poll(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from select import poll\n"
                                  "poll().modify()"))

  def test_convert_charref_from_sgmllib_SGMLParser(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from sgmllib import SGMLParser\n"
                                  "SGMLParser().convert_charref()"))

  def test_convert_codepoint_from_sgmllib_SGMLParser(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from sgmllib import SGMLParser\n"
                                  "SGMLParser().convert_codepoint()"))

  def test_convert_entityref_from_sgmllib_SGMLParser(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from sgmllib import SGMLParser\n"
                                  "SGMLParser().convert_entityref()"))

  def test_chown_from_shutil(self):
    self.assertOnlyIn((3, 3), self.detect("import shutil\nshutil.chown()"))

  def test_disk_usage_from_shutil(self):
    self.assertOnlyIn((3, 3), self.detect("import shutil\nshutil.disk_usage()"))

  def test_get_archive_formats_from_shutil(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import shutil\nshutil.get_archive_formats()"))

  def test_get_terminal_size_from_shutil(self):
    self.assertOnlyIn((3, 3), self.detect("import shutil\nshutil.get_terminal_size()"))

  def test_get_unpack_formats_from_shutil(self):
    self.assertOnlyIn((3, 2), self.detect("import shutil\nshutil.get_unpack_formats()"))

  def test_ignore_patterns_from_shutil(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import shutil\nshutil.ignore_patterns()"))

  def test_make_archive_from_shutil(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import shutil\nshutil.make_archive()"))

  def test_move_from_shutil(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import shutil\nshutil.move()"))

  def test_register_archive_format_from_shutil(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
        "import shutil\nshutil.register_archive_format()"))

  def test_register_unpack_format_from_shutil(self):
    self.assertOnlyIn((3, 2), self.detect("import shutil\nshutil.register_unpack_format()"))

  def test_unpack_archive_from_shutil(self):
    self.assertOnlyIn((3, 2), self.detect("import shutil\nshutil.unpack_archive()"))

  def test_unregister_archive_format_from_shutil(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
        "import shutil\nshutil.unregister_archive_format()"))

  def test_unregister_unpack_format_from_shutil(self):
    self.assertOnlyIn((3, 2), self.detect("import shutil\nshutil.unregister_unpack_format()"))

  def test_which_from_shutil(self):
    self.assertOnlyIn((3, 3), self.detect("import shutil\nshutil.which()"))

  def test_getitimer_from_signal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import signal\nsignal.getitimer()"))

  def test_pthread_kill_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.pthread_kill()"))

  def test_pthread_sigmask_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.pthread_sigmask()"))

  def test_raise_signal_from_signal(self):
    self.assertOnlyIn((3, 8), self.detect("import signal\nsignal.raise_signal()"))

  def test_set_wakeup_fd_from_signal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import signal\nsignal.set_wakeup_fd()"))

  def test_setitimer_from_signal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import signal\nsignal.setitimer()"))

  def test_siginterrupt_from_signal(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import signal\nsignal.siginterrupt()"))

  def test_sigpending_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.sigpending()"))

  def test_sigtimedwait_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.sigtimedwait()"))

  def test_sigwait_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.sigwait()"))

  def test_sigwaitinfo_from_signal(self):
    self.assertOnlyIn((3, 3), self.detect("import signal\nsignal.sigwaitinfo()"))

  def test_strsignal_from_signal(self):
    self.assertOnlyIn((3, 8), self.detect("import signal\nsignal.strsignal()"))

  def test_valid_signals_from_signal(self):
    self.assertOnlyIn((3, 8), self.detect("import signal\nsignal.valid_signals()"))

  def test_pidfd_send_signal_from_signal(self):
    self.assertOnlyIn((3, 9), self.detect("import signal\nsignal.pidfd_send_signal()"))

  def test_getsitepackages_from_site(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import site\nsite.getsitepackages()"))

  def test_getuserbase_from_site(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import site\nsite.getuserbase()"))

  def test_getusersitepackages_from_site(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import site\nsite.getusersitepackages()"))

  def test_starttls_from_smtplib_SMTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from smtplib import SMTP\n"
                                  "SMTP().starttls()"))

  def test_create_connection_from_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import socket\nsocket.create_connection()"))

  def test_getaddrinfo_from_socket(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import socket\nsocket.getaddrinfo()"))

  def test_getdefaulttimeout_from_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import socket\nsocket.getdefaulttimeout()"))

  def test_getnameinfo_from_socket(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import socket\nsocket.getnameinfo()"))

  def test_inet_ntop_from_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import socket\nsocket.inet_ntop()"))

  def test_inet_pton_from_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import socket\nsocket.inet_pton()"))

  def test_setdefaulttimeout_from_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import socket\nsocket.setdefaulttimeout()"))

  def test_gettimeout_from_socket_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().gettimeout()"))

  def test_ioctl_from_socket_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().ioctl()"))

  def test_recv_into_from_socket_socket(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().recv_into()"))

  def test_recvfrom_into_from_socket_socket(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().recvfrom_into()"))

  def test_settimeout_from_socket_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().settimeout()"))

  def test_socketpair_from_socket(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import socket\nsocket.socketpair()"))

  def test_service_actions_from_socketserver_BaseServer(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from socketserver import BaseServer\n"
                                  "BaseServer().service_actions()"))

  def test_backup_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().backup()"))

  def test_blobopen_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().blobopen()"))

  def test_create_window_function_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().create_window_function()"))

  def test_deserialize_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().deserialize()"))

  def test_compression_from_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().compression()"))

  def test_get_channel_binding_from_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().get_channel_binding()"))

  def test_selected_alpn_protocol_from_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 5)),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().selected_alpn_protocol()"))

  def test_selected_npn_protocol_from_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 3)),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().selected_npn_protocol()"))

  def test_sendfile_from_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().sendfile()"))

  def test_shared_ciphers_from_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().shared_ciphers()"))

  def test_version_from_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 5)),
                      self.detect("from ssl import SSLSocket\n"
                                  "SSLSocket().version()"))

  def test_get_identifiers_from_string_Template(self):
    self.assertOnlyIn((3, 11), self.detect("""
from string import Template
Template().get_identifiers()
"""))

  def test_is_valid_from_string_Template(self):
    self.assertOnlyIn((3, 11), self.detect("""
from string import Template
Template().is_valid()
"""))

  def test_rsplit_from_string(self):
    self.assertOnlyIn((2, 4), self.detect("import string\nstring.rsplit()"))

  def test_iter_unpack_from_struct_Struct(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from struct import Struct\n"
                                  "Struct().iter_unpack()"))

  def test_iter_unpack_from_struct(self):
    self.assertOnlyIn((3, 4), self.detect("import struct\nstruct.iter_unpack()"))

  def test_pack_into_from_struct(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import struct\nstruct.pack_into()"))

  def test_unpack_from_from_struct(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import struct\nstruct.unpack_from()"))

  def test_is_annotated_from_symtable_Symbol(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from symtable import Symbol\n"
                                  "Symbol().is_annotated()"))

  def test__clear_type_cache_from_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import sys\nsys._clear_type_cache()"))

  def test__current_frames_from_sys(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import sys\nsys._current_frames()"))

  def test__debugmallocstats_from_sys(self):
    self.assertOnlyIn((3, 3), self.detect("import sys\nsys._debugmallocstats()"))

  def test__enablelegacywindowsfsencoding_from_sys(self):
    self.assertOnlyIn((3, 6), self.detect("import sys\nsys._enablelegacywindowsfsencoding()"))

  def test_breakpointhook_from_sys(self):
    self.assertOnlyIn((3, 7), self.detect("import sys\nsys.breakpointhook()"))

  def test_get_asyncgen_hooks_from_sys(self):
    self.assertOnlyIn((3, 6), self.detect("import sys\nsys.get_asyncgen_hooks()"))

  def test_get_coroutine_origin_tracking_depth_from_sys(self):
    self.assertOnlyIn((3, 7), self.detect("import sys\nsys.get_coroutine_origin_tracking_depth()"))

  def test_getallocatedblocks_from_sys(self):
    self.assertOnlyIn((3, 4), self.detect("import sys\nsys.getallocatedblocks()"))

  def test_getandroidapilevel_from_sys(self):
    self.assertOnlyIn((3, 7), self.detect("import sys\nsys.getandroidapilevel()"))

  def test_getfilesystemencodeerrors_from_sys(self):
    self.assertOnlyIn((3, 6), self.detect("import sys\nsys.getfilesystemencodeerrors()"))

  def test_getswitchinterval_from_sys(self):
    self.assertOnlyIn((3, 2), self.detect("import sys\nsys.getswitchinterval()"))

  def test_is_finalizing_from_sys(self):
    self.assertOnlyIn((3, 5), self.detect("import sys\nsys.is_finalizing()"))

  def test_set_asyncgen_hooks_from_sys(self):
    self.assertOnlyIn((3, 6), self.detect("import sys\nsys.set_asyncgen_hooks()"))

  def test_set_coroutine_origin_tracking_depth_from_sys(self):
    self.assertOnlyIn((3, 7), self.detect("import sys\nsys.set_coroutine_origin_tracking_depth()"))

  def test_setdefaultencoding_from_sys(self):
    self.assertOnlyIn((2, 0), self.detect("import sys\nsys.setdefaultencoding()"))

  def test_setdlopenflags_from_sys(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import sys\nsys.setdlopenflags()"))

  def test_setswitchinterval_from_sys(self):
    self.assertOnlyIn((3, 2), self.detect("import sys\nsys.setswitchinterval()"))

  def test_settscdump_from_sys(self):
    self.assertOnlyIn((2, 4), self.detect("import sys\nsys.settscdump()"))

  def test_read_sb_data_from_telnetlib_Telnet(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from telnetlib import Telnet\n"
                                  "Telnet().read_sb_data()"))

  def test_NamedTemporaryFile_from_tempfile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect(
        "import tempfile\ntempfile.NamedTemporaryFile()"))

  def test_SpooledTemporaryFile_from_tempfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "import tempfile\ntempfile.SpooledTemporaryFile()"))

  def test_TemporaryDirectory_from_tempfile(self):
    self.assertOnlyIn((3, 2), self.detect("import tempfile\ntempfile.TemporaryDirectory()"))

  def test_gettempdir_from_tempfile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import tempfile\ntempfile.gettempdir()"))

  def test_gettempdirb_from_tempfile(self):
    self.assertOnlyIn((3, 5), self.detect("import tempfile\ntempfile.gettempdirb()"))

  def test_gettempprefixb_from_tempfile(self):
    self.assertOnlyIn((3, 5), self.detect("import tempfile\ntempfile.gettempprefixb()"))

  def test_mkdtemp_from_tempfile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import tempfile\ntempfile.mkdtemp()"))

  def test_mkstemp_from_tempfile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import tempfile\ntempfile.mkstemp()"))

  def test_tcgetwinsize_from_termios(self):
    self.assertOnlyIn((3, 11), self.detect("import termios\ntermios.tcgetwinsize()"))

  def test_tcsetwinsize_from_termios(self):
    self.assertOnlyIn((3, 11), self.detect("import termios\ntermios.tcsetwinsize()"))

  def test_interrupt_main_from_thread(self):
    self.assertOnlyIn((2, 3), self.detect("import thread\nthread.interrupt_main()"))

  def test_stack_size_from_thread(self):
    self.assertOnlyIn((2, 5), self.detect("import thread\nthread.stack_size()"))

  def test_notify_all_from_threading_Condition(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Condition\n"
                                  "Condition().notify_all()"))

  def test_wait_for_from_threading_Condition(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from threading import Condition\n"
                                  "Condition().wait_for()"))

  def test_is_set_from_threading_Event(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Event\n"
                                  "Event().is_set()"))

  def test_is_alive_from_threading_Thread(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Thread\n"
                                  "Thread().is_alive()"))

  def test_active_count_from_threading(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import threading\nthreading.active_count()"))

  def test_current_thread_from_threading(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import threading\nthreading.current_thread()"))

  def test_setprofile_from_threading(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import threading\nthreading.setprofile()"))

  def test_getprofile_from_threading(self):
    self.assertOnlyIn((3, 10), self.detect("import threading\nthreading.getprofile()"))

  def test_gettrace_from_threading(self):
    self.assertOnlyIn((3, 10), self.detect("import threading\nthreading.gettrace()"))

  def test_settrace_from_threading(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import threading\nthreading.settrace()"))

  def test_stack_size_from_threading(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import threading\nthreading.stack_size()"))

  def test_tzset_from_time(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import time\ntime.tzset()"))

  def test_autorange_from_timeit_Timer(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from timeit import Timer\n"
                                  "Timer().autorange()"))

  def test_format_frame_summary_from_traceback_StackSummary(self):
    self.assertOnlyIn((3, 11), self.detect("""
from traceback import StackSummary
StackSummary().format_frame_summary()
"""))

  def test_clear_frames_from_traceback(self):
    self.assertOnlyIn((3, 4), self.detect("import traceback\ntraceback.clear_frames()"))

  def test_format_exc_from_traceback(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("import traceback\ntraceback.format_exc()"))

  def test_walk_stack_from_traceback(self):
    self.assertOnlyIn((3, 5), self.detect("import traceback\ntraceback.walk_stack()"))

  def test_walk_tb_from_traceback(self):
    self.assertOnlyIn((3, 5), self.detect("import traceback\ntraceback.walk_tb()"))

  def test_replace_from_types_CodeType(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from types import CodeType\n"
                                  "CodeType().replace()"))

  def test_DynamicClassAttribute_from_types(self):
    self.assertOnlyIn((3, 4), self.detect("import types\ntypes.DynamicClassAttribute()"))

  def test_clear_from_types_FrameType(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from types import FrameType\n"
                                  "FrameType().clear()"))

  def test_coroutine_from_types(self):
    self.assertOnlyIn((3, 5), self.detect("import types\ntypes.coroutine()"))

  def test_new_class_from_types(self):
    self.assertOnlyIn((3, 3), self.detect("import types\ntypes.new_class()"))

  def test_prepare_class_from_types(self):
    self.assertOnlyIn((3, 3), self.detect("import types\ntypes.prepare_class()"))

  def test_resolve_bases_from_types(self):
    self.assertOnlyIn((3, 7), self.detect("import types\ntypes.resolve_bases()"))

  def test_east_asian_width_from_unicodedata(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
        "import unicodedata\nunicodedata.east_asian_width()"))

  def test_normalize_from_unicodedata(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import unicodedata\nunicodedata.normalize()"))

  def test_addClassCleanup_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().addClassCleanup()"))

  def test_assertCountEqual_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertCountEqual()"))

  def test_assertLogs_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertLogs()"))

  def test_assertNoLogs_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertNoLogs()"))

  def test_assertRaisesRegex_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertRaisesRegex()"))

  def test_assertWarns_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertWarns()"))

  def test_assertWarnsRegex_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().assertWarnsRegex()"))

  def test_doClassCleanups_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().doClassCleanups()"))

  def test_setUpClass_from_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().setUpClass()"))

  def test_skipTest_from_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().skipTest()"))

  def test_subTest_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().subTest()"))

  def test_tearDownClass_from_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().tearDownClass()"))

  def test_addSubTest_from_unittest_TestResult(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from unittest import TestResult\n"
                                  "TestResult().addSubTest()"))

  def test_installHandler_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import unittest\nunittest.installHandler()"))

  def test_assert_called_from_unittest_mock_Mock(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from unittest.mock import Mock\n"
                                  "Mock().assert_called()"))

  def test_assert_called_once_from_unittest_mock_Mock(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from unittest.mock import Mock\n"
                                  "Mock().assert_called_once()"))

  def test_assert_not_called_from_unittest_mock_Mock(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest.mock import Mock\n"
                                  "Mock().assert_not_called()"))

  def test_registerResult_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import unittest\nunittest.registerResult()"))

  def test_removeHandler_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import unittest\nunittest.removeHandler()"))

  def test_removeResult_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import unittest\nunittest.removeResult()"))

  def test_http_error_308_from_urllib_request_HTTPRedirectHandler(self):
    self.assertOnlyIn((3, 11),
                      self.detect("from urllib.request import HTTPRedirectHandler\n"
                                  "HTTPRedirectHandler().http_error_308()"))

  def test_remove_header_from_urllib_request_Request(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from urllib.request import Request\n"
                                  "Request().remove_header()"))

  def test_crawl_delay_from_urllib_robotparser_RobotFileParser(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from urllib.robotparser import RobotFileParser\n"
                                  "RobotFileParser().crawl_delay()"))

  def test_request_rate_from_urllib_robotparser_RobotFileParser(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from urllib.robotparser import RobotFileParser\n"
                                  "RobotFileParser().request_rate()"))

  def test_site_maps_from_urllib_robotparser_RobotFileParser(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from urllib.robotparser import RobotFileParser\n"
                                  "RobotFileParser().site_maps()"))

  def test_getcode_from_urllib_urlopen(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from urllib import urlopen\n"
                                  "urlopen().getcode()"))

  def test_add_unredirected_header_from_urllib2_Request(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from urllib2 import Request\n"
                                  "Request().add_unredirected_header()"))

  def test_has_header_from_urllib2_Request(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from urllib2 import Request\n"
                                  "Request().has_header()"))

  def test_geturl_from_urlparse_ParseResult(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import ParseResult\n"
                                  "ParseResult().geturl()"))

  def test_parse_qs_from_urlparse(self):
    self.assertOnlyIn((2, 6), self.detect("import urlparse\nurlparse.parse_qs()"))

  def test_parse_qsl_from_urlparse(self):
    self.assertOnlyIn((2, 6), self.detect("import urlparse\nurlparse.parse_qsl()"))

  def test_urlsplit_from_urlparse(self):
    self.assertOnlyIn((2, 2), self.detect("import urlparse\nurlparse.urlsplit()"))

  def test_urlunsplit_from_urlparse(self):
    self.assertOnlyIn((2, 2), self.detect("import urlparse\nurlparse.urlunsplit()"))

  def test_create_from_venv(self):
    self.assertOnlyIn((3, 3), self.detect("import venv\nvenv.create()"))

  def test_open_new_tab_from_webbrowser_controller(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from webbrowser import controller\n"
                                  "controller().open_new_tab()"))

  def test_open_new_tab_from_webbrowser(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import webbrowser\nwebbrowser.open_new_tab()"))

  def test_CreateKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2), self.detect("import winreg\nwinreg.CreateKeyEx()"))

  def test_DeleteKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2), self.detect("import winreg\nwinreg.DeleteKeyEx()"))

  def test_MessageBeep_from_winsound(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import winsound\nwinsound.MessageBeep()"))

  def test_normalize_from_xml_dom_Node(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.dom import Node\n"
                                  "Node().normalize()"))

  def test_toprettyxml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "Node().toprettyxml()"))

  def test_pi_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree.ElementTree import TreeBuilder\n"
                                  "TreeBuilder().pi()"))

  def test_EntityDeclHandler_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().EntityDeclHandler()"))

  def test_GetInputContext_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().GetInputContext()"))

  def test_UseForeignDTD_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().UseForeignDTD()"))

  def test_XmlDeclHandler_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().XmlDeclHandler()"))

  def test_copy_from_zlib_Compress(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from zlib import Compress\n"
                                  "Compress().copy()"))

  def test_copy_from_zlib_Decompress(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from zlib import Decompress\n"
                                  "Decompress().copy()"))

  def test_unparse_from_ast(self):
    self.assertOnlyIn((3, 9), self.detect("import ast\nast.unparse()"))

  def test_reset_peak_from_tracemalloc(self):
    self.assertOnlyIn((3, 9), self.detect("import tracemalloc\ntracemalloc.reset_peak()"))

  def test_upgrade_dependencies_from_venv_EnvBuilder(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from venv import EnvBuilder\n"
                                  "EnvBuilder().upgrade_dependencies()"))

  def test_issoftkeyword_from_keyword(self):
    self.assertOnlyIn((3, 9), self.detect("from keyword import issoftkeyword"))

  def test_print_warning_from_test_support(self):
    self.assertOnlyIn((3, 9), self.detect("from test.support import print_warning"))

  def test_wait_process_from_test_support(self):
    self.assertOnlyIn((3, 9), self.detect("from test.support import wait_process"))

  def test_skip_if_broken_multiprocessing_synchronize_from_test_support(self):
    self.assertOnlyIn((3, 10), self.detect("""
from test.support import skip_if_broken_multiprocessing_synchronize
"""))

  def test_check_disallow_instantiation_from_test_support(self):
    self.assertOnlyIn((3, 10), self.detect("""
from test.support import check_disallow_instantiation
"""))

  def test_zscore_from_statistics_NormalDist(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from statistics import NormalDist\nNormalDist().zscore()"))

  def test_send_fds_from_socket(self):
    self.assertOnlyIn((3, 9), self.detect("from socket import send_fds"))

  def test_recv_fds_from_socket(self):
    self.assertOnlyIn((3, 9), self.detect("from socket import recv_fds"))

  def test_create_module_from_importlib_machinery_FrozenImporter(self):
    self.assertOnlyIn((3, 4),
                      self.detect("import importlib.machinery.FrozenImporter\n"
                                  "importlib.machinery.FrozenImporter.create_module()"))

  def test_exec_module_from_importlib_machinery_FrozenImporter(self):
    self.assertOnlyIn((3, 4),
                      self.detect("import importlib.machinery.FrozenImporter\n"
                                  "importlib.machinery.FrozenImporter.exec_module()"))

  def test_get_stats_profile_from_pstats_Stats(self):
    self.assertOnlyIn((3, 9), self.detect("import pstats.Stats\npstats.Stats.get_stats_profile()"))

  def test__get_preferred_schemes_from_sysconfig(self):
    self.assertOnlyIn((3, 10), self.detect("from sysconfig import _get_preferred_schemes"))

  def test_get_preferred_scheme_from_sysconfig(self):
    self.assertOnlyIn((3, 10), self.detect("from sysconfig import get_preferred_scheme"))

  def test_get_default_scheme_from_sysconfig(self):
    self.assertOnlyIn((3, 10), self.detect("from sysconfig import get_default_scheme"))

  def test_packages_distributions_from_importlib_metadata(self):
    self.assertOnlyIn((3, 10), self.detect("from importlib.metadata import packages_distributions"))
