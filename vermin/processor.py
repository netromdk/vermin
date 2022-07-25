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

    # Potential generic/literal annotations used.
    self.maybe_annotations = False

  def __repr__(self):
    return """{} at 0x{:x}
path={}
node={}
mins={}
text={}
novermin={}
bps={}
maybe_annotations={}""".format(self.__class__.__name__, id(self), self.path, self.node, self.mins,
                               self.text, self.novermin, self.bps, self.maybe_annotations)

class Processor:
  def process(self, paths, config, processes=mp.cpu_count()):
    assert config is not None
    unique_versions = set()
    all_backports = set()
    used_novermin = False
    maybe_annotations = False
    mins = [(0, 0), (0, 0)]
    incomp = False

    try:
      # pylint: disable=consider-using-with
      pool = mp.Pool(processes=processes) if processes > 1 else None

      def print_incomp(path, text):
        if not config.ignore_incomp():
          if len(text) > 0:
            text = "\n  " + text
          nprint("File with incompatible versions: {}{}".format(path, text), config)

      # Automatically don't use concurrency when only one process is specified to be used.
      def act():
        if processes == 1:
          return [self.process_individual((path, config)) for path in paths]  # pragma: no cover
        return pool.imap(self.process_individual, ((path, config) for path in paths))

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

        used_novermin |= (len(proc_res.novermin) > 0)
        maybe_annotations |= proc_res.maybe_annotations

        # For violations mode, only show file names and findings if there are any - no empty ones
        # that do not violate the input targets. This is especially important when scanning many
        # files since it can be hard to spot violations. Otherwise, show as normal.
        if not config.only_show_violations() or len(proc_res.text) > 0:
          config.format().output_result(proc_res)

        try:
          mins = combine_versions(mins, proc_res.mins, config)
        except InvalidVersionException:
          incomp = True
          print_incomp(proc_res.path, proc_res.text)

      if pool:
        pool.close()
    except RuntimeError:
      nprint("""RuntimeError: If running `Processor.process()` outside of
`if __name__ == \"__main__\":` it, or the code calling it, must be done within it instead.""",
             config)

    unique_versions = list(unique_versions)
    unique_versions.sort()
    return (mins, incomp, unique_versions, all_backports, used_novermin, maybe_annotations)

  @staticmethod
  def process_individual(args):
    (path, config) = args
    res = ProcessResult(path)

    source = None
    try:
      with open(path, mode="rb") as fp:
        source = fp.read()
        parser = Parser(source, path)
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

    visitor = SourceVisitor(config, path, source)
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
      res.maybe_annotations = visitor.maybe_annotations()
    except InvalidVersionException as ex:
      res.mins = None
      res.text = str(ex)

    return res
