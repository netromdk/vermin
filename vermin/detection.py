from os import listdir
from os.path import abspath, isfile, isdir, join

def probably_python_file(path):
  if not isfile(path):
    return False

  pl = path.lower()
  if pl.endswith(".pyc"):
    return False
  if pl.endswith(".py") or pl.endswith(".pyw"):
    return True

  # Try opening file for reading as a text device.
  try:
    with open(path, mode="rt") as fp:
      for i in range(10):
        # A script with a magic line might contain "python".
        line = fp.readline().lower()
        if "python" in line:
          return True
  except Exception:
    # Not python if not readable text file.
    return False

  return False

# Some detected paths might not be python code since not all files use ".py" and ".pyw". But try
# directly specified files on CLI, on depth 0, in any case (non-pyhton files will be ignored when
# trying to parse them).
def detect_paths(paths, hidden=False, depth=0):
  accept_paths = []
  for path in paths:
    if not hidden and path != "." and path[0] == ".":
      continue
    path = abspath(path)
    if isdir(path):
      files = [join(path, p) for p in listdir(path) if hidden or p[0] != "."]
      accept_paths += detect_paths(files, hidden, depth + 1)
    elif isfile(path) and (depth == 0 or probably_python_file(path)):
      accept_paths.append(path)
  return accept_paths
