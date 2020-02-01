import sys
from os.path import abspath

from .config import Config
from .printing import nprint, vprint
from .detection import detect_paths
from .processor import Processor
from .arguments import Arguments
from .utility import version_strings, dotted_name

def main():
  config = Config.get()

  args = Arguments(sys.argv[1:]).parse()
  if "usage" in args:
    Arguments.print_usage(args["full"])
    sys.exit(args["code"])

  if args["code"] != 0:
    sys.exit(args["code"])

  processes = args["processes"]
  targets = args["targets"]
  no_tips = args["no-tips"]
  hidden = args["hidden"]
  paths = args["paths"]

  # Detect paths, remove duplicates, and sort for deterministic results.
  vprint("Detecting python files..")
  paths = [abspath(p) for p in paths]
  paths = list(set(detect_paths(paths, hidden=hidden, processes=processes)))
  paths.sort()

  amount = len(paths)
  if amount == 0:
    print("No files specified to analyze!")
    sys.exit(1)

  msg = "Analyzing"
  if amount > 1:
    msg += " {} files".format(amount)
  vprint("{} using {} processes..".format(msg, processes))

  try:
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, processes)
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
    print("No known reason found that it will not work with 2+ and 3+.")
    print("Please report if it does not: https://github.com/netromdk/vermin/issues/")
    if config.lax_mode() and not no_tips:
      print("Tip: Try without using lax mode for more thorough analysis.")

  unique_bps = sorted(backports - config.backports())
  if len(unique_bps) > 0 and not no_tips:
    print("Tip: You're using potentially backported modules: {}".format(", ".join(unique_bps)))
    print("If so, try using the following for better results: {}\n".
          format("".join([" --backport {}".format(n) for n in unique_bps]).strip()))

  if len(reqs) > 0:
    print("Minimum required versions: {}".format(version_strings(reqs)))

  # Don't show incompatible versions when -i is given, unless there are no non-incompatible versions
  # found then we need must show the incompatible versions - nothing will be shown otherwise. That
  # case is when both py2 and py3 incompatibilities were found - in which case `incomps = [2, 3]`
  # and `reqs = []`. But if `incomps = [2]` and `reqs = [3.4]`, for instance, then it makes sense
  # not to show incompatible versions with -i specified.
  if len(incomps) > 0 and (not config.ignore_incomp() or len(reqs) == 0):
    print("Incompatible versions:     {}".format(version_strings(incomps)))

  if args["versions"] and len(unique_versions) > 0:
    print("Version range:             {}".format(version_strings(unique_versions)))

  if len(targets) > 0:
    if not (len(reqs) == len(targets) and
            all(((exact and target == req) or (not exact and target >= req)) for
                ((exact, target), req) in zip(targets, reqs))):
      vers = ["{}{}".format(dotted_name(t), "-" if not e else "") for (e, t) in targets]
      print("Target versions not met:   {}".format(version_strings(vers)))
      if len(targets) < len(reqs):
        print("Note: Number of specified targets ({}) doesn't match number of detected minimum "
              "versions ({}).".format(len(targets), len(reqs)))
      sys.exit(1)

  sys.exit(0)
