from multiprocessing import Pool

from .printing import nprint, vprint
from .config import Config
from .utility import combine_versions, InvalidVersionException
from .parsing import parse_detect_source
from .source_visitor import SourceVisitor

def versions_string(vers):
  res = []
  for i in range(len(vers)):
    ver = vers[i]
    # When versions aren't known, show something instead of nothing. It might run with any version.
    if ver == 0:
      res.append("~{}".format(i + 2))
    elif ver is None:
      res.append("!{}".format(i + 2))
    else:
      res.append(str(ver))
  return ", ".join(res)

def process_path(args):
  (path, config) = args
  node = None
  mins = None
  text = ""
  novermin = set()
  with open(path, mode="rb") as fp:
    try:
      (node, mins, novermin) = parse_detect_source(fp.read(), path=path)
    except KeyboardInterrupt:
      return (path, mins, text)
    except Exception as ex:
      text = "{}: {}, {}".format(path, type(ex), ex)
      mins = [0, 0]

  if node is None:
    return (path, mins, text)

  visitor = SourceVisitor(config)
  visitor.set_no_lines(novermin)

  try:
    visitor.visit(node)
  except KeyboardInterrupt:
    return (path, mins, text)

  try:
    mins = visitor.minimum_versions()
    text = visitor.output_text()
  except InvalidVersionException as ex:
    mins = None
    text = str(ex)

  return (path, mins, text)

def process_paths(paths, processes):
  pool = Pool(processes=processes)
  mins = [0, 0]
  incomp = False
  config = Config.get()

  def print_incomp(path):
    if not config.ignore_incomp():
      nprint("File with incompatible versions: {}".format(path))

  unique_versions = set()
  for (path, min_versions, text) in pool.imap(process_path, ((path, config) for path in paths)):
    if min_versions is None:
      incomp = True
      print_incomp(path)
      continue

    for ver in min_versions:
      if ver is not None and ver > 0:
        unique_versions.add(ver)

    # Indent subtext.
    subtext = ""
    if len(text) > 0:
      # Keep newlines and throw away dups.
      lines = list(set(text.splitlines(True)))
      lines.sort()
      subtext = "\n  " + "  ".join(lines)
      if not subtext.endswith("\n"):
        subtext += "\n"

    vprint("{:<12} {}{}".format(versions_string(min_versions), path, subtext))
    try:
      mins = combine_versions(mins, min_versions)
    except InvalidVersionException:
      incomp = True
      print_incomp(path)

  pool.close()

  unique_versions = list(unique_versions)
  unique_versions.sort()
  return (mins, incomp, unique_versions)
