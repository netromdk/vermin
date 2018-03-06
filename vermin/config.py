class Config:
  __instance = None

  def __init__(self):
    if not Config.__instance:
      self.__quiet = False
      self.__verbose = 0
      self.__print_visits = False
      self.__ignore_incomp = False

      Config.__instance = self

  @staticmethod
  def get():
    if not Config.__instance:
      Config()
    return Config.__instance

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
