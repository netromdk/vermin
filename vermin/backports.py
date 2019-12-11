BACKPORTS = (
  ("configparser", "https://pypi.org/project/configparser/"),
  ("faulthandler", "https://pypi.org/project/faulthandler/"),
  ("typing", "https://pypi.org/project/typing/"),
)

class Backports:
  @staticmethod
  def str(indent=0):
    res = []
    for (mod, link) in BACKPORTS:
      res.append("{}{}\t - {}".format(" " * indent, mod, link))
    return "\n".join(res)

  @staticmethod
  def modules():
    return {mod for (mod, link) in BACKPORTS}

  @staticmethod
  def is_backport(module):
    return module in Backports.modules()
