[![Build Status](https://travis-ci.org/netromdk/minpy.svg?branch=master)](https://travis-ci.org/netromdk/minpy)
![Commits since last release](https://img.shields.io/github/commits-since/netromdk/minpy/latest.svg)

# minpy
Concurrently detect the minimum Python versions needed to run code.

Since the code is vanilla Python, and it doesn't have any external dependencies, it works with v2.7+ and v3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and matches against internal dictionaries with 222 rules divided into 47 modules, 146 classes/functions/constants members of modules, 26 kwargs of functions, and 4 strftime directives. Including looking for v2/v3 `print expr` and `print(expr)`, `long`, f-strings, `"..".format(..)`, imports (`import X`, `from X import Y`, `from X import *`), function calls wrt. name and kwargs, and `strftime`+`strptime` directives used.

## Usage
It is fairly straightforward to use Minpy:
```
./minpy.py /path/to/your/project
```

## Examples
```
% ./minpy.py
Minpy 0.1
Usage: ./minpy.py [options] <python source files and folders..>

Options:
  -q      Quite mode. It only prints the final versions verdict.
  -v..    Verbosity level 1 to 2. -v shows less than -vv but more than no verbosity.
  -i      Ignore incompatible version warnings.
  -p=X    Use X concurrent processes to analyze files (defaults to all cores = 8).
  -d      Dump AST node visits.

% ./minpy.py -q minpy.py
Minimum required versions: 2.7, 3.0

% ./minpy.py -v examples
Detecting python files..
Analyzing 6 files using 8 processes..
             /path/to/examples/formatv2.py
2.7, 3.2     /path/to/examples/argparse.py
2.7, 3.0     /path/to/examples/formatv3.py
2.0, 3.0     /path/to/examples/printv3.py
!2, 3.4      /path/to/examples/abc.py
             /path/to/examples/unknown.py
Minimum required versions: !2, 3.4
```
When it yields `!2` or `!3` it means that it explicitly cannot run on that version.

## Contributing
Contributions are very welcome, especially adding and updating detection rules of modules, functions, classes etc. to cover as many Python versions as possible. For PRs, make sure to keep the code vanilla Python and run `make test` first. Note that code must be remain valid and working on Python v2.7+ and v3+.
