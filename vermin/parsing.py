import ast

from .printing import vvprint

def parse_source(source, path=None):
  """Parse python source into an AST."""
  path = "<unknown>" if path is None else path
  return ast.parse(source, filename=path)

def parse_detect_source(source, path=None):
  try:
    return (parse_source(source, path=path), [])
  except SyntaxError as err:
    text = err.text.strip() if err.text is not None else ""
    # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
    # NOTE: This is only triggered when running a python 3 on v2 code!
    if err.msg.lower().find("missing parentheses in call to 'print'") != -1:
      vvprint("`{}` requires 2.0".format(text))
      return (None, [2.0, None])
    else:
      vvprint("{}: {}".format(err, text))
  return (None, [0, 0])
