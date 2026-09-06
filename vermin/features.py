from .utility import format_title_descs

DEFAULT_FEATURES = ("fstring-self-doc", "fstring-pep701")

FEATURES = (
  ("fstring-self-doc", [
    "Detect self-documenting fstrings. Enabled by default.",
  ]),
  ("fstring-pep701", [
    "Detect PEP 701 f-string features (3.12+): same-quote",
    "nesting and multi-line expressions. Requires running on",
    "Python 3.12+. Enabled by default."
  ]),
  ("union-types", [
    "[Unstable] Detect union types `X | Y`. Can in some cases",
    "wrongly report union types due to having to employ heuristics."
  ]),
)

class Features:
  @staticmethod
  def defaults():
    return set(DEFAULT_FEATURES)

  @staticmethod
  def str(indent=0):
    return format_title_descs(FEATURES, Features.features(), indent)

  @staticmethod
  def features():
    return {name for (name, desc) in FEATURES}

  @staticmethod
  def is_feature(feature):
    return feature in Features.features()
