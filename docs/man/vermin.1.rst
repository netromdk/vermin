======
vermin
======

-------------------------------------------------------------------
Concurrently detect the minimum Python versions needed to run code.
-------------------------------------------------------------------

:Manual section: 1

.. contents::

Synopsis
========

``vermin`` [OPTIONS] *PATH* ...

Description
===========

Vermin parses Python code into an abstract syntax tree (AST) and matches that
against an internal library of rules in order to determine the minimum Python
version that the code can be run with.

Heuristics are employed to determine which files to analyze:

  * 'py', 'py3', 'pyw', 'pyj', 'pyi' are always scanned, unless otherwise excluded.
  * 'pyc', 'pyd', 'pxd', 'pyx', 'pyo', and various other files are ignored.
  * Magic lines with 'python' are accepted, like: ``#!/usr/bin/env python``.
  * Files that cannot be opened for reading as text devices are ignored.

However, vermin will always attempt to parse any file paths directly specified on
the command line, even without accepted extensions or heuristics, unless otherwise
excluded.

Results interpretation
  ~2
    No known reason it won't work with Python 2
  !2
    It is known that it won't work with Python 2.
  2.5, !3
    Works with Python 2.5+ but it is known it won't work with Python 3.
  ~2, 3.4
    No known reason it won't work with Python 2, works with Python 3.4+.

Incompatible versions notices mean that several files were detected incompatible
with Python 2 and Python 3 simultaneously. In such cases the results might be
inconclusive.

A config file is automatically detected from the current working directory
where vermin is run, following parent folders until either the root or project
boundary files/folders are reached. However, if ``--config-file`` is specified, no
configuration is auto-detected and loaded.

Config file names being looked for:

 * vermin.ini
 * vermin.conf
 * .vermin
 * setup.cfg

Project boundary files/folders:

 * .bzr
 * .fslckout
 * .git
 * .hg
 * .p4root
 * .pijul
 * .svn
 * _darcs

Options
=======

-q, --quiet
  Enable quiet mode. If used together with ``--violations``, quiet mode is preserved while
  showing only violations: no descriptive text, tips, or verdicts.

--no-quiet
  Disable quiet mode.

-v..
  Verbosity level 1 to 4. ``-v``, ``-vv``, ``-vvv``, and ``-vvvv`` shows increasingly more information.

  -v
    will show the individual versions required per file.
  -vv
    will also show which modules, functions etc. that constitutes the requirements.
  -vvv
    will also show line/column numbers.
  -vvvv
    will also show user-defined symbols being ignored

-t=VERSION, --target=VERSION
  Target version that files must abide by. Can be specified once or twice.
  A '-' can be appended to match target version or smaller, like '``-t=3.5-``'.
  If not met Vermin will exit with code 1. Vermin will only compare target
  versions with the same major version, so if you do not care about Python
  2, you can just specify one target for Python 3. However, if used in
  conjunction with ``--violations``, and no rules are triggered, it will exit
  with code 0.

--no-target (default)
  Don't expect certain target version(s).

-p=NUMBER, --processes=NUMBER
  Use NUMBER concurrent processes to detect and analyze files. Defaults to all cores.

-i, --ignore
  Ignore incompatible versions and warnings. However, if no compatible versions
  are found then incompatible versions will be shown in the end to not have an
  absence of results.

--no-ignore (default)
  Don't ignore incompatible versions and warnings.

-d, --dump
  Dump AST node visits.

--no-dump (default)
  Don't dump AST node visits.

-h, --help
  Show the help information and exits.

-V, --version
  Show the version number and exits.

-c=FILE, --config-file=FILE
  Loads the specified config file unless ``--no-config-file`` is specified. Any
  additional arguments supplied are applied on top of that config. See vermin.ini(5)
  section for more information.

--no-config-file
  Disable automatic configuration file detection and disallow the ``--config-file`` argument.

--hidden
  Analyze 'hidden' files and folders starting with '``.``'s.

--no-hidden (default)
  Don't analyze hidden files and folders unless specified directly.

--versions
  In the end, print all unique versions required by the analyzed code.

--show-tips (default)
  Show helpful tips at the end, like those relating to backports or usage of
  unevaluated generic/literal annotations.

--no-tips
  Don't show tips.

--lint, --violations
  Show only results that violate versions described by ``--target`` arguments,
  which are required to be specified. Verbosity mode is automatically set to
  at least 2 in order to show violations in output text, but can be increased
  if necessary.

  If no rules are triggered while used in conjunction with ``--target``, an exit
  code 0 will still be yielded due to inconclusivity.

  Can be used together with ``--quiet`` such that only the violations are shown:
  no descriptive text, tips, or verdicts.

--no-lint, --no-violations (default)
  Show regular results.

--pessimistic
  Enable pessimistic mode: syntax errors are interpreted as the major Python version
  in use being incompatible.

--no-pessimistic (default)
  Disable pessimistic mode.

--eval-annotations
  Instructs parser that annotations will be manually evaluated in code, which
  changes minimum versions in certain cases. Otherwise, function and variable
  annotations are not evaluated at definition time. Apply this argument if
  code uses ``typing.get_type_hints`` or ``eval(obj.__annotations__)`` or
  otherwise forces evaluation of annotations.

--no-eval-annotations (default)
  Disable annotations evaluation.

--parse-comments (default)
  Parse for comments to influence exclusion of code for analysis via "``# novm``"
  and "``# novermin``".

--no-parse-comments
  Don't parse for comments. Not parsing comments can sometimes yield a speedup
  of 30-40%+.

--scan-symlink-folders
  Scan symlinks to folders to include in analysis.

--no-symlink-folders (default)
  Don't scan symlinks to folders to include in analysis. Symlinks to non-folders
  or top-level folders will always be scanned.

-f=FORMAT, --format=FORMAT
  Format to show results and output in. Supported formats:

  default
    Default formatting.
  colored
    Same as default, but prints with ANSI styling.
  parsable
    Each result is on form 'file:line:column:py2:py3:feature'. The
    last line has no path or line/column numbers and contains the minimum py2 and
    py3 versions. Minimum verbosity level is set to 3 but can be increased.
    Tips, hints, incompatible versions, and `--versions` are disabled. File paths
    containing ':' are ignored.
  github
    Same as parsable format, but each result is formatted as a GitHub
    Actions annotation. Minimum version messages are annotated as errors, and all
    other verbose messages as notices. The intent is that it be used for linting
    in a GitHub Actions pipeline.

--exclude=NAME
  Exclude full names, like 'email.parser.FeedParser', from analysis. Useful to
  ignore conditional logic that can trigger incompatible results. This option may
  be specified multiple times.

--exclude-file=FILE
  Exclude full names, like 'email.parser.FeedParser', from analysis but read from
  the specified file instead. Each line of the file constitutes an exclusion with
  the same format as with `--exclude`.

--no-exclude (default)
  Use no excludes. Clears any excludes specified before this.

--exclude-regex=PATTERN
  Exclude files from analysis by matching a regex pattern against their entire
  path as expanded from the Vermin command line. Patterns are matched using
  `re.search()`, so '^' or '$' anchors should be applied as needed.

--no-exclude-regex (default)
  Use no exclude patterns. Clears any exclude patterns specified before this.

--make-paths-absolute (default)
  Convert any relative paths from the command line into absolute paths. This
  affects the path printed to the terminal if a file fails a check, and requires
  ``--exclude-regex`` patterns to match absolute paths.

--no-make-paths-absolute
  Do not convert relative paths from the command line into absolute paths.

--backport=NAME
  Some features are sometimes backported into packages, in repositories such as PyPi,
  that are widely used but aren't in the standard language. If such a backport is
  specified as being used, the results will reflect that instead. Versioned
  backports are only used when minimum versions change. Unversioned backports must
  be the newest among versioned and unversioned. Supported backports:

  *argparse*
    https://pypi.org/project/argparse/ (2.3, 3.1)
  *asyncio*
    https://pypi.org/project/asyncio/ (!2, 3.3)
  *configparser*
    https://pypi.org/project/configparser/ (2.6, 3.0)
  *contextvars*
    https://pypi.org/project/contextvars/ (!2, 3.5)
  *dataclasses*
    https://pypi.org/project/dataclasses/ (!2, 3.6)
  *enum*
    https://pypi.org/project/enum34/ (2.4, 3.3)
  *faulthandler*
    https://pypi.org/project/faulthandler/ (2.6, 3.0)
  *importlib*
    https://pypi.org/project/importlib/ (2.3, 3.0)
  *ipaddress*
    https://pypi.org/project/ipaddress/ (2.6, 3.2)
  *mock*
    https://pypi.org/project/mock/ (!2, 3.6)
  *statistics*
    https://pypi.org/project/statistics/ (2.6, 3.4)
  *typing*
    https://pypi.org/project/typing/ (2.7, 3.2)
  *typing_extensions==4.0*
    https://pypi.org/project/typing-extensions/4.0.0/ (!2, 3.6)
  *typing_extensions==4.3*
    https://pypi.org/project/typing-extensions/4.3.0/ (!2, 3.7)
  *typing_extensions*
    https://pypi.org/project/typing-extensions/ (!2, 3.7)
  *zoneinfo*
    https://pypi.org/project/backports.zoneinfo/ (!2, 3.6)

--no-backport (default)
  Use no backports. Clears any backports specified before this.

--feature=NAME
  Some features are disabled by default due to being unstable:

  fstring-self-doc
    Detect self-documenting fstrings. Can in some cases wrongly report fstrings
    as self-documenting.
  union-types
    Detect union types `X | Y`. Can in some cases wrongly report union types due
    to having to employ heuristics.

--no-feature (default)
  Use no features. Clears any features specified before this.

Examples
========

Check the minimum compatible versions:

.. code-block:: console

  % ./vermin.py vermin
  Minimum required versions: 3.0
  Incompatible versions:     2.x

Check if the target version is supported:

.. code-block:: console

  % ./vermin.py -t=3.3 vermin
  Minimum required versions: 3.0
  Incompatible versions:     2.x
  Target versions not met:   3.3
  % echo $?
  1

List the unique versions required by the code:

.. code-block:: console

  % ./vermin.py --versions vermin
  Minimum required versions: 3.0
  Incompatible versions:     2.x
  Version range:             2.0, 2.6, 2.7, 3.0

Show the versions required for each file:

.. code-block:: console

  % ./vermin.py -v examples
  Detecting python files..
  Analyzing 6 files using 8 processes..
               /path/to/examples/formatv2.py
  2.7, 3.2     /path/to/examples/argparse.py
  2.7, 3.0     /path/to/examples/formatv3.py
  2.0, 3.0     /path/to/examples/printv3.py
  !2, 3.4      /path/to/examples/abc.py
               /path/to/examples/unknown.py
  Minimum required versions:   3.4
  Incompatible versions:       2.x

Show which code elements constitute the requirements:

.. code-block:: console

  % ./vermin.py -vv /path/to/examples/abc.py
  Detecting python files..
  Analyzing using 8 processes..
  !2, 3.4      /path/to/examples/abc.py
    'abc' requires 2.6, 3.0
    'abc.ABC' requires !2, 3.4

  Minimum required versions: 3.4
  Incompatible versions:     2.x

Show the line and column numbers of the requirements:

.. code-block:: console

  % ./vermin.py -vvv /path/to/examples/abc.py
  Detecting python files..
  Analyzing using 8 processes..
  !2, 3.4      /path/to/examples/abc.py
    L1 C7: 'abc' requires 2.6, 3.0
    L2: 'abc.ABC' requires !2, 3.4

  Minimum required versions: 3.4
  Incompatible versions:     2.x

Output the results in a machine-readable format:

.. code-block:: console

  % ./vermin.py -f parsable /path/to/examples/abc.py
  /path/to/examples/abc.py:1:7:2.6:3.0:'abc' module
  /path/to/examples/abc.py:2::!2:3.4:'abc.ABC' member
  /path/to/examples/abc.py:::!2:3.4:
  :::!2:3.4:


See also
========

vermin.ini(5), sample.vermin.ini
