import os
import re

from ..utility import bounded_str_hash, version_strings
from .parsable_format import ParsableFormat

def escape(value):
  """Escape special characters in GitHub Actions annotations. Not to be used for messages."""
  return (
    str(value)
    .replace('%', '%25')  # must be first
    .replace(',', '%2C')
    .replace(':', '%3A')
  )

class GitHubFormat(ParsableFormat):
  """Variant of ParsableFormat which outputs as Github Actions annotations."""

  def __init__(self, name="github"):
    super().__init__(name)
    self.order = {}
    """cache sort order of lines; SourceVisitor maintains an internal list of outputs from
    format_output_line; these are later deduplicated in a set, then passed to sort_output_lines;
    so caching their order uses minimal extra memory and avoids a fragile parse of the already
    serialized data to extract its sort order
    """
    self.cwd = os.getcwd()
    """current working directory, to relativize paths"""

  def format_output_line(self, msg, path=None, line=None, col=None,
                         versions=None, plural=None, violation=False):
    # default title is for generic analysis errors/notices
    title = "Python version requirement analysis"
    level = "error" if violation else "notice"
    if versions is not None:
      versions = version_strings(versions)
      title = "Requires Python {}".format(versions)
    if msg is None:
      if versions is None:
        msg = "user-defined symbols being ignored"
      # msg is None when providing a summary
      elif path is None:
        msg = "Minimum Python version required across all files: {}".format(versions)
      else:
        msg = "Minimum Python version required for this file: {}".format(versions)
    # github actions can't display multiline messages
    if msg is not None:
      msg = re.sub(r'(\r\n|\r|\n)', ' | ', str(msg))
    # relativize path so github can link to it in a PR
    if path is not None:
      try:
        path = os.path.abspath(path)
        path = os.path.relpath(path, self.cwd)
      except ValueError:
        pass
    vals = {
      "file": path,
      "line": line,
      "col": col,
      "title": title,
    }
    args = ",".join("{}={}".format(k, escape(v)) for k, v in vals.items() if v is not None)
    out = "::{} {}::{}".format(level, args, msg)

    # pre-calculate sort order
    order = (line or 0) + (float(col or 0) + bounded_str_hash(title + "\n" + msg)) / 1000
    self.order[out] = order
    return out

  def _sort_key(self, line):
    """Uses cached order, falling back to plain hash if not found."""
    if line not in self.order:
      return bounded_str_hash(line)
    return self.order[line]

  def sort_output_lines(self, lines):
    lines.sort(key=self._sort_key)
    # SourceVisitor, which calls this, overwrites its internal list of outputs; so the input
    # lines will never be reused; safe to clear the cache here. Only deleting the lines we've
    # seen, to handle depth-first AST traversals.
    for line in lines:
      if line in self.order:
        del self.order[line]
    return lines
