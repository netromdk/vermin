from os import listdir
from os.path import abspath, isfile, isdir, join

from .printing import nprint

def detect_paths(paths, hidden=False):
  accept_paths = []
  for path in paths:
    if not hidden and path != "." and path[0] == ".":
      continue
    path = abspath(path)
    if isdir(path):
      try:
        files = [join(path, p) for p in listdir(path) if hidden or p[0] != "."]
        accept_paths += detect_paths(files)
      except OSError as ex:
        nprint("Ignoring {}: {}".format(path, ex))
      continue
    if not isfile(path) or (not path.lower().endswith(".py") and not path.lower().endswith(".pyw")):
      continue
    accept_paths.append(path)
  return accept_paths
