import sys

from .config import Config
from .printing import nprint
from .detection import detect_paths
from .processing import process_paths
from .arguments import parse_args, print_usage

def version_strings(vers):
  return ", ".join(str(v) for v in vers)

def main():
  config = Config.get()

  args = parse_args(sys.argv[1:])
  if "usage" in args:
    print_usage()
  if args["code"] != 0:
    sys.exit(args["code"])

  processes = args["processes"]
  targets = args["targets"]

  nprint("Detecting python files..")
  paths = set(detect_paths(args["paths"]))
  amount = len(paths)
  if amount == 0:
    print("No files specified to analyze!")
    sys.exit(1)

  msg = "Analyzing"
  if amount > 1:
    msg += " {} files".format(amount)
  nprint("{} using {} processes..".format(msg, processes))

  try:
    (mins, incomp) = process_paths(paths, processes)
  except KeyboardInterrupt:
    print("Aborting..")
    sys.exit(1)

  if incomp and not config.ignore_incomp():
    nprint("Note: Some files had incompatible versions so the results might not be correct!")

  incomps = []
  reqs = []
  for i in range(len(mins)):
    ver = mins[i]
    if ver is None:
      incomps.append(i + 2)
    elif ver is not None and ver != 0:
      reqs.append(ver)

  if len(reqs) == 0 and len(incomps) == 0:
    print("Could not determine minimum required versions!")
    sys.exit(1)

  if len(reqs) > 0:
    print("Minimum required versions: {}".format(version_strings(reqs)))
  if len(incomps) > 0:
    print("Incompatible versions:     {}".format(version_strings(incomps)))

  if len(targets) > 0 and targets != reqs:
    print("Target versions not met:   {}".format(version_strings(targets)))
    sys.exit(1)
