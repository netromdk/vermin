#!/usr/bin/env python
import sys
import unittest

def runsuite(suite):
  print("Running test suite: {}".format(suite))
  res = unittest.main(suite, exit=False).result
  if len(res.failures) > 0 or len(res.errors) > 0:
    sys.exit(-1)

runsuite("general_tests")
runsuite("lang_tests")
runsuite("module_tests")
runsuite("class_tests")
runsuite("function_tests")
runsuite("constants_tests")
runsuite("kwargs_tests")
