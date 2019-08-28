from multiprocessing import cpu_count

from vermin import parse_args, Config

from .testutils import VerminTest

class VerminArgumentsTests(VerminTest):
  def __init__(self, methodName):
    super(VerminArgumentsTests, self).__init__(methodName)
    self.config = Config.get()

  def setUp(self):
    self.config.reset()

  def tearDown(self):
    self.config.reset()

  def test_not_enough_args(self):
    self.assertContainsDict({"code": 1, "usage": True}, parse_args([]))

  def test_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py", "file2.py", "folder/folder2"]},
                            parse_args(["file.py", "file2.py", "folder/folder2"]))

  def test_mix_options_and_files(self):
    self.assertContainsDict({"code": 0, "paths": ["file.py"], "targets": [2.7]},
                            parse_args(["-q", "-t=2.7", "file.py"]))

  def test_quiet(self):
    self.assertFalse(self.config.quiet())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-q"]))
    self.assertTrue(self.config.quiet())

  def test_verbose(self):
    self.assertEqual(0, self.config.verbose())
    for n in range(1, 10):
      self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-" + n * "v"]))
      self.assertEqual(n, self.config.verbose())

  def test_cant_mix_quiet_and_verbose(self):
    self.assertContainsDict({"code": 1}, parse_args(["-q", "-v"]))

  def test_targets(self):
    self.assertContainsDict({"code": 0, "targets": [2.8], "paths": []},
                            parse_args(["-t=2.8"]))
    self.assertContainsDict({"code": 0, "targets": [2.8, 3.0], "paths": []},
                            parse_args(["-t=3", "-t=2.8"]))
    self.assertContainsDict({"code": 1},
                            parse_args(["-t=3.1", "-t=2.8", "-t=3"]))

    # Invalid values.
    self.assertContainsDict({"code": 1}, parse_args(["-t=a"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=-1"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=1.8"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=4"]))
    self.assertContainsDict({"code": 1}, parse_args(["-t=10"]))

  def test_ignore_incomp(self):
    self.assertFalse(self.config.ignore_incomp())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-i"]))
    self.assertTrue(self.config.ignore_incomp())

  def test_processes(self):
    # Default value is cpu_count().
    self.assertContainsDict({"code": 0, "processes": cpu_count(), "paths": []},
                            parse_args(["-q"]))

    # Valid values.
    self.assertContainsDict({"code": 0, "processes": 1, "paths": []},
                            parse_args(["-p=1"]))
    self.assertContainsDict({"code": 0, "processes": 9, "paths": []},
                            parse_args(["-p=9"]))

    # Invalid values.
    self.assertContainsDict({"code": 1}, parse_args(["-p=hello"]))
    self.assertContainsDict({"code": 1}, parse_args(["-p=-1"]))
    self.assertContainsDict({"code": 1}, parse_args(["-p=0"]))

  def test_print_visits(self):
    self.assertFalse(self.config.print_visits())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-d"]))
    self.assertTrue(self.config.print_visits())

  def test_lax_mode(self):
    self.assertFalse(self.config.lax_mode())
    self.assertContainsDict({"code": 0, "paths": []}, parse_args(["-l"]))
    self.assertTrue(self.config.lax_mode())
