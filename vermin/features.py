FEATURES = (
  ("fstring-self-doc", [
    "[Unstable] Detect self-documenting fstrings. Can in",
    "some cases wrongly report fstrings as self-documenting."
  ]),
)

class Features:
  @staticmethod
  def str(indent=0):
    res = []
    longest = len(max(Features.features(), key=lambda x: len(x)))
    for (name, desc) in FEATURES:
      title = "{}{:{fill}} - ".format(" " * indent, name, fill=longest)
      first_line = desc[0]
      res.append("{}{}".format(title, first_line))
      if len(desc) > 1:
        for line in desc[1:]:
          res.append("{}{}".format(" " * len(title), line))
    return "\n".join(res)

  @staticmethod
  def features():
    return {name for (name, desc) in FEATURES}

  @staticmethod
  def is_feature(feature):
    return feature in Features.features()
