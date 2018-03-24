from .testutils import VerminTest, detect

class VerminFunctionMemberTests(VerminTest):
  def test_exc_clear_of_sys(self):
    self.assertOnlyIn(2.3, detect("from sys import exc_clear"))

  def test_getcheckinterval_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("from sys import getcheckinterval"))

  def test_getdefaultencoding_of_sys(self):
    self.assertOnlyIn((2.0, 3.0), detect("from sys import getdefaultencoding"))

  def test_getdlopenflags_of_sys(self):
    self.assertOnlyIn((2.2, 3.0), detect("from sys import getdlopenflags"))

  def test_getfilesystemencoding_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("from sys import getfilesystemencoding"))

  def test_getsizeof_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("from sys import getsizeof"))

  def test_getprofile_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("from sys import getprofile"))

  def test_gettrace_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("from sys import gettrace"))

  def test_getwindowsversion_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("from sys import getwindowsversion"))

  def test_commonpath_of_os_path(self):
    self.assertOnlyIn(3.5, detect("from os.path import commonpath"))

  def test_getctime_of_os_path(self):
    self.assertOnlyIn((2.3, 3.0), detect("from os.path import getctime"))

  def test_ismount_of_os_path(self):
    self.assertOnlyIn(3.4, detect("from os.path import ismount"))

  def test_lexists_of_os_path(self):
    self.assertOnlyIn((2.4, 3.0), detect("from os.path import lexists"))

  def test_realpath_of_os_path(self):
    self.assertOnlyIn((2.2, 3.0), detect("from os.path import realpath"))

  def test_relpath_of_os_path(self):
    self.assertOnlyIn((2.6, 3.0), detect("from os.path import relpath"))

  def test_getpgid_of_os(self):
    self.assertOnlyIn((2.3, 3.0), detect("from os import getpgid"))

  def test_getresgid_of_os(self):
    self.assertOnlyIn((2.7, 3.0), detect("from os import getresgid"))

  def test_getresuid_of_os(self):
    self.assertOnlyIn((2.7, 3.0), detect("from os import getresuid"))

  def test_getsid_of_os(self):
    self.assertOnlyIn((2.4, 3.0), detect("from os import getsid"))

  def test_initgroups_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("from os import initgroups"))

  def test_setgroups_of_os(self):
    self.assertOnlyIn((2.2, 3.0), detect("from os import setgroups"))

  def test_setresgid_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("from os import setresgid"))

  def test_setresuid_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("from os import setresuid"))

  def test_fsencode_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import fsencode"))

  def test_fsdecode_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import fsdecode"))

  def test_fspath_of_os(self):
    self.assertOnlyIn(3.6, detect("from os import fspath"))

  def test_getenvb_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import getenvb"))

  def test_get_exec_path_of_os(self):
    self.assertOnlyIn(3.2, detect("from os import get_exec_path"))

  def test_getgrouplist_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import getgrouplist"))

  def test_getpriority_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import getpriority"))

  def test_setpriority_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import setpriority"))

  def test_get_blocking_of_os(self):
    self.assertOnlyIn(3.5, detect("from os import get_blocking"))

  def test_set_blocking_of_os(self):
    self.assertOnlyIn(3.5, detect("from os import set_blocking"))

  def test_lockf_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import lockf"))

  def test_pipe2_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import pipe2"))

  def test_posix_fallocate_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import posix_fallocate"))

  def test_posix_fadvise_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import posix_fadvise"))

  def test_pread_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import pread"))

  def test_pwrite_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import pwrite"))

  def test_sendfile_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import sendfile"))

  def test_readv_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import readv"))

  def test_writev_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import writev"))

  def test_get_terminal_size_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import get_terminal_size"))

  def test_get_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import get_inheritable"))

  def test_set_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import set_inheritable"))

  def test_get_handle_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import get_handle_inheritable"))

  def test_set_handle_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("from os import set_handle_inheritable"))

  def test_starmap_of_multiprocessing_Pool(self):
    self.assertOnlyIn(3.3, detect("from multiprocessing import Pool\np = Pool()\np.starmap()"))

  def test_starmap_async_of_multiprocessing_Pool(self):
    self.assertOnlyIn(3.3,
                      detect("from multiprocessing import Pool\np = Pool()\np.starmap_async()"))

  def test_wait_of_multiprocessing_connection(self):
    self.assertOnlyIn(3.3, detect("from multiprocessing import connection\nconnection.wait()"))

  def test_get_all_start_methods_of_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("from multiprocessing import get_all_start_methods"))

  def test_get_start_method_of_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("from multiprocessing import get_start_method"))

  def test_set_start_method_of_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("from multiprocessing import set_start_method"))

  def test_get_context_of_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("from multiprocessing import get_context"))

  def test_assertIs_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1), detect("from unittest import TestCase\nTestCase.assertIs()"))

  def test_assertIsNot_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1), detect("from unittest import TestCase\nTestCase.assertIsNot()"))

  def test_assertIsNone_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1), detect("from unittest import TestCase\nTestCase.assertIsNone()"))

  def test_assertIsNotNone_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertIsNotNone()"))

  def test_assertIn_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1), detect("from unittest import TestCase\nTestCase.assertIn()"))

  def test_assertNotIn_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1), detect("from unittest import TestCase\nTestCase.assertNotIn()"))

  def test_assertIsInstance_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from unittest import TestCase\nTestCase.assertIsInstance()"))

  def test_assertNotIsInstance_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from unittest import TestCase\nTestCase.assertNotIsInstance()"))

  def test_assertRaisesRegexp_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertRaisesRegexp()"))

  def test_assertGreater_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertGreater()"))

  def test_assertGreaterEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertGreaterEqual()"))

  def test_assertLess_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertLess()"))

  def test_assertLessEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertLessEqual()"))

  def test_assertRegexpMatches_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertRegexpMatches()"))

  def test_assertNotRegexpMatches_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertNotRegexpMatches()"))

  def test_assertItemsEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertItemsEqual()"))

  def test_assertDictContainsSubset_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertDictContainsSubset()"))

  def test_addTypeEqualityFunc_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.addTypeEqualityFunc()"))

  def test_assertMultilineEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertMultilineEqual()"))

  def test_assertSequenceEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertSequenceEqual()"))

  def test_assertListEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertListEqual()"))

  def test_assertTupleEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertTupleEqual()"))

  def test_assertRegex_of_unittest_TestCase(self):
    self.assertOnlyIn(3.1, detect("from unittest import TestCase\nTestCase.assertRegex()"))

  def test_assertNotRegex_of_unittest_TestCase(self):
    self.assertOnlyIn(3.1, detect("from unittest import TestCase\nTestCase.assertNotRegex()"))

  def test_assertSetEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertSetEqual()"))

  def test_assertDictEqual_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.assertDictEqual()"))

  def test_longMessage_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.longMessage()"))

  def test_maxDiff_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from unittest import TestCase\nTestCase.maxDiff()"))

  def test_addCleanup_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.addCleanup()"))

  def test_doCleanups_of_unittest_TestCase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestCase\nTestCase.doCleanups()"))

  def test_discover_of_unittest_TestLoader(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from unittest import TestLoader\nTestLoader.discover()"))

  def test_startTestRun_of_unittest_TestResult(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestResult\nTestResult.startTestRun()"))

  def test_stopTestRun_of_unittest_TestResult(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from unittest import TestResult\nTestResult.stopTestRun()"))

  def test_total_seconds_of_datetime_timedelta(self):
    self.assertOnlyIn(3.2, detect("from datetime import timedelta\ntimedelta.total_seconds()"))

  def test_timestamp_of_datetime_datetime(self):
    self.assertOnlyIn(3.3, detect("from datetime import datetime\ndatetime.timestamp()"))

  def test_NewType_of_typing(self):
    self.assertOnlyIn(3.5, detect("import typing\ntyping.NewType()"))

  def test_pbkdf2_hmac_of_hashlib(self):
    self.assertOnlyIn((2.7, 3.4), detect("import hashlib\nhashlib.pbkdf2_hmac()"))

  def test_scrypt_of_hashlib(self):
    self.assertOnlyIn(3.6, detect("import hashlib\nhashlib.scrypt()"))

  def test_open_of_bz2(self):
    self.assertOnlyIn(3.3, detect("import bz2\nbz2.open()"))

  def test_peek_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.peek()"))

  def test_fileno_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.fileno()"))

  def test_readable_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.readable()"))

  def test_seekable_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.seekable()"))

  def test_writable_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.writable()"))
    self.assertOnlyIn(3.3, detect("import bz2\nf = bz2.BZ2File()\nf.writable()"))
    self.assertOnlyIn(3.3, detect("import bz2\nf = bz2.BZ2File\nf.writable"))

  def test_read1_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.read1()"))

  def test_readinto_of_bz2_BZ2File(self):
    self.assertOnlyIn(3.3, detect("from bz2 import BZ2File\nf = BZ2File()\nf.readinto()"))

  def test_count_of_collections_deque(self):
    self.assertOnlyIn((2.7, 3.2), detect("from collections import deque\nd = deque()\nd.count()"))

  def test_remove_of_collections_deque(self):
    self.assertOnlyIn((2.5, 3.0), detect("from collections import deque\nd = deque()\nd.remove()"))

  def test_reverse_of_collections_deque(self):
    self.assertOnlyIn((2.7, 3.2), detect("from collections import deque\nd = deque()\nd.reverse()"))

  def test_copy_of_collections_deque(self):
    self.assertOnlyIn(3.5, detect("from collections import deque\nd = deque()\nd.copy()"))

  def test_index_of_collections_deque(self):
    self.assertOnlyIn(3.5, detect("from collections import deque\nd = deque()\nd.index()"))

  def test_insert_of_collections_deque(self):
    self.assertOnlyIn(3.5, detect("from collections import deque\nd = deque()\nd.insert()"))

  def test_move_to_end_of_collections_OrderedDict(self):
    self.assertOnlyIn(3.2,
                      detect("from collections import OrderedDict\n"
                             "d = OrderedDict()\n"
                             "d.move_to_end()"))

  def test_suppress_of_contextlib(self):
    self.assertOnlyIn(3.4, detect("import contextlib\ncontextlib.suppress()"))

  def test_redirect_stdout_of_contextlib(self):
    self.assertOnlyIn(3.4, detect("import contextlib\ncontextlib.redirect_stdout()"))

  def test_redirect_stderr_of_contextlib(self):
    self.assertOnlyIn(3.5, detect("import contextlib\ncontextlib.redirect_stderr()"))

  def test_field_size_limit_of_csv(self):
    self.assertOnlyIn((2.5, 3.0), detect("import csv\ncsv.field_size_limit()"))

  def test_find_msvcrt_of_ctypes_util(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes.util\nctypes.util.find_msvcrt()"))

  def test_get_errno_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.get_errno()"))

  def test_get_last_error_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.get_last_error()"))

  def test_set_errno_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.set_errno()"))

  def test_set_last_error_of_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.set_last_error()"))

  def test_from_buffer_of_ctypes__CData(self):
    self.assertOnlyIn((2.6, 3.0), detect("from ctypes import _CData\n_CData.from_buffer()"))

  def test_from_buffer_copy_of_ctypes__CData(self):
    self.assertOnlyIn((2.6, 3.0), detect("from ctypes import _CData\n_CData.from_buffer_copy()"))

  def test_canonical_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.canonical()"))

  def test_compare_signal_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.compare_signal()"))

  def test_compare_total_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.compare_total()"))

  def test_compare_total_mag_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from decimal import Decimal\nDecimal.compare_total_mag()"))

  def test_conjugate_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.conjugate()"))

  def test_copy_abs_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.copy_abs()"))

  def test_copy_negate_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.copy_negate()"))

  def test_copy_sign_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.copy_sign()"))

  def test_exp_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.exp()"))

  def test_from_float_of_decimal_Decimal(self):
    self.assertOnlyIn((2.7, 3.1), detect("from decimal import Decimal\nDecimal.from_float()"))

  def test_fma_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.fma()"))

  def test_is_canonical_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_canonical()"))

  def test_is_finite_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_finite()"))

  def test_is_infinite_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_infinite()"))

  def test_is_nan_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_nan()"))

  def test_is_normal_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_normal()"))

  def test_is_qnan_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_qnan()"))

  def test_is_signed_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_signed()"))

  def test_is_snan_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_snan()"))

  def test_is_subnormal_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_subnormal()"))

  def test_is_zero_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.is_zero()"))

  def test_ln_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.ln()"))

  def test_log10_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.log10()"))

  def test_logb_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.logb()"))

  def test_logical_and_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.logical_and()"))

  def test_logical_invert_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.logical_invert()"))

  def test_logical_or_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.logical_or()"))

  def test_logical_xor_of_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.logical_xor()"))

  def test_max_mag_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.max_mag()"))

  def test_min_mag_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.min_mag()"))

  def test_next_minus_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.next_minus()"))

  def test_next_plus_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.next_plus()"))

  def test_next_toward_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.next_toward()"))

  def test_number_class_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.number_class()"))

  def test_radix_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.radix()"))

  def test_rotate_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.rotate()"))

  def test_scaleb_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.scaleb()"))

  def test_shift_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0), detect("from decimal import Decimal\nDecimal.shift()"))

  def test_to_integral_exact_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from decimal import Decimal\nDecimal.to_integral_exact()"))

  def test_to_integral_value_decimal_Decimal(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from decimal import Decimal\nDecimal.to_integral_value()"))

  def test_as_integer_ratio_decimal_Decimal(self):
    self.assertOnlyIn(3.6, detect("from decimal import Decimal\nDecimal.as_integer_ratio()"))

  def test_localcontext_decimal(self):
    self.assertOnlyIn((2.5, 3.0), detect("import decimal\ndecimal.localcontext()"))

  def test_create_decimal_from_float_decimal_Context(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from decimal import Context\nContext.create_decimal_from_float()"))

  def test_clear_traps_decimal_Context(self):
    self.assertOnlyIn(3.3, detect("from decimal import Context\nContext.clear_traps()"))

  def test_context_diff_difflib(self):
    self.assertOnlyIn((2.3, 3.0), detect("import difflib\ndifflib.context_diff()"))

  def test_unified_diff_difflib(self):
    self.assertOnlyIn((2.3, 3.0), detect("import difflib\ndifflib.unified_diff()"))

  def test_diff_bytes_difflib(self):
    self.assertOnlyIn(3.5, detect("import difflib\ndifflib.diff_bytes()"))

  def test_get_grouped_opcodes_difflib_SequenceMatcher(self):
    self.assertOnlyIn((2.3, 3.0),
                      detect("from difflib import SequenceMatcher\n"
                             "SequenceMatcher.get_grouped_opcodes()"))

  def test_cmp_to_key_from_functools(self):
    self.assertOnlyIn((2.7, 3.2), detect("import functools\nfunctools.cmp_to_key()"))

  def test_total_ordering_from_functools(self):
    self.assertOnlyIn((2.7, 3.2), detect("import functools\nfunctools.total_ordering()"))

  def test_reduce_from_functools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import functools\nfunctools.reduce()"))

  def test_lru_cache_from_functools(self):
    self.assertOnlyIn(3.2, detect("import functools\nfunctools.lru_cache()"))

  def test_partial_method_from_functools(self):
    self.assertOnlyIn(3.4, detect("import functools\nfunctools.partial_method()"))

  def test_heappushpop_from_heapq(self):
    self.assertOnlyIn((2.6, 3.0), detect("import heapq\nheapq.heappushpop()"))

  def test_merge_from_heapq(self):
    self.assertOnlyIn((2.6, 3.0), detect("import heapq\nheapq.merge()"))

  def test_nlargest_from_heapq(self):
    self.assertOnlyIn((2.4, 3.0), detect("import heapq\nheapq.nlargest()"))

  def test_nsmallest_from_heapq(self):
    self.assertOnlyIn((2.4, 3.0), detect("import heapq\nheapq.nsmallest()"))

  def test_compare_digest_from_hmac(self):
    self.assertOnlyIn((2.7, 3.3), detect("import hmac\nhmac.compare_digest()"))

  def test_isgenerator_from_inspect(self):
    self.assertOnlyIn((2.6, 3.0), detect("import inspect\ninspect.isgenerator()"))

  def test_isgeneratorfunction_from_inspect(self):
    self.assertOnlyIn((2.6, 3.0), detect("import inspect\ninspect.isgeneratorfunction()"))

  def test_isabstract_from_inspect(self):
    self.assertOnlyIn((2.6, 3.0), detect("import inspect\ninspect.isabstract()"))

  def test_isdatadescriptor_from_inspect(self):
    self.assertOnlyIn((2.3, 3.0), detect("import inspect\ninspect.isdatadescriptor()"))

  def test_isgetsetdescriptor_from_inspect(self):
    self.assertOnlyIn((2.5, 3.0), detect("import inspect\ninspect.isgetsetdescriptor()"))

  def test_ismemberdescriptor_from_inspect(self):
    self.assertOnlyIn((2.5, 3.0), detect("import inspect\ninspect.ismemberdescriptor()"))

  def test_cleandoc_from_inspect(self):
    self.assertOnlyIn((2.6, 3.0), detect("import inspect\ninspect.cleandoc()"))

  def test_getcallargs_from_inspect(self):
    self.assertOnlyIn((2.7, 3.2), detect("import inspect\ninspect.getcallargs()"))

  def test_iscoroutine_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.iscoroutine()"))

  def test_iscoroutinefunction_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.iscoroutinefunction()"))

  def test_isawaitable_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.isawaitable()"))

  def test_isasyncgen_from_inspect(self):
    self.assertOnlyIn(3.6, detect("import inspect\ninspect.isasyncgen()"))

  def test_isasyncgenfunction_from_inspect(self):
    self.assertOnlyIn(3.6, detect("import inspect\ninspect.isasyncgenfunction()"))

  def test_signature_from_inspect(self):
    self.assertOnlyIn(3.3, detect("import inspect\ninspect.signature()"))

  def test_apply_defaults_from_inspect_BoundArguments(self):
    self.assertOnlyIn(3.6, detect("from inspect import BoundArguments\n"
                                  "ba = BoundArguments()\n"
                                  "ba.apply_defaults()"))

  def test_getclosurevars_from_inspect(self):
    self.assertOnlyIn(3.3, detect("import inspect\ninspect.getclosurevars()"))

  def test_unwrap_from_inspect(self):
    self.assertOnlyIn(3.4, detect("import inspect\ninspect.unwrap()"))

  def test_getattr_static_from_inspect(self):
    self.assertOnlyIn(3.2, detect("import inspect\ninspect.getattr_static()"))

  def test_getgeneratorstate_from_inspect(self):
    self.assertOnlyIn(3.2, detect("import inspect\ninspect.getgeneratorstate()"))

  def test_getgeneratorlocals_from_inspect(self):
    self.assertOnlyIn(3.2, detect("import inspect\ninspect.getgeneratorlocals()"))

  def test_getcoroutinestate_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.getcoroutinestate()"))

  def test_getcoroutinelocals_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.getcoroutinelocals()"))

  def test_detach_from_io_BufferedIOBase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from io import BufferedIOBase\n"
                             "bb = BufferedIOBase()\n"
                             "bb.detach()"))

  def test_readinto1_from_io_BufferedIOBase(self):
    self.assertOnlyIn(3.5,
                      detect("from io import BufferedIOBase\n"
                             "bb = BufferedIOBase()\n"
                             "bb.readinto1()"))

  def test_readinto1_from_io_BytesIO(self):
    self.assertOnlyIn(3.5,
                      detect("from io import BytesIO\n"
                             "bb = BytesIO()\n"
                             "bb.readinto1()"))

  def test_getbuffer_from_io_BytesIO(self):
    self.assertOnlyIn(3.2,
                      detect("from io import BytesIO\n"
                             "bb = BytesIO()\n"
                             "bb.getbuffer()"))

  def test_detach_from_io_TextIOBase(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from io import TextIOBase\n"
                             "bb = TextIOBase()\n"
                             "bb.detach()"))

  def test_combinations_from_itertools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import itertools\nitertools.combinations()"))

  def test_combinations_with_replacement_from_itertools(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("import itertools\nitertools.combinations_with_replacement()"))

  def test_compress_from_itertools(self):
    self.assertOnlyIn((2.7, 3.1), detect("import itertools\nitertools.compress()"))

  def test_groupby_from_itertools(self):
    self.assertOnlyIn((2.4, 3.0), detect("import itertools\nitertools.groupby()"))

  def test_izip_longest_from_itertools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import itertools\nitertools.izip_longest()"))

  def test_permutations_from_itertools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import itertools\nitertools.permutations()"))

  def test_product_from_itertools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import itertools\nitertools.product()"))

  def test_tee_from_itertools(self):
    self.assertOnlyIn((2.4, 3.0), detect("import itertools\nitertools.tee()"))

  def test_accumulate_from_itertools(self):
    self.assertOnlyIn(3.2, detect("import itertools\nitertools.accumulate()"))

  def test_getChild_from_logging_Logger(self):
    self.assertOnlyIn((2.7, 3.2), detect("from logging import Logger\nLogger.getChild()"))

  def test_hasHandlers_from_logging_Logger(self):
    self.assertOnlyIn(3.2, detect("from logging import Logger\nLogger.hasHandlers()"))

  def test_getLogRecordFactory_from_logging(self):
    self.assertOnlyIn(3.2, detect("import logging\nlogging.getLogRecordFactory()"))

  def test_setLogRecordFactory_from_logging(self):
    self.assertOnlyIn(3.2, detect("import logging\nlogging.setLogRecordFactory()"))

  def test_optimize_from_pickletools(self):
    self.assertOnlyIn((2.6, 3.0), detect("import pickletools\npickletools.optimize()"))

  def test_get_data_from_pkgutil(self):
    self.assertOnlyIn((2.6, 3.0), detect("import pkgutil\npkgutil.get_data()"))

  def test_python_branch_from_platform(self):
    self.assertOnlyIn((2.6, 3.0), detect("import platform\nplatform.python_branch()"))

  def test_python_implementation_from_platform(self):
    self.assertOnlyIn((2.6, 3.0), detect("import platform\nplatform.python_implementation()"))

  def test_python_revision_from_platform(self):
    self.assertOnlyIn((2.6, 3.0), detect("import platform\nplatform.python_revision()"))

  def test_linux_distribution_from_platform(self):
    self.assertOnlyIn((2.6, 3.0), detect("import platform\nplatform.linux_distribution()"))

  def test_run_path_from_runpy(self):
    self.assertOnlyIn((2.7, 3.2), detect("import runpy\nrunpy.run_path()"))

  def test_split_from_shlex(self):
    self.assertOnlyIn((2.3, 3.0), detect("import shlex\nshlex.split()"))

  def test_push_source_from_shlex(self):
    self.assertOnlyIn((2.1, 3.0), detect("import shlex\nshlex.push_source()"))

  def test_pop_source_from_shlex(self):
    self.assertOnlyIn((2.1, 3.0), detect("import shlex\nshlex.pop_source()"))

  def test_quote_from_shlex(self):
    self.assertOnlyIn(3.3, detect("import shlex\nshlex.quote()"))

  def test_register_introspection_functions_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn(2.3,
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                             "srv = SimpleXMLRPCServer()\n"
                             "srv.register_introspection_functions()"))
    self.assertOnlyIn(3.0,
                      detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                             "srv = SimpleXMLRPCServer()\n"
                             "srv.register_introspection_functions()"))

  def test_set_progress_handler_from_sqlite3_Connection(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from sqlite3 import Connection\n"
                             "conn = Connection()\n"
                             "conn.set_progress_handler()"))

  def test_enable_load_extension_from_sqlite3_Connection(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from sqlite3 import Connection\n"
                             "conn = Connection()\n"
                             "conn.enable_load_extension()"))

  def test_load_extension_from_sqlite3_Connection(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from sqlite3 import Connection\n"
                             "conn = Connection()\n"
                             "conn.load_extension()"))

  def test_iter_dump_from_sqlite3_Connection(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from sqlite3 import Connection\n"
                             "conn = Connection()\n"
                             "conn.iter_dump()"))

  def test_set_trace_callback_from_sqlite3_Connection(self):
    self.assertOnlyIn(3.3,
                      detect("from sqlite3 import Connection\n"
                             "conn = Connection()\n"
                             "conn.set_trace_callback()"))

  def test_keys_from_sqlite3_Row(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from sqlite3 import Row\n"
                             "conn = Row()\n"
                             "conn.keys()"))

  def test_create_default_context_from_ssl(self):
    self.assertOnlyIn((2.7, 3.4), detect("import ssl\nssl.create_default_context()"))

  def test__https_verify_certificates_from_ssl(self):
    self.assertOnlyIn(2.7, detect("import ssl\nssl._https_verify_certificates()"))

  def test_RAND_bytes_from_ssl(self):
    self.assertOnlyIn(3.3, detect("import ssl\nssl.RAND_bytes()"))

  def test_RAND_pseudo_bytes_from_ssl(self):
    self.assertOnlyIn(3.3, detect("import ssl\nssl.RAND_pseudo_bytes()"))

  def test_match_hostname_from_ssl(self):
    self.assertOnlyIn((2.7, 3.2), detect("import ssl\nssl.match_hostname()"))

  def test_get_default_verify_paths_from_ssl(self):
    self.assertOnlyIn((2.7, 3.4), detect("import ssl\nssl.get_default_verify_paths()"))

  def test_enum_certificates_from_ssl(self):
    self.assertOnlyIn((2.7, 3.4), detect("import ssl\nssl.enum_certificates()"))

  def test_enum_crls_from_ssl(self):
    self.assertOnlyIn((2.7, 3.4), detect("import ssl\nssl.enum_crls()"))

  def test_compression_from_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("import ssl\nssl.compression()"))

  def test_shared_ciphers_from_ssl(self):
    self.assertOnlyIn(3.5, detect("import ssl\nssl.shared_ciphers()"))

  def test_get_channel_binding_from_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("import ssl\nssl.get_channel_binding()"))

  def test_selected_alpn_protocol_from_ssl(self):
    self.assertOnlyIn((2.7, 3.5), detect("import ssl\nssl.selected_alpn_protocol()"))

  def test_selected_npn_protocol_from_ssl(self):
    self.assertOnlyIn((2.7, 3.3), detect("import ssl\nssl.selected_npn_protocol()"))

  def test_version_from_ssl(self):
    self.assertOnlyIn((2.7, 3.5), detect("import ssl\nssl.version()"))

  def test_set_alpn_protocols_from_ssl_SSLContext(self):
    self.assertOnlyIn((2.7, 3.5),
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.set_alpn_protocols()"))

  def test_cert_store_stats_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.4,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.cert_store_stats()"))

  def test_load_default_certs_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.4,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.load_default_certs()"))

  def test_get_ca_certs_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.4,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.get_ca_certs()"))

  def test_get_ciphers_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.6,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.get_ciphers()"))

  def test_set_npn_protocols_from_ssl_SSLContext(self):
    self.assertOnlyIn((2.7, 3.3),
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.set_npn_protocols()"))

  def test_load_dh_params_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.3,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.load_dh_params()"))

  def test_set_ecdh_curve_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.3,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.set_ecdh_curve()"))

  def test_set_servername_callback_from_ssl_SSLContext(self):
    self.assertOnlyIn(3.4,
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.set_servername_callback()"))

  def test_check_call_from_subprocess(self):
    self.assertOnlyIn((2.5, 3.0), detect("import subprocess\nsubprocess.check_call()"))

  def test_check_output_from_subprocess(self):
    self.assertOnlyIn((2.7, 3.1), detect("import subprocess\nsubprocess.check_output()"))

  def test_send_signal_from_subprocess_Popen(self):
    self.assertOnlyIn((2.6, 3.0), detect("from subprocess import Popen\nPopen.send_signal()"))

  def test_terminate_from_subprocess_Popen(self):
    self.assertOnlyIn((2.6, 3.0), detect("from subprocess import Popen\nPopen.terminate()"))

  def test_kill_from_subprocess_Popen(self):
    self.assertOnlyIn((2.6, 3.0), detect("from subprocess import Popen\nPopen.kill()"))

  def test_run_from_subprocess(self):
    self.assertOnlyIn(3.5, detect("import subprocess\nsubprocess.run()"))

  def test_check_returncode_from_subprocess_CompletedProcess(self):
    self.assertOnlyIn(3.5, detect("from subprocess import CompletedProcess\n"
                                  "cp = CompletedProcess()\n"
                                  "cp.check_returncode()"))

  def test_extractall_from_tarfile_TarFile(self):
    self.assertOnlyIn((2.5, 3.0), detect("from tarfile import TarFile\nTarFile.extractall()"))

  def test_fromtarfile_from_tarfile_TarInfo(self):
    self.assertOnlyIn((2.6, 3.0), detect("from tarfile import TarInfo\nTarInfo.fromtarfile()"))

  def test_shorten_from_textwrap(self):
    self.assertOnlyIn(3.4, detect("import textwrap\ntextwrap.shorten()"))

  def test_indent_from_textwrap(self):
    self.assertOnlyIn(3.3, detect("import textwrap\ntextwrap.indent()"))

  def test_timeit_from_timeit(self):
    self.assertOnlyIn((2.6, 3.0), detect("import timeit\ntimeit.timeit()"))

  def test_repeat_from_timeit(self):
    self.assertOnlyIn((2.6, 3.0), detect("import timeit\ntimeit.repeat()"))

  def test_warnpy3k_from_warnings(self):
    self.assertOnlyIn((2.6, 3.0), detect("import warnings\nwarnings.warnpy3k()"))

  def test_iterkeyrefs_from_weakref_WeakKeyDictionary(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from weakref import WeakKeyDictionary\n"
                             "wkd = WeakKeyDictionary()\n"
                             "wkd.iterkeyrefs()"))

  def test_keyrefs_from_weakref_WeakKeyDictionary(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from weakref import WeakKeyDictionary\n"
                             "wkd = WeakKeyDictionary()\n"
                             "wkd.keyrefs()"))

  def test_itervaluerefs_from_weakref_WeakValueDictionary(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from weakref import WeakValueDictionary\n"
                             "wkd = WeakValueDictionary()\n"
                             "wkd.itervaluerefs()"))

  def test_valuerefs_from_weakref_WeakValueDictionary(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from weakref import WeakValueDictionary\n"
                             "wkd = WeakValueDictionary()\n"
                             "wkd.valuerefs()"))

  def test_read_environ_from_wsgiref_handlers(self):
    self.assertOnlyIn(3.2, detect("import wsgiref.handlers\nwsgiref.handlers.read_environ()"))

  def test_fromstringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree import ElementTree\n"
                             "tree = ElementTree()\n"
                             "tree.fromstringlist()"))

  def test_register_namespace_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree import ElementTree\n"
                             "tree = ElementTree()\n"
                             "tree.register_namespace()"))

  def test_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree import ElementTree\n"
                             "tree = ElementTree()\n"
                             "tree.tostringlist()"))

  def test_extend_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import Element\n"
                             "elm = Element()\n"
                             "elm.extend()"))

  def test_iter_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import Element\n"
                             "elm = Element()\n"
                             "elm.iter()"))

  def test_iterfind_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import Element\n"
                             "elm = Element()\n"
                             "elm.iterfind()"))

  def test_itertext_from_xml_etree_ElementTree_Element(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import Element\n"
                             "elm = Element()\n"
                             "elm.itertext()"))

  def test_iterfind_from_xml_etree_ElementTree_ElementTree(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import ElementTree\n"
                             "tree = ElementTree()\n"
                             "tree.iterfind()"))

  def test_doctype_from_xml_etree_ElementTree_TreeBuilder(self):
    self.assertOnlyIn((2.7, 3.2),
                      detect("from xml.etree.ElementTree import TreeBuilder\n"
                             "tree = TreeBuilder()\n"
                             "tree.doctype()"))

  def test_open_from_zipfile_ZipFile(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.open()"))

  def test_extract_from_zipfile_ZipFile(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.extract()"))

  def test_extractall_from_zipfile_ZipFile(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.extractall()"))

  def test_setpassword_from_zipfile_ZipFile(self):
    self.assertOnlyIn((2.6, 3.0),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.setpassword()"))

  def test_from_file_from_zipfile_ZipInfo(self):
    self.assertOnlyIn(3.6,
                      detect("from zipfile import ZipInfo\n"
                             "zf = ZipInfo()\n"
                             "zf.from_file()"))

  def test_is_dir_from_zipfile_ZipInfo(self):
    self.assertOnlyIn(3.6,
                      detect("from zipfile import ZipInfo\n"
                             "zf = ZipInfo()\n"
                             "zf.is_dir()"))

  def test_get_filename_from_zipimport_zipimporter(self):
    self.assertOnlyIn((2.7, 3.1),
                      detect("from zipimport import zipimporter\n"
                             "zi = zipimporter()\n"
                             "zi.get_filename()"))

  def test_Tcl_from_Tkinter(self):
    self.assertOnlyIn(2.4, detect("import Tkinter\nTkinter.Tcl()"))
