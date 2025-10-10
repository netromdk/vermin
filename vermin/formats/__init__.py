from .format import Format
from .default_format import DefaultFormat
from .parsable_format import ParsableFormat
from .github_format import GitHubFormat
from ..utility import format_title_descs

FORMATS = (
  ("default", ["Default formatting."]),
  ("colored", ["Same as default, but prints with ANSI styling."]),
  ("parsable", [
    "Each result is on form 'file:line:column:py2:py3:feature'. The",
    "last line has no path or line/column numbers and contains the",
    "minimum py2 and py3 versions. Minimum verbosity level is set to",
    "3 but can be increased. Tips, hints, incompatible versions, and",
    "`--versions` are disabled. File paths containing ':' are ignored."
  ]),
  ("github", [
    "Same as parsable format, but each result is formatted as a GitHub",
    "Actions annotation. Minimum version messages are annotated as",
    "errors, and all other verbose messages as notices. The intent is",
    "that it be used for linting in a GitHub Actions pipeline."
  ]),
)

def names():
  return {name for (name, desc) in FORMATS}

def from_name(name):
  if name == "default":
    return DefaultFormat()
  if name == "colored":
    return DefaultFormat(colored=True)
  if name == "parsable":
    return ParsableFormat()
  if name == "github":
    return GitHubFormat()
  return None

def help_str(indent=0):
  return format_title_descs(FORMATS, names(), indent)

__all__ = [
  "DefaultFormat",
  "Format",
  "ParsableFormat",
  "GitHubFormat",
  "from_name",
  "help_str",
  "names",
]
