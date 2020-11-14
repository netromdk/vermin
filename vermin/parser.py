import ast
import io
import sys
from tokenize import generate_tokens, COMMENT, NEWLINE, NL

from .printing import vvprint
from .utility import version_strings

class Parser:
  def __init__(self, source, path=None):
    self.__source = source
    self.__path = "<unknown>" if path is None else path

  def parse(self):
    """Parse python source into an AST."""
    node = ast.parse(self.__source, filename=self.__path)
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
    for token in tokens:
      # <3.0: tuple instance.
      # 3.0+: TokenInfo instance.
      is_tuple = (type(token) == tuple)
      typ = token[0] if is_tuple else token.type

      if typ == COMMENT:
        if is_tuple:  # pragma: no cover
          comment, lineno, linecol = token[1], token[2][0], token[2][1]
        else:
          comment, lineno, linecol = token.string, token.start[0], token.start[1]

        # Check each comment segment for "novermin" and "novm", not just the start of the whole
        # comment. A comment is alone on a line if the previous token is a newline or the line
        # column is zero.
        alone = (prev_newline or linecol == 0)
        any(find_comment(segment.strip(), lineno, alone)
            for segment in comment[1:].strip().split("#"))

      prev_newline = typ in (NEWLINE, NL)
    return novermin

  def detect(self, config):
    """Parse python source into an AST and yield minimum versions."""
    assert(config is not None)
    try:
      (node, novermin) = self.parse()
      return (node, [], novermin)
    except SyntaxError as err:
      text = err.text.strip() if err.text is not None else ""
      lmsg = err.msg.lower()  # pylint: disable=no-member
      parsable = (config.format().name() == "parsable")
      if parsable:
        text = text.replace("\n", "\\n")

      # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
      # NOTE: This is only triggered when running a python 3 on v2 code!
      if lmsg.find("missing parentheses in call to 'print'") != -1:
        versions = "2.0:!3:" if parsable else ""
        vvprint("{}:{}:{}:{}info: `{}` requires 2.0".
                format(err.filename, err.lineno, err.offset, versions, text), config)
        return (None, [(2, 0), None], set())

      min_versions = [(0, 0), (0, 0)]
      if config.pessimistic():
        min_versions[sys.version_info.major - 2] = None
      versions = version_strings(min_versions) + ":" if parsable else ""
      vvprint("{}:{}:{}:{}error: {}: {}".
              format(err.filename, err.lineno, err.offset, versions, err.msg, text), config)
    return (None, min_versions, set())
