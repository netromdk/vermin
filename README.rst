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
matches against internal dictionaries with **2974** rules, covering v2.0-2.7 and v3.0-3.8, divided
into **134** modules, **2180** classes/functions/constants members of modules, **628** kwargs of
functions, **4** strftime directives, **3** bytes format directives, **2** array typecodes, **3**
codecs error handler names, and **20** codecs encodings. Including looking for v2/v3 ``print expr``
and ``print(expr)``, ``long``, f-strings, coroutines (``async`` and ``await``), asynchronous
generators (``await`` and ``yield`` in same function), asynchronous comprehensions, ``await`` in
comprehensions, boolean constants, named expressions, keyword-only parameters, positional-only
parameters, ``yield from``, exception context cause (``raise .. from ..``), ``dict`` comprehensions,
infix matrix multiplication, ``"..".format(..)``, imports (``import X``, ``from X import Y``, ``from
X import *``), function calls wrt. name and kwargs, ``strftime`` + ``strptime`` directives used,
function and variable annotations (also ``Final`` and ``Literal``), ``continue`` in ``finally``
block, modular inverse ``pow()``, array typecodes, codecs error handler names, encodings, ``%``
formatting and directives for bytes and bytearray, and generalized unpacking. It tries to detect and
ignore user-defined functions, classes, arguments, and variables with names that clash with
library-defined symbols.

Backports of the standard library, like ``typing``, can be enabled for better results.

The project is fairly well-tested with **3240** unit and integration tests employing **3854**
assertions.

It is recommended to use the most recent Python version to run Vermin on projects since Python's own
language parser is used to detect language features, like f-strings since Python 3.6 etc.

Usage
=====

It is fairly straightforward to use Vermin::

  ./vermin.py /path/to/your/project

Or via `PyPi <https://pypi.python.org/pypi/vermin/>`__::

  % pip install vermin
  % vermin /path/to/your/project

Or via `Arch Linux (AUR) <https://aur.archlinux.org/packages/python-vermin/>`__::

  % yay -S python-vermin

When using continuous integration (CI) tools, like `Travis CI <https://travis-ci.org/>`_, Vermin can
be used to check that the minimum required versions didn't change. The following is an excerpt::

  install:
  - ./setup_virtual_env.sh
  - pip install vermin
  script:
  - vermin -t=2.7 -t=3 project_package otherfile.py

Caveats
=======

Self-documenting fstrings detection has been disabled by default because the built-in AST cannot
distinguish ``f'{a=}'`` from ``f'a={a}'``, for instance, since it optimizes some information away
(`#39 <https://github.com/netromdk/vermin/issues/39>`__). And this incorrectly marks some source
code as using fstring self-doc when only using general fstring. To enable (unstable) fstring
self-doc detection, use ``--feature fstring-self-doc``.

Examples
========

::

  % ./vermin.py -q vermin
  Minimum required versions: 2.7, 3.0

  % ./vermin.py -q -t=3.3 vermin
  Minimum required versions: 2.7, 3.0
  Target versions not met:   3.3
  % echo $?
  1

  % ./vermin.py -q --versions vermin
  Minimum required versions: 2.7, 3.0
  Version range:             2.0, 2.2, 2.5, 2.7, 3.0

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

Lax Mode
========

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

Analysis Exclusions
===================

Another approach to conditional logic than lax mode, is to exclude modules, members, kwargs, codecs
error handler names, or codecs encodings by name from being analysed via argument ``--exclude
<name>`` (multiple can be specified). Consider the following code block that checks if
``PROTOCOL_TLS`` is an attribute of ``ssl``:

.. code-block:: python

  import ssl
  tls_version = ssl.PROTOCOL_TLSv1
  if hasattr(ssl, "PROTOCOL_TLS"):
    tls_version = ssl.PROTOCOL_TLS

It will state that "'ssl.PROTOCOL_TLS' requires (2.7, 3.6)" but to exclude that from the results,
use ``--exclude 'ssl.PROTOCOL_TLS'``. Afterwards, only "'ssl' requires (2.6, 3.0)" will be shown and
the final minimum required versions are v2.6 and v3.0 instead of v2.7 and v3.6.

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

Contributing
============

Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible. For PRs, make sure to keep the
code vanilla Python and run ``make test`` first. Note that code must remain valid and working on
Python v2.7+ and v3+.
