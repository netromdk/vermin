import sys

from .config import Config
from .printing import nprint
from .detection import detect_paths
from .processing import process_paths, versions_string
from .arguments import parse_args

def unknown_versions(vers):
  """Versions are unknown if all values are either 0 or None."""
  return len(vers) == vers.count(0) + vers.count(None)

def main():
  config = Config.get()
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
