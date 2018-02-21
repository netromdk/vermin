#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import ast
from pprint import pprint

# Module requirements: name -> min version per major
MOD_REQS = {"argparse": (2.7, 3.2)}

def parse_source(source):
  """Parse python source into an AST."""
  return ast.parse(source)

def parse_source_file(path):
  """Parse python source file into an AST."""
  with open(path, "r") as fp:
    return parse_source(fp.read())

class SourceVisitor(ast.NodeVisitor):
  pass

# TODO: Find modules by import: import X and from X import Y..
# TODO: For each found module check version requirements.
def find_modules(node):
  pass

# TODO: Maybe impl. class with visitor pattern that keeps track of the sub node it is visiting, like
# import X, from X import Y, class, function etc.

# TODO: Detect version from language use, like "print expr" (2) vs "print(expr)" (3)

if __name__ == "__main__":
  try:
    if len(sys.argv) == 2:
      node = parse_source_file(sys.argv[1])
    else:
      #node = parse_source("import argparse")
      node = parse_source("from argparse import ArgumentParser")
      pprint(ast.dump(node))
  except SyntaxError as err:
    print("Could not parse input: {}".format(err))
