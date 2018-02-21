#!/usr/bin/env python

# TODO: This script needs to use the lowest possible python to run so that people don't need another
# version to determine what minimum version they need!

import sys
import parser
from symbol import sym_name
from token import tok_name
from pprint import pprint

# Module requirements: name -> min version per major
MOD_REQS = {"argparse": (2.7, 3.2)}

def parse_source(source):
  """Parse python source into a tree of statements and expressions."""
  return parser.suite(source).totuple()

def parse_source_file(path):
  """Parse python source file into a tree of statements and expressions."""
  with open(path, "r") as fp:
    return parse_source(fp.read())

def parse_expression(expr):
  """Parse python expression into a tree of statements and expression."""
  return parser.expr(expr).totuple()

def symbol_or_token_name(num):
  if num in sym_name:
    return sym_name[num]
  if num in tok_name:
    return tok_name[num]
  return None

def print_tree(tree, indent=0, parent=None):
  if isinstance(tree, tuple):
    for elm in tree:
      indent_str = "  " * indent
      if isinstance(elm, int):
        print(indent_str, symbol_or_token_name(elm), "({})".format(elm))
      elif isinstance(elm, tuple):
        print_tree(elm, indent=indent+1, parent=tree)
      else:
        print(indent_str, elm, type(elm))

# TODO: Find modules by import: import X and from X import Y..
# TODO: For each found module check version requirements.
def find_modules(tree):
  pass

# TODO: Maybe impl. class with visitor pattern that keeps track of the sub tree it is visiting, like
# import X, from X import Y, class, function etc.

# TODO: Detect version from language use, like "print expr" (2) vs "print(expr)" (3)

if __name__ == "__main__":
  try:
    if len(sys.argv) == 2:
      tree = parse_source_file(sys.argv[1])
    else:
      tree = parse_source("import argparse")
      #tree = parse_source("from argparse import ArgumentParser")
    print_tree(tree)
  except SyntaxError as err:
    print("Could not parse input: {}".format(err))
