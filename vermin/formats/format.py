from abc import ABCMeta, abstractmethod

class Format:
  """Format encapsulates a format for presenting minimum versions and related information during
processing."""

  # Can't use `class Format(metaclass=ABCMeta)` in py2.
  __metaclass__ = ABCMeta

  def __init__(self, name):
    self.__name = name
    self.__config = None

  def name(self):
    return self.__name

  def config(self):
    return self.__config

  def set_config(self, config):
    self.__config = config

  @staticmethod
  def require_config(funcobj):
    """Decorator that checks config is not None."""
    def _require_config(self, *args, **kwargs):
      assert(self.config() is not None)
      return funcobj(self, *args, **kwargs)
    return _require_config

  @abstractmethod
  def skip_output_line(self):
    """Whether or not to skip outputting a line."""

  @abstractmethod
  def format_output_line(self, msg, path=None, line=None, col=None, versions=None):
    """Yield formatted output line given file name, line, column, text, minimum versions."""

  @abstractmethod
  def output_result(self, proc_res):
    """Output processed result."""

  @abstractmethod
  def sort_output_lines(self, lines):
    """Sort and return output lines."""
