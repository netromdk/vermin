#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import ast
from os import listdir
from os.path import abspath, isfile, isdir, join
from multiprocessing import Pool

# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {
  "ConfigParser": (2.0, None),
  "HTMLParser": (2.2, None),
  "Queue": (2.0, None),
  "SocketServer": (2.0, None),
  "__builtin__": (2.0, None),
  "_markupbase": (None, 3.0),
  "_winreg": (2.0, None),
  "abc": (2.6, 3.0),
  "argparse": (2.7, 3.2),
  "ast": (2.6, 3.0),
  "builtins": (None, 3.0),
  "configparser": (None, 3.0),
  "copy_reg": (2.0, None),
  "copyreg": (None, 3.0),
  "dbm.io": (None, 3.0),
  "dbm.ndbm": (None, 3.0),
  "dbm.os": (None, 3.0),
  "dbm.struct": (None, 3.0),
  "dbm.sys": (None, 3.0),
  "dbm.whichdb": (None, 3.0),
  "html": (None, 3.0),
  "htmlentitydefs": (2.0, None),
  "http": (None, 3.0),
  "markupbase": (2.0, None),
  "md5": (2.0, None),
  "multiprocessing": (2.6, 3.0),
  "new": (2.0, None),
  "queue": (None, 3.0),
  "repr": (2.0, None),
  "reprlib": (None, 3.0),
  "sets": (2.0, None),
  "socketserver": (None, 3.0),
  "string.letters": (2.0, None),
  "string.lowercase": (2.0, None),
  "string.uppercase": (2.0, None),
  "tkinter": (None, 3.0),
  "urllib2": (2.0, None),
  "winreg": (None, 3.0),
  "xmlrpc": (None, 3.0),
}

# Module member requirements: member -> (module, requirements)
MOD_MEM_REQS = {
  # Classes
  "ABC": ("abc", (None, 3.4)),

  # Functions
  "commonpath": ("os.path", (None, 3.5)),
  "exc_clear": ("sys", (2.3, None)),
  "getcheckinterval": ("sys", (2.3, 3.0)),
  "getctime": ("os.path", (2.3, 3.0)),
  "getdefaultencoding": ("sys", (2.0, 3.0)),
  "getdlopenflags": ("sys", (2.2, 3.0)),
  "getfilesystemencoding": ("sys", (2.3, 3.0)),
  "getpgid": ("os", (2.3, 3.0)),
  "getprofile": ("sys", (2.6, 3.0)),
  "getresgid": ("os", (2.7, 3.0)),
  "getresuid": ("os", (2.7, 3.0)),
  "getsid": ("os", (2.4, 3.0)),
  "getsizeof": ("sys", (2.6, 3.0)),
  "gettrace": ("sys", (2.6, 3.0)),
  "getwindowsversion": ("sys", (2.3, 3.0)),
  "initgroups": ("os", (2.7, 3.0)),
  "ismount": ("os.path", (None, 3.4)),
  "lexists": ("os.path", (2.4, 3.0)),
  "realpath": ("os.path", (2.6, 3.0)),
  "setgroups": ("os", (2.2, 3.0)),
  "setresgid": ("os", (2.7, 3.0)),
  "setresuid": ("os", (2.7, 3.0)),

  # Variables
  "flags": ("sys", (2.6, 3.0)),
  "supports_unicode_filenames": ("os.path", (2.3, 3.0)),
}

V2_DISABLED = False
V3_DISABLED = False

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
    self.__star_imports = []

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

  def __add_star_import(self, module):
    self.__star_imports.append(module)

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
      if name.name == "*":
        self.__add_star_import(node.module)
      elif name.name is not None:
        self.__add_module(node.module + "." + name.name)
        self.__add_member(name.name)

  def visit_alias(self, node):
    if self.__import:
      self.__add_module(node.name)

      # If the import path has several levels then remember last member, like "ABC" of "abc.ABC".
      elms = node.name.split(".")
      if len(elms) >= 2:
        self.__add_member(elms[-1])

  def visit_Name(self, node):
    # In the case of star imports it checks if the member is in one of such star imports before
    # adding as member.
    if len(self.__star_imports) > 0:
      if node.id in MOD_MEM_REQS:
        (mod, vers) = MOD_MEM_REQS[node.id]
        if mod in self.__star_imports:
          self.__add_member(node.id)

  def visit_Print(self, node):
    self.__printv2 = True
    self.generic_visit(node)

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

  global V2_DISABLED
  global V3_DISABLED

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
        V2_DISABLED = True

      # Same for v3 when v2 only.
      if vers[0] is not None and vers[1] is None:
        mins[1] = None
        V3_DISABLED = True

  return mins

def all_none(elms):
  return len(elms) == elms.count(None)

def versions_string(vers):
  return ", ".join([str(v) for v in vers if v is not None])

def detect_paths(paths):
  accept_paths = []
  for path in paths:
    path = abspath(path)
    if isdir(path):
      accept_paths += detect_paths([join(path, p) for p in listdir(path)])
      continue
    if not isfile(path) or not path.lower().endswith(".py"):
      continue
    accept_paths.append(path)
  return accept_paths

def process_path(path):
  return (path, detect_min_versions_path(path))

def process_paths(paths):
  pool = Pool()
  mins = [None, None]
  for (path, min_versions) in pool.imap(process_path, paths):
    if not all_none(min_versions):
      print("{:<12} {}".format(versions_string(min_versions), path))
      mins = combine_versions(mins, min_versions)
  return mins

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: {} [-v|--verbose] <python source files and folders..>".format(sys.argv[0]))
    sys.exit(-1)

  path_pos = 1
  arg1 = sys.argv[1].lower()
  if arg1 == "-v" or arg1 == "--verbose":
    VERBOSE = True
    path_pos += 1

  paths = detect_paths(sys.argv[path_pos:])
  mins = process_paths(paths)

  if V2_DISABLED:
    mins[0] = None
  if V3_DISABLED:
    mins[1] = None

  if all_none(mins):
    print("Could not determine minimum required versions!")
  else:
    print("Minimum required versions: {}".format(versions_string(mins)))
