import re

from .utility import format_title_descs, version_strings

VERSIONED_BACKPORT_REGEX = re.compile(r"([\w_\.]+)\=\=.+")

# Versioned backports must be ordered from oldest minimum version to newest and placed before
# unversioned backport.
BACKPORTS = (
  ("argparse", ["https://pypi.org/project/argparse/"], ((2, 3), (3, 1))),
  ("asyncio", ["https://pypi.org/project/asyncio/"], (None, (3, 3))),
  ("configparser", ["https://pypi.org/project/configparser/"], ((2, 6), (3, 0))),
  ("contextvars", ["https://pypi.org/project/contextvars/"], (None, (3, 5))),
  ("dataclasses", ["https://pypi.org/project/dataclasses/"], (None, (3, 6))),
  ("enum", ["https://pypi.org/project/enum34/"], ((2, 4), (3, 3))),
  ("faulthandler", ["https://pypi.org/project/faulthandler/"], ((2, 6), (3, 0))),
  ("importlib", ["https://pypi.org/project/importlib/"], ((2, 3), (3, 0))),
  ("ipaddress", ["https://pypi.org/project/ipaddress/"], ((2, 6), (3, 2))),
  ("mock", ["https://pypi.org/project/mock/"], (None, (3, 6))),
  ("statistics", ["https://pypi.org/project/statistics/"], ((2, 6), (3, 4))),

  # Notes:
  #  Although `typing` backport now requires 2.7 or 3.4+, it originally supported 3.2 and 3.3.
  #  See: https://github.com/python/typing/blob/02c9d79eb7/prototyping/setup.py
  ("typing", ["https://pypi.org/project/typing/"], ((2, 7), (3, 2))),

  ("typing_extensions==4.0", ["https://pypi.org/project/typing-extensions/4.0.0/"], (None, (3, 6))),
  ("typing_extensions==4.3", ["https://pypi.org/project/typing-extensions/4.3.0/"], (None, (3, 7))),
  ("typing_extensions", ["https://pypi.org/project/typing-extensions/4.3.0/"], (None, (3, 7))),

  ("zoneinfo", ["https://pypi.org/project/backports.zoneinfo/"], (None, (3, 6))),
)

class Backports:
  @staticmethod
  def str(indent=0, backports=BACKPORTS):
    return format_title_descs(((mod, ["{} ({})".format(link[0], version_strings(mins))])
                               for (mod, link, mins) in backports), Backports.modules(), indent)

  @staticmethod
  def modules():
    return {mod for (mod, link, mins) in BACKPORTS}

  @staticmethod
  def is_backport(module):
    return module in Backports.modules()

  @staticmethod
  def version_filter(module):
    m = VERSIONED_BACKPORT_REGEX.match(module)
    if m:
      return m.group(1)
    return module

  @staticmethod
  def unversioned_filter(modules):
    return {Backports.version_filter(bp) for bp in modules}

  @staticmethod
  def expand_versions(module):
    lst = [(mod, link, mins) for (mod, link, mins) in BACKPORTS
           if Backports.version_filter(mod) == module]
    lst.reverse()  # Unversioned should come first.
    return lst
