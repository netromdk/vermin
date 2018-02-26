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
