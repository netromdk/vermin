from multiprocessing import Pool

from .printing import nprint, vprint
from .detection import detect_min_versions_path, combine_versions, InvalidVersionException
from .config import Config

def versions_string(vers):
  res = []
  for i in range(len(vers)):
    ver = vers[i]
    if ver == 0:
      continue
    if ver is None:
      res.append("!{}".format(i + 2))
    else:
      res.append(str(ver))
  return ", ".join(res)

def process_path(path):
  try:
    mins = detect_min_versions_path(path)
  except InvalidVersionException as ex:
    mins = None
    vprint(ex)
  return (path, mins)

def process_paths(paths, processes):
  pool = Pool(processes=processes)
  mins = [0, 0]
  incomp = False

  def print_incomp(path):
    if not Config.get().ignore_incomp():
      nprint("File with incompatible versions: {}".format(path))

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
