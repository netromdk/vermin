#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import ast
from os.path import abspath, isfile

# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {"argparse": (2.7, 3.2),
            "abc": (2.6, 3.0)}

# Module member requirements: member -> (module, requirements)
MOD_MEM_REQS = {"ABC": ("abc", (None, 3.4))}

V2_DISABLED = False

VERBOSE = False

def parse_source(source):
  """Parse python source into an AST."""
  return ast.parse(source)

def parse_source_file(path):
  """Parse python source file into an AST."""
  with open(path, "r") as fp:
    return parse_source(fp.read())

def vprint(msg):
  global VERBOSE
  if VERBOSE:
    print(msg)

class SourceVisitor(ast.NodeVisitor):
  def __init__(self):
    super(SourceVisitor, self).__init__()
    self.__import = False
    self.__modules = []
    self.__members = []
    self.__printv2 = False
    self.__printv3 = False
    self.__format = False

  def modules(self):
    return self.__modules

  def members(self):
    return self.__members

  def printv2(self):
    return self.__printv2

  def printv3(self):
    return self.__printv3

  def format(self):
    return self.__format

  def __add_module(self, module):
    self.__modules.append(module)

  def __add_member(self, member):
    self.__members.append(member)

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

    # Remember module members and full module paths, like "ABC" member of module "abc" and "abc.ABC"
    # module.
    for name in node.names:
      if name.name is not None:
        self.__add_module(node.module + "." + name.name)
        self.__add_member(name.name)

  def visit_alias(self, node):
    if self.__import:
      self.__add_module(node.name)

      # If the import path has several levels then remember last member, like "ABC" of "abc.ABC".
      elms = node.name.split(".")
      if len(elms) >= 2:
        self.__add_member(elms[-1])

  def visit_Print(self, node):
    self.__printv2 = True

  def visit_Call(self, node):
    if hasattr(node, "func"):
      func = node.func
      if hasattr(func, "id") and func.id == "print":
        self.__printv3 = True
      elif hasattr(func, "attr") and func.attr == "format" and \
           hasattr(func, "value") and isinstance(func.value, ast.Str):
        vprint("`\"..\".format(..)` requires [2.7, 3.0]")
        self.__format = True
    self.generic_visit(node)

  def visit_Load(self, node):
    pass

  def visit_Pass(self, node):
    pass

def combine_versions(list1, list2):
  assert len(list1) == len(list2)
  res = []
  for i in range(len(list1)):
    v1 = list1[i]
    v2 = list2[i]
    if v1 is None and v2 is None:
      res.append(None)
    elif v1 is None:
      res.append(v2)
    elif v2 is None:
      res.append(v1)
    else:
      res.append(max(v1, v2))
  return res

def detect_min_versions_path(path):
  with open(path, "r") as fp:
    return detect_min_versions_source(fp.read())

def detect_min_versions_source(source):
  try:
    node = parse_source(source)
  except SyntaxError as err:
    # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
    # NOTE: This is only triggered when running a python 3 on v2 code!
    if err.msg.lower().find("missing parentheses in call to 'print'") != -1:
      vprint("`{}` requires 2.0".format(err.text.strip()))
      return [2.0, None]
    return [None, None]

  return detect_min_versions(node)

def detect_min_versions(node):
  visitor = SourceVisitor()
  visitor.visit(node)

  mins = [None, None]

  if visitor.printv2():
    mins[0] = 2.0
  if visitor.printv3():
    mins[1] = 3.0

  if visitor.format():
    mins = combine_versions(mins, (2.7, 3.0))

  mods = visitor.modules()
  for mod in mods:
    if mod in MOD_REQS:
      vers = MOD_REQS[mod]
      vprint("'{}' requires {}".format(mod, vers))
      mins = combine_versions(mins, vers)

  mems = visitor.members()
  for mem in mems:
    if mem in MOD_MEM_REQS:
      (mod, vers) = MOD_MEM_REQS[mem]
      vprint("'{}.{}' requires {}".format(mod, mem, vers))
      mins = combine_versions(mins, vers)

      # If the member of the module doesn't support v2 but only v3 then clear the v2 to None.
      # Example: "import abc" requires (2.6, 3.0) and "from abc import ABC" requires 3.4+ so if the
      # latter is used then the v2.6 has to be ignored!
      if vers[0] is None and vers[1] is not None:
        mins[0] = None

        # v2 is disabled globally so other files in same "session" can't change the v2 value
        # requirement.
        global V2_DISABLED
        V2_DISABLED = True

  return mins

def all_none(data):
  for elm in data:
    if elm is not None:
      return False
  return True

def versions_string(vers):
  return ", ".join([str(v) for v in vers if v is not None])

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: {} [-v|--verbose] <python source files..>".format(sys.argv[0]))
    sys.exit(-1)

  path_pos = 1
  arg1 = sys.argv[1].lower()
  if arg1 == "-v" or arg1 == "--verbose":
    VERBOSE = True
    path_pos += 1

  paths = sys.argv[path_pos:]

  mins = [None, None]
  for path in paths:
    path = abspath(path)
    if not isfile(path):
      continue
    if not path.lower().endswith(".py"):
      continue
    min_versions = detect_min_versions_path(path)
    if not all_none(min_versions):
      print("{:<12} {}".format(versions_string(min_versions), path))
      mins = combine_versions(mins, min_versions)

  if V2_DISABLED:
    mins[0] = None

  if all_none(mins):
    print("Could not determine minimum required versions!")
  else:
    print("\nMinimum required versions: {}".format(versions_string(mins)))
