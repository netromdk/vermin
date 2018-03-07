import sys
from multiprocessing import cpu_count

from .constants import VERSION
from .config import Config

def print_usage():
  print("Vermin {}".format(VERSION))
  print("Usage: {} [options] <python source files and folders..>".format(sys.argv[0]))
  print("\nOptions:")
  print("  -q      Quite mode. It only prints the final versions verdict.")
  print("  -v..    Verbosity level 1 to 2. -v shows less than -vv but more than no verbosity.")
  print("  -t=V    Target version that files must abide by. Can be specified once or twice.\n"
        "          If not met Vermin will exit with code -1.")
  print("  -p=N    Use N concurrent processes to analyze files (defaults to all cores = {})."
        .format(cpu_count()))
  print("  -i      Ignore incompatible version warnings.")
  print("  -d      Dump AST node visits.")

def parse_args():
  if len(sys.argv) < 2:
    print_usage()
    sys.exit(-1)

  config = Config.get()
  path_pos = 1
  processes = cpu_count()
  targets = []
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i].lower()
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
        sys.exit(-1)
      if target < 2.0 or target >= 4.0:
        print("Invalid target: {}".format(target))
        sys.exit(-1)
      targets.append(target)
    elif arg == "-i":
      config.set_ignore_incomp(True)
      path_pos += 1
    elif arg.startswith("-p="):
      value = arg.split("=")[1]
      try:
        processes = int(value)
      except ValueError:
        print("Invalid value: {}".format(value))
        sys.exit(-1)
      if processes <= 0:
        print("Non-positive number: {}".format(processes))
        sys.exit(-1)
    elif arg == "-d":
      config.set_print_visits(True)
      path_pos += 1

  if config.quiet() and config.verbose() > 0:
    print("Cannot use quiet and verbose modes together!")
    sys.exit(-1)

  if len(targets) > 2:
    print("A maximum of two targets can be specified!")
    sys.exit(-1)
  targets.sort()

  paths = sys.argv[path_pos:]
  return {"paths": paths,
          "processes": processes,
          "targets": targets}
