from .format import Format
from .default_format import DefaultFormat
from .parsable_format import ParsableFormat
from ..utility import format_title_descs

FORMATS = (
  ("default", ["Default formatting."]),
  ("parsable", [
    "Each result is on form 'file:line:column:py2:py3:feature'. The",
    "last line has no path or line/column numbers and contains the",
    "minimum py2 and py3 versions. Minimum verbosity level is set to",
    "3 but can be increased. Tips, hints, incompatible versions, and",
    "`--versions` are disabled. File paths containing ':' are ignored."
  ])
)

def names():
  return {name for (name, desc) in FORMATS}

def from_name(name):
  if name == "default":
    return DefaultFormat()
  if name == "parsable":
    return ParsableFormat()
  return None

def help_str(indent=0):
  return format_title_descs(FORMATS, names(), indent)

__all__ = [
  "DefaultFormat",
  "Format",
  "ParsableFormat",
  "from_name",
  "help_str",
  "names",
]
