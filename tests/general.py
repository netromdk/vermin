import sys
import os
from os.path import abspath, basename, join, splitext
from tempfile import NamedTemporaryFile, mkdtemp
from shutil import rmtree

from vermin import combine_versions, InvalidVersionException, detect_paths,\
  detect_paths_incremental, probably_python_file, Processor, process_individual, reverse_range,\
  dotted_name, remove_whitespace, main, sort_line_column

from .testutils import VerminTest, current_version, ScopedTemporaryFile, detect, visit

def touch(fld, name):
  filename = join(fld, name)
  fp = open(filename, mode="w")
  fp.close()
  return filename

class VerminGeneralTests(VerminTest):
  def test_detect_without_config(self):
    self.config.add_exclusion("abc")
    self.config.add_exclusion("abc.ABC")
    self.assertNotEqual(self.detect("from abc import ABC"),
                        detect("from abc import ABC", config=None))

  def test_visit_without_config(self):
    self.config.add_exclusion("abc")
    self.config.add_exclusion("abc.ABC")
    self.assertNotEqual(self.visit("from abc import ABC").minimum_versions(),
                        visit("from abc import ABC", config=None).minimum_versions())

  def test_visit_has_output_text(self):
    # Use level 2 since that triggers output text in SourceVisitor.
    self.config.set_verbose(2)

    # Earlier, it wouldn't have output text defined because `minimum_versions()` wasn't called.
    visitor = self.visit("from abc import ABC")
    self.assertNotEmpty(visitor.output_text())

  def test_format(self):
    # Empty field name requires 2.7+
    visitor = self.visit("print('{}'.format(42))")
    self.assertTrue(visitor.format27())

    # Non-empty field name requires 2.6+
    visitor = self.visit("print('{0}'.format(42))")
    self.assertFalse(visitor.format27())

  def test_strftime_directives(self):
    visitor = self.visit("from datetime import datetime\ndatetime.now().strftime('%A %d. %B %Y')")
    self.assertOnlyIn(("A", "d", "B", "Y"), visitor.strftime_directives())
    visitor = self.visit("from datetime import datetime\ndatetime.strptime('2018', '%Y')")
    self.assertOnlyIn("Y", visitor.strftime_directives())

  def test_modules(self):
    visitor = self.visit("import ast\nimport sys, argparse\nfrom os import *")
    self.assertOnlyIn(("ast", "sys", "argparse", "os"), visitor.modules())

  def test_member_class(self):
    visitor = self.visit("from abc import ABC")
    self.assertOnlyIn("abc.ABC", visitor.members())
    visitor = self.visit("import abc\nclass a(abc.ABC): pass")
    self.assertOnlyIn("abc.ABC", visitor.members())

  def test_member_function(self):
    visitor = self.visit("from sys import exc_clear")
    self.assertOnlyIn("sys.exc_clear", visitor.members())

  def test_member_constant(self):
    visitor = self.visit("from sys import version_info")
    self.assertOnlyIn("sys.version_info", visitor.members())

  def test_member_kwargs(self):
    visitor = self.visit("from os import open\nfd = open(dir_fd = None)")
    self.assertOnlyIn([("os.open", "dir_fd")], visitor.kwargs())
    visitor = self.visit("fd = open(dir_fd = None)")
    self.assertOnlyIn([("open", "dir_fd")], visitor.kwargs())
    visitor = self.visit("ZipFile().writestr(compress_type=None)")
    self.assertOnlyIn([("ZipFile.writestr", "compress_type")], visitor.kwargs())

  def test_probably_python_file(self):
    tmp_fld = mkdtemp()

    self.assertTrue(probably_python_file(touch(tmp_fld, "test.py")))
    self.assertTrue(probably_python_file(touch(tmp_fld, "test.pyw")))
    self.assertFalse(probably_python_file(touch(tmp_fld, "test.pyc")))

    # Empty file isn't python.
    f = touch(tmp_fld, "test")
    self.assertFalse(probably_python_file(f))

    # Magic line.
    with open(f, mode="w") as fp:
      fp.write("#!/usr/bin/env python\n")
    self.assertTrue(probably_python_file(f))

    # Binary file isn't python code.
    f = touch(tmp_fld, "binary")
    with open(f, mode="wb") as fp:
      fp.write(b"\x80\x89\x90")
    self.assertFalse(probably_python_file(f))

    rmtree(tmp_fld)

  def test_detect_paths(self):
    paths = detect_paths([abspath("vermin")])
    self.assertEqual(14, len(paths))

  def test_detect_hidden_paths(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    paths = detect_paths([tmp_fld], hidden=False)
    without_dot = [files[1], files[3]]
    self.assertEqualItems(without_dot, paths)

    paths2 = detect_paths([tmp_fld], hidden=True)
    self.assertEqualItems(files, paths2)

    rmtree(tmp_fld)

  def test_detect_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = False
    (accepted, further_args) = detect_paths_incremental(([tmp_fld], depth, hidden))

    self.assertEmpty(accepted)
    self.assertEqual(len(further_args), 1)

    (paths, depth, hidden) = further_args[0]
    self.assertEqualItems(paths, [files[1], files[3]])
    self.assertEqual(depth, 1)
    self.assertFalse(hidden)

    rmtree(tmp_fld)

  def test_detect_hidden_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = True
    (accepted, further_args) = detect_paths_incremental(([tmp_fld], depth, hidden))

    self.assertEmpty(accepted)
    self.assertEqual(len(further_args), 1)

    (paths, depth, hidden) = further_args[0]
    self.assertEqualItems(paths, [files[0], files[1], files[2], files[3]])
    self.assertEqual(depth, 1)
    self.assertTrue(hidden)

    rmtree(tmp_fld)

  # Even though hidden=False it will detect files given at the top level (depth=0) because those
  # files were directly specified on the CLI in real cases.
  def test_detect_top_level_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = False
    (accepted, further_args) = detect_paths_incremental((files, depth, hidden))

    self.assertEqualItems(accepted, files)
    self.assertEmpty(further_args)

    rmtree(tmp_fld)

  def test_detect_nonexistent_paths_incrementally(self):
    depth = 0
    hidden = False
    (accepted, further_args) = detect_paths_incremental((["i-do-not-exist"], depth, hidden))
    self.assertEmpty(accepted)
    self.assertEmpty(further_args)

  def test_detect_nonexistent_paths_with_dot_incrementally(self):
    depth = 0
    hidden = False
    (accepted, further_args) = detect_paths_incremental(([".i-start-with-dot"], depth, hidden))
    self.assertEmpty(accepted)
    self.assertEmpty(further_args)

  # Files directly specified at depth 0 should be accepted in any case, even if not with .py or
  # heuristics, but extensions and heuristics must be used further down.
  def test_detect_vermin_paths_directly(self):
    tmp_fld = mkdtemp()

    # Won't be picked by heuristics.
    f = touch(tmp_fld, "no-shebang")
    with open(f, mode="w") as fp:
      fp.write("print('this is code')")

    paths = detect_paths([tmp_fld])
    self.assertEmpty(paths)

    paths = detect_paths([join(tmp_fld, "no-shebang")])
    self.assertEqual(paths, [f])

    rmtree(tmp_fld)

  # Ensure all proper Python source code files are detected: py, py3, pyw, pyj, pyi
  def test_detect_vermin_paths_all_exts(self):
    tmp_fld = mkdtemp()

    exts = ('py', 'py3', 'pyw', 'pyj', 'pyi')
    for ext in exts:
      f = touch(tmp_fld, "code." + ext)
      with open(f, mode="w") as fp:
        fp.write("print('this is code')")

    found_exts = set()
    for path in detect_paths([tmp_fld]):
      _, ext = splitext(path)
      found_exts.add(ext[1:])
    self.assertEqualItems(found_exts, exts)

    rmtree(tmp_fld)

  # Ensure all non-Python source code files are not detected: pyc, pyd, pxd, pyx, pyo
  def test_detect_vermin_paths_no_invalid_exts(self):
    tmp_fld = mkdtemp()

    exts = ("pyc", "pyd", "pxd", "pyx", "pyo")
    for ext in exts:
      f = touch(tmp_fld, "code." + ext)
      with open(f, mode="w") as fp:
        fp.write("print('this is code')")

    # Since the detection ignores the extensions, no body of this for-loop will be executed.
    found_exts = set()
    for path in detect_paths([tmp_fld]):  # pragma: no cover
      _, ext = splitext(path)
      found_exts.add(ext[1:])
    self.assertEmpty(found_exts)

    rmtree(tmp_fld)

  def test_detect_vermin_min_versions(self):
    paths = detect_paths([abspath("vermin")])
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)
    self.assertOnlyIn(((2, 7), (3, 0)), mins)
    self.assertEmpty(backports)

  def test_combine_versions(self):
    with self.assertRaises(AssertionError):
      combine_versions([None], [None, None], self.config)
    self.assertEqual([(2, 0), (3, 1)],
                     combine_versions([(2, 0), (3, 0)], [(2, 0), (3, 1)], self.config))
    self.assertEqual([(2, 0), (3, 1)], combine_versions([2, (3, 0)], [(2, 0), 3.1], self.config))
    self.assertEqual([(2, 0), (3, 1)], combine_versions([(2, 0), 3], [2, 3.1], self.config))
    self.assertEqual([(2, 0), (3, 1)], combine_versions([2.0, 3.0], [2.0, 3.1], self.config))
    self.assertEqual([(2, 1), (3, 0)], combine_versions([2.1, 3.0], [2.0, 3.0], self.config))
    self.assertEqual([None, (3, 0)], combine_versions([2.0, 3.0], [None, 3.0], self.config))
    self.assertEqual([(2, 0), None], combine_versions([2.0, None], [2.0, 3.0], self.config))
    self.assertEqual([None, None], combine_versions([2.0, 3.0], [None, None], self.config))
    self.assertEqual([None, None], combine_versions([None, None], [2.0, 3.0], self.config))
    with self.assertRaises(InvalidVersionException):
      combine_versions([2.0, None], [None, 3.0], self.config)
    with self.assertRaises(InvalidVersionException):
      combine_versions([None, 3.0], [2.0, None], self.config)
    self.assertEqual([(0, 0), (3, 0)], combine_versions([0, 3.0], [0, 3.0], self.config))
    self.assertEqual([(2, 0), (3, 0)], combine_versions([0, 3.0], [2.0, 3.0], self.config))
    self.assertEqual([(2, 0), (3, 0)], combine_versions([2.0, 3.0], [0, 3.0], self.config))
    self.assertEqual([(2, 0), (3, 0)], combine_versions([2.0, 0], [2.0, 3.0], self.config))
    self.assertEqual([(2, 0), (3, 0)], combine_versions([2.0, 3.0], [2.0, 0], self.config))

  def test_detect_min_version(self):
    self.assertEqual([(2, 6), (3, 0)], self.detect("import abc"))

    # (2.6, 3.0) vs. (2.7, 3.2) = (2.7, 3.2)
    self.assertEqual([(2, 7), (3, 2)], self.detect("import abc, argparse"))

    # (2.6, 3.0) vs. (None, 3.4) = (None, 3.4)
    self.assertEqual([None, (3, 4)], self.detect("import abc\nfrom abc import ABC"))

    # (2.0, None) vs. (2.0, 3.0) = (2.0, None)
    self.assertEqual([(2, 0), None], self.detect("import repr\nfrom sys import getdefaultencoding"))

    # (2.0, None) vs. (None, 3.0) = both exclude the other major version -> exception!
    with self.assertRaises(InvalidVersionException):
      self.detect("import copy_reg, http")

  def test_ignore_non_top_level_imports(self):
    vers = [(0, 0), (0, 0)]
    self.assertNotEqual(vers, self.detect("from typing import Final"))  # Don't ignore
    self.assertEqual(vers, self.detect("from .typing import Final"))    # Ignore
    self.assertEqual(vers, self.detect("from ..typing import Final"))   # Ignore

  def test_reverse_range(self):
    self.assertEqual(list(reverse_range([1, 2, 3])), [2, 1, 0])
    self.assertEqual(list(reverse_range([1, 2])), [1, 0])
    self.assertEqual(list(reverse_range([])), [])

  def test_dotted_name(self):
    self.assertEqual(dotted_name(["hello", "world"]), "hello.world")
    self.assertEqual(dotted_name(["foo", ["bar", "baz"], "boom"]), "foo.bar.baz.boom")
    self.assertEqual(dotted_name(["foo", ("bar", "baz"), "boom"]), "foo.bar.baz.boom")
    self.assertEqual(dotted_name(1), "1")
    self.assertEqual(dotted_name(4.2), "4.2")
    self.assertEqual(dotted_name([1, 2, 3]), "1.2.3")
    self.assertEqual(dotted_name("right"), "right")
    self.assertEqual(dotted_name(["hello", None, "world"]), "hello.world")
    self.assertEqual(dotted_name(["foo", (None, "baz"), None]), "foo.baz")

    # Invalid values yield `assert False`.
    with self.assertRaises(AssertionError):
      dotted_name([4.2])

  def test_remove_whitespace(self):
    self.assertEqual(remove_whitespace("abc"), "abc")
    self.assertEqual(remove_whitespace("abc", ["a", "c"]), "b")
    self.assertEqual(remove_whitespace(" \t\n\r\f\v"), "")
    self.assertEqual(remove_whitespace(" \t1\n2\r3\f\v", ["1", "3"]), "2")

  def test_sort_line_column(self):
    text = [
      "L2: two",
      "hello, world",
      "L2 C10: two ten",
      "L1: one",
      "L3: three",
      "print",
      "L2 C2: two two",
    ]

    expected = [
      "print",
      "hello, world",
      "L1: one",
      "L2: two",
      "L2 C2: two two",
      "L2 C10: two ten",
      "L3: three"
    ]

    value = text
    value.sort(key=sort_line_column)
    self.assertEqual(value, expected)

    # Repeated sortings yield the same.
    value2 = text
    value2.sort(key=sort_line_column)
    self.assertEqual(value2, expected)

  def test_assign_rvalue_attribute(self):
    self.assertEqual([None, (3, 3)], self.detect("import bz2\nv = bz2.BZ2File\nv.writable"))

  def test_user_defined(self):
    visitor = self.visit("def hello(): pass\nhello2()\nclass foo(): pass")
    self.assertOnlyIn(["hello", "foo"], visitor.user_defined())

  def test_ignore_members_when_user_defined_funcs(self):
    # `next()` was builtin from 2.6.
    visitor = self.visit("def next(): pass\nnext()")
    self.assertOnlyIn("next", visitor.user_defined())
    self.assertEmpty(visitor.members())

  def test_ignore_members_when_user_defined_classes(self):
    # `bytearray` was builtin from 2.6.
    visitor = self.visit("class bytearray: pass\nba = bytearray()")
    self.assertOnlyIn(["bytearray", "ba"], visitor.user_defined())
    self.assertEmpty(visitor.members())

  def test_ignore_modules_when_user_defined_funcs(self):
    # This test relies on the rule for "SimpleXMLRPCServer" module.

    # Ignore module due to class def.
    visitor = self.visit("import SimpleXMLRPCServer\n"
                         "def SimpleXMLRPCServer(): pass\n"
                         "src = SimpleXMLRPCServer()")
    self.assertOnlyIn(["SimpleXMLRPCServer", "src"], visitor.user_defined())
    self.assertEmpty(visitor.modules())

  def test_ignore_modules_when_user_defined_classes(self):
    # This test relies on the rule for "SimpleXMLRPCServer" module.

    # Ignore module due to class def.
    visitor = self.visit("import SimpleXMLRPCServer\n"
                         "class SimpleXMLRPCServer: pass\n"
                         "src = SimpleXMLRPCServer()")
    self.assertOnlyIn(["SimpleXMLRPCServer", "src"], visitor.user_defined())
    self.assertEmpty(visitor.modules())

  def test_mod_inverse_pow(self):
    # All arguments must be ints.
    visitor = self.visit("pow(1.1, -1, 3)")
    self.assertFalse(visitor.modular_inverse_pow())
    visitor = self.visit("pow(1, -1.0, 3)")
    self.assertFalse(visitor.modular_inverse_pow())
    visitor = self.visit("pow(1, -1, 3.0)")
    self.assertFalse(visitor.modular_inverse_pow())

    # The second argument can be negative to yield modular inverse calculation.
    visitor = self.visit("pow(1, -2, 3)")
    self.assertTrue(visitor.modular_inverse_pow())
    self.assertOnlyIn((3, 8), visitor.minimum_versions())

  def test_main_no_args(self):
    # Print usage and exit with code 1.
    with self.assertRaises(SystemExit) as ex:
      main()
    self.assertEqual(ex.exception.code, 1)

  def test_main_full_usage(self):
    # Print full usage and exit with code 0.
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "--help"]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 0)

  def test_main_print_version(self):
    # Print version and exit with code 0.
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "--version"]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 0)

  def test_main_print_versions_range(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import weakref")
    fp.close()

    # Print versions range and exit with code 0.
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "--versions", fp.path()]
      main()

    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 0)

  def test_main_no_paths(self):
    # The path doesn't exist and isn't a .py file which means no paths are detected.
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "nonexistentfilethatisntpy"]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 1)

  def test_main_no_rules_hit(self):
    # Python file that doesn't hit any rules should exit successfully.
    fp = ScopedTemporaryFile()
    fp.close()
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], fp.path()]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 0)

  def test_main_target_not_met(self):
    # Ensure exit code 1 when target isn't met.
    fp = ScopedTemporaryFile()
    fp.close()
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "-t=3.0", fp.path()]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 1)

  def test_process_file_not_Found(self):
    if current_version() >= 3.0:
      exc = FileNotFoundError
    else:
      exc = Exception  # pragma: no cover
    with self.assertRaises(exc):
      process_individual(("nonexistent", self.config))

  def test_process_runtests_py(self):
    proc_res = process_individual((sys.argv[0], self.config))
    self.assertEqual(basename(proc_res.path), "runtests.py")
    self.assertEqual(proc_res.mins, [(2, 7), (3, 1)])
    self.assertEmpty(proc_res.text)
    self.assertEmpty(proc_res.bps)

  def test_process_syntax_error(self):
    # Syntax error triggers minimum versions [0, 0].
    fp = ScopedTemporaryFile()
    fp.write(b'(')  # SyntaxError: unexpected EOF while parsing
    fp.close()
    proc_res = process_individual((fp.path(), self.config))
    self.assertEqual(proc_res.mins, [(0, 0), (0, 0)])
    self.assertEmpty(proc_res.text)
    self.assertEmpty(proc_res.bps)

  def test_process_value_error(self):
    # (Py3) ValueError: source code string cannot contain null bytes
    # (Py2) TypeError: compile() expected string without null bytes
    fp = ScopedTemporaryFile()
    fp.write(b'\0')
    fp.close()
    proc_res = process_individual((fp.path(), self.config))
    self.assertEqual(proc_res, None)

  def test_process_invalid_versions(self):
    with ScopedTemporaryFile() as fp:
      fp.write(b"""long(42)
breakpoint()
""")
      fp.close()
      proc_res = process_individual((fp.path(), self.config))
      self.assertEqual(proc_res.mins, None)
      msg = "'long' member (requires 2.0, !3) vs. 'breakpoint' member (requires !2, 3.7)"
      self.assertEqual(proc_res.text, msg)
      self.assertEmpty(proc_res.bps)

    with ScopedTemporaryFile() as fp:
      fp.write(b"""try:
  import socketserver
except ImportError:
  import SocketServer
""")
      fp.close()
      proc_res = process_individual((fp.path(), self.config))
      self.assertEqual(proc_res.mins, None)
      msg = "'socketserver' module (requires !2, 3.0) vs. 'SocketServer' module (requires 2.0, !3)"
      self.assertEqual(proc_res.text, msg)
      self.assertEmpty(proc_res.bps)

    with ScopedTemporaryFile() as fp:
      fp.write(b"""import time
time.strftime("%u", gmtime())

from urllib import urlopen
urlopen(context=None)
""")
      fp.close()
      proc_res = process_individual((fp.path(), self.config))
      self.assertEqual(proc_res.mins, None)
      msg =\
        "strftime directive 'u' (requires !2, 3.6) vs. 'urllib.urlopen(context)' (requires 2.7, !3)"
      self.assertEqual(proc_res.text, msg)
      self.assertEmpty(proc_res.bps)

  def test_process_file_using_backport(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import typing")
    fp.close()
    proc_res = process_individual((fp.path(), self.config))
    self.assertEmpty(proc_res.text)
    self.assertEqualItems(["typing"], proc_res.bps)

  def test_processor_value_error(self):
    fp = ScopedTemporaryFile()
    fp.write(b"\0")
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertFalse(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)

  def test_processor_incompatible(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import Queue")  # 2.0, !3
    fp.writeln(b"import builtins")  # !2, 3.0
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertTrue(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)

  def test_processor_separately_incompatible(self):
    paths = []
    codes = [
      b"import Queue\n",  # 2.0, !3
      b"import builtins\n",  # !2, 3.0
    ]
    for code in codes:
      fp = NamedTemporaryFile(suffix=".py", delete=False)
      fp.write(code)
      fp.close()
      paths.append(fp.name)

    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)
    self.assertEqual(mins, [(2, 0), None])  # Because the Queue file is analyzed first.
    self.assertTrue(incomp)
    self.assertEqual(unique_versions, [(2, 0), (3, 0)])
    self.assertEmpty(backports)

    for path in paths:
      os.remove(path)

  def test_processor_indent_show_output_text(self):
    self.config.set_verbose(4)  # Ensure output text.

    # Trigger SourceVisitor.__nprint() while visiting AST, which is one way to add some output text.
    self.config.set_print_visits(True)

    fp = ScopedTemporaryFile()
    fp.write(b"""def foo(): pass
foo()              # Ignoring member 'foo' because it's user-defined!
import Queue
class Queue: pass  # Ignoring module 'Queue' because it's user-defined!
def any(): pass
any(test=1)        # Ignoring function 'any' because it's user-defined!
print('hello')     # print(expr) requires 2+ or 3+
""")
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)

    if current_version() >= 3.0:
      self.assertEqual(mins, [(2, 0), (3, 0)])
      self.assertEqual(unique_versions, [(2, 0), (3, 0)])
    else:  # pragma: no cover
      self.assertEqual(mins, [(2, 0), (0, 0)])
      self.assertEqual(unique_versions, [(2, 0)])

    self.assertFalse(incomp)
    self.assertEmpty(backports)

  # Since python 3.8+, the multiprocessing context on macOS started using spawn() instead of fork(),
  # which means that the concurrently run functionality doesn't inherit the same information. It was
  # fixed such that when spawn() is used, it reestablishes the information that isn't inherited.
  # This test fails if that isn't done, and always succeeds when fork() is used.
  def test_processor_argparse_backport_spawn_or_fork(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import argparse")  # 2.7, 3.2
    fp.close()
    self.config.add_backport("argparse")  # -> 2.3, 3.1
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports) = processor.process(paths, self.config)
    self.assertEqual(mins, [(2, 3), (3, 1)])
    self.assertFalse(incomp)
    self.assertEqual(unique_versions, [(2, 3), (3, 1)])
    self.assertEqual(backports, {"argparse"})
