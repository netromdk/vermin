#!/usr/bin/env python

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
  "PathLike": ("os", (None, 3.6)),
  "terminal_size": ("os", (None, 3.3)),

  # Functions
  "commonpath": ("os.path", (None, 3.5)),
  "exc_clear": ("sys", (2.3, None)),
  "fsdecode": ("os", (None, 3.2)),
  "fsencode": ("os", (None, 3.2)),
  "fspath": ("os", (None, 3.6)),
  "get_blocking": ("os", (None, 3.5)),
  "get_exec_path": ("os", (None, 3.2)),
  "get_handle_inheritable": ("os", (None, 3.4)),
  "get_inheritable": ("os", (None, 3.4)),
  "get_terminal_size": ("os", (None, 3.3)),
  "getcheckinterval": ("sys", (2.3, 3.0)),
  "getctime": ("os.path", (2.3, 3.0)),
  "getdefaultencoding": ("sys", (2.0, 3.0)),
  "getdlopenflags": ("sys", (2.2, 3.0)),
  "getenvb": ("os", (None, 3.2)),
  "getfilesystemencoding": ("sys", (2.3, 3.0)),
  "getgrouplist": ("os", (None, 3.3)),
  "getpgid": ("os", (2.3, 3.0)),
  "getpriority": ("os", (None, 3.3)),
  "getprofile": ("sys", (2.6, 3.0)),
  "getresgid": ("os", (2.7, 3.0)),
  "getresuid": ("os", (2.7, 3.0)),
  "getsid": ("os", (2.4, 3.0)),
  "getsizeof": ("sys", (2.6, 3.0)),
  "gettrace": ("sys", (2.6, 3.0)),
  "getwindowsversion": ("sys", (2.3, 3.0)),
  "initgroups": ("os", (2.7, 3.2)),
  "ismount": ("os.path", (None, 3.4)),
  "lexists": ("os.path", (2.4, 3.0)),
  "lockf": ("os", (None, 3.3)),
  "pipe2": ("os", (None, 3.3)),
  "posix_fadvise": ("os", (None, 3.3)),
  "posix_fallocate": ("os", (None, 3.3)),
  "pread": ("os", (None, 3.3)),
  "pwrite": ("os", (None, 3.3)),
  "readv": ("os", (None, 3.3)),
  "realpath": ("os.path", (2.6, 3.0)),
  "sendfile": ("os", (None, 3.3)),
  "set_blocking": ("os", (None, 3.5)),
  "set_handle_inheritable": ("os", (None, 3.4)),
  "set_inheritable": ("os", (None, 3.4)),
  "setgroups": ("os", (2.2, 3.0)),
  "setpriority": ("os", (None, 3.3)),
  "setresgid": ("os", (2.7, 3.2)),
  "setresuid": ("os", (2.7, 3.2)),
  "writev": ("os", (None, 3.3)),

  # Variables and Constants
  "F_LOCK": ("os", (None, 3.3)),
  "F_TEST": ("os", (None, 3.3)),
  "F_TLOCK": ("os", (None, 3.3)),
  "F_ULOCK": ("os", (None, 3.3)),
  "O_CLOEXEC": ("os", (None, 3.3)),
  "O_PATH": ("os", (None, 3.4)),
  "O_TMPFILE": ("os", (None, 3.4)),
  "POSIX_FADV_DONTNEED": ("os", (None, 3.3)),
  "POSIX_FADV_NOREUSE": ("os", (None, 3.3)),
  "POSIX_FADV_NORMAL": ("os", (None, 3.3)),
  "POSIX_FADV_RANDOM": ("os", (None, 3.3)),
  "POSIX_FADV_SEQUENTIAL": ("os", (None, 3.3)),
  "POSIX_FADV_WILLNEED": ("os", (None, 3.3)),
  "PRIO_PGRP": ("os", (None, 3.3)),
  "PRIO_PROCESS": ("os", (None, 3.3)),
  "PRIO_USER": ("os", (None, 3.3)),
  "SF_MNOWAIT": ("os", (None, 3.3)),
  "SF_NODISKIO": ("os", (None, 3.3)),
  "SF_SYNC": ("os", (None, 3.3)),
  "api_version": ("sys", (2.3, 3.0)),
  "environb": ("os", (None, 3.2)),
  "flags": ("sys", (2.6, 3.0)),
  "float_info": ("sys", (2.6, 3.0)),
  "float_repr_style": ("sys", (2.7, 3.0)),
  "long_info": ("sys", (2.7, None)),
  "py3kwarning": ("sys", (2.6, None)),
  "subversion": ("sys", (2.5, None)),
  "supports_bytes_environ": ("os", (None, 3.2)),
  "supports_unicode_filenames": ("os.path", (2.3, 3.0)),
  "version_info": ("sys", (2.0, 3.0)),
}

# Keyword arguments requirements: (function, keyword argument) -> requirements
KWARGS_REQS = {
  ("access", "dir_fd"): (None, 3.3),  # os
  ("access", "effective_ids"): (None, 3.3),  # os
  ("access", "follow_symlinks"): (None, 3.3),  # os
  ("chflags", "follow_symlinks"): (None, 3.3),  # os
  ("chmod", "dir_fd"): (None, 3.3),  # os
  ("chmod", "follow_symlinks"): (None, 3.3),  # os
  ("chown", "dir_fd"): (None, 3.3),  # os
  ("chown", "follow_symlinks"): (None, 3.3),  # os
  ("dup2", "inheritable"): (None, 3.4),  # os
  ("link", "dst_dir_fd"): (None, 3.3),  # os
  ("link", "follow_symlinks"): (None, 3.3),  # os
  ("link", "src_dir_fd"): (None, 3.3),  # os
  ("open", "dir_fd"): (None, 3.3),  # os
}

VERBOSE = 0
PRINT_VISITS = False

def parse_source(source):
  """Parse python source into an AST."""
  return ast.parse(source)

def verbose_print(msg, level):
  global VERBOSE
  if VERBOSE == level:
    print(msg)

def vprint(msg):
  verbose_print(msg, 1)

def vvprint(msg):
  verbose_print(msg, 2)

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
    self.__function_name = None
    self.__kwargs = []

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

  def kwargs(self):
    return self.__kwargs

  def __add_module(self, module):
    self.__modules.append(module)

  def __add_member(self, member):
    self.__members.append(member)

  def __add_star_import(self, module):
    self.__star_imports.append(module)

  def __add_kwargs(self, function, keyword):
    self.__kwargs.append((function, keyword))

  def generic_visit(self, node):
    if PRINT_VISITS:
      print("{}: {}".format(type(node).__name__, ast.dump(node)))
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
      if hasattr(func, "id"):
        self.__function_name = func.id
        if func.id == "print":
          self.__printv3 = True
      elif hasattr(func, "attr") and func.attr == "format" and \
           hasattr(func, "value") and isinstance(func.value, ast.Str):
        vvprint("`\"..\".format(..)` requires [2.7, 3.0]")
        self.__format = True
    self.generic_visit(node)
    self.__function_name = None

  def visit_Attribute(self, node):
    # When a function is called like "os.path.ismount(..)" it is an attribute list where the "first"
    # (this one) is the function name. Stop visiting here.
    if hasattr(node, "attr"):
      self.__function_name = node.attr

      # Also add as a possible module member, like `B` in `class A(B)`.
      self.__add_member(node.attr)

  def visit_keyword(self, node):
    if self.__function_name is not None:
      self.__add_kwargs(self.__function_name, node.arg)

  def visit_Load(self, node):
    pass

  def visit_Pass(self, node):
    pass

class InvalidVersionException(BaseException):
  pass

def combine_versions(list1, list2):
  assert len(list1) == len(list2)
  assert len(list1) == 2
  if (list1[0] is None and list1[1] is not None and list2[0] is not None and list2[1] is None) or\
     (list1[0] is not None and list1[1] is None and list2[0] is None and list2[1] is not None):
    raise InvalidVersionException("Versions could not be combined: {} and {}".format(list1, list2))
  res = []
  for i in range(len(list1)):
    v1 = list1[i]
    v2 = list2[i]
    if v1 is 0 and v2 is 0:
      res.append(0)
    elif v1 is 0:
      res.append(v2)
    elif v2 is 0:
      res.append(v1)
    elif v1 is None or v2 is None:
      res.append(None)
    else:
      res.append(max(v1, v2))
  return res

def detect_min_versions_path(path):
  with open(path, "r") as fp:
    try:
      return detect_min_versions_source(fp.read())
    except Exception as ex:
      print("{}: {}".format(path, ex))
      return [0, 0]

def parse_detect_source(source):
  try:
    return (parse_source(source), [])
  except SyntaxError as err:
    # `print expr` is a Python 2 construct, in v3 it's `print(expr)`.
    # NOTE: This is only triggered when running a python 3 on v2 code!
    if err.msg.lower().find("missing parentheses in call to 'print'") != -1:
      vvprint("`{}` requires 2.0".format(err.text.strip()))
      return (None, [2.0, None])
    return (None, [0, 0])

def detect_min_versions_source(source):
  (node, mins) = parse_detect_source(source)
  if node is None:
    return mins
  return detect_min_versions(node)

def detect_min_versions(node):
  visitor = SourceVisitor()
  visitor.visit(node)

  mins = [0, 0]

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
      vvprint("'{}' requires {}".format(mod, vers))
      mins = combine_versions(mins, vers)

  mems = visitor.members()
  for mem in mems:
    if mem in MOD_MEM_REQS:
      (mod, vers) = MOD_MEM_REQS[mem]
      vvprint("'{}.{}' requires {}".format(mod, mem, vers))
      mins = combine_versions(mins, vers)

  kwargs = visitor.kwargs()
  for fn_kw in kwargs:
    if fn_kw in KWARGS_REQS:
      vers = KWARGS_REQS[fn_kw]
      mins = combine_versions(mins, vers)

  return mins

def all_none(elms):
  return len(elms) == elms.count(None)

def versions_string(vers):
  return ", ".join([str(v) for v in vers if v is not None and v is not 0])

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
  try:
    mins = detect_min_versions_path(path)
  except InvalidVersionException as ex:
    mins = None
    vprint(ex)
  return (path, mins)

def process_paths(paths):
  pool = Pool()
  mins = [0, 0]
  incomp = False

  def print_incomp(path):
    print("File with incompatible versions: {}".format(path))

  for (path, min_versions) in pool.imap(process_path, paths):
    if min_versions is None:
      incomp = True
      print_incomp(path)
      continue
    vprint("{:<12} {}".format(versions_string(min_versions), path))
    try:
      mins = combine_versions(mins, min_versions)
    except InvalidVersionException as ex:
      incomp = True
      print_incomp(path)
  return (mins, incomp)

def unknown_versions(vers):
  """Versions are unknown if all values are either 0 or None."""
  return len(vers) == vers.count(0) + vers.count(None)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: {} [-v..] <python source files and folders..>".format(sys.argv[0]))
    print("  -v..    Verbosity level 1 to 2. -v shows less than -vv but more than no verbosity.")
    sys.exit(-1)

  path_pos = 1
  arg1 = sys.argv[1].lower()
  if arg1.startswith("-v"):
    VERBOSE = arg1.count("v")
    path_pos += 1

  print("Detecting python files..", end=" ")
  sys.stdout.flush()
  paths = detect_paths(sys.argv[path_pos:])
  print(len(paths))

  (mins, incomp) = process_paths(paths)

  if incomp:
    print("Note: Some files had incompatible versions so the results might not be correct!")

  if unknown_versions(mins):
    print("Could not determine minimum required versions!")
  else:
    print("Minimum required versions: {}".format(versions_string(mins)))
