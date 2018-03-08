|PyPI version| |Build Status| |Coverage|

.. |PyPI version| image:: https://badge.fury.io/py/vermin.svg
   :target: https://pypi.python.org/pypi/vermin/

.. |Build Status| image:: https://travis-ci.org/netromdk/vermin.svg?branch=master
   :target: https://travis-ci.org/netromdk/vermin

.. |Coverage| image:: https://coveralls.io/repos/github/netromdk/vermin/badge.svg?branch=master
   :target: https://coveralls.io/github/netromdk/vermin?branch=master

Vermin
******

Concurrently detect the minimum Python versions needed to run code. Additionally, since the code is
vanilla Python, and it doesn't have any external dependencies, it works with v2.7+ and v3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and
matches against internal dictionaries with 222 rules divided into 47 modules, 146
classes/functions/constants members of modules, 26 kwargs of functions, and 4 strftime
directives. Including looking for v2/v3 ``print expr`` and ``print(expr)``, ``long``, f-strings,
``"..".format(..)``, imports (``import X``, ``from X import Y``, ``from X import *``), function
calls wrt. name and kwargs, and ``strftime`` + ``strptime`` directives used.

Usage
=====

It is fairly straightforward to use Vermin::

  ./vermin.py /path/to/your/project

Or via `PyPi <https://pypi.python.org/pypi/vermin/>`__::

  % pip install vermin
  % vermin /path/to/your/project

Examples
========

::

  % ./vermin.py
  Vermin 0.2.3
  Usage: ./vermin.py [options] <python source files and folders..>

  Options:
    -q      Quite mode. It only prints the final versions verdict.
    -v..    Verbosity level 1 to 2. -v shows less than -vv but more than no verbosity.
    -t=V    Target version that files must abide by. Can be specified once or twice.
            If not met Vermin will exit with code 1.
    -p=N    Use N concurrent processes to analyze files (defaults to all cores = 8).
    -i      Ignore incompatible version warnings.
    -d      Dump AST node visits.

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

Contributing
============

Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible. For PRs, make sure to keep the
code vanilla Python and run ``make test`` first. Note that code must be remain valid and working on
Python v2.7+ and v3+.
