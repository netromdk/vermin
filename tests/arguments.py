import os

from vermin import Backports, Features, DEFAULT_PROCESSES
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
    self.assertContainsDict({"code": 0, "paths": ["file.py"]},
                            self.parse_args(["-q", "-t=2.7", "file.py"]))
    self.assertTrue(self.config.show_tips())
    self.assertEqual([(True, (2, 7))], self.config.targets())

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
     {"code": 0, "paths": []}, [(True, (2, 8))]),
    (["--target=2.8"],
     {"code": 0, "paths": []}, [(True, (2, 8))]),
    (["-t=2,8"],
     {"code": 0, "paths": []}, [(True, (2, 8))]),
    (["--target=2,8"],
     {"code": 0, "paths": []}, [(True, (2, 8))]),
    (["-t=2.8-"],
     {"code": 0, "paths": []}, [(False, (2, 8))]),
    (["--target=2.8-"],
     {"code": 0, "paths": []}, [(False, (2, 8))]),
    (["-t=2,8-"],
     {"code": 0, "paths": []}, [(False, (2, 8))]),
    (["--target=2,8-"],
     {"code": 0, "paths": []}, [(False, (2, 8))]),
    (["-t=3-", "-t=2.8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),
    (["--target=3-", "--target=2.8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),
    (["-t=3-", "--target=2.8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),
    (["-t=3-", "-t=2,8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),
    (["--target=3-", "--target=2,8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),
    (["-t=3-", "--target=2,8"],
     {"code": 0, "paths": []}, [(True, (2, 8)), (False, (3, 0))]),

    # Too many targets (>2). It still adds up to two targets.
    (["-t=3.1", "-t=2.8", "-t=3"], {"code": 1}, [(True, (2, 8)), (True, (3, 1))]),
    (["--target=3.1", "--target=2.8", "--target=3"], {"code": 1}, [(True, (2, 8)), (True, (3, 1))]),
    (["--target=3.1", "-t=2.8", "--target=3"], {"code": 1}, [(True, (2, 8)), (True, (3, 1))]),

    # Invalid values.
    (["-t=a"], {"code": 1}, []),            # NaN
    (["--target=a"], {"code": 1}, []),
    (["-t=-1"], {"code": 1}, []),           # < 2
    (["--target=-1"], {"code": 1}, []),
    (["-t=1.8"], {"code": 1}, []),          # < 2
    (["--target=1.8"], {"code": 1}, []),
    (["-t=4"], {"code": 1}, []),            # >= 4
    (["--target=4"], {"code": 1}, []),
    (["-t=4,5"], {"code": 1}, []),          # > 4
    (["--target=4,5"], {"code": 1}, []),
    (["-t=2+"], {"code": 1}, []),           # Only - allowed.
    (["--target=2+"], {"code": 1}, []),
    (["-t=2,0.1"], {"code": 1}, []),        # 3 vals disallowed.
    (["--target=2,0.1"], {"code": 1}, []),
    (["-t=2.0,1"], {"code": 1}, []),        # 3 vals disallowed.
    (["--target=2.0,1"], {"code": 1}, []),
  ])
  def test_targets(self, args, parsed_args, expected):
    self.config.reset()
    self.assertParseArgs(args, parsed_args)
    self.assertEqual(self.config.targets(), expected)

  def test_ignore_incomp(self):
    self.assertFalse(self.config.ignore_incomp())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-i"]))
    self.assertTrue(self.config.ignore_incomp())
    self.config.set_ignore_incomp(False)
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["--ignore"]))
    self.assertTrue(self.config.ignore_incomp())

  @VerminTest.parameterized_args([
    (["-q"], {"code": 0, "paths": []}, DEFAULT_PROCESSES),

    # Valid values.
    (["-p=1"], {"code": 0, "paths": []}, 1),
    (["--processes=1"], {"code": 0, "paths": []}, 1),
    (["-p=9"], {"code": 0, "paths": []}, 9),
    (["--processes=9"], {"code": 0, "paths": []}, 9),

    # Invalid values.
    (["-p=hello"], {"code": 1}, DEFAULT_PROCESSES),
    (["--processes=hello"], {"code": 1}, DEFAULT_PROCESSES),
    (["-p=-1"], {"code": 1}, DEFAULT_PROCESSES),
    (["--processes=-1"], {"code": 1}, DEFAULT_PROCESSES),
    (["-p=0"], {"code": 1}, DEFAULT_PROCESSES),
    (["--processes=0"], {"code": 1}, DEFAULT_PROCESSES),
  ])
  def test_processes(self, args, parsed_args, expected):
    self.config.reset()
    self.assertParseArgs(args, parsed_args)
    self.assertEqual(self.config.processes(), expected)

  def test_print_visits(self):
    self.assertFalse(self.config.print_visits())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-d"]))
    self.assertTrue(self.config.print_visits())

  def test_lax(self):
    self.assertFalse(self.config.lax())
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["-l"]))
    self.assertTrue(self.config.lax())
    self.config.set_lax(False)
    self.assertContainsDict({"code": 0, "paths": []}, self.parse_args(["--lax"]))
    self.assertTrue(self.config.lax())

  def test_hidden(self):
    self.assertContainsDict({"code": 0}, self.parse_args(["--hidden"]))
    self.assertTrue(self.config.analyze_hidden())

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
    self.assertContainsDict({"code": 0}, self.parse_args(["--no-tips"]))
    self.assertFalse(self.config.show_tips())

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
      self.assertContainsDict({"code": 0, "versions": False}, self.parse_args(args))
      self.assertEqual(3, self.config.verbose())
      self.assertTrue(self.config.ignore_incomp())
      self.assertFalse(self.config.show_tips())

    # Verbosity can be higher for parsable.
    self.config.reset()
    self.assertContainsDict({"code": 0, "versions": False},
                            self.parse_args(["--format", "parsable", "-vvvv"]))
    self.assertEqual(4, self.config.verbose())
    self.assertTrue(self.config.ignore_incomp())
    self.assertFalse(self.config.show_tips())

  def test_pessimistic(self):
    self.assertFalse(self.config.pessimistic())
    self.assertContainsDict({"code": 0}, self.parse_args(["--pessimistic"]))
    self.assertTrue(self.config.pessimistic())

  def test_config_file(self):
    fp = ScopedTemporaryFile()
    fp.write(b"""[vermin]
verbose = 3
pessimistic = on
""")
    fp.close()

    self.assertContainsDict({"code": 0}, self.parse_args(["--config-file", fp.path()]))
    self.assertEqual(3, self.config.verbose())
    self.assertTrue(self.config.pessimistic())
    self.config.reset()
    self.assertContainsDict({"code": 0}, self.parse_args(["-c", fp.path()]))
    self.assertEqual(3, self.config.verbose())
    self.assertTrue(self.config.pessimistic())

    # Unspecified config file.
    self.assertContainsDict({"code": 1}, self.parse_args(["--config-file"]))
    self.assertContainsDict({"code": 1}, self.parse_args(["-c"]))

    # Nonexistent config file.
    self.assertContainsDict({"code": 1}, self.parse_args(["--config-file", "doesnotexist"]))
    self.assertContainsDict({"code": 1}, self.parse_args(["-c", "doesnotexist"]))

    # Other arguments must override any loaded config file, which means the config file must be
    # loaded first no matter the order of arguments passed on CLI.
    self.config.reset()
    self.assertContainsDict({"code": 0}, self.parse_args(["-v", "-c", fp.path()]))
    self.assertEqual(1, self.config.verbose())
    self.assertTrue(self.config.pessimistic())
    self.config.reset()
    self.assertContainsDict({"code": 0}, self.parse_args(["-c", fp.path(), "-v"]))
    self.assertEqual(1, self.config.verbose())
    self.assertTrue(self.config.pessimistic())

    # Can't use quiet and verbose modes together, even across CLI arguments and config file
    # settings.
    self.config.reset()
    self.assertContainsDict({"code": 1}, self.parse_args(["-c", fp.path(), "-q"]))
    self.config.reset()
    self.assertContainsDict({"code": 1}, self.parse_args(["-q", "-c", fp.path()]))
