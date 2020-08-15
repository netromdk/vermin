BACKPORTS = (
  ("argparse", "https://pypi.org/project/argparse/"),
  ("configparser", "https://pypi.org/project/configparser/"),
  ("enum", "https://pypi.org/project/enum34/"),
  ("faulthandler", "https://pypi.org/project/faulthandler/"),
  ("typing", "https://pypi.org/project/typing/"),
)

class Backports:
  @staticmethod
  def str(indent=0):
    res = []
    longest = len(max(Backports.modules(), key=lambda x: len(x)))
    for (mod, link) in BACKPORTS:
      res.append("{}{:{fill}} - {}".format(" " * indent, mod, link, fill=longest))
    return "\n".join(res)

  @staticmethod
  def modules():
    return {mod for (mod, link) in BACKPORTS}

  @staticmethod
  def is_backport(module):
    return module in Backports.modules()
