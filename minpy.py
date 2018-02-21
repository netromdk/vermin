#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import ast
from os.path import abspath, isfile

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

  def __add_module(self, module):
    self.__modules.append(module)

  def generic_visit(self, node):
    #print("{}: {}".format(type(node).__name__, ast.dump(node)))
    super(SourceVisitor, self).generic_visit(node)

  def visit_Import(self, node):
    self.__import = True
    self.generic_visit(node)
    self.__import = False

  def visit_ImportFrom(self, node):
    if node.module is None:
      return

    self.__add_module(node.module)

    # Remember full module paths, like "abc.ABC" via "from abc import ABC".
    for name in node.names:
      if name.name is not None:
        self.__add_module(node.module + "." + name.name)

  def visit_alias(self, node):
    if self.__import:
      self.__add_module(node.name)

  def visit_Load(self, node):
    pass

  def visit_Pass(self, node):
    pass

# TODO: Detect version from language use, like "print expr" (2) vs "print(expr)" (3)

def detect_min_versions_path(path):
  try:
    node = parse_source_file(path)
  except SyntaxError as err:
    print("Could not parse input: {}".format(err))
    sys.exit(-1)

  return detect_min_versions(node)

def detect_min_versions(node):
  visitor = SourceVisitor()
  visitor.visit(node)

  mins = [None, None]
  mods = visitor.modules()
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

  # Return non-None values.
  return [ver for ver in mins if ver is not None]

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: {} <python source files..>".format(sys.argv[0]))
    sys.exit(-1)

  for path in sys.argv[1:]:
    path = abspath(path)
    if not isfile(path):
      continue
    if not path.lower().endswith(".py"):
      continue
    print("{}:".format(path))
    min_versions = detect_min_versions_path(path)
    if len(min_versions) > 0:
      print(min_versions)
