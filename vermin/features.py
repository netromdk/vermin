from .utility import format_title_descs

FEATURES = (
  ("fstring-self-doc", [
    "[Unstable] Detect self-documenting fstrings. Can in",
    "some cases wrongly report fstrings as self-documenting."
  ]),
  ("fstring-pep701", [
    "[Unstable] Detect PEP 701 f-string features (3.12+).",
    "Same-quote nesting and multi-line expressions.",
    "Requires running on Python 3.12+."
  ]),
  ("union-types", [
    "[Unstable] Detect union types `X | Y`. Can in some cases",
    "wrongly report union types due to having to employ heuristics."
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
