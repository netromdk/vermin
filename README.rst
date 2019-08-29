|PyPI version| |Build Status| |Coverage| |Commits since last|

.. |PyPI version| image:: https://badge.fury.io/py/vermin.svg
   :target: https://pypi.python.org/pypi/vermin/

.. |Build Status| image:: https://travis-ci.org/netromdk/vermin.svg?branch=master
   :target: https://travis-ci.org/netromdk/vermin

.. |Coverage| image:: https://coveralls.io/repos/github/netromdk/vermin/badge.svg?branch=master
   :target: https://coveralls.io/github/netromdk/vermin?branch=master

.. |Commits since last| image:: https://img.shields.io/github/commits-since/netromdk/vermin/latest.svg

Vermin
******

Concurrently detect the minimum Python versions needed to run code. Additionally, since the code is
vanilla Python, and it doesn't have any external dependencies, it works with v2.7+ and v3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and
matches against internal dictionaries with **1000** rules divided into **124** modules, **668**
classes/functions/constants members of modules, **179** kwargs of functions, **4** strftime
directives, **2** array typecodes, **3** codecs error handler names, and **20** codecs
encodings. Including looking for v2/v3 ``print expr`` and ``print(expr)``, ``long``, f-strings,
coroutines (``async`` and ``await``), boolean constants, named expressions, positional-only
parameters, ``"..".format(..)``, imports (``import X``, ``from X import Y``, ``from X import *``),
function calls wrt. name and kwargs, ``strftime`` + ``strptime`` directives used, and function,
function and variable annotations, array typecodes, codecs error handler names and encodings. It
tries to detect and ignore user-defined functions, classes, arguments, and variables with names that
clash with library-defined symbols.

Usage
=====

It is fairly straightforward to use Vermin::

  ./vermin.py /path/to/your/project

Or via `PyPi <https://pypi.python.org/pypi/vermin/>`__::

  % pip install vermin
  % vermin /path/to/your/project

When using continuous integration (CI) tools, like `Travis CI <https://travis-ci.org/>`_, Vermin can
be used to check that the minimum required versions didn't change. The following is an exerpt::

  install:
  - ./setup_virtual_env.sh
  - pip install vermin
  script:
  - vermin -t=2.7 -t=3 project_package otherfile.py

Examples
========

::

  % ./vermin.py
  Vermin 0.6.3
  Usage: ./vermin.py [options] <python source files and folders..>

  Options:
    -q    Quite mode. It only prints the final versions verdict.
    -v..  Verbosity level 1 to 3. -v, -vv, and -vvv shows increasingly more information.
          -v    will show the individual versions required per file.
          -vv   will also show which modules, functions etc. that constitutes
                the requirements.
          -vvv  will also show line/col numbers.
    -t=V  Target version that files must abide by. Can be specified once or twice.
          If not met Vermin will exit with code 1.
    -p=N  Use N concurrent processes to analyze files (defaults to all cores = 8).
    -i    Ignore incompatible version warnings.
    -l    Lax mode: ignores conditionals (if, ternary, for, while, try, bool op) on AST
          traversal, which can be useful when minimum versions are detected in
          conditionals that it is known does not affect the results.
    -d    Dump AST node visits.
    --hidden
          Analyze 'hidden' files and folders starting with '.' (ignored by default).

  Results interpretation:
    ~2       No known reason it won't work with py2.
    !2       It is known that it won't work with py2.
    2.5, !3  Works with 2.5+ but it is known it won't work with py3.
    ~2, 3.4  No known reason it won't work with py2, works with 3.4+

  % ./vermin.py -q vermin
  Minimum required versions: 2.7, 3.0

  % ./vermin.py -q -t=3.3 vermin
  Minimum required versions: 2.7, 3.0
  Target versions not met:   3.3
  % echo $?
  1

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
    'abc' requires (2.6, 3.0)
    'abc.ABC' requires (None, 3.4)

  Minimum required versions: 3.4
  Incompatible versions:     2

  % ./vermin.py -vvv /path/to/examples/abc.py
  Detecting python files..
  Analyzing using 8 processes..
  !2, 3.4      /path/to/examples/abc.py
    L1 C7: 'abc' requires (2.6, 3.0)
    L2: 'abc.ABC' requires (None, 3.4)

  Minimum required versions: 3.4
  Incompatible versions:     2

Known Limitations
=================

Vermin parses Python source code into abstract syntax trees (ASTs) which it traverses to do
analysis. However, it doesn't do conditional logic, i.e. deciding which branches will be taken at
runtime, since it can cause unexpected side-effects to actually evaluate code. As an example,
analysis of the following:

.. code-block:: python

  if False:
    print(f"..but I won't be evaluated")

Will yield "f-strings require 3.6+" even though the branch will not be evaluated at runtime.

The lax mode, via argument ``-l``, was created to circumvent cases like this. *But it's not a
perfect solution* since it will skip all ``if``, ternarys, ``for``, ``while``, ``try``, and boolean
operations. Therefore it is recommended to run with and without lax mode to get a better
understanding of individual cases.

Contributing
============

Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible. For PRs, make sure to keep the
code vanilla Python and run ``make test`` first. Note that code must be remain valid and working on
Python v2.7+ and v3+.
