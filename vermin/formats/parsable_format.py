import sys

from .format import Format
from ..utility import version_strings, sort_line_column_parsable

class ParsableFormat(Format):
  def __init__(self):
    super(ParsableFormat, self).__init__("parsable")

  def set_config(self, config):
    config.set_verbose(max(3, config.verbose()))
    config.set_ignore_incomp(True)
    config.set_show_tips(False)
    super(ParsableFormat, self).set_config(config)

  def skip_output_line(self):
    """Never skip."""
    return False

  def format_output_line(self, msg, path=None, line=None, col=None, versions=None):
    vers = version_strings(versions, ":") if versions is not None else ":"
    if msg is None:
      msg = ""
    msg = msg.replace("\n", "\\n")
    path = "" if path is None else path
    return "{}:{}:{}:{}:{}".format(path, line if line is not None else "",
                                   col if col is not None else "", vers, msg)

  def output_result(self, proc_res):
    # Output all findings of the file.
    sys.stdout.write(proc_res.text)

    # Then output summary of the file with no line/col numbers and no description.
    summary = self.format_output_line(msg=None, path=proc_res.path, versions=proc_res.mins)
    sys.stdout.write("{}\n".format(summary))

  def sort_output_lines(self, lines):
    lines.sort(key=sort_line_column_parsable)
    return lines
