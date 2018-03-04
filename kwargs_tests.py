from testutils import MinpyTest, detect

class MinpyKwargsTests(MinpyTest):
  def test_inheritable_of_dup2_from_os(self):
    self.assertOnlyIn(3.4, detect("import os\nv = os.dup2(inheritable=True)"))
    self.assertOnlyIn(3.4, detect("from os import dup2\nv = dup2(inheritable=True)"))

  def test_dir_fd_of_open_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.open(dir_fd=None)"))

  def test_dir_fd_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(dir_fd=None)"))

  def test_effective_ids_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(effective_ids=None)"))

  def test_follow_symlinks_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(follow_symlinks=None)"))

  def test_follow_symlinks_of_chflags_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chflags(follow_symlinks=None)"))

  def test_dir_fd_of_chmod_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chmod(dir_fd=None)"))

  def test_follow_symlinks_of_chmod_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chmod(follow_symlinks=None)"))

  def test_dir_fd_of_chown_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chown(dir_fd=None)"))

  def test_follow_symlinks_of_chown_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chown(follow_symlinks=None)"))

  def test_src_dir_fd_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(src_dir_fd=None)"))

  def test_dst_dir_fd_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(dst_dir_fd=None)"))

  def test_follow_symlinks_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(follow_symlinks=None)"))

  def test_maxtasksperchild_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn(3.2, detect("import multiprocessing\nPool(maxtasksperchild=3)"))

  def test_context_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("import multiprocessing\nPool(context=None)"))

  def test_daemon_of_Process_from_multiprocessing(self):
    self.assertOnlyIn(3.3, detect("import multiprocessing\nProcess(daemon=None)"))

  def test_compact_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.PrettyPrinter(compact=True)"))

  def test_compact_of_pformat_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.pformat(compact=True)"))

  def test_compact_of_pprint_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.pprint(compact=True)"))

  def test_delta_of_assertAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestCase\nTestCase.assertAlmostEqual(delta=1)"))

  def test_delta_of_assertNotAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestCase\n"
                             "TestCase.assertNotAlmostEqual(delta=1)"))

  def test_fold_of_datetime_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime(fold=1)"))

  def test_tzinfo_of_combine_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.combine(tzinfo=1)"))

  def test_fold_of_replace_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.isoformat(timespec=1)"))
