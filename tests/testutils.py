import unittest
import sys
import os
from contextlib import contextmanager
from os.path import join
from tempfile import NamedTemporaryFile

from vermin import Config, Arguments, detect, visit

def current_version():
  return sys.version_info

def touch(fld, name, contents=None):
  filename = join(fld, name)
  with open(filename, mode="w", encoding="utf-8") as fp:
    if contents is not None:
      fp.write(contents)
  return filename

@contextmanager
def working_dir(path):
  prev_wd = os.getcwd()
  try:
    os.chdir(path)
    yield
  finally:
    os.chdir(prev_wd)

class VerminTest(unittest.TestCase):
  """General test case class for all Vermin tests."""

  def __init__(self, methodName):
    super().__init__(methodName)

    # Allow test diffs of any size (instead of 640 char max).
    self.maxDiff = None

    # Append additional assertion message to the end of the normal failure message, instead of
    # replacing it.
    self.longMessage = True

    self.config = Config()

  def setUp(self):
    self.config.reset()

  def detect(self, source):
    return detect(source, config=self.config)

  def visit(self, source, path=None):
    return visit(source, config=self.config, path=path)

  def parse_args(self, args, detect_path=None):
    return Arguments(args).parse(self.config, detect_path)

  @staticmethod
  def skipUnlessVersion(major_version, minor_version=0):
    """Decorator that only runs test if at least the specified Python version is being used."""
    def decorator(func):
      def wrapper(self, *args, **kwargs):
        if current_version() >= (major_version, minor_version):
          func(self, *args, **kwargs)
      return wrapper
    return decorator

  @staticmethod
  def skipUnlessPlatform(platform):
    """Decorator that only runs test if executing on specified platform. It checks that the platform
starts with the provided value, like 'win32' or 'darwin'."""
    def decorator(func):
      def wrapper(self, *args, **kwargs):
        if sys.platform.lower().startswith(platform.strip().lower()):
          func(self, *args, **kwargs)
      return wrapper
    return decorator

  @staticmethod
  def skipPlatform(platform):
    """Decorator that runs test if executing not on specified platform. It checks that the platform
starts with the provided value, like 'win32' or 'darwin'."""
    def decorator(func):
      def wrapper(self, *args, **kwargs):
        if not sys.platform.lower().startswith(platform.strip().lower()):
          func(self, *args, **kwargs)
      return wrapper
    return decorator

  @staticmethod
  def parameterized_args(tuple_args):
    """Decorator accepting a list of tuples of arguments."""
    def decorator(func):
      def wrapper(self):
        for args in tuple_args:
          func(self, *args)
      return wrapper
    return decorator

  @staticmethod
  def parameterized_exceptions(tuple_args):
    """Decorator accepting a list of tuples of arguments, where the first must be the exception type
expected to be raised."""
    def decorator(func):
      def wrapper(self):
        for args in tuple_args:
          assert len(args) > 1, "Expected tuple: (exception type, test function args..)"
          try:
            func(self, *args[1:])
          except args[0]:
            continue
          except Exception as ex:  # pragma: no cover
            raise AssertionError("Raised {} instead of {} for args: {}".
                                 format(type(ex), args[0], args[1:])) from ex
          # pragma: no cover
          raise AssertionError("Didn't raise {} for args: {}".format(args[0], args[1:]))
      return wrapper
    return decorator

  def assertOnlyIn(self, values, data, msg=None):
    """Assert only value(s) is in data but ignores None and 0 values."""
    size = 1
    multiple = isinstance(values, (list, tuple))
    if multiple:
      # Unless it's a tuple of ints, then it's a version and not a multiple.
      if all(isinstance(x, int) for x in values):
        multiple = False
      else:
        size = len(values)
    self.assertEqual(len(data) - data.count(None) - data.count(0) - data.count((0, 0)), size, msg)
    if multiple:
      for value in values:
        self.assertIn(value, data, msg)
    else:
      self.assertIn(values, data, msg)

  def assertContainsDict(self, dictionary, data, msg=None):
    """Assert data contains all keys and values of dictionary input."""
    msg = ", " + msg if msg is not None else ""
    for key in dictionary:
      self.assertTrue(key in data, msg="Data doesn't have key '{}'{}".format(key, msg))
      value = dictionary[key]
      value2 = data[key]
      self.assertEqual(value, value2,
                       msg="key={}, value={} != target={}{}".format(key, value, value2, msg))

  def assertEmpty(self, data):
    self.assertTrue(len(data) == 0,
                    msg="Input not empty! size={}, '{}'".format(len(data), data))

  def assertNotEmpty(self, data):
    self.assertTrue(len(data) != 0, msg="Input empty!")

  def assertEqualItems(self, expected, actual):
    """Assert that two sequences contain the same elements, regardless of the ordering.
`assertItemsEqual()` is a 2.7 unittest function. In 3.2 it's called `assertCountEqual()`. This
override is made to work for all versions, also 3.0-3.1."""
    v = current_version()
    if v >= (3, 2):
      self.assertCountEqual(expected, actual)
    if (2, 7) <= v < (3, 0):  # pragma: no cover
      self.assertItemsEqual(expected, actual)  # pylint: disable=no-member
    else:
      self.assertEqual(sorted(expected), sorted(actual))

  def assertDetectMinVersions(self, source, min_versions):
    """Assert the minimum versions of `source` is `min_versions`."""
    res_versions = self.detect(source)
    self.assertOnlyIn(min_versions, res_versions, msg="""Minimum versions: {}
Expected: {}
Source:
{}""".format(res_versions, min_versions, source))

  def assertParseArgs(self, args, parsed_args):
    """Assert the parsed arguments from input arguments."""
    self.assertContainsDict(parsed_args, self.parse_args(args),
                            msg="args={}".format(args))

class ScopedTemporaryFile:
  """Creates a temporary file that is automatically removed when this instance goes out of scope.
The difference to NamedTemporaryFile is that it isn't deleted when closing the file.
  """

  def __init__(self, suffix=".py"):
    # pylint: disable=consider-using-with
    self.__fp = NamedTemporaryFile(suffix=suffix, delete=False)

  def __del__(self):
    os.remove(self.path())

  def __enter__(self):
    return self

  def __exit__(self, _exc_type, _exc_val, _exc_tb):
    return False

  def write(self, data, newline=False):
    self.__fp.write(data)
    if newline:
      self.__fp.write(b"\n")

  def writeln(self, data):
    self.write(data, newline=True)

  def close(self):
    self.__fp.close()

  def path(self):
    return self.__fp.name
