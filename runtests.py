#!/usr/bin/env python
import os
import sys
import unittest
from time import time

ROOT_MODULE = "tests."

# Isolate tests to be run "suite[.Class.test_method]". Class and method are optional.
ISOLATE = os.getenv("VERMIN_TEST_ISOLATE")
if ISOLATE is not None:
  ISOLATE = ROOT_MODULE + ISOLATE.strip()

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
  # skip suite if doesn't match isolation filter
  suite = ROOT_MODULE + suite
  if ISOLATE:
    if ISOLATE != suite and not ISOLATE.startswith(suite + "."):
      print("Skipping test suite: {}".format(suite))
      return 0
    print("Isolated test(s): {}".format(ISOLATE))
  print("Running test suite: {}".format(suite))
  # Buffer output such that only on test errors will stdout/stderr be shown.
  if ISOLATE:
    res = unittest.main(None, argv=[sys.argv[0], ISOLATE], exit=False, buffer=True).result
  else:
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
