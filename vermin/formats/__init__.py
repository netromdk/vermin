from .format import Format
from .default_format import DefaultFormat
from .parsable_format import ParsableFormat

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
  elif name == "parsable":
    return ParsableFormat()
  return None

def help_str(indent=0):
  res = []
  longest = len(max(names(), key=lambda x: len(x)))
  for (name, desc) in FORMATS:
    title = "{}{:{fill}} - ".format(" " * indent, name, fill=longest)
    first_line = desc[0]
    res.append("{}{}".format(title, first_line))
    if len(desc) > 1:
      for line in desc[1:]:
        res.append("{}{}".format(" " * len(title), line))
  return "\n".join(res)

__all__ = [
  "DefaultFormat",
  "Format",
  "ParsableFormat",
  "from_name",
  "help_str",
  "names",
]
