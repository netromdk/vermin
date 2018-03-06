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
  print("  -i      Ignore incompatible version warnings.")
  print("  -p=X    Use X concurrent processes to analyze files (defaults to all cores = {})."
        .format(cpu_count()))
  print("  -d      Dump AST node visits.")

def parse_args():
  if len(sys.argv) < 2:
    print_usage()
    sys.exit(-1)

  config = Config.get()
  path_pos = 1
  processes = cpu_count()
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i].lower()
    if arg == "-q":
      config.set_quiet(True)
      path_pos += 1
    elif arg.startswith("-v"):
      config.set_verbose(arg.count("v"))
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

  paths = sys.argv[path_pos:]
  return {"paths": paths,
          "processes": processes}
