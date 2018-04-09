import sys
from multiprocessing import cpu_count

from .constants import VERSION
from .config import Config

def print_usage():
  print("Vermin {}".format(VERSION))
  print("Usage: {} [options] <python source files and folders..>".format(sys.argv[0]))
  print("\nOptions:")
  print("  -q      Quite mode. It only prints the final versions verdict.")
  print("  -v..    Verbosity level 1 to 3. -v, -vv, and -vvv shows increasingly more information.\n"
        "          -v will show the individual versions required per file, -vv will additionally\n"
        "          show which modules, functions etc. that constitutes the requirements.")
  print("  -t=V    Target version that files must abide by. Can be specified once or twice.\n"
        "          If not met Vermin will exit with code 1.")
  print("  -p=N    Use N concurrent processes to analyze files (defaults to all cores = {})."
        .format(cpu_count()))
  print("  -i      Ignore incompatible version warnings.")
  print("  -d      Dump AST node visits.")

def parse_args(args):
  if len(args) == 0:
    return {"code": 1, "usage": True}

  config = Config.get()
  path_pos = 0
  processes = cpu_count()
  targets = []
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
    elif arg == "-d":
      config.set_print_visits(True)
      path_pos += 1

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
          "targets": targets}
