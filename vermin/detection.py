from os import listdir
from os.path import abspath, isfile, isdir, join

from .parsing import parse_detect_source
from .rules import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS
from .source_visitor import SourceVisitor
from .config import Config
from .printing import nprint, vvprint

class InvalidVersionException(BaseException):
  pass

def combine_versions(list1, list2):
  assert len(list1) == len(list2)
  assert len(list1) == 2
  if not Config.get().ignore_incomp() and\
    ((list1[0] is None and list1[1] is not None and list2[0] is not None and list2[1] is None) or
     (list1[0] is not None and list1[1] is None and list2[0] is None and list2[1] is not None)):
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
  with open(path, mode="rb") as fp:
    try:
      return detect_min_versions_source(fp.read(), path=path)
    except Exception as ex:
      nprint("{}: {}".format(path, ex))
      return [0, 0]

def detect_min_versions_source(source, path=None):
  (node, mins) = parse_detect_source(source, path)
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
    mins = combine_versions(mins, (2.0, 3.0))

  if visitor.format():
    mins = combine_versions(mins, (2.7, 3.0))

  if visitor.longv2():
    mins = combine_versions(mins, (2.0, None))

  if visitor.bytesv3():
    mins[1] = 3.0

  if visitor.fstrings():
    mins = combine_versions(mins, (None, 3.6))

  for directive in visitor.strftime_directives():
    if directive in STRFTIME_REQS:
      vers = STRFTIME_REQS[directive]
      vvprint("strftime directive '{}' requires {}".format(directive, vers))
      mins = combine_versions(mins, vers)

  mods = visitor.modules()
  for mod in mods:
    if mod in MOD_REQS:
      vers = MOD_REQS[mod]
      vvprint("'{}' requires {}".format(mod, vers))
      mins = combine_versions(mins, vers)

  mems = visitor.members()
  for mem in mems:
    if mem in MOD_MEM_REQS:
      for (mod, vers) in MOD_MEM_REQS[mem]:
        # Only consider if module has been visited.
        if mod in mods:
          vvprint("'{}.{}' requires {}".format(mod, mem, vers))
          mins = combine_versions(mins, vers)

  kwargs = visitor.kwargs()
  for fn_kw in kwargs:
    if fn_kw in KWARGS_REQS:
      vers = KWARGS_REQS[fn_kw]
      vvprint("'{}' requires {}".format(fn_kw, vers))
      mins = combine_versions(mins, vers)

  return mins

def detect_paths(paths):
  accept_paths = []
  for path in paths:
    path = abspath(path)
    if isdir(path):
      try:
        accept_paths += detect_paths([join(path, p) for p in listdir(path)])
      except PermissionError as ex:
        nprint("Ignoring {}: {}".format(path, ex))
      continue
    if not isfile(path) or not path.lower().endswith(".py"):
      continue
    accept_paths.append(path)
  return accept_paths
