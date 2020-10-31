import multiprocessing as mp

from .printing import nprint
from .utility import combine_versions, InvalidVersionException
from .parser import Parser
from .source_visitor import SourceVisitor
from .backports import Backports

class ProcessResult:
  def __init__(self, path):
    self.path = path       # Path of processed file.
    self.node = None       # AST root node.
    self.mins = None       # Minimum versions detected.
    self.text = ""         # Output or exception text.
    self.novermin = set()  # novermin/novm lines.
    self.bps = set()       # Potential backport modules used.

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
  res = ProcessResult(path)

  with open(path, mode="rb") as fp:
    try:
      parser = Parser(fp.read(), path)
      (res.node, res.mins, res.novermin) = parser.detect(config)
    except KeyboardInterrupt:  # pragma: no cover
      return res

    # When input isn't python code, ignore it.
    except ValueError:
      # source code string cannot contain null bytes
      return None
    except TypeError:  # pragma: no cover
      # compile() expected string without null bytes
      return None

    except Exception as ex:  # pragma: no cover
      res.text = "{}: {}, {}".format(path, type(ex), ex)
      res.mins = [(0, 0), (0, 0)]

  if res.node is None:
    return res

  visitor = SourceVisitor(config, path)
  visitor.set_no_lines(res.novermin)

  try:
    visitor.tour(res.node)
  except KeyboardInterrupt:  # pragma: no cover
    return res

  try:
    res.mins = visitor.minimum_versions()
    res.text = visitor.output_text()
    for m in visitor.modules():
      if Backports.is_backport(m):
        res.bps.add(m)
  except InvalidVersionException as ex:
    res.mins = None
    res.text = str(ex)

  return res

class Processor:
  def process(self, paths, config, processes=mp.cpu_count()):  # pylint: disable=no-self-use
    assert(config is not None)

    pool = mp.Pool(processes=processes) if processes > 1 else None
    mins = [(0, 0), (0, 0)]
    incomp = False

    def print_incomp(path, text):
      if not config.ignore_incomp():
        if len(text) > 0:
          text = "\n  " + text
        nprint("File with incompatible versions: {}{}".format(path, text), config)

    # Automatically don't use concurrency when only one process is specified to be used.
    def act():
      if processes == 1:
        return [process_individual((path, config)) for path in paths]  # pragma: no cover
      return pool.imap(process_individual, ((path, config) for path in paths))

    unique_versions = set()
    all_backports = set()
    for proc_res in act():
      # Ignore paths that didn't contain python code.
      if proc_res is None:
        continue

      if proc_res.mins is None:
        incomp = True
        print_incomp(proc_res.path, proc_res.text)
        continue

      all_backports = all_backports | proc_res.bps

      for ver in proc_res.mins:
        if ver is not None and ver > (0, 0):
          unique_versions.add(ver)

      config.format().output_result(proc_res)

      try:
        mins = combine_versions(mins, proc_res.mins, config)
      except InvalidVersionException:
        incomp = True
        print_incomp(proc_res.path, proc_res.text)

    if pool:
      pool.close()

    unique_versions = list(unique_versions)
    unique_versions.sort()
    return (mins, incomp, unique_versions, all_backports)
