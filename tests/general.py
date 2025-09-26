import sys
import os
import re
import io
from os.path import abspath, basename, join, splitext
from tempfile import NamedTemporaryFile, mkdtemp
from shutil import rmtree
from multiprocessing import cpu_count

from vermin import combine_versions, InvalidVersionException, detect_paths,\
  detect_paths_incremental, probably_python_file, Processor, reverse_range, dotted_name,\
  remove_whitespace, main, sort_line_column, sort_line_column_parsable, version_strings,\
  format_title_descs, DEFAULT_PROCESSES
from vermin.formats import ParsableFormat, GitHubFormat
from vermin.utility import compare_requirements

from .testutils import VerminTest, current_version, ScopedTemporaryFile, detect, visit, touch, \
  working_dir

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

  def test_visit_output_text_has_correct_lines(self):
    self.config.set_verbose(3)  # Line numbers start at verbosity 3.
    visitor = self.visit("""a = 1
import abc
b = 2
if 1:
  import zoneinfo
  import argparse
c = 3
""")

    # Output text is sorted for line numbers/columns when verbosity level is 3+.
    self.assertEqual(visitor.output_text(), """L2 C7: 'abc' module requires 2.6, 3.0
L5 C9: 'zoneinfo' module requires !2, 3.9
L6 C9: 'argparse' module requires 2.7, 3.2
""")

  def test_visit_output_text_has_correct_lines_parsable(self):
    self.config.set_format(ParsableFormat())

    src = """a = 1
import abc
b = 2
if 1:
  import zoneinfo
  import argparse
c = 3
"""

    visitor = self.visit(src)
    self.assertEqual(visitor.output_text(), """<unknown>:2:7:2.6:3.0:'abc' module
<unknown>:5:9:!2:3.9:'zoneinfo' module
<unknown>:6:9:2.7:3.2:'argparse' module
""")

    visitor = self.visit(src, path="test.py")
    self.assertEqual(visitor.output_text(), """test.py:2:7:2.6:3.0:'abc' module
test.py:5:9:!2:3.9:'zoneinfo' module
test.py:6:9:2.7:3.2:'argparse' module
""")

    # Paths with ":" or "\n" aren't allowed with parsable format. On Windows, paths cannot contain
    # ":" except for the drive part so the test doesn't make sense.
    if not sys.platform.startswith("win32"):
      with self.assertRaises(AssertionError):
        self.visit(src, path="te:st.py")
      with self.assertRaises(AssertionError):
        self.visit(src, path="te\nst.py")

  def test_visit_output_text_has_correct_lines_github(self):
    self.config.set_format(GitHubFormat())
    # error level for target violations only
    self.config.add_target((3, 4), False)

    # example cwd

    src = """a = 1
import abc
b = 2
if 1:
  import zoneinfo
  import argparse
c = 3
"""

    for path, path_str in (None, "<unknown>"), ("test.py", "test.py"):
      visitor = self.visit(src, path=path)
      self.assertEqual(visitor.output_text(), (
        """::notice file={path},line=2,col=7,title=Requires Python 2.6%2C 3.0::'abc' module
::error file={path},line=5,col=9,title=Requires Python !2%2C 3.9::'zoneinfo' module
::notice file={path},line=6,col=9,title=Requires Python 2.7%2C 3.2::'argparse' module
""".format(path=path_str)))

    # subclasses ParsableFormat, so should also reject these paths
    if not sys.platform.startswith("win32"):
      with self.assertRaises(AssertionError):
        self.visit(src, path="te:st.py")
      with self.assertRaises(AssertionError):
        self.visit(src, path="te\nst.py")

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
    with open(f, mode="w", encoding="utf-8") as fp:
      fp.write("#!/usr/bin/env python\n")
    self.assertTrue(probably_python_file(f))

    # Binary file isn't python code.
    f = touch(tmp_fld, "binary")
    with open(f, mode="wb") as fp:
      fp.write(b"\x80\x89\x90")
    self.assertFalse(probably_python_file(f))

    rmtree(tmp_fld)

  def test_detect_paths(self):
    paths = detect_paths([abspath("vermin")], config=self.config)
    self.assertEqual(20, len(paths))

  def test_detect_hidden_paths(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    paths = detect_paths([tmp_fld], hidden=False, config=self.config)
    without_dot = [files[1], files[3]]
    self.assertEqualItems(without_dot, paths)

    paths2 = detect_paths([tmp_fld], hidden=True, config=self.config)
    self.assertEqualItems(files, paths2)

    rmtree(tmp_fld)

  def test_detect_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = False
    ignore_chars = []
    scan_symlink_folders = False
    (accepted, further_args) = detect_paths_incremental(
      ([tmp_fld], depth, hidden, ignore_chars, scan_symlink_folders, self.config))

    self.assertEmpty(accepted)
    self.assertEqual(len(further_args), 1)

    (paths, depth, hidden, ignore_chars, scan_symlink_folders, config) = further_args[0]
    self.assertEqualItems(paths, [files[1], files[3]])
    self.assertEqual(depth, 1)
    self.assertFalse(hidden)
    self.assertEmpty(ignore_chars)
    self.assertFalse(scan_symlink_folders)
    self.assertNotEqual(config, None)

    rmtree(tmp_fld)

  def test_detect_hidden_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = True
    ignore_chars = []
    scan_symlink_folders = False
    (accepted, further_args) = detect_paths_incremental(
      ([tmp_fld], depth, hidden, ignore_chars, scan_symlink_folders, self.config))

    self.assertEmpty(accepted)
    self.assertEqual(len(further_args), 1)

    (paths, depth, hidden, ignore_chars, scan_symlink_folders, config) = further_args[0]
    self.assertEqualItems(paths, [files[0], files[1], files[2], files[3]])
    self.assertEqual(depth, 1)
    self.assertTrue(hidden)
    self.assertEmpty(ignore_chars)
    self.assertFalse(scan_symlink_folders)
    self.assertNotEqual(config, None)

    rmtree(tmp_fld)

  # Even though hidden=False it will detect files given at the top level (depth=0) because those
  # files were directly specified on the CLI in real cases.
  def test_detect_top_level_paths_incrementally(self):
    tmp_fld = mkdtemp()
    files = [touch(tmp_fld, ".test.py"), touch(tmp_fld, "test.py"), touch(tmp_fld, ".test2.py"),
             touch(tmp_fld, "test2.py")]

    depth = 0
    hidden = False
    ignore_chars = []
    scan_symlink_folders = False
    (accepted, further_args) = detect_paths_incremental(
      (files, depth, hidden, ignore_chars, scan_symlink_folders, self.config))

    self.assertEqualItems(accepted, files)
    self.assertEmpty(further_args)

    rmtree(tmp_fld)

  def test_detect_nonexistent_paths_incrementally(self):
    depth = 0
    hidden = False
    ignore_chars = []
    scan_symlink_folders = False
    (accepted, further_args) = detect_paths_incremental((["i-do-not-exist"], depth, hidden,
                                                         ignore_chars, scan_symlink_folders,
                                                         self.config))
    self.assertEmpty(accepted)
    self.assertEmpty(further_args)

  def test_detect_nonexistent_paths_with_dot_incrementally(self):
    depth = 0
    hidden = False
    ignore_chars = []
    scan_symlink_folders = False
    (accepted, further_args) = detect_paths_incremental(([".i-start-with-dot"], depth, hidden,
                                                         ignore_chars, scan_symlink_folders,
                                                         self.config))
    self.assertEmpty(accepted)
    self.assertEmpty(further_args)

  # Files directly specified at depth 0 should be accepted in any case, even if not with .py or
  # heuristics, but extensions and heuristics must be used further down.
  def test_detect_vermin_paths_directly(self):
    tmp_fld = mkdtemp()

    # Won't be picked by heuristics.
    f = touch(tmp_fld, "no-shebang")
    with open(f, mode="w", encoding="utf-8") as fp:
      fp.write("print('this is code')")

    paths = detect_paths([tmp_fld], config=self.config)
    self.assertEmpty(paths)

    paths = detect_paths([join(tmp_fld, "no-shebang")], config=self.config)
    self.assertEqual(paths, [f])

    rmtree(tmp_fld)

  # Ensure all proper Python source code files are detected: py, py3, pyw, pyj, pyi
  def test_detect_vermin_paths_all_exts(self):
    tmp_fld = mkdtemp()

    exts = ('py', 'py3', 'pyw', 'pyj', 'pyi')
    for ext in exts:
      f = touch(tmp_fld, "code." + ext)
      with open(f, mode="w", encoding="utf-8") as fp:
        fp.write("print('this is code')")

    found_exts = set()
    for path in detect_paths([tmp_fld], config=self.config):
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
      with open(f, mode="w", encoding="utf-8") as fp:
        fp.write("print('this is code')")

    # Since the detection ignores the extensions, no body of this for-loop will be executed.
    found_exts = set()
    for path in detect_paths([tmp_fld], config=self.config):  # pragma: no cover
      _, ext = splitext(path)
      found_exts.add(ext[1:])
    self.assertEmpty(found_exts)

    rmtree(tmp_fld)

  def test_exclude_pyi_regex(self):
    tmp_fld = mkdtemp()

    # With the default of --make-paths-absolute, this will match .pyi files in any subdirectory. The
    # most common use case for --exclude-regex is expected to be for file extensions, so it's great
    # that will work regardless of the --make-paths-absolute setting.
    self.config.add_exclusion_regex(r"\.pyi$")

    f = touch(tmp_fld, "code.pyi")
    with open(f, mode="w", encoding="utf-8") as fp:
      fp.write("print('this is code')")

    paths = detect_paths([tmp_fld], config=self.config)
    self.assertEmpty(paths)

    rmtree(tmp_fld)

  def test_exclude_directory_regex(self):
    tmp_fld = mkdtemp()

    # Excluding the directory .../a should exclude any files recursively beneath it as well.
    self.config.add_exclusion_regex('^' + re.escape(join(tmp_fld, "a")) + '$')

    # Create .../a and .../a/b directories.
    os.mkdir(join(tmp_fld, "a"))
    os.mkdir(join(tmp_fld, "a/b"))

    paths = ["code.py", "a/code.py", "a/b/code.py"]
    for p in paths:
      f = touch(tmp_fld, p)
      with open(f, mode="w", encoding="utf-8") as fp:
        fp.write("print('this is code')")

    paths = detect_paths([tmp_fld], config=self.config)
    self.assertEqual(paths, [join(tmp_fld, "code.py")])

    rmtree(tmp_fld)

  def test_exclude_regex_relative(self):
    tmp_fld = mkdtemp()

    # Keep paths relative, and provide patterns matching relative paths.
    self.config.set_make_paths_absolute(False)
    self.config.add_exclusion_regex("^a{0}b$".format(re.escape(os.path.sep)))
    self.config.add_exclusion_regex("^a{0}.+pyi$".format(re.escape(os.path.sep)))

    # Create .../a and .../a/b directories.
    os.mkdir(join(tmp_fld, "a"))
    os.mkdir(join(tmp_fld, "a", "b"))

    paths = [
      join("a", "code.py"),
      join("a", "code.pyi"),
      join("a", "b", "code.py"),
    ]
    for p in paths:
      f = touch(tmp_fld, p)
      with open(f, mode="w", encoding="utf-8") as fp:
        fp.write("print('this is code')")

    # Temporarily modify the working directory.
    with working_dir(tmp_fld):
      paths = detect_paths(["a"], config=self.config)
      self.assertEqual(paths, [join("a", "code.py")])

    # When running on Windows, this can sometimes fail:
    #   PermissionError: [WinError 32] The process cannot access the file because it is being used
    #                    by another process:
    #                    'C:\\Users\\RUNNER~1\\AppData\\Local\\Temp\\tmpAAAANNNN'
    # But we can ignore that since the files reside in a temporary folder anyway, and the
    # folders/files aren't being used any longer either.
    rmtree(tmp_fld, ignore_errors=True)

  def test_detect_vermin_min_versions(self):
    paths = detect_paths([abspath("vermin")], config=self.config)
    processor = Processor()
    (mins, _incomp, _unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertOnlyIn((3, 0), mins)
    self.assertEmpty(backports)
    self.assertTrue(used_novermin)
    self.assertFalse(maybe_anns)

  def test_detect_vermin_min_versions_parsable(self):
    paths = detect_paths([abspath("vermin")], config=self.config)
    processor = Processor()
    self.config.set_format(ParsableFormat())
    (mins, _incomp, _unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertOnlyIn((3, 0), mins)
    self.assertEmpty(backports)
    self.assertTrue(used_novermin)
    self.assertFalse(maybe_anns)

  @VerminTest.parameterized_args([
    ([(2, 0), (3, 0)], [(2, 0), (3, 1)], [(2, 0), (3, 1)]),
    ([2, (3, 0)], [(2, 0), 3.1], [(2, 0), (3, 1)]),
    ([(2, 0), 3], [2, 3.1], [(2, 0), (3, 1)]),
    ([2.0, 3.0], [2.0, 3.1], [(2, 0), (3, 1)]),
    ([2.1, 3.0], [2.0, 3.0], [(2, 1), (3, 0)]),
    ([2.0, 3.0], [None, 3.0], [None, (3, 0)]),
    ([2.0, None], [2.0, 3.0], [(2, 0), None]),
    ([2.0, 3.0], [None, None], [None, None]),
    ([None, None], [2.0, 3.0], [None, None]),
    ([0, 3.0], [0, 3.0], [(0, 0), (3, 0)]),
    ([0, 3.0], [2.0, 3.0], [(2, 0), (3, 0)]),
    ([2.0, 3.0], [0, 3.0], [(2, 0), (3, 0)]),
    ([2.0, 0], [2.0, 3.0], [(2, 0), (3, 0)]),
    ([2.0, 3.0], [2.0, 0], [(2, 0), (3, 0)]),
  ])
  def test_combine_versions(self, lhs, rhs, expected):
    self.assertEqual(combine_versions(lhs, rhs, self.config), expected)

  @VerminTest.parameterized_exceptions([
    (AssertionError, [None], [None, None]),  # Not same size.
    (AssertionError, [None, None], [None]),  # Not same size.
    (InvalidVersionException, [2.0, None], [None, 3.0]),
    (InvalidVersionException, [None, 3.0], [2.0, None]),
  ])
  def test_combine_versions_assert(self, lhs, rhs):
    combine_versions(lhs, rhs, self.config)

  @VerminTest.parameterized_args([
    ([0.0, 0.0], None, "~2, ~3"),
    ([2.0, 0.0], None, "2.0, ~3"),
    ([2.0, 3.0], None, "2.0, 3.0"),
    ([0.0, 3.1], None, "~2, 3.1"),
    ([None, 3.0], None, "!2, 3.0"),
    ([2.0, None], None, "2.0, !3"),
    ([None, None], None, "!2, !3"),
    ([0.0, 3.1], ":", "~2:3.1"),
    ([None, 3.0], ":", "!2:3.0"),
    ([2.0, None], ":", "2.0:!3"),
    ([None, None], ":", "!2:!3"),
    ([2.3], None, "2.3"),
    ([3.4], None, "3.4"),
    ([2.3, 2.7, 3.1], None, "2.3, 2.7, 3.1"),
    ([2.0, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9],
     None, "2.0, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9"),
  ])
  def test_version_strings(self, versions, separator, expected):
    self.assertEqual(version_strings(versions, separator), expected)

  @VerminTest.parameterized_exceptions([
    (AssertionError, []),  # Cannot be empty.

    # If there is at least one zero value, then there can only be one or two values!
    (AssertionError, [1, 0.0, 2]),
    (AssertionError, [1, 0, 2]),
    (AssertionError, [1, (0, 0), 2]),
    (AssertionError, [1, 2, 3, 0.0]),
    (AssertionError, [(0, 0), 2, 3, 4]),
  ])
  def test_version_strings_assert(self, versions):
    version_strings(versions)

  @VerminTest.parameterized_args([
    ("import abc", [(2, 6), (3, 0)]),

    # (2.6, 3.0) vs. (2.7, 3.2) = (2.7, 3.2)
    ("import abc, argparse", [(2, 7), (3, 2)]),

    # (2.6, 3.0) vs. (None, 3.4) = (None, 3.4)
    ("import abc\nfrom abc import ABC", (3, 4)),

    # (2.0, None) vs. (2.0, 3.0) = (2.0, None)
    ("import repr\nfrom sys import getdefaultencoding", (2, 0)),
  ])
  def test_detect_min_version(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_exceptions([
    # (2.0, None) vs. (None, 3.0) = both exclude the other major version -> exception!
    (InvalidVersionException, "import copy_reg, http"),
  ])
  def test_detect_min_version_assert(self, source):
    self.detect(source)

  def test_ignore_non_top_level_imports(self):
    vers = [(0, 0), (0, 0)]
    self.assertNotEqual(vers, self.detect("from typing import Final"))  # Don't ignore
    self.assertEqual(vers, self.detect("from .typing import Final"))    # Ignore
    self.assertEqual(vers, self.detect("from ..typing import Final"))   # Ignore

  @VerminTest.parameterized_args([
    ([1, 2, 3], [2, 1, 0]),
    ([1, 2], [1, 0]),
    ([], []),
  ])
  def test_reverse_range(self, values, expected):
    self.assertEqual(list(reverse_range(values)), expected)

  @VerminTest.parameterized_args([
    (["hello", "world"], "hello.world"),
    (["foo", ["bar", "baz"], "boom"], "foo.bar.baz.boom"),
    (["foo", ("bar", "baz"), "boom"], "foo.bar.baz.boom"),
    (1, "1"),
    (4.2, "4.2"),
    ([1, 2, 3], "1.2.3"),
    ("right", "right"),
    (["hello", None, "world"], "hello.world"),
    (["foo", (None, "baz"), None], "foo.baz"),
  ])
  def test_dotted_name(self, names, expected):
    self.assertEqual(dotted_name(names), expected)

  @VerminTest.parameterized_exceptions([
    # Invalid values yield `assert False`.
    (AssertionError, [4.2]),
  ])
  def test_dotted_name_assert(self, names):
    dotted_name(names)

  @VerminTest.parameterized_args([
    ("abc", None, "abc"),
    ("abc", ["a", "c"], "b"),
    (" \t\n\r\f\v", None, ""),
    (" \t1\n2\r3\f\v", ["1", "3"], "2"),
  ])
  def test_remove_whitespace(self, value, extras, expected):
    self.assertEqual(remove_whitespace(value, extras), expected)

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

  def test_sort_line_column_parsable(self):
    text = [
      "final_annotation.py:7::!2:3.6:variable annotations",
      "final_annotation.py:1:5:!2:3.5:'typing' module",
      "final_annotation.py:3::!2:3.8:final variable annotations",
      "final_annotation.py:7::!2:3.8:final variable annotations",

      # This line won't actually happen but it's handled anyway.
      "weird line",

      "final_annotation.py:4::!2:3.6:variable annotations",
      "final_annotation.py:1::!2:3.5:'typing' module",
      "final_annotation.py:3::!2:3.6:variable annotations",
      "final_annotation.py:4::!2:3.8:final variable annotations",
      "final_annotation.py:1:7:!2:3.8:'typing.Final' member",
    ]

    expected = [
      "weird line",
      "final_annotation.py:1::!2:3.5:'typing' module",
      "final_annotation.py:1:5:!2:3.5:'typing' module",
      "final_annotation.py:1:7:!2:3.8:'typing.Final' member",
      "final_annotation.py:3::!2:3.6:variable annotations",
      "final_annotation.py:3::!2:3.8:final variable annotations",
      "final_annotation.py:4::!2:3.6:variable annotations",
      "final_annotation.py:4::!2:3.8:final variable annotations",
      "final_annotation.py:7::!2:3.6:variable annotations",
      "final_annotation.py:7::!2:3.8:final variable annotations",
    ]

    value = text
    value.sort(key=sort_line_column_parsable)
    self.assertEqual(value, expected)

    # Repeated sortings yield the same.
    value2 = text
    value2.sort(key=sort_line_column_parsable)
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
    self.assertEqual(ex.exception.code, 0)
    with self.assertRaises(SystemExit) as ex:
      sys.argv[1] = "-V"
      main()
    self.assertEqual(ex.exception.code, 0)
    sys.argv = [sys.argv[0]]

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

  def test_main_no_rules_hit_target_not_met_violations_mode(self):
    # Python file that doesn't hit any rules, even with targets, should exit successfully for
    # violations mode.
    fp = ScopedTemporaryFile()
    fp.close()
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "-t=3.0", "--violations", fp.path()]
      main()
    sys.argv = [sys.argv[0]]
    self.assertEqual(ex.exception.code, 0)

  @VerminTest.skipUnlessPlatform("win32")
  def test_main_parsable_dont_ignore_paths_with_colon_in_drive_part(self):
    # Tests that detection of paths works with ":" in them (due to parsable format) especially on
    # Windows where the first part of an absolute path, the drive part, contains a ":".

    # Detect newly created file path in parent folder even though using parsable format.
    tmp_fld = mkdtemp()
    touch(tmp_fld, "test.py")
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "--format", "parsable", tmp_fld]
      main()

    sys.argv = [sys.argv[0]]
    rmtree(tmp_fld)

    # Check for no error. It would incorrectly yield "No files specified to analyze!" before the
    # fix.
    self.assertEqual(ex.exception.code, 0)

  def test_main_parsable_has_last_results_line(self):
    tmp_fld = mkdtemp()
    file_name = "test.py"
    path = join(tmp_fld, file_name)
    touch(tmp_fld, file_name)
    temp_stdout = io.StringIO()
    backup_stdout = sys.stdout
    with self.assertRaises(SystemExit) as ex:
      sys.argv = [sys.argv[0], "--format", "parsable", tmp_fld]
      sys.stdout = temp_stdout
      main()

    sys.argv = [sys.argv[0]]
    sys.stdout = backup_stdout
    rmtree(tmp_fld)

    # Check successful execution.
    self.assertEqual(ex.exception.code, 0)

    # Check that the last line is on the form `:::v2:v3:`.
    lines = temp_stdout.getvalue().splitlines()
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "{}:::~2:~3:".format(path))
    self.assertEqual(lines[1], ":::~2:~3:")

  def test_process_file_not_Found(self):
    path = "nonexistent"
    res = Processor.process_individual((path, self.config))
    self.assertNotEqual(res, None)
    self.assertEqual(res.path, path)
    self.assertEqual(res.mins, [(0, 0), (0, 0)])
    self.assertEqual(res.node, None)

  def test_process_runtests_py(self):
    proc_res = Processor.process_individual((sys.argv[0], self.config))
    self.assertEqual(basename(proc_res.path), "runtests.py")
    self.assertEqual(proc_res.mins, [(2, 7), (3, 2)])
    self.assertEmpty(proc_res.text)
    self.assertEmpty(proc_res.bps)

  def test_process_syntax_error(self):
    # Syntax error triggers minimum versions [0, 0].
    fp = ScopedTemporaryFile()
    fp.write(b'(')  # SyntaxError: unexpected EOF while parsing
    fp.close()
    proc_res = Processor.process_individual((fp.path(), self.config))
    self.assertEqual(proc_res.mins, [(0, 0), (0, 0)])
    self.assertTrue(proc_res.text.startswith("error: "))
    self.assertEmpty(proc_res.bps)

  @VerminTest.skipUnlessVersion(3, 12)
  def test_process_syntax_error_null_bytes(self):
    # SyntaxError: source code string cannot contain null bytes
    fp = ScopedTemporaryFile()
    fp.write(b'\0')
    fp.close()
    proc_res = Processor.process_individual((fp.path(), self.config))
    self.assertEqual(proc_res.mins, [(0, 0), (0, 0)])
    self.assertTrue(proc_res.text.startswith("error: "))
    self.assertEmpty(proc_res.bps)

  def test_process_invalid_versions(self):
    with ScopedTemporaryFile() as fp:
      fp.write(b"""long(42)
breakpoint()
""")
      fp.close()
      proc_res = Processor.process_individual((fp.path(), self.config))
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
      proc_res = Processor.process_individual((fp.path(), self.config))
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
      proc_res = Processor.process_individual((fp.path(), self.config))
      self.assertEqual(proc_res.mins, None)
      msg =\
        "strftime directive 'u' (requires !2, 3.6) vs. 'urllib.urlopen(context)' (requires 2.7, !3)"
      self.assertEqual(proc_res.text, msg)
      self.assertEmpty(proc_res.bps)

  def test_process_file_using_backport(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import typing")
    fp.close()
    proc_res = Processor.process_individual((fp.path(), self.config))
    self.assertEmpty(proc_res.text)
    self.assertEqualItems(["typing"], proc_res.bps)

  def test_processor_value_error(self):
    fp = ScopedTemporaryFile()
    fp.write(b"\0")
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertFalse(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertFalse(maybe_anns)

  def test_processor_incompatible(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import Queue")  # 2.0, !3
    fp.writeln(b"import builtins")  # !2, 3.0
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertTrue(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertFalse(maybe_anns)

  def test_processor_separately_incompatible(self):
    paths = []
    codes = [
      b"import Queue\n",  # 2.0, !3
      b"import builtins\n",  # !2, 3.0
    ]
    for code in codes:
      with NamedTemporaryFile(suffix=".py", delete=False) as fp:
        fp.write(code)
        fp.close()
        paths.append(fp.name)

    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(2, 0), None])  # Because the Queue file is analyzed first.
    self.assertTrue(incomp)
    self.assertEqual(unique_versions, [(2, 0), (3, 0)])
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertFalse(maybe_anns)

    for path in paths:
      os.remove(path)

  def test_processor_used_novermin(self):
    fp = ScopedTemporaryFile()
    fp.writeln(b"import Queue  # novm")  # 2.0, !3
    fp.writeln(b"import builtins")       # !2, 3.0
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    print(mins)
    self.assertEqual(mins, [None, (3, 0)])
    self.assertFalse(incomp)
    self.assertEqual(unique_versions, [(3, 0)])
    self.assertEmpty(backports)
    self.assertTrue(used_novermin)
    self.assertFalse(maybe_anns)

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
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)

    self.assertEqual(mins, [(2, 0), (3, 0)])
    self.assertEqual(unique_versions, [(2, 0), (3, 0)])
    self.assertFalse(incomp)
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertFalse(maybe_anns)

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
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(2, 3), (3, 1)])
    self.assertFalse(incomp)
    self.assertEqual(unique_versions, [(2, 3), (3, 1)])
    self.assertEqual(backports, {"argparse"})
    self.assertFalse(used_novermin)
    self.assertFalse(maybe_anns)

  def test_processor_maybe_annotations(self):
    fp = ScopedTemporaryFile()
    fp.write(b"list[str]()")  # Generic annotations used.
    fp.close()
    self.config.set_eval_annotations(False)
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertFalse(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertTrue(maybe_anns)

  # Evaluating annotations is turned off by default.
  def test_processor_maybe_annotations_default(self):
    fp = ScopedTemporaryFile()
    fp.write(b"list[str]()")  # Generic annotations used.
    fp.close()
    paths = [fp.path()]
    processor = Processor()
    (mins, incomp, unique_versions, backports, used_novermin, maybe_anns) =\
      processor.process(paths, self.config)
    self.assertEqual(mins, [(0, 0), (0, 0)])
    self.assertFalse(incomp)
    self.assertEmpty(unique_versions)
    self.assertEmpty(backports)
    self.assertFalse(used_novermin)
    self.assertTrue(maybe_anns)

  def test_format_title_descs(self):
    descs = (
      ("one", [
        "one.one",
        "one.two",
        "one.three"
      ]),
      ("two", [
        "two.one",
        "two.two",
        "two.three"
      ]),
      ("three", [
        "three.one",
        "three.two",
        "three.three"
      ]),
    )
    titles = ["one", "two", "three"]
    self.assertEqual("""one   - one.one
        one.two
        one.three
two   - two.one
        two.two
        two.three
three - three.one
        three.two
        three.three""", format_title_descs(descs, titles))
    self.assertEqual("""  one   - one.one
          one.two
          one.three
  two   - two.one
          two.two
          two.three
  three - three.one
          three.two
          three.three""", format_title_descs(descs, titles, indent=2))

  def test_pessimistic_syntax_error(self):
    expected = [(0, 0), (0, 0)]
    self.assertEqual(expected, self.detect("if"))  # invalid syntax: if
    self.config.set_pessimistic(True)
    expected[current_version().major - 2] = None
    self.assertEqual(expected, self.detect("if"))

  def test_default_processes(self):
    self.assertEqual(cpu_count(), DEFAULT_PROCESSES)

  def test_compare_requirements_py2_and_py3_compatible(self):
    reqs = [(2, 7), (3, 6)]

    # User provides only one target
    self.assertFalse(compare_requirements(reqs, [(True, (2, 6))]))
    self.assertFalse(compare_requirements(reqs, [(False, (2, 6))]))
    self.assertTrue(compare_requirements(reqs, [(True, (2, 7))]))
    self.assertTrue(compare_requirements(reqs, [(False, (2, 7))]))
    self.assertFalse(compare_requirements(reqs, [(True, (3, 3))]))
    self.assertFalse(compare_requirements(reqs, [(False, (3, 3))]))
    self.assertTrue(compare_requirements(reqs, [(True, (3, 6))]))
    self.assertTrue(compare_requirements(reqs, [(False, (3, 6))]))
    self.assertFalse(compare_requirements(reqs, [(True, (3, 7))]))
    self.assertTrue(compare_requirements(reqs, [(False, (3, 7))]))

    # Missing and invalid targets
    self.assertFalse(compare_requirements(reqs, []))
    self.assertFalse(compare_requirements(reqs, [(True, (4, 1))]))

    # User provides multiple valid requirements, return true when both are
    # satisfied.
    self.assertTrue(compare_requirements(reqs, [(True, (2, 7)), (False, (3, 7))]))
    self.assertFalse(compare_requirements(reqs, [(True, (2, 7)), (True, (3, 7))]))

    # User provides valid along with invalid version: fail because the target
    # major version is missing
    self.assertFalse(compare_requirements(reqs, [(True, (2, 7)), (False, (4, 7))]))
    self.assertFalse(compare_requirements(reqs, [(True, (2, 7)), (True, (4, 7))]))

  def test_compare_requirements_py2_only(self):
    reqs = [(2, 7)]

    # Correct major version, compare against minor version
    self.assertFalse(compare_requirements(reqs, [(True, (2, 6))]))
    self.assertFalse(compare_requirements(reqs, [(False, (2, 6))]))
    self.assertTrue(compare_requirements(reqs, [(True, (2, 7))]))
    self.assertTrue(compare_requirements(reqs, [(False, (2, 7))]))

    # The user specifies the wrong major version: this will always fail
    self.assertFalse(compare_requirements(reqs, [(True, (3, 3))]))
    self.assertFalse(compare_requirements(reqs, [(False, (3, 3))]))
    self.assertFalse(compare_requirements(reqs, [(True, (3, 6))]))
    self.assertFalse(compare_requirements(reqs, [(False, (3, 6))]))
    self.assertFalse(compare_requirements(reqs, [(True, (3, 7))]))
    self.assertFalse(compare_requirements(reqs, [(False, (3, 7))]))
    self.assertFalse(compare_requirements(reqs, [(True, (4, 1))]))

    # Missing target: fail
    self.assertFalse(compare_requirements(reqs, []))

    # Multiple targets: fail because one target major version is missing
    self.assertFalse(compare_requirements(reqs, [(False, (2, 7)), (False, (3, 6))]))

  def test_compare_requirements_py3_only(self):
    reqs = [(3, 6)]
    # The user specifies the wrong major version: this will always fail
    self.assertFalse(compare_requirements(reqs, [(True, (2, 6))]))
    self.assertFalse(compare_requirements(reqs, [(False, (2, 6))]))
    self.assertFalse(compare_requirements(reqs, [(True, (2, 7))]))
    self.assertFalse(compare_requirements(reqs, [(False, (2, 7))]))
    self.assertFalse(compare_requirements(reqs, [(True, (4, 1))]))

    # Correct major version, compare against minor version
    self.assertFalse(compare_requirements(reqs, [(True, (3, 3))]))
    self.assertFalse(compare_requirements(reqs, [(False, (3, 3))]))
    self.assertTrue(compare_requirements(reqs, [(True, (3, 6))]))
    self.assertTrue(compare_requirements(reqs, [(False, (3, 6))]))
    self.assertFalse(compare_requirements(reqs, [(True, (3, 7))]))
    self.assertTrue(compare_requirements(reqs, [(False, (3, 7))]))

    # Missing and invalid requirements
    self.assertFalse(compare_requirements(reqs, []))

    # Multiple targets: fail because one target amjor version is missing
    self.assertFalse(compare_requirements(reqs, [(False, (2, 7)), (False, (3, 6))]))
