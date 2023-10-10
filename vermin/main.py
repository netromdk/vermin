import sys
from os.path import abspath
from copy import deepcopy

from .config import Config
from .printing import nprint, vprint
from .detection import detect_paths
from .processor import Processor
from .arguments import Arguments
from .utility import version_strings, dotted_name, compare_requirements
from .backports import Backports

def main():
  config = Config()

  args = Arguments(sys.argv[1:]).parse(config)
  if "usage" in args:
    Arguments.print_usage(args["full"])
    sys.exit(args["code"])

  if args["code"] != 0:
    sys.exit(args["code"])  # pragma: no cover

  paths = args["paths"]
  parsable = config.format().name() == "parsable"

  # Detect paths, remove duplicates, and sort for deterministic results.
  if not parsable:
    vprint("Detecting python files..", config)
  if config.make_paths_absolute():
    paths = [abspath(p) for p in paths]

  # Parsable format ignores paths with ":" in particular because it interferes with the format that
  # uses ":" a lot.
  ignore_chars = []
  if parsable and not sys.platform.startswith("win32"):
    ignore_chars = [":", "\n"]

  paths = list(set(detect_paths(paths, hidden=config.analyze_hidden(),
                                processes=config.processes(), ignore_chars=ignore_chars,
                                scan_symlink_folders=config.scan_symlink_folders(), config=config)))
  paths.sort()

  amount = len(paths)
  if amount == 0:
    nprint("No files specified to analyze!", config)
    sys.exit(1)

  msg = "Analyzing"
  if amount > 1:
    msg += " {} files".format(amount)
  if not parsable:
    vprint("{} using {} processes..".format(msg, config.processes()), config)

  try:
    # In violations mode it is allowed to use quiet mode to show literally only discrepancies and
    # nothing else. But the processor must use the original verbosity level and not be quiet!
    local_config = deepcopy(config)
    if local_config.only_show_violations() and local_config.quiet():  # pragma: no cover
      local_config.set_verbose(config.verbose())
      local_config.set_quiet(False)

    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_annotations) =\
      processor.process(paths, local_config, local_config.processes())
  except KeyboardInterrupt:  # pragma: no cover
    nprint("Aborting..", config)
    sys.exit(1)

  if incomp and not config.ignore_incomp():  # pragma: no cover
    nprint("Note: Some files had incompatible versions so the results might not be correct!",
           config)

  incomps = []
  reqs = []
  for (i, ver) in enumerate(mins):
    if ver is None:
      incomps.append(i + 2)  # pragma: no cover
    elif ver is not None and ver != 0:
      reqs.append(ver)

  tips = []

  if not parsable and (len(reqs) == 0 and len(incomps) == 0):  # pragma: no cover
    nprint("No known reason found that it will not work with 2+ and 3+.", config)
    nprint("Please report if it does not: https://github.com/netromdk/vermin/issues/", config)

  if config.show_tips():  # pragma: no cover
    if maybe_annotations and not config.eval_annotations():
      tips.append([
        "Generic or literal annotations might be in use. If so, try using: --eval-annotations",
        "But check the caveat section: https://github.com/netromdk/vermin#caveats"
      ])

    # Only look at unversioned backports.
    unique_bps = sorted(backports - Backports.unversioned_filter(config.backports()))
    if len(unique_bps) > 0:
      tips.append([
        "You're using potentially backported modules: {}".format(", ".join(unique_bps)),
        "If so, try using the following for better results: {}".
        format("".join([" --backport {}".format(n) for n in unique_bps]).strip())
      ])

    if not used_novermin and config.parse_comments():
      tips.append(["Since '# novm' or '# novermin' weren't used, a speedup can be achieved using: "
                   "--no-parse-comments"])

    if len(tips) > 0:
      verbose = config.verbose()
      if len(reqs) == 0 or (reqs == [(0, 0), (0, 0)] and verbose > 0) or \
         (len(reqs) > 0 and 0 < verbose < 2):
        nprint("", config)
      nprint("Tips:", config)
      for tip in tips:
        nprint("- " + "\n  ".join(tip), config)
      nprint("(disable using: --no-tips)", config)
      if len(reqs) > 0:
        nprint("", config)

  if parsable:  # pragma: no cover
    print(config.format().format_output_line(msg=None, path=None, versions=mins))
  elif len(reqs) > 0:
    nprint("Minimum required versions: {}".format(version_strings(reqs)), config)
    if any(req == (0, 0) for req in reqs):
      vers = [req.replace("~", "") for req in version_strings(reqs, ",").split(",") if "~" in req]
      nprint("Note: Not enough evidence to conclude it won't work with Python {}.".
             format(" or ".join(vers)), config)

  # Don't show incompatible versions when -i is given, unless there are no non-incompatible versions
  # found then we need must show the incompatible versions - nothing will be shown otherwise. That
  # case is when both py2 and py3 incompatibilities were found - in which case `incomps = [2, 3]`
  # and `reqs = []`. But if `incomps = [2]` and `reqs = [3.4]`, for instance, then it makes sense
  # not to show incompatible versions with -i specified.
  if len(incomps) > 0 and (not parsable and (not config.ignore_incomp() or len(reqs) == 0)):
    # pragma: no cover
    nprint("Incompatible versions:     {}".format(version_strings(incomps)), config)

  if args["versions"] and len(unique_versions) > 0:
    nprint("Version range:             {}".format(version_strings(unique_versions)), config)

  targets = config.targets()
  if len(targets) > 0:
    # For violations mode, if all findings are inconclusive, like empty files or no rules triggered,
    # don't fail wrt. targets.
    all_inconclusive = config.only_show_violations() and len(reqs) > 0 and \
      all(req == (0, 0) for req in reqs)
    if not all_inconclusive and not compare_requirements(reqs, targets):
      if not parsable:
        vers = ["{}{}".format(dotted_name(t), "-" if not e else "") for (e, t) in targets]
        nprint("Target versions not met:   {}".format(version_strings(vers)), config)
      sys.exit(1)

  sys.exit(0)
