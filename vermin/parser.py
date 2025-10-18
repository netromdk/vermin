import ast
import io
import sys
import re
from tokenize import generate_tokens, COMMENT, NEWLINE, NL, STRING

# 'type' identifier [type_params] "=" expression
TYPE_ALIAS_STMT = re.compile(r"type\s+(\w+)\s+(\[.+?\]\s+)?=\s+(.+)")

class Parser:
  def __init__(self, source, path=None):
    self.__source = source
    self.__path = "<unknown>" if path is None else path

  def parse(self, parse_comments=True):
    """Parse python source into an AST."""
    node = ast.parse(self.__source, filename=self.__path)
    novermin = set()
    if parse_comments:
      novermin = self.comments()
    return (node, novermin)

  def comments(self):
    """Finds 'novermin' and 'novm' comments and associates to line numbers."""
    novermin = set()
    src = self.__source
    if isinstance(src, bytes):
      src = src.decode(errors="ignore")

    try:
      tokens = generate_tokens(io.StringIO(src).readline)
    except Exception:  # pragma: no cover
      return novermin

    def find_comment(comment, lineno, alone):
      if comment.startswith("novermin") or comment.startswith("novm"):
        # Associate with next line if the comment is "alone" on a line, i.e. '#' starts the line.
        novermin.add(lineno + 1 if alone else lineno)
        return True
      return False

    prev_newline = False
    multiline_string = None
    for token in tokens:
      string, lno, lcol, lend = token.string, token.start[0], token.start[1], token.end[0]

      if token.type == STRING:
        string = string.strip()
        if (string.startswith("\"\"\"") and string.endswith("\"\"\"")) or\
           (string.startswith("'''") and string.endswith("'''")):
          multiline_string = (lno, lend)
      elif token.type == COMMENT:
        # For multi-line strings, any comment marking starts at the beginning and not at the end.
        if multiline_string is not None and multiline_string[1] == lno:
          lno = multiline_string[0]
        multiline_string = None

        # Check each comment segment for "novermin" and "novm", not just the start of the whole
        # comment. A comment is alone on a line if the previous token is a newline or the line
        # column is zero.
        alone = (prev_newline or lcol == 0)
        any(find_comment(segment.strip(), lno, alone)
            for segment in string[1:].strip().split("#"))

      prev_newline = token.type in (NEWLINE, NL)
    return novermin

  def detect(self, config):
    """Parse python source into an AST and yield minimum versions."""
    assert config is not None
    try:
      (node, novermin) = self.parse(config.parse_comments())
      return (node, [], novermin, None)
    except SyntaxError as err:
      def format_error(msg, versions):
        """Generate an error message, as would be done by the SourceVisitor."""
        return config.format()\
          .format_output_line(msg, path=err.filename, line=err.lineno, col=err.offset,
                              versions=versions, violation=True)

      text = err.text.strip() if err.text is not None else ""
      lmsg = err.msg.lower()  # pylint: disable=no-member

      # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
      # NOTE: This is only triggered when running a python 3 on v2 code!
      if lmsg.find("missing parentheses in call to 'print'") != -1:
        msg = "info: `{}` requires 2.0".format(text)
        versions = [(2, 0), None]
        return (None, versions, set(), format_error(msg, versions))

      # Type alias statements.
      # NOTE: This is only triggered with Python 3.11 or older.
      if lmsg == "invalid syntax" and TYPE_ALIAS_STMT.match(text) is not None:
        msg = "info: type alias statement `{}` requires !2, 3.12".format(text)
        versions = [None, (3, 12)]
        return (None, versions, set(), format_error(msg, versions))

      min_versions = [(0, 0), (0, 0)]
      if config.pessimistic():
        min_versions[sys.version_info.major - 2] = None
      msg = "error: {}: {}".format(err.msg, text)
      return (None, min_versions, set(), format_error(msg, min_versions))
