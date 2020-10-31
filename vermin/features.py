from .utility import format_title_descs

FEATURES = (
  ("fstring-self-doc", [
    "[Unstable] Detect self-documenting fstrings. Can in",
    "some cases wrongly report fstrings as self-documenting."
  ]),
)

class Features:
  @staticmethod
  def str(indent=0):
    return format_title_descs(FEATURES, Features.features(), indent)

  @staticmethod
  def features():
    return {name for (name, desc) in FEATURES}

  @staticmethod
  def is_feature(feature):
    return feature in Features.features()
