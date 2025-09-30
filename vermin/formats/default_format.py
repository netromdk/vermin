from .format import Format
from ..utility import version_strings, sort_line_column
from ..printing import vprint, sgr

class DefaultFormat(Format):
  def __init__(self, colored=False):
    super().__init__("colored" if colored else "default")
    self.colored = colored
    """Whether ANSI colored styling is enabled."""

  def __maybe_style(self, msg, violation):
    if self.colored:
      return sgr(msg, 91 if violation else 92)  # bright red or bright green
    return msg

  @Format.require_config
  def skip_output_line(self):
    return self.config().quiet()

  @Format.require_config
  def format_output_line(self, msg, path=None, line=None, col=None,
                         versions=None, plural=None, violation=False):
    if plural is None:
      plural = msg.strip().endswith("s")
    if self.config().verbose() < 3:
      line = None
      col = None
    line = "L{}".format(line) if line is not None else ""
    col = " C{}".format(col) if col is not None else ""
    lc = "{}{}".format(line, col)
    if len(lc) > 0:
      lc += ": "
    vers = " require{} {}".format("s" if not plural else "", version_strings(versions)) \
      if versions is not None else ""
    return self.__maybe_style("{}{}{}".format(lc, msg, vers), violation)

  @Format.require_config
  def output_result(self, proc_res):
    # Indent subtext.
    subtext = ""
    if len(proc_res.text) > 0:
      lines = proc_res.text.splitlines(True)
      subtext = "\n  " + "  ".join(lines)
      if not subtext.endswith("\n"):
        subtext += "\n"  # pragma: no cover
    msg = "{:<12} {}{}".format(version_strings(proc_res.mins), proc_res.path, subtext)
    vprint(msg, self.config())

  @Format.require_config
  def sort_output_lines(self, lines):
    if self.config().verbose() > 2 and not self.config().print_visits():
      lines.sort(key=sort_line_column)  # pragma: no cover
    else:
      lines.sort()
    return lines
