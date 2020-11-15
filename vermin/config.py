import io
import sys

# novm
try:
  from configparser import ConfigParser
except ImportError:
  from ConfigParser import SafeConfigParser as ConfigParser

from .backports import Backports
from .features import Features
from .formats import Format, DefaultFormat
from . import formats

class Config:
  def __init__(self):
    self.reset()

  def reset(self):
    self.__quiet = False
    self.__verbose = 0
    self.__print_visits = False
    self.__ignore_incomp = False
    self.__lax = False
    self.__pessimistic = False
    self.__exclusions = set()
    self.__backports = set()
    self.__features = set()
    self.set_format(DefaultFormat())

  def __repr__(self):
    return """{}(
  quiet = {}
  verbose = {}
  print_visits = {}
  ignore_incomp = {}
  lax = {}
  pessimistic = {}
  exclusions = {}
  backports = {}
  features = {}
  format = {}
)""".format(self.__class__.__name__, self.quiet(), self.verbose(), self.print_visits(),
            self.ignore_incomp(), self.lax(), self.pessimistic(), self.exclusions(),
            list(self.backports()), list(self.features()), self.format().name())

  @staticmethod
  def parse_file(path):
    try:
      return Config.parse_fp(open(path, mode="r"), filename=path)
    except Exception as ex:
      print("Could not load config file: {}".format(path))
      print(ex)
    return None

  @staticmethod
  def parse_data(data):
    try:
      return Config.parse_fp(io.StringIO(data))
    except Exception as ex:
      print("Could not load config data")
      print(ex)
    return None

  @staticmethod
  def parse_fp(fp, filename=None):
    filename = filename or "<???>"
    config = Config()

    def encode_list(iterable):
      return "\n".join(iterable)

    # Parser with default values from initial instance.
    parser = ConfigParser({
      "quiet": config.quiet(),
      "verbose": config.verbose(),
      "print_visits": config.print_visits(),
      "ignore_incomp": config.ignore_incomp(),
      "lax": config.lax(),
      "pessimistic": config.pessimistic(),
      "exclusions": encode_list(config.exclusions()),
      "backports": encode_list(config.backports()),
      "features": encode_list(config.features()),
      "format": config.format().name(),
    }, allow_no_value=True)

    try:
      if sys.version_info < (3, 2):
        parser.readfp(fp, filename=filename)  # pylint: disable=deprecated-method
      else:
        # `read_file` supercedes `readfp` since 3.2.
        def readline_generator(fp):
          line = fp.readline()
          while line:
            yield line
            line = fp.readline()
        parser.read_file(readline_generator(fp), source=filename)
    except Exception as ex:
      print("Could not load config: {}".format(filename))
      print(ex)
      return None

    section = "vermin"
    if not parser.has_section(section):
      print("Missing `[{}]` section in config: {}".format(section, filename))
      return None

    def getbool(option):
      try:
        return parser.getboolean(section, option)
      except ValueError:
        return "True" == parser.defaults()[option]

    def getuint(option):
      value = parser.get(section, option)
      if len(value) == 0:
        return int(parser.defaults()[option])
      value = int(value)
      if value < 0:
        raise ValueError("Not a positive integer (0+): {}".format(option))
      return value

    def getstringlist(option):
      keepends = False
      return parser.get(section, option).strip().splitlines(keepends)

    config.set_quiet(getbool("quiet"))
    config.set_verbose(getuint("verbose"))
    config.set_print_visits(getbool("print_visits"))
    config.set_ignore_incomp(getbool("ignore_incomp"))
    config.set_lax(getbool("lax"))
    config.set_pessimistic(getbool("pessimistic"))

    for exclusion in getstringlist("exclusions"):
      config.add_exclusion(exclusion)

    for backport in getstringlist("backports"):
      if not config.add_backport(backport):
        print("Unknown backport: {}".format(backport))
        return None

    for feature in getstringlist("features"):
      if not config.enable_feature(feature):
        print("Unknown feature: {}".format(feature))
        return None

    fmt_str = parser.get(section, "format").strip()
    fmt = formats.from_name(fmt_str)
    if fmt is None:
      print("Unknown format: {}".format(fmt_str))
      return None
    config.set_format(fmt)

    return config

  def quiet(self):
    return self.__quiet

  def set_quiet(self, quiet):
    self.__quiet = quiet

  def verbose(self):
    return self.__verbose

  def set_verbose(self, verbose):
    self.__verbose = verbose

  def print_visits(self):
    return self.__print_visits

  def set_print_visits(self, enable):
    self.__print_visits = enable

  def ignore_incomp(self):
    return self.__ignore_incomp

  def set_ignore_incomp(self, ignore):
    self.__ignore_incomp = ignore

  def lax(self):
    return self.__lax

  def set_lax(self, lax):
    self.__lax = lax

  def add_exclusion(self, name):
    self.__exclusions.add(name)

  def add_exclusion_file(self, filename):
    try:
      with open(filename, mode="r") as f:
        for line in f.readlines():
          self.add_exclusion(line.strip())
    except Exception as ex:
      print(ex)

  def exclusions(self):
    res = list(self.__exclusions)
    res.sort()
    return res

  def is_excluded(self, name):
    return name in self.__exclusions

  def is_excluded_kwarg(self, function, keyword):
    return "{}({})".format(function, keyword) in self.__exclusions

  def is_excluded_codecs_error_handler(self, name):
    return "ceh={}".format(name) in self.__exclusions

  def is_excluded_codecs_encoding(self, name):
    return "ce={}".format(name) in self.__exclusions

  def add_backport(self, name):
    if not Backports.is_backport(name):
      return False
    self.__backports.add(name)
    return True

  def backports(self):
    return self.__backports

  def enable_feature(self, name):
    if not Features.is_feature(name):
      return False
    self.__features.add(name)
    return True

  def has_feature(self, name):
    return name in self.__features

  def features(self):
    return self.__features

  def set_format(self, fmt):
    assert(isinstance(fmt, Format))
    fmt.set_config(self)
    self.__format = fmt

  def format(self):
    return self.__format

  def set_pessimistic(self, pessimistic):
    self.__pessimistic = pessimistic

  def pessimistic(self):
    return self.__pessimistic
