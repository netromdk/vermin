import ast
import io
from tokenize import generate_tokens, COMMENT

from .printing import vvprint

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
      def only_comments(token):
        return token[0] == COMMENT if type(token) == tuple else token.type == COMMENT
      tokens = filter(only_comments, generate_tokens(io.StringIO(src).readline))
    except Exception:  # pragma: no cover
      return novermin

    def find_comment(comment, lineno, linecol):
      if comment.startswith("novermin") or comment.startswith("novm"):
        # Associate with next line if the comment is "alone" on a line, i.e. '#' starts the line.
        novermin.add(lineno + 1 if linecol == 0 else lineno)
        return True
      return False

    for token in tokens:
      # <3.0: tuple instance.
      if type(token) == tuple:  # pragma: no cover
        comment, lineno, linecol = token[1], token[2][0], token[2][1]

      # 3.0+: TokenInfo instance.
      else:
        comment, lineno, linecol = token.string, token.start[0], token.start[1]

      # Check each comment segment for "novermin" and "novm", not just the start of the whole
      # comment.
      any(find_comment(segment.strip(), lineno, linecol)
          for segment in comment[1:].strip().split("#"))
    return novermin

  def detect(self):
    """Parse python source into an AST and yield minimum versions."""
    try:
      (node, novermin) = self.parse()
      return (node, [], novermin)
    except SyntaxError as err:
      text = err.text.strip() if err.text is not None else ""
      # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
      # NOTE: This is only triggered when running a python 3 on v2 code!
      if err.msg.lower().find("missing parentheses in call to 'print'") != -1:
        vvprint("{}:{}:{}: info: `{}` requires 2.0".
                format(err.filename, err.lineno, err.offset, text))
        return (None, [(2, 0), None], set())
      else:
        vvprint("{}:{}:{}: error: {}: {}".
                format(err.filename, err.lineno, err.offset, err.msg, text))
    return (None, [(0, 0), (0, 0)], set())
