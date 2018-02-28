from testutils import MinpyTest, detect

class MinpyFunctionMemberTests(MinpyTest):
  def test_exc_clear_of_sys(self):
    self.assertOnlyIn(2.3, detect("from sys import exc_clear"))

  def test_used_in_context_of_star_import(self):
    self.assertOnlyIn(2.3, detect("from sys import *\nvar=exc_clear"))
    self.assertOnlyIn(2.3, detect("from sys import *\nprint(exc_clear)"))

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
    self.assertOnlyIn((2.6, 3.0), detect("from os.path import realpath"))

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
