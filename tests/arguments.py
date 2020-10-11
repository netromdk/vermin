import os
from multiprocessing import cpu_count

from vermin import Arguments, Backports, Features

from .testutils import VerminTest, ScopedTemporaryFile

def parse_args(args):
  return Arguments(args).parse()

class VerminArgumentsTests(VerminTest):
  def test_not_enough_args(self):
    self.assertContainsDict({"code": 1, "usage": True, "full": False}, parse_args([]))

  def test_help(self):
    self.assertContainsDict({"code": 0, "usage": True, "full": True}, parse_args(["-h"]))
    self.assertContainsDict({"code": 0, "usage": True, "full": True}, parse_args(["--help"]))

  def test_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py", "file2.py", "folder/folder2"]},
                            parse_args(["file.py", "file2.py", "folder/folder2"]))

  def test_mix_options_and_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py"], "targets": [(True, (2, 7))],
                             "no-tips": False},
                            parse_args(["-q", "-t=2.7", "file.py"]))

  def test_quiet(self):
    self.assertFalse(self.config.quiet())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-q"]))
    self.assertTrue(self.config.quiet())
    self.config.set_quiet(False)
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["--quiet"]))
    self.assertTrue(self.config.quiet())

  def test_verbose(self):
    self.assertEqual(0, self.config.verbose())
    for n in range(1, 10):
      self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-" + n * "v"]))
      self.assertEqual(n, self.config.verbose())

  def test_cant_mix_quiet_and_verbose(self):
    self.assertContainsDict({"code": 1}, parse_args(["-q", "-v"]))

  def test_targets(self):
    # The boolean value means match target version exactly or not (equal or smaller).
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8))], "paths": []},
                            parse_args(["-t=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8))], "paths": []},
                            parse_args(["--target=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8))], "paths": []},
                            parse_args(["-t=2,8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8))], "paths": []},
                            parse_args(["--target=2,8"]))
    self.assertContainsDict({"code": 0, "targets": [(False, (2, 8))], "paths": []},
                            parse_args(["-t=2.8-"]))
    self.assertContainsDict({"code": 0, "targets": [(False, (2, 8))], "paths": []},
                            parse_args(["--target=2.8-"]))
    self.assertContainsDict({"code": 0, "targets": [(False, (2, 8))], "paths": []},
                            parse_args(["-t=2,8-"]))
    self.assertContainsDict({"code": 0, "targets": [(False, (2, 8))], "paths": []},
                            parse_args(["--target=2,8-"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["-t=3-", "-t=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["--target=3-", "--target=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["-t=3-", "--target=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["-t=3-", "-t=2,8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["--target=3-", "--target=2,8"]))
    self.assertContainsDict({"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []},
                            parse_args(["-t=3-", "--target=2,8"]))

    # Too many targets (>2).
    self.assertContainsDict({"code": 1},
                            parse_args(["-t=3.1", "-t=2.8", "-t=3"]))
    self.assertContainsDict({"code": 1},
                            parse_args(["--target=3.1", "--target=2.8", "--target=3"]))
    self.assertContainsDict({"code": 1},
                            parse_args(["--target=3.1", "-t=2.8", "--target=3"]))

    # Invalid values.
    self.assertContainsDict({"code": 1}, parse_args(["-t=a"]))            # NaN
    self.assertContainsDict({"code": 1}, parse_args(["--target=a"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=-1"]))           # < 2
    self.assertContainsDict({"code": 1}, parse_args(["--target=-1"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=1.8"]))          # < 2
    self.assertContainsDict({"code": 1}, parse_args(["--target=1.8"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=4"]))            # >= 4
    self.assertContainsDict({"code": 1}, parse_args(["--target=4"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=4,5"]))          # > 4
    self.assertContainsDict({"code": 1}, parse_args(["--target=4,5"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=2+"]))           # Only - allowed.
    self.assertContainsDict({"code": 1}, parse_args(["--target=2+"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=2,0.1"]))        # 3 values disallowed.
    self.assertContainsDict({"code": 1}, parse_args(["--target=2,0.1"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=2.0,1"]))        # 3 values disallowed.
    self.assertContainsDict({"code": 1}, parse_args(["--target=2.0,1"]))

  def test_ignore_incomp(self):
    self.assertFalse(self.config.ignore_incomp())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-i"]))
    self.assertTrue(self.config.ignore_incomp())
    self.config.set_ignore_incomp(False)
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["--ignore"]))
    self.assertTrue(self.config.ignore_incomp())

  def test_processes(self):
    # Default value is cpu_count().
    self.assertContainsDict({"code": 0, "processes": cpu_count(), "paths": []},
                            parse_args(["-q"]))

    # Valid values.
    self.assertContainsDict({"code": 0, "processes": 1, "paths": []},
                            parse_args(["-p=1"]))
    self.assertContainsDict({"code": 0, "processes": 1, "paths": []},
                            parse_args(["--processes=1"]))
    self.assertContainsDict({"code": 0, "processes": 9, "paths": []},
                            parse_args(["-p=9"]))
    self.assertContainsDict({"code": 0, "processes": 9, "paths": []},
                            parse_args(["--processes=9"]))

    # Invalid values.
    self.assertContainsDict({"code": 1}, parse_args(["-p=hello"]))
    self.assertContainsDict({"code": 1}, parse_args(["--processes=hello"]))
    self.assertContainsDict({"code": 1}, parse_args(["-p=-1"]))
    self.assertContainsDict({"code": 1}, parse_args(["--processes=-1"]))
    self.assertContainsDict({"code": 1}, parse_args(["-p=0"]))
    self.assertContainsDict({"code": 1}, parse_args(["--processes=0"]))

  def test_print_visits(self):
    self.assertFalse(self.config.print_visits())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-d"]))
    self.assertTrue(self.config.print_visits())

  def test_lax_mode(self):
    self.assertFalse(self.config.lax_mode())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-l"]))
    self.assertTrue(self.config.lax_mode())
    self.config.set_lax_mode(False)
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["--lax"]))
    self.assertTrue(self.config.lax_mode())

  def test_hidden(self):
    self.assertContainsDict({"hidden": True}, parse_args(["--hidden"]))

  def test_versions(self):
    self.assertContainsDict({"versions": True}, parse_args(["--versions"]))

  def test_exclude(self):
    self.assertContainsDict({"code": 1}, parse_args(["--exclude"]))  # Needs <file> part.
    self.assertEmpty(self.config.exclusions())

    self.assertContainsDict({"code": 0}, parse_args(["--exclude", "bbb", "--exclude", "aaa"]))
    self.assertEqual(["aaa", "bbb"], self.config.exclusions())  # Expect it sorted.
    self.assertFalse(self.config.is_excluded("iamnotthere"))
    self.assertTrue(self.config.is_excluded("aaa"))
    self.assertTrue(self.config.is_excluded("bbb"))

    self.config.reset()
    args = ["--exclude", "foo.bar(baz)",
            "--exclude", "ceh=surrogateescape",
            "--exclude", "ce=utf-8"]
    self.assertContainsDict({"code": 0}, parse_args(args))
    self.assertTrue(self.config.is_excluded_kwarg("foo.bar", "baz"))
    self.assertTrue(self.config.is_excluded_codecs_error_handler("surrogateescape"))
    self.assertTrue(self.config.is_excluded_codecs_encoding("utf-8"))

  def test_exclude_file(self):
    self.assertContainsDict({"code": 1}, parse_args(["--exclude-file"]))  # Needs <file> part.
    self.assertEmpty(self.config.exclusions())

    fp = ScopedTemporaryFile()
    fp.write(b"""bbb
aaa
""")
    fp.close()
    self.assertContainsDict({"code": 0}, parse_args(["--exclude-file", fp.path()]))
    self.assertEqual(["aaa", "bbb"], self.config.exclusions())  # Expect it sorted.

    # Nonexistent file is ignored.
    fn = "nonexistentfile"
    self.assertFalse(os.path.exists(fn))
    self.config.reset()
    self.assertContainsDict({"code": 0}, parse_args(["--exclude-file", fn]))
    self.assertEmpty(self.config.exclusions())

  def test_backport(self):
    # Needs <name> part.
    self.assertContainsDict({"code": 1}, parse_args(["--backport"]))
    self.assertEmpty(self.config.backports())

    # Unknown module.
    self.assertContainsDict({"code": 1}, parse_args(["--backport", "foobarbaz"]))
    self.assertEmpty(self.config.backports())

    # Known modules.
    for mod in Backports.modules():
      self.config.reset()
      self.assertContainsDict({"code": 0}, parse_args(["--backport", mod]))
      self.assertEqualItems([mod], self.config.backports())

  def test_no_tips(self):
    self.assertContainsDict({"no-tips": True}, parse_args(["--no-tips"]))

  def test_feature(self):
    # Needs <name> part.
    self.assertContainsDict({"code": 1}, parse_args(["--feature"]))
    self.assertEmpty(self.config.features())

    # Unknown feature.
    self.assertContainsDict({"code": 1}, parse_args(["--feature", "foobarbaz"]))
    self.assertEmpty(self.config.features())

    # Known features.
    for feature in Features.features():
      self.config.reset()
      self.assertContainsDict({"code": 0}, parse_args(["--feature", feature]))
      self.assertEqualItems([feature], self.config.features())
