from .backports import Backports
from .features import Features

class Config:
  __instance = None

  def __init__(self):
    if not Config.__instance:
      self.reset()
      Config.__instance = self

  @staticmethod
  def get():
    if not Config.__instance:
      Config()
    return Config.__instance

  def reset(self):
    self.__quiet = False
    self.__verbose = 0
    self.__print_visits = False
    self.__ignore_incomp = False
    self.__lax_mode = False
    self.__exclusions = set()
    self.__backports = set()
    self.__features = set()

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

  def lax_mode(self):
    return self.__lax_mode

  def set_lax_mode(self, lax):
    self.__lax_mode = lax

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
