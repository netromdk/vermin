import os
from multiprocessing import cpu_count

from vermin import Backports, Features
import vermin.formats

from .testutils import VerminTest, ScopedTemporaryFile

class VerminArgumentsTests(VerminTest):
  def test_not_enough_args(self):
    self.assertContainsDict({"code": 1, "usage": True, "full": False}, self.parse_args([]))

  def test_help(self):
    self.assertContainsDict({"code": 0, "usage": True, "full": True}, self.parse_args(["-h"]))
    self.assertContainsDict({"code": 0, "usage": True, "full": True}, self.parse_args(["--help"]))

  def test_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py", "file2.py", "folder/folder2"]},
                            self.parse_args(["file.py", "file2.py", "folder/folder2"]))

  def test_mix_options_and_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py"], "targets": [(True, (2, 7))],
                             "no-tips": False},
                            self.parse_args(["-q", "-t=2.7", "file.py"]))

  def test_quiet(self):
    self.assertFalse(self.config.quiet())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-q"]))
    self.assertTrue(self.config.quiet())
    self.config.set_quiet(False)
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["--quiet"]))
    self.assertTrue(self.config.quiet())

  def test_verbose(self):
    self.assertEqual(0, self.config.verbose())
    for n in range(1, 10):
      self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-" + n * "v"]))
      self.assertEqual(n, self.config.verbose())

  def test_cant_mix_quiet_and_verbose(self):
    self.assertContainsDict({"code": 1}, self.parse_args(["-q", "-v"]))

  @VerminTest.parameterized_args([
    # The boolean value means match target version exactly or not (equal or smaller).
    (["-t=2.8"],
     {"code": 0, "targets": [(True, (2, 8))], "paths": []}),
    (["--target=2.8"],
     {"code": 0, "targets": [(True, (2, 8))], "paths": []}),
    (["-t=2,8"],
     {"code": 0, "targets": [(True, (2, 8))], "paths": []}),
    (["--target=2,8"],
     {"code": 0, "targets": [(True, (2, 8))], "paths": []}),
    (["-t=2.8-"],
     {"code": 0, "targets": [(False, (2, 8))], "paths": []}),
    (["--target=2.8-"],
     {"code": 0, "targets": [(False, (2, 8))], "paths": []}),
    (["-t=2,8-"],
     {"code": 0, "targets": [(False, (2, 8))], "paths": []}),
    (["--target=2,8-"],
     {"code": 0, "targets": [(False, (2, 8))], "paths": []}),
    (["-t=3-", "-t=2.8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),
    (["--target=3-", "--target=2.8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),
    (["-t=3-", "--target=2.8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),
    (["-t=3-", "-t=2,8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),
    (["--target=3-", "--target=2,8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),
    (["-t=3-", "--target=2,8"],
     {"code": 0, "targets": [(True, (2, 8)), (False, (3, 0))], "paths": []}),

    # Too many targets (>2).
    (["-t=3.1", "-t=2.8", "-t=3"], {"code": 1}),
    (["--target=3.1", "--target=2.8", "--target=3"], {"code": 1}),
    (["--target=3.1", "-t=2.8", "--target=3"], {"code": 1}),

    # Invalid values.
    (["-t=a"], {"code": 1}),            # NaN
    (["--target=a"], {"code": 1}),
    (["-t=-1"], {"code": 1}),           # < 2
    (["--target=-1"], {"code": 1}),
    (["-t=1.8"], {"code": 1}),          # < 2
    (["--target=1.8"], {"code": 1}),
    (["-t=4"], {"code": 1}),            # >= 4
    (["--target=4"], {"code": 1}),
    (["-t=4,5"], {"code": 1}),          # > 4
    (["--target=4,5"], {"code": 1}),
    (["-t=2+"], {"code": 1}),           # Only - allowed.
    (["--target=2+"], {"code": 1}),
    (["-t=2,0.1"], {"code": 1}),        # 3 vals disallowed.
    (["--target=2,0.1"], {"code": 1}),
    (["-t=2.0,1"], {"code": 1}),        # 3 vals disallowed.
    (["--target=2.0,1"], {"code": 1}),
  ])
  def test_targets(self, args, parsed_args):
    self.assertParseArgs(args, parsed_args)

  def test_ignore_incomp(self):
    self.assertFalse(self.config.ignore_incomp())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-i"]))
    self.assertTrue(self.config.ignore_incomp())
    self.config.set_ignore_incomp(False)
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["--ignore"]))
    self.assertTrue(self.config.ignore_incomp())

  @VerminTest.parameterized_args([
    # Default value is cpu_count().
    (["-q"], {"code": 0, "processes": cpu_count(), "paths": []}),

    # Valid values.
    (["-p=1"], {"code": 0, "processes": 1, "paths": []}),
    (["--processes=1"], {"code": 0, "processes": 1, "paths": []}),
    (["-p=9"], {"code": 0, "processes": 9, "paths": []}),
    (["--processes=9"], {"code": 0, "processes": 9, "paths": []}),

    # Invalid values.
    (["-p=hello"], {"code": 1}),
    (["--processes=hello"], {"code": 1}),
    (["-p=-1"], {"code": 1}),
    (["--processes=-1"], {"code": 1}),
    (["-p=0"], {"code": 1}),
    (["--processes=0"], {"code": 1}),
  ])
  def test_processes(self, args, parsed_args):
    self.assertParseArgs(args, parsed_args)

  def test_print_visits(self):
    self.assertFalse(self.config.print_visits())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-d"]))
    self.assertTrue(self.config.print_visits())

  def test_lax_mode(self):
    self.assertFalse(self.config.lax_mode())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-l"]))
    self.assertTrue(self.config.lax_mode())
    self.config.set_lax_mode(False)
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["--lax"]))
    self.assertTrue(self.config.lax_mode())

  def test_hidden(self):
    self.assertContainsDict({"hidden": True}, self.parse_args(["--hidden"]))

  def test_versions(self):
    self.assertContainsDict({"versions": True}, self.parse_args(["--versions"]))

  def test_exclude(self):
    self.assertContainsDict({"code": 1}, self.parse_args(["--exclude"]))  # Needs <file> part.
    self.assertEmpty(self.config.exclusions())

    self.assertContainsDict({"code": 0}, self.parse_args(["--exclude", "bbb", "--exclude", "aaa"]))
    self.assertEqual(["aaa", "bbb"], self.config.exclusions())  # Expect it sorted.
    self.assertFalse(self.config.is_excluded("iamnotthere"))
    self.assertTrue(self.config.is_excluded("aaa"))
    self.assertTrue(self.config.is_excluded("bbb"))

    self.config.reset()
    args = ["--exclude", "foo.bar(baz)",
            "--exclude", "ceh=surrogateescape",
            "--exclude", "ce=utf-8"]
    self.assertContainsDict({"code": 0}, self.parse_args(args))
    self.assertTrue(self.config.is_excluded_kwarg("foo.bar", "baz"))
    self.assertTrue(self.config.is_excluded_codecs_error_handler("surrogateescape"))
    self.assertTrue(self.config.is_excluded_codecs_encoding("utf-8"))

  def test_exclude_file(self):
    self.assertContainsDict({"code": 1}, self.parse_args(["--exclude-file"]))  # Needs <file> part.
    self.assertEmpty(self.config.exclusions())

    fp = ScopedTemporaryFile()
    fp.write(b"""bbb
aaa
""")
    fp.close()
    self.assertContainsDict({"code": 0}, self.parse_args(["--exclude-file", fp.path()]))
    self.assertEqual(["aaa", "bbb"], self.config.exclusions())  # Expect it sorted.

    # Nonexistent file is ignored.
    fn = "nonexistentfile"
    self.assertFalse(os.path.exists(fn))
    self.config.reset()
    self.assertContainsDict({"code": 0}, self.parse_args(["--exclude-file", fn]))
    self.assertEmpty(self.config.exclusions())

  def test_backport(self):
    # Needs <name> part.
    self.assertContainsDict({"code": 1}, self.parse_args(["--backport"]))
    self.assertEmpty(self.config.backports())

    # Unknown module.
    self.assertContainsDict({"code": 1}, self.parse_args(["--backport", "foobarbaz"]))
    self.assertEmpty(self.config.backports())

    # Known modules.
    for mod in Backports.modules():
      self.config.reset()
      self.assertContainsDict({"code": 0}, self.parse_args(["--backport", mod]))
      self.assertEqualItems([mod], self.config.backports())

  def test_no_tips(self):
    self.assertContainsDict({"no-tips": True}, self.parse_args(["--no-tips"]))

  def test_feature(self):
    # Needs <name> part.
    self.assertContainsDict({"code": 1}, self.parse_args(["--feature"]))
    self.assertEmpty(self.config.features())

    # Unknown feature.
    self.assertContainsDict({"code": 1}, self.parse_args(["--feature", "foobarbaz"]))
    self.assertEmpty(self.config.features())

    # Known features.
    for feature in Features.features():
      self.config.reset()
      self.assertContainsDict({"code": 0}, self.parse_args(["--feature", feature]))
      self.assertEqualItems([feature], self.config.features())

  def test_format(self):
    self.assertEqual("default", self.config.format().name())

    # Needs <name> part.
    self.assertContainsDict({"code": 1}, self.parse_args(["--format"]))
    self.assertEqual("default", self.config.format().name())

    # Unknown format.
    self.assertContainsDict({"code": 1}, self.parse_args(["--format", "foobarbaz"]))
    self.assertEqual("default", self.config.format().name())

    # Known formats.
    for fmt in vermin.formats.names():
      self.config.reset()
      self.assertContainsDict({"code": 0}, self.parse_args(["--format", fmt]))
      self.assertEqual(fmt, self.config.format().name())

    # Parsable verbose level 3, no tips, ignore incompatible versions, no `--versions`.
    for args in (["--format", "parsable"], ["--format", "parsable", "--verbose"],
                 ["--format", "parsable", "--versions"]):
      self.config.reset()
      self.assertContainsDict({"code": 0, "versions": False, "no-tips": True},
                              self.parse_args(args))
      self.assertEqual(3, self.config.verbose())
      self.assertTrue(self.config.ignore_incomp())

    # Verbosity can be higher for parsable.
    self.config.reset()
    self.assertContainsDict({"code": 0, "versions": False, "no-tips": True},
                            self.parse_args(["--format", "parsable", "-vvvv"]))
    self.assertEqual(4, self.config.verbose())
    self.assertTrue(self.config.ignore_incomp())
