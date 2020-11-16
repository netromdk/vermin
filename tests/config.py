from vermin import Backports, Features, Config
import vermin.formats

from .testutils import VerminTest, ScopedTemporaryFile

class VerminConfigTests(VerminTest):
  def test_defaults(self):
    self.assertFalse(self.config.quiet())
    self.assertEqual(0, self.config.verbose())
    self.assertFalse(self.config.print_visits())
    self.assertFalse(self.config.ignore_incomp())
    self.assertFalse(self.config.lax())
    self.assertFalse(self.config.pessimistic())
    self.assertTrue(self.config.show_tips())
    self.assertEmpty(self.config.exclusions())
    self.assertEmpty(self.config.backports())
    self.assertEmpty(self.config.features())
    self.assertEqual("default", self.config.format().name())

  def test_override_from(self):
    other = Config()
    other.set_quiet(True)
    other.set_verbose(3)
    other.set_print_visits(True)
    other.set_ignore_incomp(True)
    other.set_lax(True)
    other.set_pessimistic(True)
    other.set_show_tips(False)
    other.add_exclusion("foo.bar.baz")
    self.assertTrue(other.add_backport("typing"))
    self.assertTrue(other.enable_feature("fstring-self-doc"))
    other.set_format(vermin.formats.ParsableFormat())

    self.config.override_from(other)
    self.assertEqual(other.quiet(), self.config.quiet())
    self.assertEqual(other.verbose(), self.config.verbose())
    self.assertEqual(other.print_visits(), self.config.print_visits())
    self.assertEqual(other.ignore_incomp(), self.config.ignore_incomp())
    self.assertEqual(other.lax(), self.config.lax())
    self.assertEqual(other.pessimistic(), self.config.pessimistic())
    self.assertEqual(other.show_tips(), self.config.show_tips())
    self.assertEqual(other.exclusions(), self.config.exclusions())
    self.assertEqual(other.backports(), self.config.backports())
    self.assertEqual(other.features(), self.config.features())
    self.assertEqual(other.format(), self.config.format())

  def test_repr(self):
    self.assertEqual(str(self.config), """{}(
  quiet = {}
  verbose = {}
  print_visits = {}
  ignore_incomp = {}
  lax = {}
  pessimistic = {}
  show_tips = {}
  exclusions = {}
  backports = {}
  features = {}
  format = {}
)""".format(self.config.__class__.__name__, self.config.quiet(), self.config.verbose(),
            self.config.print_visits(), self.config.ignore_incomp(), self.config.lax(),
            self.config.pessimistic(), self.config.show_tips(), self.config.exclusions(),
            list(self.config.backports()), list(self.config.features()),
            self.config.format().name()))

  @VerminTest.parameterized_args([
    [u""],
    [u"""
"""],
    [u"""[vermin
"""],
    [u"""vermin]
"""],
    [u"""[ vermin ]
"""],
  ])
  def test_parse_invalid_section(self, data):
    self.assertIsNone(Config.parse_data(data))

  @VerminTest.parameterized_args([
    # Testing all possible, case-insensitive supported boolean values: 0, 1, on, off, no, yes, true,
    # false. Does not need to be repeated for each following boolean test.
    [u"""[vermin]
quiet =
""", False],
    [u"""[vermin]
#quiet = True
""", False],
    [u"""[vermin]
quiet = 1
""", True],
    [u"""[vermin]
quiet = on
""", True],
    [u"""[vermin]
quiet = yes
""", True],
    [u"""[vermin]
quiet = true
""", True],
    [u"""[vermin]
quiet = True
""", True],
    [u"""[vermin]
quiet = 0
""", False],
    [u"""[vermin]
quiet = off
""", False],
    [u"""[vermin]
quiet = no
""", False],
    [u"""[vermin]
quiet = false
""", False],
    [u"""[vermin]
quiet = False
""", False],
  ])
  def test_parse_quiet(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.quiet(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
verbose =
""", 0],
    [u"""[vermin]
#verbose = 1
""", 0],
    [u"""[vermin]
verbose = 0
""", 0],
    [u"""[vermin]
verbose = 1
""", 1],
    [u"""[vermin]
verbose = 2
""", 2],
  ])
  def test_parse_verbose(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.verbose(), expected)

  def test_parse_invalid_verbose(self):
    self.assertIsNone(Config.parse_data(u"""[vermin]
verbose = -1
"""))

  @VerminTest.parameterized_args([
    [u"""[vermin]
print_visits =
""", False],
    [u"""[vermin]
#print_visits = True
""", False],
    [u"""[vermin]
print_visits = True
""", True],
    [u"""[vermin]
print_visits = False
""", False],
  ])
  def test_parse_print_visits(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.print_visits(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
ignore_incomp =
""", False],
    [u"""[vermin]
#ignore_incomp = True
""", False],
    [u"""[vermin]
ignore_incomp = True
""", True],
    [u"""[vermin]
ignore_incomp = False
""", False],
  ])
  def test_parse_ignore_incomp(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.ignore_incomp(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
lax =
""", False],
    [u"""[vermin]
#lax = True
""", False],
    [u"""[vermin]
lax = True
""", True],
    [u"""[vermin]
lax = False
""", False],
  ])
  def test_parse_lax(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.lax(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
pessimistic =
""", False],
    [u"""[vermin]
#pessimistic = True
""", False],
    [u"""[vermin]
pessimistic = True
""", True],
    [u"""[vermin]
pessimistic = False
""", False],
  ])
  def test_parse_pessimistic(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.pessimistic(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
show_tips =
""", True],
    [u"""[vermin]
#show_tips = False
""", True],
    [u"""[vermin]
show_tips = False
""", False],
    [u"""[vermin]
show_tips = True
""", True],
  ])
  def test_parse_show_tips(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.show_tips(), expected)

  @VerminTest.parameterized_args([
    [u"""[vermin]
exclusions =
""", []],
    [u"""[vermin]
#exclusions = mod.member
""", []],
    [u"""[vermin]
exclusions = mod.member
""", [u"mod.member"]],
    [u"""[vermin]
exclusions = mod.member
  foo.bar(baz)
""", [u"foo.bar(baz)", u"mod.member"]],
    [u"""[vermin]
exclusions =
  mod.member
  foo.bar(baz)
""", [u"foo.bar(baz)", u"mod.member"]],
  ])
  def test_parse_exclusions(self, data, expected):
    config = Config.parse_data(data)
    self.assertIsNotNone(config)
    self.assertEqual(config.exclusions(), expected)

  def test_parse_backports(self):
    bps = Backports.modules()
    config = Config.parse_data(u"""[vermin]
backports = {}
""".format("\n  ".join(bps)))
    self.assertIsNotNone(config)
    self.assertEqual(bps, config.backports())

    config = Config.parse_data(u"""[vermin]
backports = unknown
""")
    self.assertIsNone(config)
    config = Config.parse_data(u"""[vermin]
backports = {}
  unknown
""".format(list(bps)[0]))
    self.assertIsNone(config)

  def test_parse_features(self):
    fs = Features.features()
    config = Config.parse_data(u"""[vermin]
features = {}
""".format("\n  ".join(fs)))
    self.assertIsNotNone(config)
    self.assertEqual(fs, config.features())

    self.assertIsNone(Config.parse_data(u"""[vermin]
features = unknown
"""))
    self.assertIsNone(Config.parse_data(u"""[vermin]
features = {}
  unknown
""".format(list(fs)[0])))

  def test_parse_format(self):
    for fmt in vermin.formats.names():
      config = Config.parse_data(u"""[vermin]
format = {}
""".format(fmt))
      self.assertIsNotNone(config)
      self.assertEqual(fmt, config.format().name())

    self.assertIsNone(Config.parse_data(u"""[vermin]
format = unknown
"""))

  def test_parse_file(self):
    fp = ScopedTemporaryFile()
    fp.write(b"""[vermin]
quiet = 1
verbose = 2
print_visits = on
ignore_incomp = yes
lax = true
pessimistic = TrUe
""")
    fp.close()
    config = Config.parse_file(fp.path())
    self.assertIsNotNone(config)
    self.assertTrue(config.quiet())
    self.assertEqual(2, config.verbose())
    self.assertTrue(config.print_visits())
    self.assertTrue(config.ignore_incomp())
    self.assertTrue(config.lax())
    self.assertTrue(config.pessimistic())
