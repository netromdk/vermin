from os import listdir
from os.path import abspath, isfile, isdir, join

from .parsing import parse_detect_source
from .source_visitor import SourceVisitor
from .printing import nprint

def detect_min_versions_source(source, path=None):
  (node, mins) = parse_detect_source(source, path)
  if node is None:
    return mins
  return detect_min_versions(node)

def detect_min_versions(node):
  visitor = SourceVisitor()
  visitor.visit(node)
  return visitor.minimum_versions()

def detect_paths(paths):
  accept_paths = []
  for path in paths:
    path = abspath(path)
    if isdir(path):
      try:
        accept_paths += detect_paths([join(path, p) for p in listdir(path)])
      except OSError as ex:
        nprint("Ignoring {}: {}".format(path, ex))
      continue
    if not isfile(path) or (not path.lower().endswith(".py") and not path.lower().endswith(".pyw")):
      continue
    accept_paths.append(path)
  return accept_paths
