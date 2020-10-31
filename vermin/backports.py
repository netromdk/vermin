from .utility import format_title_descs

BACKPORTS = (
  ("argparse", ["https://pypi.org/project/argparse/"]),
  ("configparser", ["https://pypi.org/project/configparser/"]),
  ("enum", ["https://pypi.org/project/enum34/"]),
  ("faulthandler", ["https://pypi.org/project/faulthandler/"]),
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
