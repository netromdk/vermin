#!/usr/bin/env python
import sys
import unittest
from time import time

SUITES = (
  "general",
  "config",
  "arguments",
  "lang",
  "module",
  "builtin_classes",
  "class",
  "exception",
  "builtin_functions",
  "builtin_constants",
  "builtin_exceptions",
  "function",
  "constants",
  "decorators",
  "kwargs",
  "strftime_directive",
  "annotation",
  "maybe_annotations",
  "array_typecodes",
  "codecs_error_handlers",
  "codecs_encodings",
  "exclusions",
  "comment_exclusions",
  "backports",
  "bytes_directive",
  "violations",
)

def runsuite(suite):
  suite = "tests.{}".format(suite)
  print("Running test suite: {}".format(suite))
  # Buffer output such that only on test errors will stdout/stderr be shown.
  res = unittest.main(suite, exit=False, buffer=True).result
  if len(res.failures) > 0 or len(res.errors) > 0:
    sys.exit(-1)
  return res.testsRun

def execute():
  total_tests = 0
  for suite in SUITES:
    total_tests += runsuite(suite)
  return total_tests

if __name__ == '__main__':
  start, total_tests = time(), execute()
  secs = time() - start
  print("Ran {} tests ({} suites) in {:.3f}s".format(total_tests, len(SUITES), secs))
