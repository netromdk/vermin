from testutils import MinpyTest, detect

class MinpyFunctionMemberTests(MinpyTest):
  def test_exc_clear_of_sys(self):
    self.assertOnlyIn(2.3, detect("import sys.exc_clear"))

  def test_used_in_context_of_star_import(self):
    self.assertOnlyIn(2.3, detect("from sys import *\nvar=exc_clear"))
    self.assertOnlyIn(2.3, detect("from sys import *\nprint(exc_clear)"))

  def test_getcheckinterval_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("import sys.getcheckinterval"))

  def test_getdefaultencoding_of_sys(self):
    self.assertOnlyIn((2.0, 3.0), detect("import sys.getdefaultencoding"))

  def test_getdlopenflags_of_sys(self):
    self.assertOnlyIn((2.2, 3.0), detect("import sys.getdlopenflags"))

  def test_getfilesystemencoding_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("import sys.getfilesystemencoding"))

  def test_getsizeof_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("import sys.getsizeof"))

  def test_getprofile_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("import sys.getprofile"))

  def test_gettrace_of_sys(self):
    self.assertOnlyIn((2.6, 3.0), detect("import sys.gettrace"))

  def test_getwindowsversion_of_sys(self):
    self.assertOnlyIn((2.3, 3.0), detect("import sys.getwindowsversion"))

  def test_commonpath_of_os_path(self):
    self.assertOnlyIn(3.5, detect("import os.path.commonpath"))

  def test_getctime_of_os_path(self):
    self.assertOnlyIn((2.3, 3.0), detect("import os.path.getctime"))

  def test_ismount_of_os_path(self):
    self.assertOnlyIn(3.4, detect("import os.path.ismount"))

  def test_lexists_of_os_path(self):
    self.assertOnlyIn((2.4, 3.0), detect("import os.path.lexists"))

  def test_realpath_of_os_path(self):
    self.assertOnlyIn((2.6, 3.0), detect("import os.path.realpath"))

  def test_getpgid_of_os(self):
    self.assertOnlyIn((2.3, 3.0), detect("import os.getpgid"))

  def test_getresgid_of_os(self):
    self.assertOnlyIn((2.7, 3.0), detect("import os.getresgid"))

  def test_getresuid_of_os(self):
    self.assertOnlyIn((2.7, 3.0), detect("import os.getresuid"))

  def test_getsid_of_os(self):
    self.assertOnlyIn((2.4, 3.0), detect("import os.getsid"))

  def test_initgroups_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("import os.initgroups"))

  def test_setgroups_of_os(self):
    self.assertOnlyIn((2.2, 3.0), detect("import os.setgroups"))

  def test_setresgid_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("import os.setresgid"))

  def test_setresuid_of_os(self):
    self.assertOnlyIn((2.7, 3.2), detect("import os.setresuid"))

  def test_fsencode_of_os(self):
    self.assertOnlyIn(3.2, detect("import os.fsencode"))

  def test_fsdecode_of_os(self):
    self.assertOnlyIn(3.2, detect("import os.fsdecode"))

  def test_fspath_of_os(self):
    self.assertOnlyIn(3.6, detect("import os.fspath"))

  def test_getenvb_of_os(self):
    self.assertOnlyIn(3.2, detect("import os.getenvb"))

  def test_get_exec_path_of_os(self):
    self.assertOnlyIn(3.2, detect("import os.get_exec_path"))

  def test_getgrouplist_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.getgrouplist"))

  def test_getpriority_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.getpriority"))

  def test_setpriority_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.setpriority"))

  def test_get_blocking_of_os(self):
    self.assertOnlyIn(3.5, detect("import os.get_blocking"))

  def test_set_blocking_of_os(self):
    self.assertOnlyIn(3.5, detect("import os.set_blocking"))

  def test_lockf_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.lockf"))

  def test_pipe2_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.pipe2"))

  def test_posix_fallocate_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.posix_fallocate"))

  def test_posix_fadvise_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.posix_fadvise"))

  def test_pread_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.pread"))

  def test_pwrite_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.pwrite"))

  def test_sendfile_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.sendfile"))

  def test_readv_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.readv"))

  def test_writev_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.writev"))

  def test_get_terminal_size_of_os(self):
    self.assertOnlyIn(3.3, detect("import os.get_terminal_size"))

  def test_get_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("import os.get_inheritable"))

  def test_set_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("import os.set_inheritable"))

  def test_get_handle_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("import os.get_handle_inheritable"))

  def test_set_handle_inheritable_of_os(self):
    self.assertOnlyIn(3.4, detect("import os.set_handle_inheritable"))
