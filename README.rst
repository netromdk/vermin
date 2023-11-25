|Test Status| |Analyze Status| |CodeQL Status| |Coverage| |PyPI version| |Commits since last| |Downloads| |CII best practices|

.. |PyPI version| image:: https://badge.fury.io/py/vermin.svg
   :target: https://pypi.python.org/pypi/vermin/

.. |Test Status| image:: https://github.com/netromdk/vermin/workflows/Test/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |Analyze Status| image:: https://github.com/netromdk/vermin/workflows/Analyze/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |CodeQL Status| image:: https://github.com/netromdk/vermin/workflows/CodeQL/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/security/code-scanning

.. |Snyk Status| image:: https://github.com/netromdk/vermin/workflows/Snyk%20Schedule/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |Coverage| image:: https://coveralls.io/repos/github/netromdk/vermin/badge.svg?branch=master
   :target: https://coveralls.io/github/netromdk/vermin?branch=master

.. |Commits since last| image:: https://img.shields.io/github/commits-since/netromdk/vermin/latest.svg

.. |Downloads| image:: https://static.pepy.tech/personalized-badge/vermin?period=total&units=international_system&left_color=gray&right_color=blue&left_text=Downloads
   :target: https://pepy.tech/project/vermin

.. |CII best practices| image:: https://bestpractices.coreinfrastructure.org/projects/6451/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/6451

Vermin
******

Concurrently detect the minimum Python versions needed to run code. Additionally, since the code is
vanilla Python, and it doesn't have any external dependencies, it can be run with v3+ but still
includes detection of v2.x functionality.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and
matches against internal dictionaries with **3796** rules, covering v2.0-2.7 and v3.0-3.12, divided
into **178** modules, **2614** classes/functions/constants members of modules, **875** kwargs of
functions, **4** strftime directives, **3** bytes format directives, **2** array typecodes, **3**
codecs error handler names, **20** codecs encodings, **78** builtin generic annotation types, **9**
builtin dict union (``|``) types, **8** builtin dict union merge (``|=``) types, and **2** user
function decorators.

Backports of the standard library, like ``typing``, can be enabled for better results. Get full list
of backports via ``--help``.

The project is fairly well-tested with **4008** unit and integration tests that are executed on
Linux, macOS, and Windows.

It is recommended to use the most recent Python version to run Vermin on projects since Python's own
language parser is used to detect language features, like f-strings since Python 3.6 etc.


Table of Contents
=================

* `Usage <#usage>`__
* `Features <#features>`__
* `Caveats <#caveats>`__
* `Configuration File <#configuration-file>`__
* `Examples <#examples>`__
* `Linting (showing only target versions violations) <#linting-showing-only-target-versions-violations>`__
* `API (experimental) <#api-experimental>`__
* `Analysis Exclusions <#analysis-exclusions>`__
* `Parsable Output <#parsable-output>`__
* `Contributing <#contributing>`__

Usage
=====

It is fairly straightforward to use Vermin.

Running it from the repository either directly or through specific interpreter::

  % ./vermin.py /path/to/your/project        # (1) executing via `/usr/bin/env python`
  % python3 vermin.py /path/to/your/project  # (2) specifically `python3`

Or if installed via `PyPi <https://pypi.python.org/pypi/vermin/>`__::

  % pip install vermin
  % vermin /path/to/your/project

`Homebrew <https://brew.sh>`__ (`pkg <https://formulae.brew.sh/formula/vermin#default>`__)::

  % brew install vermin

`Spack <https://spack.io>`__ (`pkg <https://github.com/spack/spack/blob/develop/var/spack/repos/builtin/packages/py-vermin/package.py>`__)::

  % git clone https://github.com/spack/spack.git
  % . spack/share/spack/setup-env.sh  # depending on shell
  % spack install py-vermin
  % spack load py-vermin

`Arch Linux (AUR) <https://aur.archlinux.org/packages/python-vermin/>`__::

  % yay -S python-vermin

When using continuous integration (CI) tools, like `Travis CI <https://travis-ci.org/>`_, Vermin can
be used to check that the minimum required versions didn't change. The following is an excerpt::

  install:
  - ./setup_virtual_env.sh
  - pip install vermin
  script:
  - vermin -t=2.7 -t=3 project_package otherfile.py

Vermin can also be used as a `pre-commit <https://pre-commit.com/>`__ hook:

.. code-block:: yaml

  repos:
    - repo: https://github.com/netromdk/vermin
      rev: GIT_SHA_OR_TAG  # ex: 'e88bda9' or 'v1.3.4'
      hooks:
        - id: vermin
          # specify your target version here, OR in a Vermin config file as usual:
          args: ['-t=3.8-', '--violations']
          # (if your target is specified in a Vermin config, you may omit the 'args' entry entirely)

When using the hook, a target version must be specified via a Vermin config file in your package,
or via the ``args`` option in your ``.pre-commit-config.yaml`` config. If you're passing the target
via ``args``, it's recommended to also include ``--violations`` (shown above).

If you're using the ``vermin-all`` hook, you can specify any target as you usually would. However,
if you're using the ``vermin`` hook, your target must be in the form of ``x.y-`` (as opposed to
``x.y``), otherwise you will run into issues when your staged changes meet a minimum version that
is lower than your target.

See the `pre-commit docs <https://pre-commit.com/#quick-start>`__ for further general information
on how to get hooks set up on your project.

Features
========

Features detected include v2/v3 ``print expr`` and ``print(expr)``, ``long``, f-strings, coroutines
(``async`` and ``await``), asynchronous generators (``await`` and ``yield`` in same function),
asynchronous comprehensions, ``await`` in comprehensions, asynchronous ``for``-loops, boolean
constants, named expressions, keyword-only parameters, positional-only parameters, ``nonlocal``,
``yield from``, exception context cause (``raise .. from ..``), ``except*``, ``set`` literals,
``set`` comprehensions, ``dict`` comprehensions, infix matrix multiplication, ``"..".format(..)``,
imports (``import X``, ``from X import Y``, ``from X import *``), function calls wrt. name and
kwargs, ``strftime`` + ``strptime`` directives used, function and variable annotations (also
``Final`` and ``Literal``), ``continue`` in ``finally`` block, modular inverse ``pow()``, array
typecodes, codecs error handler names, encodings, ``%`` formatting and directives for bytes and
bytearray, ``with`` statement, asynchronous ``with`` statement, multiple context expressions in a
``with`` statement, multiple context expressions in a ``with`` statement grouped with parenthesis,
unpacking assignment, generalized unpacking, ellipsis literal (``...``) out of slices, dictionary
union (``{..}  | {..}``), dictionary union merge (``a = {..}; a |= {..}``), builtin generic type
annotations (``list[str]``), function decorators, class decorators, relaxed decorators,
``metaclass`` class keyword, pattern matching with ``match``, union types written as ``X | Y``, and
type alias statements (``type X = SomeType``). It tries to detect and ignore user-defined functions,
classes, arguments, and variables with names that clash with library-defined symbols.

Caveats
=======

For frequently asked questions, check out the `FAQ discussions
<https://github.com/netromdk/vermin/discussions/categories/faq>`__.

Self-documenting fstrings detection has been disabled by default because the built-in AST cannot
distinguish ``f'{a=}'`` from ``f'a={a}'``, for instance, since it optimizes some information away
(`#39 <https://github.com/netromdk/vermin/issues/39>`__). And this incorrectly marks some source
code as using fstring self-doc when only using general fstring. To enable (unstable) fstring
self-doc detection, use ``--feature fstring-self-doc``.

Detecting union types (``X | Y`` `PEP 604 <https://www.python.org/dev/peps/pep-0604/>`__) can be
tricky because Vermin doesn't know all underlying details of constants and types since it parses and
traverses the AST. For this reason, heuristics are employed and this can sometimes yield incorrect
results (`#103 <https://github.com/netromdk/vermin/issues/103>`__). To enable (unstable) union types
detection, use ``--feature union-types``.

Function and variable annotations aren't evaluated at definition time when ``from __future__ import
annotations`` is used (`PEP 563 <https://www.python.org/dev/peps/pep-0563/>`__). This is why
``--no-eval-annotations`` is on by default (since v1.1.1, `#66
<https://github.com/netromdk/vermin/issues/66>`__). If annotations are being evaluated at runtime,
like using ``typing.get_type_hints`` or evaluating ``__annotations__`` of an object,
``--eval-annotations`` should be used for best results.

Configuration File
==================

Vermin automatically tries to detect a config file, starting in the current working directory where
it is run, following parent folders until either the root or project boundary files/folders are
reached. However, if ``--config-file`` is specified, no config is auto-detected and loaded.

Config file names being looked for: ``vermin.ini``, ``vermin.conf``, ``.vermin``, ``setup.cfg``

Project boundary files/folders: ``.git``, ``.svn``, ``.hg``, ``.bzr``, ``_darcs``, ``.fslckout``,
``.p4root``, ``.pijul``

A sample config file can be found `here <sample.vermin.ini>`__.

Note that Vermin config can be in the same INI file as other configs, like the commonly used
``setup.cfg``:

.. code-block:: ini

  [vermin]
  verbose = 1
  processes = 4

  [flake8]
  ignore = E111,F821

Examples
========

.. code-block:: console

  % ./vermin.py vermin
  Minimum required versions: 3.0
  Incompatible versions:     2

  % ./vermin.py -t=3.3 vermin
  Minimum required versions: 3.0
  Incompatible versions:     2
  Target versions not met:   3.3
  % echo $?
  1

  % ./vermin.py --versions vermin
  Minimum required versions: 3.0
  Incompatible versions:     2
  Version range:             2.0, 2.6, 2.7, 3.0

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
  Incompatible versions:         2

  % ./vermin.py -vv /path/to/examples/abc.py
  Detecting python files..
  Analyzing using 8 processes..
  !2, 3.4      /path/to/examples/abc.py
    'abc' requires 2.6, 3.0
    'abc.ABC' requires !2, 3.4

  Minimum required versions: 3.4
  Incompatible versions:     2

  % ./vermin.py -vvv /path/to/examples/abc.py
  Detecting python files..
  Analyzing using 8 processes..
  !2, 3.4      /path/to/examples/abc.py
    L1 C7: 'abc' requires 2.6, 3.0
    L2: 'abc.ABC' requires !2, 3.4

  Minimum required versions: 3.4
  Incompatible versions:     2

  % ./vermin.py -f parsable /path/to/examples/abc.py
  /path/to/examples/abc.py:1:7:2.6:3.0:'abc' module
  /path/to/examples/abc.py:2::!2:3.4:'abc.ABC' member
  /path/to/examples/abc.py:::!2:3.4:
  :::!2:3.4:

See `Parsable Output <#parsable-output>`__ for more information about parsable output format.

Linting: Showing only target versions violations
================================================

Vermin shows lots of useful minimum version results when run normally, but it can also be used as a
linter to show only rules violating specified target versions by using ``--violations`` (or
``--lint``) and one or two ``--target`` values. Verbosity level 2 is automatically set when showing
only violations, but can be increased if necessary. The final versions verdict is still calculated
and printed at the end and the program exit code signifies whether the specified targets were met
(``0``) or violated (``1``). However, if no rules are triggered the exit code will be ``0`` due to
inconclusivity.

.. code-block:: console

  % cat test.py
  import argparse  # 2.7, 3.2
  all()            # 2.5, 3.0
  enumerate()      # 2.3, 3.0

  % ./vermin.py -t=2.4- -t=3 --violations test.py ; echo $?
  Detecting python files..
  Analyzing using 8 processes..
  2.7, 3.2     test.py
    'all' member requires 2.5, 3.0
    'argparse' module requires 2.7, 3.2

  Minimum required versions: 2.7, 3.2
  Target versions not met:   2.4-, 3.0
  1

The two first lines violate the targets but the third line matches and is therefore not shown.

API (experimental)
==================

Information such as minimum versions, used functionality constructs etc. can also be accessed
programmatically via the ``vermin`` Python module, though it's an experimental feature. It is still
recommended to use the command-line interface.

.. code-block:: python

  >>> import vermin as V
  >>> V.version_strings(V.detect("a = long(1)"))
  '2.0, !3'

  >>> config = V.Config()
  >>> config.add_exclusion("long")
  >>> V.version_strings(V.detect("a = long(1)", config))
  '~2, ~3'

  >>> config.set_verbose(3)
  >>> v = V.visit("""from argparse import ArgumentParser
  ... ap = ArgumentParser(allow_abbrev=True)
  ... """, config)
  >>> print(v.output_text(), end="")
  L1 C5: 'argparse' module requires 2.7, 3.2
  L2: 'argparse.ArgumentParser(allow_abbrev)' requires !2, 3.5
  >>> V.version_strings(v.minimum_versions())
  '!2, 3.5'

Analysis Exclusions
===================

Analysis exclusion can be necessary in certain cases. The argument ``--exclude <name>`` (multiple
can be specified) can be used to exclude modules, members, kwargs, codecs error handler names, or
codecs encodings by name from being analysed via . Consider the following code block that checks if
``PROTOCOL_TLS`` is an attribute of ``ssl``:

.. code-block:: python

  import ssl
  tls_version = ssl.PROTOCOL_TLSv1
  if hasattr(ssl, "PROTOCOL_TLS"):
    tls_version = ssl.PROTOCOL_TLS

It will state that "'ssl.PROTOCOL_TLS' requires 2.7, 3.6" but to exclude that from the results, use
``--exclude 'ssl.PROTOCOL_TLS'``. Afterwards, only "'ssl' requires 2.6, 3.0" will be shown and the
final minimum required versions are v2.6 and v3.0 instead of v2.7 and v3.6.

Code can even be excluded on a more fine grained level using the ``# novermin`` or ``# novm``
comments at line level. The following yields the same behavior as the previous code block, but only
for that particular ``if`` and its body:

.. code-block:: python

  import ssl
  tls_version = ssl.PROTOCOL_TLSv1
  if hasattr(ssl, "PROTOCOL_TLS"):  # novermin
    tls_version = ssl.PROTOCOL_TLS

In scenarios where multiple tools are employed that use comments for various features, exclusions
can be defined by having ``#`` for each comment "segment":

.. code-block:: python

  if hasattr(ssl, "PROTOCOL_TLS"):  # noqa # novermin # pylint: disable=no-member
    tls_version = ssl.PROTOCOL_TLS

Note that if a code base does not have any occurrences of ``# novermin`` or ``# novm``, speedups up
to 30-40%+ can be achieved by using the ``--no-parse-comments`` argument or ``parse_comments = no``
config setting.

Parsable Output
===============

For scenarios where the results of Vermin output is required, it is recommended to use the parsable
output format (``--format parsable``) instead of the default output. With this format enabled, each
line will be on the form:

.. code-block::

  <file>:<line>:<column>:<py2>:<py3>:<feature>

The ``<line>`` and ``<column>`` are only shown when the verbosity level is high enough, otherwise
they are empty.

Each feature detected per processed file will have the ``<feature>`` defined on an individual
line. The last line of the processed file will have a special line with the corresponding ``<file>``
and no ``<feature>``, constituting the minimum versions of that file:

.. code-block::

   <file>:::<py2>:<py3>:

The very last line is the final minimum versions results of the entire scan and therefore has no
``<file>`` and ``<feature>``:

.. code-block::

   :::<py2>:<py3>:

Inspection of example output
----------------------------

.. code-block:: console

  % ./vermin.py -f parsable /path/to/project
  /path/to/project/abc.py:1:7:2.6:3.0:'abc' module
  /path/to/project/abc.py:2::!2:3.4:'abc.ABC' member
  /path/to/project/abc.py:::!2:3.4:
  /path/to/project/except_star.py:::~2:~3:
  /path/to/project/annotations.py:::2.0:3.0:print(expr)
  /path/to/project/annotations.py:1::!2:3.0:annotations
  /path/to/project/annotations.py:::!2:3.0:
  :::!2:3.4:

``abc.py`` requires ``!2`` and ``3.4`` via:

.. code-block::

  /path/to/project/abc.py:::!2:3.4:

``except_star.py`` requires ``~2`` and ``~3`` via:

.. code-block::

  /path/to/project/except_star.py:::~2:~3:

And ``annotations.py`` requires ``!2`` and ``3.0`` via:

.. code-block::

  /path/to/project/annotations.py:::!2:3.0:

That means that the final result is ``!2`` and ``3.4``, which is shown by the last line:

.. code-block::

  :::!2:3.4:

Contributing
============

Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible. See `CONTRIBUTING.md
<CONTRIBUTING.md>`__ for more information.
