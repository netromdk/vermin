import ast
import re

from .printing import vvprint

RE_COMMENT = re.compile(".*(#)(.+)", re.IGNORECASE)

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
    lineno = 0
    novermin = set()
    src = self.__source
    if isinstance(src, bytes):
      src = src.decode(errors="ignore")
    for line in src.splitlines():
      lineno += 1
      line = line.strip()
      m = RE_COMMENT.match(line)
      if m is not None:
        comment = m.group(2).strip()
        if comment == "novermin" or comment == "novm":
          # Ignore if it is inside another comment, like: `# test: # novm`
          if m.start(0) < m.start(1) and m.group(0).strip().startswith("#"):
            continue
          # Associate with next line if the comment is "alone" on a line, i.e. '#' starts the line.
          novermin.add(lineno + 1 if m.start(1) == 0 else lineno)
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
