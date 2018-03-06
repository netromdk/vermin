Vermin
======

Concurrently detect the minimum Python versions needed to run code.

Since the code is vanilla Python, and it doesn't have any external dependencies, it works with v2.7+
and v3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and
matches against internal dictionaries with 222 rules divided into 47 modules, 146
classes/functions/constants members of modules, 26 kwargs of functions, and 4 strftime
directives. Including looking for v2/v3 print expr and print(expr), long, f-strings,
"..".format(..), imports (import X, from X import Y, from X import *), function calls wrt. name and
kwargs, and strftime+strptime directives used.
