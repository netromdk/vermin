from .utility import format_title_descs

BACKPORTS = (
  ("argparse", ["https://pypi.org/project/argparse/"]),
  ("asyncio", ["https://pypi.org/project/asyncio/"]),
  ("configparser", ["https://pypi.org/project/configparser/"]),
  ("contextvars", ["https://pypi.org/project/contextvars/"]),
  ("dataclasses", ["https://pypi.org/project/dataclasses/"]),
  ("enum", ["https://pypi.org/project/enum34/"]),
  ("faulthandler", ["https://pypi.org/project/faulthandler/"]),
  ("importlib", ["https://pypi.org/project/importlib/"]),
  ("ipaddress", ["https://pypi.org/project/ipaddress/"]),
  ("statistics", ["https://pypi.org/project/statistics/"]),
  ("typing", ["https://pypi.org/project/typing/"]),
)

class Backports:
  @staticmethod
  def str(indent=0):
    return format_title_descs(BACKPORTS, Backports.modules(), indent)

  @staticmethod
  def modules():
    return {mod for (mod, link) in BACKPORTS}

  @staticmethod
  def is_backport(module):
    return module in Backports.modules()
