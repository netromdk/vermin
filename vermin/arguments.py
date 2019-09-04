import sys
from multiprocessing import cpu_count

from .constants import VERSION
from .config import Config

def print_usage():
  print("Vermin {}".format(VERSION))
  print("Usage: {} [options] <python source files and folders..>".format(sys.argv[0]))
  print("\nOptions:")
  print("  -q    Quite mode. It only prints the final versions verdict.")
  print("  -v..  Verbosity level 1 to 3. -v, -vv, and -vvv shows increasingly more information.\n"
        "        -v    will show the individual versions required per file.\n"
        "        -vv   will also show which modules, functions etc. that constitutes\n"
        "              the requirements.\n"
        "        -vvv  will also show line/col numbers.")
  print("  -t=V  Target version that files must abide by. Can be specified once or twice.\n"
        "        If not met Vermin will exit with code 1.")
  print("  -p=N  Use N concurrent processes to analyze files (defaults to all cores = {})."
        .format(cpu_count()))
  print("  -i    Ignore incompatible version warnings.")
  print("  -l    Lax mode: ignores conditionals (if, ternary, for, while, try, bool op) on AST\n"
        "        traversal, which can be useful when minimum versions are detected in\n"
        "        conditionals that it is known does not affect the results.")
  print("  -d    Dump AST node visits.")
  print("\n  --hidden\n"
        "        Analyze 'hidden' files and folders starting with '.' (ignored by default).")
  print("\n  --versions\n"
        "        In the end, print all unique versions required by the analysed code.")
  print("\n  [--exclude <name>] ...\n"
        "        Exclude full names, like 'email.parser.FeedParser', from analysis. Useful to\n"
        "        ignore conditional logic that can trigger incompatible results. It's more fine\n"
        "        grained than lax mode.\n\n"
        "        Examples:\n"
        "          Exclude 'foo.bar.baz' module/member: --exclude 'foo.bar.baz'\n"
        "          Exclude 'foo' kwarg:                 --exclude 'somemodule.func(foo)'\n"
        "          Exclude 'bar' codecs error handler:  --exclude 'ceh=bar'\n"
        "          Exclude 'baz' codecs encoding:       --exclude 'ce=baz'")
  print("\n  [--exclude-file <file name>] ...\n"
        "        Exclude full names like --exclude but from a specified file instead. Each line\n"
        "        constitues an exclusion with the same format as with --exclude.")
  print("\nResults interpretation:")
  print("  ~2       No known reason it won't work with py2.")
  print("  !2       It is known that it won't work with py2.")
  print("  2.5, !3  Works with 2.5+ but it is known it won't work with py3.")
  print("  ~2, 3.4  No known reason it won't work with py2, works with 3.4+")

def parse_args(args):
  if len(args) == 0:
    return {"code": 1, "usage": True}

  config = Config.get()
  path_pos = 0
  processes = cpu_count()
  targets = []
  hidden = False
  versions = False
  for i in range(len(args)):
    arg = args[i].lower()
    if arg == "-q":
      config.set_quiet(True)
      path_pos += 1
    elif arg.startswith("-v"):
      config.set_verbose(arg.count("v"))
      path_pos += 1
    elif arg.startswith("-t="):
      value = arg.split("=")[1]
      try:
        target = float(value)
      except ValueError:
        print("Invalid target: {}".format(value))
        return {"code": 1}
      if target < 2.0 or target >= 4.0:
        print("Invalid target: {}".format(target))
        return {"code": 1}
      targets.append(target)
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
    elif arg == "--exclude":
      if (i + 1) >= len(args):
        print("Exclusion requires a name! Example: --exclude email.parser.FeedParser")
        return {"code": 1}
      config.add_exclusion(args[i + 1])
      path_pos += 2
    elif arg == "--exclude-file":
      if (i + 1) >= len(args):
        print("Exclusion requires a file name! Example: --exclude-file '~/exclusions.txt'")
        return {"code": 1}
      config.add_exclusion_file(args[i + 1])
      path_pos += 2

  if config.quiet() and config.verbose() > 0:
    print("Cannot use quiet and verbose modes together!")
    return {"code": 1}

  if len(targets) > 2:
    print("A maximum of two targets can be specified!")
    return {"code": 1}
  targets.sort()

  paths = args[path_pos:]
  return {"code": 0,
          "paths": paths,
          "processes": processes,
          "targets": targets,
          "hidden": hidden,
          "versions": versions}
