[![Build Status](https://travis-ci.org/netromdk/minpy.svg?branch=master)](https://travis-ci.org/netromdk/minpy)

# minpy
Concurrently detect the minimum Python version needed to run code.

Everything is contained within "minpy.py" - no other file is necessary.

Since the code is vanilla Python, and it doesn't have any external dependencies, it works with v2.7+ and v3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and matches against internal dictionaries of 39 modules, 88 classes/functions/constants members of modules, and 16 kwargs of functions. Including looking for v2/v3 `print expr` and `print(expr)`, `"..".format(..)`, imports (`import X`, `from X import Y`, `from X import *`), and function calls wrt. name and kwargs.

## Usage
It is fairly straightforward to use Minpy:
```
./minpy.py /path/to/your/project
```

Or copy "minpy.py" to your project:
```
./minpy.py .
```

## Examples
```
% ./minpy.py
Usage: ./minpy.py [options] <python source files and folders..>

Options:
  -v..    Verbosity level 1 to 2. -v shows less than -vv but more than no verbosity.
  -i      Ignore incompatible version warnings.
  -p=X    Use X concurrent processes to analyze files (defaults to all cores = 8).

% ./minpy.py minpy.py
Detecting python files..
Analyzing using 8 processes..
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
