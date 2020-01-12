#!/usr/bin/env python
import sys
import unittest

def runsuite(suite):
  suite = "tests.{}".format(suite)
  print("Running test suite: {}".format(suite))
  res = unittest.main(suite, exit=False).result
  if len(res.failures) > 0 or len(res.errors) > 0:
    sys.exit(-1)

if __name__ == '__main__':
  runsuite("general")
  runsuite("arguments")
  runsuite("lax_mode")
  runsuite("lang")
  runsuite("module")
  runsuite("builtin_classes")
  runsuite("class")
  runsuite("exception")
  runsuite("builtin_functions")
  runsuite("builtin_constants")
  runsuite("function")
  runsuite("constants")
  runsuite("decorators")
  runsuite("kwargs")
  runsuite("strftime_directive")
  runsuite("annotation")
  runsuite("array_typecodes")
  runsuite("codecs_error_handlers")
  runsuite("codecs_encodings")
  runsuite("exclusions")
  runsuite("comment_exclusions")
  runsuite("backports")
  runsuite("bytes_directive")
