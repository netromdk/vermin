import sys
import re
from multiprocessing import cpu_count

from .constants import VERSION
from .config import Config
from .backports import Backports
from .features import Features

TARGETS_SPLIT = re.compile("[\\.,]")

class Arguments:
  def __init__(self, args):
    self.__args = args

  @staticmethod
  def print_usage(full=False):
    print("Vermin {}".format(VERSION))
    print("Usage: {} [options] <python source files and folders..>".format(sys.argv[0]))
    print("\nConcurrently detect the minimum Python versions needed to run code.")

    if not full:
      print("\nFor full help and options, use `-h` or `--help`.")

    print("\nHeuristics are employed to determine which files to analyze:\n"
          "  - 'py', 'py3', 'pyw', 'pyj', 'pyi' are always scanned\n"
          "  - 'pyc', 'pyd', 'pxd', 'pyx', 'pyo' are ignored (including various other files)\n"
          "  - Magic lines with 'python' are accepted, like: #!/usr/bin/env python\n"
          "  - Files that cannot be opened for reading as text devices are ignored")
    print("\nHowever, files directly specified are always attempted parsing, even without\n"
          "accepted extensions or heuristics.")
    print("\nResults interpretation:")
    print("  ~2       No known reason it won't work with py2.")
    print("  !2       It is known that it won't work with py2.")
    print("  2.5, !3  Works with 2.5+ but it is known it won't work with py3.")
    print("  ~2, 3.4  No known reason it won't work with py2, works with 3.4+")
    print("\nIncompatible versions notices mean that several files were detected incompatible\n"
          "with py2 and py3 simultaneously. In such cases the results might be inconclusive.")

    if full:
      print("\nOptions:")
      print("  -q    Quiet mode. It only prints the final versions verdict.")
      print("  -v..  Verbosity level 1 to 4. -v, -vv, -vvv, and -vvvv shows increasingly more\n"
            "        information.\n"
            "        -v     will show the individual versions required per file.\n"
            "        -vv    will also show which modules, functions etc. that constitutes\n"
            "               the requirements.\n"
            "        -vvv   will also show line/col numbers.\n"
            "        -vvvv  will also show user-defined symbols being ignored.")
      print("  -t=V  Target version that files must abide by. Can be specified once or twice.\n"
            "        A '-' can be appended to match target version or smaller, like '-t=3.5-'.\n"
            "        If not met Vermin will exit with code 1. Note that the amount of target\n"
            "        versions must match the amount of minimum required versions detected.")
      print("  -p=N  Use N concurrent processes to detect and analyze files. Defaults to all\n"
            "        cores ({}).".format(cpu_count()))
      print("  -i    Ignore incompatible versions and warnings. However, if no compatible\n"
            "        versions are found then incompatible versions will be shown in the end to\n"
            "        not have an absence of results.")
      print("  -l    Lax mode: ignores conditionals (if, ternary, for, while, try, bool op) on\n"
            "        AST traversal, which can be useful when minimum versions are detected in\n"
            "        conditionals that it is known does not affect the results.")
      print("  -d    Dump AST node visits.")
      print("\n  --help | -h\n"
            "        Shows this information and exists.")
      print("\n  --version\n"
            "        Shows version number and exits.")
      print("\n  --hidden\n"
            "        Analyze 'hidden' files and folders starting with '.' (ignored by default\n"
            "        when not specified directly).")
      print("\n  --versions\n"
            "        In the end, print all unique versions required by the analysed code.")
      print("\n  --no-tips\n"
            "        Don't show any helpful tips at the end, like those relating to backports or\n"
            "        lax mode.")
      print("\n  [--exclude <name>] ...\n"
            "        Exclude full names, like 'email.parser.FeedParser', from analysis. Useful to\n"
            "        ignore conditional logic that can trigger incompatible results. It's more\n"
            "        fine grained than lax mode.\n\n"
            "        Examples:\n"
            "          Exclude 'foo.bar.baz' module/member: --exclude 'foo.bar.baz'\n"
            "          Exclude 'foo' kwarg:                 --exclude 'somemodule.func(foo)'\n"
            "          Exclude 'bar' codecs error handler:  --exclude 'ceh=bar'\n"
            "          Exclude 'baz' codecs encoding:       --exclude 'ce=baz'")
      print("\n  [--exclude-file <file name>] ...\n"
            "        Exclude full names like --exclude but from a specified file instead. Each\n"
            "        line constitutes an exclusion with the same format as with --exclude.")
      print("\n  [--backport <name>] ...\n"
            "        Some features are sometimes backported into packages, in repositories such\n"
            "        as PyPi, that are widely used but aren't in the standard language. If such a\n"
            "        backport is specified as being used, the results will reflect that instead."
            "\n\n"
            "        Supported backports:\n{}".format(Backports.str(10)))
      print("\n  [--feature <name>] ...\n"
            "        Some features are disabled by default due to being unstable:\n{}".
            format(Features.str(10)))

  def parse(self):
    if len(self.__args) == 0:
      return {"code": 1, "usage": True, "full": False}

    config = Config.get()
    path_pos = 0
    processes = cpu_count()
    targets = []
    hidden = False
    versions = False
    no_tips = False
    for i in range(len(self.__args)):
      arg = self.__args[i].lower()
      if arg == "-h" or arg == "--help":
        return {"code": 0, "usage": True, "full": True}
      if arg == "--version":
        print(VERSION)
        exit(0)
      if arg == "-q":
        config.set_quiet(True)
        path_pos += 1
      elif arg.startswith("-v"):
        config.set_verbose(arg.count("v"))
        path_pos += 1
      elif arg.startswith("-t="):
        value = arg.split("=")[1]
        exact = True
        if value.endswith("-"):
          exact = False
          value = value[:-1]

        # Parse target as a tuple separated by either commas or dots, which preserves support for
        # old float-number inputs.
        elms = TARGETS_SPLIT.split(value)
        if len(elms) != 1 and len(elms) != 2:
          print("Invalid target: {}".format(value))
          return {"code": 1}

        for i in range(len(elms)):
          try:
            n = int(elms[i])
            if n < 0:
              print("Invalid target: {}".format(value))
              return {"code": 1}
            elms[i] = n
          except ValueError:
            print("Invalid target: {}".format(value))
            return {"code": 1}

        # When only specifying major version, use zero as minor.
        if len(elms) == 1:
          elms.append(0)

        elms = tuple(elms)
        if not (elms >= (2, 0) and elms < (4, 0)):
          print("Invalid target: {}".format(value))
          return {"code": 1}

        targets.append((exact, elms))
        path_pos += 1
      elif arg == "-i":
        config.set_ignore_incomp(True)
        path_pos += 1
      elif arg.startswith("-p="):
        value = arg.split("=")[1]
        try:
          processes = int(value)
        except ValueError:
          print("Invalid value: {}".format(value))
          return {"code": 1}
        if processes <= 0:
          print("Non-positive number: {}".format(processes))
          return {"code": 1}
        path_pos += 1
      elif arg == "-l":
        print("Running in lax mode!")
        config.set_lax_mode(True)
        path_pos += 1
      elif arg == "-d":
        config.set_print_visits(True)
        path_pos += 1
      elif arg == "--hidden":
        hidden = True
        path_pos += 1
      elif arg == "--versions":
        versions = True
        path_pos += 1
      elif arg == "--no-tips":
        no_tips = True
        path_pos += 1
      elif arg == "--exclude":
        if (i + 1) >= len(self.__args):
          print("Exclusion requires a name! Example: --exclude email.parser.FeedParser")
          return {"code": 1}
        config.add_exclusion(self.__args[i + 1])
        path_pos += 2
      elif arg == "--exclude-file":
        if (i + 1) >= len(self.__args):
          print("Exclusion requires a file name! Example: --exclude-file '~/exclusions.txt'")
          return {"code": 1}
        config.add_exclusion_file(self.__args[i + 1])
        path_pos += 2
      elif arg == "--backport":
        if (i + 1) >= len(self.__args):
          print("Requires a backport name! Example: --backport typing")
          return {"code": 1}
        name = self.__args[i + 1]
        if not config.add_backport(name):
          print("Unknown backport: {}".format(name))
          return {"code": 1}
        path_pos += 2
      elif arg == "--feature":
        if (i + 1) >= len(self.__args):
          print("Requires a feature name! Example: --feature fstring-self-doc")
          return {"code": 1}
        name = self.__args[i + 1]
        if not config.enable_feature(name):
          print("Unknown feature: {}".format(name))
          return {"code": 1}
        path_pos += 2

    if config.quiet() and config.verbose() > 0:
      print("Cannot use quiet and verbose modes together!")
      return {"code": 1}

    if len(targets) > 2:
      print("A maximum of two targets can be specified!")
      return {"code": 1}

    # Sort target versions, not boolean values.
    targets.sort(key=lambda t: t[1])

    paths = self.__args[path_pos:]
    return {"code": 0,
            "paths": paths,
            "processes": processes,
            "targets": targets,
            "hidden": hidden,
            "versions": versions,
            "no-tips": no_tips}
