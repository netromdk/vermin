==========
vermin.ini
==========

-----------------------------
Configuration file for vermin
-----------------------------

:Manual section: 5

.. contents::

Description
===========

``vermin.ini`` is an INI-formatted configuration file. Options applicable to vermin
are in the ``[vermin]`` section so that it may be included in other configuration files
such as ``setup.cfg``. For example:

.. code-block:: ini

  [vermin]
  verbose = 1
  processes = 4

  [flake8]
  ignore = E111,F821

Options
=======

The default values are marked with asterisks (`*`).

quiet = ***no*** | yes
  Enable quiet mode. If used together with ``--violations``, quiet mode is preserved while
  showing only violations: no descriptive text, tips, or verdicts.

verbose = ***0***
  Verbosity level 1 to 4 showing increasingly more information. Turned off at level 0.

print_visits = ***no*** | yes
  Dump AST node visits.

targets = VERSION
  Target version that files must abide by. Can be specified once or twice.
  A '-' can be appended to match target version or smaller, like '``-t=3.5-``'.
  If not met Vermin will exit with code 1. Vermin will only compare target
  versions with the same major version, so if you do not care about Python
  2, you can just specify one target for Python 3. However, if used in
  conjunction with ``--violations``, and no rules are triggered, it will exit
  with code 0.

processes = ***0***
  Use N concurrent processes to detect and analyze files. Defaults to 0, meaning
  all cores available.

ignore_incomp = ***no*** | yes
  Ignore incompatible versions and warnings. However, if no compatible versions
  are found then incompatible versions will be shown in the end to not have an
  absence of results.

analyze_hidden = ***no*** | yes
  Analyze 'hidden' files and folders starting with '``.``'s.

show_tips = ***yes*** | no
  Show helpful tips at the end, like those relating to backports or usage of
  unevaluated generic/literal annotations.

pessimistic = ***no*** | yes
  Enable pessimistic mode: syntax errors are interpreted as the major Python version
  in use being incompatible.

exclusions = NAME
  Exclude full names, like 'email.parser.FeedParser', from analysis. Useful to
  ignore conditional logic that can trigger incompatible results

exclusion_regex = REGEX
  Exclude files from analysis by matching a regex pattern against their entire
  path as expanded from the Vermin command line. Patterns are matched using
  `re.search()`, so '^' or '$' anchors should be applied as needed.

make_paths_absolute = ***yes*** | no
  Convert any relative paths from the command line into absolute paths. This
  affects the path printed to the terminal if a file fails a check, and requires
  ``--exclude-regex`` patterns to match absolute paths.

backports = NAME
  Some features are sometimes backported into packages, in repositories such as PyPi,
  that are widely used but aren't in the standard language. If such a backport is
  specified as being used, the results will reflect that instead. Versioned
  backports are only used when minimum versions change. Unversioned backports must
  be the newest among versioned and unversioned.

  See ``--help`` or vermin(1) for a full list of supported backports.

features = NAME
  Some features are disabled by default due to being unstable:

  See ``--help`` or vermin(1) for a full list of supported features.

format = **default**
  Format to show results and output in. Supported formats:

  See ``--help`` or vermin(1) for a full list of supported formats.

eval_annotations = ***no*** | yes
  Instructs parser that annotations will be manually evaluated in code, which
  changes minimum versions in certain cases. Otherwise, function and variable
  annotations are not evaluated at definition time. Apply this argument if
  code uses ``typing.get_type_hints`` or ``eval(obj.__annotations__)`` or
  otherwise forces evaluation of annotations.

only_show_violations = ***no*** | yes
  Show only results that violate versions described by ``--target`` arguments,
  which are required to be specified. Verbosity mode is automatically set to
  at least 2 in order to show violations in output text, but can be increased
  if necessary.

parse_comments = ***yes*** | no
  Parse for comments to influence exclusion of code for analysis via "``# novm``"
  and "``# novermin``".

scan_symlink_folders = ***no*** | yes
  Scan symlinks to folders to include in analysis.


Examples
========

Specify targets to Python 2.7 and Python 3.9 or less:

.. code-block:: ini

  targets = 2.7
    3.9-

Exclude multiple full names:

.. code-block:: ini

  exclusions =
    email.parser.FeedParser
    argparse.ArgumentParser(allow_abbrev)

Include multiple backports:

.. code-block:: ini

  backports =
    typing
    argparse

Enable an unstable feature:

.. code-block:: ini

  features =
    fstring-self-doc

Exclude a directory using regex:

.. code-block:: ini

  exclusion_regex =
    ^a/b$

  # Required for the above regex
  make_paths_absolute = no

See also
========

vermin(1), sample.vermin.ini
