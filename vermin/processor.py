from multiprocessing import Pool, cpu_count

from .printing import nprint, vprint
from .config import Config
from .utility import combine_versions, InvalidVersionException
from .parser import Parser
from .source_visitor import SourceVisitor

# NOTE: This function isn't in the Processor class because Python 2's multiprocessing.pool doesn't
# like it being an instance method:
#
# File "vermin/vermin/processor.py", line 36, in process
#   pool.imap(self.process_individual, ((path, config) for path in paths)):
# File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/
#       multiprocessing/pool.py", line 673, in next
#   raise value
# PicklingError:
#   Can't pickle <type 'instancemethod'>: attribute lookup __builtin__.instancemethod failed
def process_individual(args):
  (path, config) = args
  node = None
  mins = None
  text = ""
  novermin = set()
  with open(path, mode="rb") as fp:
    try:
      parser = Parser(fp.read(), path)
      (node, mins, novermin) = parser.detect()
    except KeyboardInterrupt:
      return (path, mins, text)

    # When input isn't python code, ignore it.
    except ValueError:
      # source code string cannot contain null bytes
      return (None, None, None)
    except TypeError:
      # compile() expected string without null bytes
      return (None, None, None)

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

class Processor:
  def __versions_string(self, vers):
    res = []
    for i in range(len(vers)):
      ver = vers[i]
      # When versions aren't known, show something instead of nothing. It might run with any
      # version.
      if ver == 0:
        res.append("~{}".format(i + 2))
      elif ver is None:
        res.append("!{}".format(i + 2))
      else:
        res.append(str(ver))
    return ", ".join(res)

  def process(self, paths, processes=cpu_count()):
    pool = Pool(processes=processes)
    mins = [0, 0]
    incomp = False
    config = Config.get()

    def print_incomp(path):
      if not config.ignore_incomp():
        nprint("File with incompatible versions: {}".format(path))

    unique_versions = set()
    for (path, min_versions, text) in \
          pool.imap(process_individual, ((path, config) for path in paths)):
      # Ignore paths that didn't contain python code.
      if path is None and min_versions is None and text is None:
        continue

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

      vprint("{:<12} {}{}".format(self.__versions_string(min_versions), path, subtext))
      try:
        mins = combine_versions(mins, min_versions)
      except InvalidVersionException:
        incomp = True
        print_incomp(path)

    pool.close()

    unique_versions = list(unique_versions)
    unique_versions.sort()
    return (mins, incomp, unique_versions)
