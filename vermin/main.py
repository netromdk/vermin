import sys
from multiprocessing import cpu_count

from .constants import VERSION
from .config import Config
from .printing import nprint
from .detection import detect_paths
from .processing import process_paths, versions_string

config = Config.get()

def all_none(elms):
  return len(elms) == elms.count(None)

def unknown_versions(vers):
  """Versions are unknown if all values are either 0 or None."""
  return len(vers) == vers.count(0) + vers.count(None)

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

def main():
  args = parse_args()
  processes = args["processes"]

  nprint("Detecting python files..")
  paths = set(detect_paths(args["paths"]))
  amount = len(paths)
  if amount == 0:
    print("No files specified to analyze!")
    sys.exit(-1)

  msg = "Analyzing"
  if amount > 1:
    msg += " {} files".format(amount)
  nprint("{} using {} processes..".format(msg, processes))
  (mins, incomp) = process_paths(paths, processes)

  if incomp and not config.ignore_incomp():
    nprint("Note: Some files had incompatible versions so the results might not be correct!")

  if unknown_versions(mins):
    print("Could not determine minimum required versions!")
  else:
    print("Minimum required versions: {}".format(versions_string(mins)))
