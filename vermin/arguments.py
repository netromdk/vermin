import sys
import os

from .constants import VERSION, DEFAULT_PROCESSES, CONFIG_FILE_NAMES, PROJECT_BOUNDARIES
from .backports import Backports
from .features import Features
from .config import Config
from .printing import nprint
from . import formats

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
    print("\nA config file is automatically tried detected from the current working directory\n"
          "where Vermin is run, following parent folders until either the root or project\n"
          "boundary files/folders are reached. However, if --config-file is specified, no config\n"
          "is auto-detected and loaded.")

    if full:
      print("\nConfig file names being looked for: {}\n"
            "Project boundary files/folders: {}".
            format(", ".join(["'{}'".format(fn) for fn in CONFIG_FILE_NAMES]),
                   ", ".join(["'{}'".format(pb) for pb in PROJECT_BOUNDARIES])))

      print("\nOptions:")
      print("  --quiet | -q\n"
            "        Quiet mode. It only prints the final versions verdict.\n")
      print("  --no-quiet (default)\n"
            "        Disable quiet mode.\n")
      print("  -v..  Verbosity level 1 to 4. -v, -vv, -vvv, and -vvvv shows increasingly more\n"
            "        information.\n"
            "        -v     will show the individual versions required per file.\n"
            "        -vv    will also show which modules, functions etc. that constitutes\n"
            "               the requirements.\n"
            "        -vvv   will also show line/col numbers.\n"
            "        -vvvv  will also show user-defined symbols being ignored.\n")
      print("  --target=V | -t=V\n"
            "        Target version that files must abide by. Can be specified once or twice.\n"
            "        A '-' can be appended to match target version or smaller, like '-t=3.5-'.\n"
            "        If not met Vermin will exit with code 1. Note that the amount of target\n"
            "        versions must match the amount of minimum required versions detected.\n")
      print("  --no-target (default)\n"
            "        Don't expect certain target version(s).\n")
      print("  --processes=N | -p=N\n"
            "        Use N concurrent processes to detect and analyze files. Defaults to all\n"
            "        cores ({}).\n".format(DEFAULT_PROCESSES))
      print("  --ignore | -i\n"
            "        Ignore incompatible versions and warnings. However, if no compatible\n"
            "        versions are found then incompatible versions will be shown in the end to\n"
            "        not have an absence of results.\n")
      print("  --no-ignore (default)\n"
            "        Don't ignore incompatible versions and warnings.\n")
      print("  --lax | -l\n"
            "        Lax mode: ignores conditionals (if, ternary, for, async for, while, with,\n"
            "        try, bool op) on AST traversal, which can be useful when minimum versions\n"
            "        are detected in conditionals that it is known does not affect the results.\n")
      print("  --no-lax (default)\n"
            "        Disable lax mode.\n")
      print("  --dump | -d\n"
            "        Dump AST node visits.\n")
      print("  --no-dump (default)\n"
            "        Don't dump AST node visits.")
      print("\n  --help | -h\n"
            "        Shows this information and exists.")
      print("\n  --version | -V\n"
            "        Shows version number and exits.")
      print("\n  --config-file <path> | -c <path>\n"
            "        Loads config file unless --no-config-file is specified. Any additional\n"
            "        arguments supplied are applied on top of that config. See configuration\n"
            "        section above for more information.")
      print("\n  --no-config-file\n"
            "        No automatic config file detection and --config-file argument is disallowed.")
      print("\n  --hidden\n"
            "        Analyze 'hidden' files and folders starting with '.'.")
      print("\n  --no-hidden (default)\n"
            "        Don't analyze hidden files and folders unless specified directly.")
      print("\n  --versions\n"
            "        In the end, print all unique versions required by the analysed code.")
      print("\n  --show-tips (default)\n"
            "        Show helpful tips at the end, like those relating to backports or lax mode.")
      print("\n  --no-tips\n"
            "        Don't show tips.")
      print("\n  --pessimistic\n"
            "        Pessimistic mode: syntax errors are interpreted as the major Python version\n"
            "        in use being incompatible.")
      print("\n  --no-pessimistic (default)\n"
            "        Disable pessimistic mode.")
      print("\n  --eval-annotations\n"
            "        Instructs parser that annotations will be manually evaluated in code, which\n"
            "        changes minimum versions in certain cases. Otherwise, function and variable\n"
            "        annotations are not evaluated at definition time. Apply this argument if\n"
            "        code uses `typing.get_type_hints` or `eval(obj.__annotations__)` or\n"
            "        otherwise forces evaluation of annotations.")
      print("\n  --no-eval-annotations (default)\n"
            "        Disable annotations evaluation.")
      print("\n  --format <name> | -f <name>\n"
            "        Format to show results and output in.\n"
            "        Supported formats:\n{}".format(formats.help_str(10)))
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
      print("\n  --no-exclude (default)\n"
            "        Use no excludes. Clears any excludes specified before this.")
      print("\n  [--backport <name>] ...\n"
            "        Some features are sometimes backported into packages, in repositories such\n"
            "        as PyPi, that are widely used but aren't in the standard language. If such a\n"
            "        backport is specified as being used, the results will reflect that instead."
            "\n\n"
            "        Supported backports:\n{}".format(Backports.str(10)))
      print("\n  --no-backport (default)\n"
            "        Use no backports. Clears any backports specified before this.")
      print("\n  [--feature <name>] ...\n"
            "        Some features are disabled by default due to being unstable:\n{}".
            format(Features.str(10)))
      print("\n  --no-feature (default)\n"
            "        Use no features. Clears any features specified before this.")

  def parse(self, config, detect_folder=None):
    assert(config is not None)

    if len(self.__args) == 0:
      return {"code": 1, "usage": True, "full": False}

    path_pos = 0
    versions = False
    fmt = None
    detected_config = Config.detect_config_file(detect_folder)
    argument_config = None
    no_config_file = False

    # Preparsing step. Help and version arguments quit immediately and config file parsing must be
    # done first such that other arguments can override its settings.
    for i in range(len(self.__args)):
      arg = self.__args[i]
      if arg in ("--help", "-h"):
        return {"code": 0, "usage": True, "full": True}
      if arg in ("--version", "-V"):
        print(VERSION)
        sys.exit(0)
      if arg == "--no-config-file":
        no_config_file = True
        detected_config = None
      if arg in ("--config-file", "-c"):
        if (i + 1) >= len(self.__args):
          print("Requires config file path! Example: --config-file /path/to/vermin.ini")
          return {"code": 1}
        argument_config = os.path.abspath(self.__args[i + 1])

    if no_config_file and argument_config:
      print("--config-file cannot be used together with --no-config-file!")
      return {"code": 1}

    # Load potential config file if detected or specified as argument, but prefer config by
    # argument.
    config_candidate = argument_config or detected_config
    loaded_config = False
    if config_candidate:
      c = Config.parse_file(config_candidate)
      if c is None:
        return {"code": 1}
      loaded_config = True
      config.override_from(c)

    # Main parsing step.
    for i in range(len(self.__args)):
      arg = self.__args[i]
      if arg in ("--config-file", "-c"):
        # Config file parsed again only to ensure path position is correctly increased: reaching
        # this point means a well-formed config file was specified and parsed.
        path_pos += 2
      elif arg in ("--quiet", "-q"):
        config.set_quiet(True)
        path_pos += 1
      elif arg == "--no-quiet":
        config.set_quiet(False)
        path_pos += 1
      elif arg.startswith("-v"):
        config.set_verbose(arg.count("v"))
        path_pos += 1
      elif arg.startswith("-t=") or arg.startswith("--target="):
        value = arg.split("=")[1]
        if not config.add_target(value):
          print("Invalid target: {}".format(value))
          return {"code": 1}
        path_pos += 1
      elif arg == "--no-target":
        config.clear_targets()
        path_pos += 1
      elif arg in ("--ignore", "-i"):
        config.set_ignore_incomp(True)
        path_pos += 1
      elif arg == "--no-ignore":
        config.set_ignore_incomp(False)
        path_pos += 1
      elif arg.startswith("-p=") or arg.startswith("--processes="):
        value = arg.split("=")[1]
        try:
          processes = int(value)
          if processes <= 0:
            print("Non-positive number: {}".format(processes))
            return {"code": 1}
          config.set_processes(processes)
        except ValueError:
          print("Invalid value: {}".format(value))
          return {"code": 1}
        path_pos += 1
      elif arg in ("--lax", "-l"):
        print("Running in lax mode!")
        config.set_lax(True)
        path_pos += 1
      elif arg == "--no-lax":
        config.set_lax(False)
        path_pos += 1
      elif arg == "--no-dump":
        config.set_print_visits(False)
        path_pos += 1
      elif arg in ("--dump", "-d"):
        config.set_print_visits(True)
        path_pos += 1
      elif arg == "--hidden":
        config.set_analyze_hidden(True)
        path_pos += 1
      elif arg == "--no-hidden":
        config.set_analyze_hidden(False)
        path_pos += 1
      elif arg == "--versions":
        versions = True
        path_pos += 1
      elif arg == "--show-tips":
        config.set_show_tips(True)
        path_pos += 1
      elif arg == "--no-tips":
        config.set_show_tips(False)
        path_pos += 1
      elif arg in ("--format", "-f"):
        if (i + 1) >= len(self.__args):
          print("Format requires a name! Example: --format parsable")
          return {"code": 1}
        fmt_str = self.__args[i + 1].lower()
        fmt = formats.from_name(fmt_str)
        if fmt is None:
          print("Unknown format: {}".format(fmt_str))
          return {"code": 1}
        path_pos += 2
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
      elif arg == "--no-exclude":
        config.clear_exclusions()
        path_pos += 1
      elif arg == "--backport":
        if (i + 1) >= len(self.__args):
          print("Requires a backport name! Example: --backport typing")
          return {"code": 1}
        name = self.__args[i + 1]
        if not config.add_backport(name):
          print("Unknown backport: {}".format(name))
          return {"code": 1}
        path_pos += 2
      elif arg == "--no-backport":
        config.clear_backports()
        path_pos += 1
      elif arg == "--feature":
        if (i + 1) >= len(self.__args):
          print("Requires a feature name! Example: --feature fstring-self-doc")
          return {"code": 1}
        name = self.__args[i + 1]
        if not config.enable_feature(name):
          print("Unknown feature: {}".format(name))
          return {"code": 1}
        path_pos += 2
      elif arg == "--no-feature":
        config.clear_features()
        path_pos += 1
      elif arg == "--pessimistic":
        config.set_pessimistic(True)
        path_pos += 1
      elif arg == "--no-pessimistic":
        config.set_pessimistic(False)
        path_pos += 1
      elif arg == "--eval-annotations":
        config.set_eval_annotations(True)
        path_pos += 1
      elif arg == "--no-eval-annotations":
        config.set_eval_annotations(False)
        path_pos += 1

    if fmt is not None:
      config.set_format(fmt)

    if config.quiet() and config.verbose() > 0:
      print("Cannot use quiet and verbose modes together!")
      return {"code": 1}

    parsable = config.format().name() == "parsable"
    if parsable:
      versions = False

    if loaded_config and detected_config and not argument_config and not parsable:
      nprint("Using detected config: {}".format(detected_config), config)

    paths = self.__args[path_pos:]
    return {"code": 0,
            "paths": paths,
            "versions": versions}
