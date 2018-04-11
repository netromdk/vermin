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
    if ver == 0:
      continue
    if ver is None:
      res.append("!{}".format(i + 2))
    else:
      res.append(str(ver))
  return ", ".join(res)

def process_path(args):
  (path, config) = args
  node = None
  mins = None
  text = ""
  with open(path, mode="rb") as fp:
    try:
      (node, mins) = parse_detect_source(fp.read(), path=path)
    except KeyboardInterrupt:
      return (path, mins, text)
    except Exception as ex:
      text = "{}: {}, {}".format(path, type(ex), ex)
      mins = [0, 0]

  if node is None:
    return (path, mins, text)

  visitor = SourceVisitor(config)

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

  for (path, min_versions, text) in pool.imap(process_path, ((path, config) for path in paths)):
    if min_versions is None:
      incomp = True
      print_incomp(path)
      continue

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
  return (mins, incomp)
