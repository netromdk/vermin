#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import ast

# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {"argparse": (2.7, 3.2)}

def parse_source(source):
  """Parse python source into an AST."""
  return ast.parse(source)

def parse_source_file(path):
  """Parse python source file into an AST."""
  with open(path, "r") as fp:
    return parse_source(fp.read())

class SourceVisitor(ast.NodeVisitor):
  def __init__(self):
    super(SourceVisitor, self).__init__()
    self.__import = False
    self.__modules = []

  def modules(self):
    return self.__modules

  def generic_visit(self, node):
    #print("{}: {}".format(type(node).__name__, ast.dump(node)))
    ast.NodeVisitor.generic_visit(self, node)

  def visit_Import(self, node):
    self.__import = True
    ast.NodeVisitor.generic_visit(self, node)
    self.__import = False

  def visit_ImportFrom(self, node):
    self.__modules.append(node.module)

  def visit_alias(self, node):
    if self.__import:
      self.__modules.append(node.name)

  def visit_Load(self, node):
    pass

  def visit_Pass(self, node):
    pass

# TODO: Detect version from language use, like "print expr" (2) vs "print(expr)" (3)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: {} <python source file>".format(sys.argv[0]))
    sys.exit(-1)

  path = sys.argv[1]
  try:
    node = parse_source_file(path)
  except SyntaxError as err:
    print("Could not parse input: {}".format(err))

  visitor = SourceVisitor()
  visitor.visit(node)

  mins = [None, None]
  mods = visitor.modules()
  print("Modules: {}".format(mods))
  for mod in mods:
    if mod in MOD_REQS:
      vers = MOD_REQS[mod]
      print("'{}' requires {}".format(mod, vers))
      for i in range(len(vers)):
        if vers[i] is None:
          continue
        if mins[i] is None:
          mins[i] = vers[i]
        else:
          mins[i] = min(vers[i], mins[i])

  actual_mins = [ver for ver in mins if ver is not None]
  if len(actual_mins) > 0:
    print("Minimum versions detected: {}".format(actual_mins))
  else:
    print("No specific minimum version detected.")
