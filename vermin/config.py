import io
import sys
import os
import re

from configparser import ConfigParser, ParsingError  # novm

from .backports import Backports
from .features import Features
from .formats import Format, DefaultFormat
from .constants import DEFAULT_PROCESSES, CONFIG_FILE_NAMES, CONFIG_SECTION, PROJECT_BOUNDARIES
from .utility import parse_target
from . import formats

class Config:
  def __init__(self):
    self.reset()

  def reset(self):
    self.__quiet = False
    self.__verbose = 0
    self.__print_visits = False
    self.__processes = DEFAULT_PROCESSES
    self.__ignore_incomp = False
    self.__pessimistic = False
    self.__show_tips = True
    self.__analyze_hidden = False
    self.__exclusions = set()
    self.__exclusion_regex = set()
    self.__make_paths_absolute = True
    self.__backports = set()
    self.__features = set()
    self.__targets = []
    self.__eval_annotations = False
    self.__only_show_violations = False
    self.__parse_comments = True
    self.__scan_symlink_folders = False
    self.set_format(DefaultFormat())

  def override_from(self, other_config):
    self.__quiet = other_config.quiet()
    self.__verbose = other_config.verbose()
    self.__print_visits = other_config.print_visits()
    self.__processes = other_config.processes()
    self.__ignore_incomp = other_config.ignore_incomp()
    self.__pessimistic = other_config.pessimistic()
    self.__show_tips = other_config.show_tips()
    self.__analyze_hidden = other_config.analyze_hidden()
    self.__exclusions = set(other_config.exclusions())
    self.__exclusion_regex = {re.compile(r) for r in other_config.exclusion_regex()}
    self.__make_paths_absolute = other_config.make_paths_absolute()
    self.__backports = other_config.backports()
    self.__features = other_config.features()
    self.__targets = other_config.targets()
    self.__eval_annotations = other_config.eval_annotations()
    self.__only_show_violations = other_config.only_show_violations()
    self.__parse_comments = other_config.parse_comments()
    self.__scan_symlink_folders = other_config.scan_symlink_folders()
    self.set_format(other_config.format())

  def __repr__(self):
    return """{}(
  quiet = {}
  verbose = {}
  print_visits = {}
  processes = {}
  ignore_incomp = {}
  pessimistic = {}
  show_tips = {}
  analyze_hidden = {}
  exclusions = {}
  exclusion_regex = {}
  make_paths_absolute = {}
  backports = {}
  features = {}
  targets = {}
  eval_annotations = {}
  only_show_violations = {}
  parse_comments = {}
  scan_symlink_folders = {}
  format = {}
)""".format(self.__class__.__name__, self.quiet(), self.verbose(), self.print_visits(),
            self.processes(), self.ignore_incomp(), self.pessimistic(), self.show_tips(),
            self.analyze_hidden(), self.exclusions(), self.exclusion_regex(),
            self.make_paths_absolute(), list(self.backports()), list(self.features()),
            self.targets(), self.eval_annotations(), self.only_show_violations(),
            self.parse_comments(), self.scan_symlink_folders(), self.format().name())

  @staticmethod
  def parse_file(path):
    try:
      return Config.parse_fp(open(path, mode="r", encoding="utf-8"), filename=path)
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
    args = {
      "quiet": str(config.quiet()),
      "verbose": str(config.verbose()),
      "print_visits": str(config.print_visits()),
      "processes": str(config.processes()),
      "ignore_incomp": str(config.ignore_incomp()),
      "pessimistic": str(config.pessimistic()),
      "show_tips": str(config.show_tips()),
      "analyze_hidden": str(config.analyze_hidden()),
      "exclusions": encode_list(config.exclusions()),
      "exclusion_regex": encode_list(config.exclusion_regex()),
      "make_paths_absolute": str(config.make_paths_absolute()),
      "backports": encode_list(config.backports()),
      "features": encode_list(config.features()),
      "targets": encode_list(config.targets()),
      "eval_annotations": str(config.eval_annotations()),
      "only_show_violations": str(config.only_show_violations()),
      "parse_comments": str(config.parse_comments()),
      "scan_symlink_folders": str(config.scan_symlink_folders()),
      "format": config.format().name(),
    }
    if sys.version_info < (3, 2):  # pragma: no cover
      parser = ConfigParser(args)
    else:
      parser = ConfigParser(args, allow_no_value=True)  # novm

    try:
      if sys.version_info < (3, 2):  # pragma: no cover
        # pylint: disable=deprecated-method disable=no-member # novm
        parser.readfp(fp, filename=filename)
      else:
        # `read_file` supercedes `readfp` since 3.2.
        def readline_generator(fp):
          line = fp.readline()
          while line:
            yield line
            line = fp.readline()
        parser.read_file(readline_generator(fp), source=filename)  # novm
    except Exception as ex:
      print("Could not load config: {}".format(filename))
      print(ex)
      return None

    if not parser.has_section(CONFIG_SECTION):
      print("Missing `[{}]` section in config: {}".format(CONFIG_SECTION, filename))
      return None

    def getbool(option):
      try:
        return parser.getboolean(CONFIG_SECTION, option)
      except ValueError:
        return str(True) == parser.defaults()[option]

    def getuint(option):
      value = parser.get(CONFIG_SECTION, option)
      if len(value) == 0:
        return int(parser.defaults()[option])
      value = int(value)
      if value < 0:
        raise ValueError("Not a positive integer (0+): {}".format(option))
      return value

    def getstringlist(option):
      keepends = False
      return parser.get(CONFIG_SECTION, option).strip().splitlines(keepends)

    config.set_quiet(getbool("quiet"))
    config.set_verbose(getuint("verbose"))
    config.set_print_visits(getbool("print_visits"))
    config.set_processes(getuint("processes"))
    config.set_ignore_incomp(getbool("ignore_incomp"))
    config.set_pessimistic(getbool("pessimistic"))
    config.set_show_tips(getbool("show_tips"))
    config.set_analyze_hidden(getbool("analyze_hidden"))
    config.set_eval_annotations(getbool("eval_annotations"))
    config.set_only_show_violations(getbool("only_show_violations"))
    config.set_parse_comments(getbool("parse_comments"))
    config.set_scan_symlink_folders(getbool("scan_symlink_folders"))

    for exclusion in getstringlist("exclusions"):
      config.add_exclusion(exclusion)

    for exclusion_regex in getstringlist("exclusion_regex"):
      config.add_exclusion_regex(exclusion_regex)

    config.set_make_paths_absolute(getbool("make_paths_absolute"))

    for backport in getstringlist("backports"):
      if not config.add_backport(backport):
        print("Unknown backport: {}".format(backport))
        return None

    for feature in getstringlist("features"):
      if not config.enable_feature(feature):
        print("Unknown feature: {}".format(feature))
        return None

    targets = getstringlist("targets")
    for target in targets:
      if not config.add_target(target):
        print("Invalid target: {}".format(target))
        return None

    fmt_str = parser.get(CONFIG_SECTION, "format").strip()
    fmt = formats.from_name(fmt_str)
    if fmt is None:
      print("Unknown format: {}".format(fmt_str))
      return None
    config.set_format(fmt)

    return config

  @staticmethod
  def detect_config_file(init_folder=None):
    """Detects Vermin config file starting from `init_folder` or CWD. It proceeds through parent
folders until root or project boundaries are reached. Each candidate is checked to be an INI with a
`[vermin]` section in it."""
    folder = init_folder or os.getcwd()
    while True:
      for candidate in CONFIG_FILE_NAMES:
        look_for = os.path.join(folder, candidate)
        if os.path.exists(look_for):
          try:
            cp = ConfigParser()
            parse_success_files = cp.read(look_for) if sys.version_info < (3, 2) \
              else cp.read(look_for, encoding="utf-8")  # novm
            if look_for in parse_success_files and cp.has_section(CONFIG_SECTION):
              return look_for
          except ParsingError:  # pragma: no cover
            pass

      # Stop if didn't find config and is at project boundary, which means it has ".git/" or
      # similar.
      stop = False
      for boundary in PROJECT_BOUNDARIES:
        path = os.path.join(folder, boundary)
        if os.path.exists(path):
          stop = True
          break
      if stop:
        break

      # Go up one level and stop at root.
      old_folder = folder
      folder = os.path.abspath(os.path.join(folder, ".."))
      if folder == old_folder:  # pragma: no cover
        break

    return None

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

  def processes(self):
    return self.__processes

  def set_processes(self, processes):
    self.__processes = processes if processes > 0 else DEFAULT_PROCESSES

  def ignore_incomp(self):
    return self.__ignore_incomp

  def set_ignore_incomp(self, ignore):
    self.__ignore_incomp = ignore

  def add_exclusion(self, name):
    self.__exclusions.add(name)

  def add_exclusion_regex(self, pattern):
    self.__exclusion_regex.add(re.compile(pattern))

  def add_exclusion_file(self, filename):
    try:
      with open(filename, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
          self.add_exclusion(line.strip())
    except Exception as ex:
      print(ex)

  def clear_exclusions(self):
    self.__exclusions.clear()

  def clear_exclusion_regex(self):
    self.__exclusion_regex.clear()

  def exclusions(self):
    res = list(self.__exclusions)
    res.sort()
    return res

  def exclusion_regex(self):
    res = [p.pattern for p in self.__exclusion_regex]
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

  def is_excluded_by_regex(self, path):
    return any(regex.search(path) for regex in self.__exclusion_regex)

  def make_paths_absolute(self):
    return self.__make_paths_absolute

  def set_make_paths_absolute(self, enable):
    self.__make_paths_absolute = enable

  def add_backport(self, name):
    if not Backports.is_backport(name):
      return False
    self.__backports.add(name)
    return True

  def clear_backports(self):
    self.__backports.clear()

  def backports(self):
    return self.__backports

  def enable_feature(self, name):
    if not Features.is_feature(name):
      return False
    self.__features.add(name)
    return True

  def has_feature(self, name):
    return name in self.__features

  def clear_features(self):
    self.__features.clear()

  def features(self):
    return self.__features

  def set_format(self, fmt):
    assert isinstance(fmt, Format)
    fmt.set_config(self)
    self.__format = fmt

  def format(self):
    return self.__format

  def set_pessimistic(self, pessimistic):
    self.__pessimistic = pessimistic

  def pessimistic(self):
    return self.__pessimistic

  def set_show_tips(self, show_tips):
    self.__show_tips = show_tips

  def show_tips(self):
    return self.__show_tips

  def set_analyze_hidden(self, analyze_hidden):
    self.__analyze_hidden = analyze_hidden

  def analyze_hidden(self):
    return self.__analyze_hidden

  def add_target(self, target, exact=True):
    """Adds a target. If target is a string it is parsed, otherwise it is required to be exactness
bool and a version tuple: [exact, (x, y)]. But it can also be a version tuple (x, y) in which case
the `exact` argument is supplied for exactness."""
    if len(self.targets()) == 2:
      print("A maximum of two targets can be specified!")
      return False

    # Bundle exactness with version for call site convenience especially if exactness is unchanged
    # (stays True):
    #   add_target((x, y)) vs. add_target([exact, (x, y)])
    if isinstance(target, tuple) and len(target) == 2:
      target = [exact, target]

    if isinstance(target, str):
      target = parse_target(target)
      if target is None:
        return None

    if len(target) != 2 or not isinstance(target[0], bool) or not isinstance(target[1], tuple) or\
       len(target[1]) != 2:
      return False

    # Add target and sort for target versions, not boolean values.
    self.__targets.append(target)
    self.__targets.sort(key=lambda t: t[1])
    return True

  def clear_targets(self):
    self.__targets = []

  def targets(self):
    return self.__targets

  def eval_annotations(self):
    return self.__eval_annotations

  def set_eval_annotations(self, eval_ann):
    self.__eval_annotations = eval_ann

  def only_show_violations(self):
    return self.__only_show_violations

  def set_only_show_violations(self, violations):
    self.__only_show_violations = violations

  def parse_comments(self):
    return self.__parse_comments

  def set_parse_comments(self, parse):
    self.__parse_comments = parse

  def scan_symlink_folders(self):
    return self.__scan_symlink_folders

  def set_scan_symlink_folders(self, scan):
    self.__scan_symlink_folders = scan
