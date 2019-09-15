from os.path import abspath
from multiprocessing import cpu_count

from vermin import parse_detect_source, combine_versions, InvalidVersionException, detect_paths,\
  process_paths, reverse_range, dotted_name

from .testutils import VerminTest, current_version, visit, detect

class VerminGeneralTests(VerminTest):
  def test_printv2(self):
    source = "print 'hello'"
    (node, mins, novermin) = parse_detect_source(source)
    v = current_version()
    if v >= 3.4:
      self.assertEqual(node, None)
      self.assertOnlyIn(2.0, mins)
    elif v >= 3.0 and v < 3.4:
      self.assertEqual(node, None)
      self.assertEqual(mins, [0, 0])
    else:  # < 3.0
      visitor = visit(source)
      self.assertTrue(visitor.printv2())
      self.assertEqual([2.0, 0], visitor.minimum_versions())

  def test_printv3(self):
    visitor = visit("print('hello')")
    if current_version() >= 3.0:
      self.assertTrue(visitor.printv3())
    else:
      self.assertTrue(visitor.printv2())

  def test_format(self):
    # Empty field name requires 2.7+
    visitor = visit("print('{}'.format(42))")
    self.assertTrue(visitor.format27())

    # Non-empty field name requires 2.6+
    visitor = visit("print('{0}'.format(42))")
    self.assertFalse(visitor.format27())

  def test_longv2(self):
    visitor = visit("n = long(42)")
    self.assertTrue(visitor.longv2())
    visitor = visit("isinstance(42, long)")
    self.assertTrue(visitor.longv2())

  def test_bytesv3(self):
    v = current_version()

    # py2: type(b'hello') = <type 'str'>
    if v >= 2.0 and v < 3.0:
      visitor = visit("s = b'hello'")
      self.assertFalse(visitor.bytesv3())
      self.assertEqual([0, 0], visitor.minimum_versions())

    # py3: type(b'hello') = <type 'bytes'>
    elif v >= 3.0:
      visitor = visit("s = b'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([None, 3.0], visitor.minimum_versions())
      visitor = visit("s = B'hello'")
      self.assertTrue(visitor.bytesv3())
      self.assertEqual([None, 3.0], visitor.minimum_versions())

  def test_fstrings(self):
    if current_version() >= 3.6:
      visitor = visit("name = 'world'\nf'hello {name}'")
      self.assertTrue(visitor.fstrings())
      self.assertEqual([None, 3.6], visitor.minimum_versions())

  def test_named_expressions(self):
    if current_version() >= 3.8:
      visitor = visit("a = 1\nif (b := a) == 1:\n\tprint(b)")
      self.assertTrue(visitor.named_expressions())
      self.assertEqual([None, 3.8], visitor.minimum_versions())

  def test_pos_only_args(self):
    if current_version() >= 3.8:
      visitor = visit("def foo(a, /, b): return a + b")
      self.assertTrue(visitor.pos_only_args())
      self.assertEqual([None, 3.8], visitor.minimum_versions())

  def test_yield_from(self):
    if current_version() >= 3.3:
      visitor = visit("def foo(x): yield from range(x)")
      self.assertTrue(visitor.yield_from())
      self.assertEqual([None, 3.3], visitor.minimum_versions())

  def test_raise_cause(self):
    if current_version() >= 3.3:
      visitor = visit("raise Exception() from None")
      self.assertTrue(visitor.raise_cause())
      self.assertEqual([None, 3.3], visitor.minimum_versions())

  def test_dict_comprehension(self):
    visitor = visit("{key: value for ld in lod for key, value in ld.items()}")
    self.assertTrue(visitor.dict_comprehension())
    self.assertEqual([2.7, 3.0], visitor.minimum_versions())

  def test_infix_matrix_multiplication(self):
    if current_version() >= 3.5:
      visitor = visit("M @ N")
      self.assertTrue(visitor.infix_matrix_multiplication())
      self.assertEqual([None, 3.5], visitor.minimum_versions())

  def test_strftime_directives(self):
    visitor = visit("from datetime import datetime\ndatetime.now().strftime('%A %d. %B %Y')")
    self.assertOnlyIn(("%A", "%d", "%B", "%Y"), visitor.strftime_directives())
    visitor = visit("from datetime import datetime\ndatetime.strptime('2018', '%Y')")
    self.assertOnlyIn("%Y", visitor.strftime_directives())

  def test_modules(self):
    visitor = visit("import ast\nimport sys, argparse\nfrom os import *")
    self.assertOnlyIn(("ast", "sys", "argparse", "os"), visitor.modules())

  def test_member_class(self):
    visitor = visit("from abc import ABC")
    self.assertOnlyIn("abc.ABC", visitor.members())
    visitor = visit("import abc\nclass a(abc.ABC): pass")
    self.assertOnlyIn("abc.ABC", visitor.members())

  def test_member_function(self):
    visitor = visit("from sys import exc_clear")
    self.assertOnlyIn("sys.exc_clear", visitor.members())

  def test_member_constant(self):
    visitor = visit("from sys import version_info")
    self.assertOnlyIn("sys.version_info", visitor.members())

  def test_member_kwargs(self):
    visitor = visit("from os import open\nfd = open(dir_fd = None)")
    self.assertOnlyIn([("os.open", "dir_fd")], visitor.kwargs())

  def test_detect_vermin_min_versions(self):
    paths = detect_paths([abspath("vermin")])
    (mins, incomp, unique_versions) = process_paths(paths, cpu_count())
    self.assertOnlyIn((2.7, 3.0), mins)

  def test_combine_versions(self):
    with self.assertRaises(AssertionError):
      combine_versions([None], [None, None])
    self.assertEqual([2.0, 3.1], combine_versions([2.0, 3.0], [2.0, 3.1]))
    self.assertEqual([2.1, 3.0], combine_versions([2.1, 3.0], [2.0, 3.0]))
    self.assertEqual([None, 3.0], combine_versions([2.0, 3.0], [None, 3.0]))
    self.assertEqual([2.0, None], combine_versions([2.0, None], [2.0, 3.0]))
    self.assertEqual([None, None], combine_versions([2.0, 3.0], [None, None]))
    self.assertEqual([None, None], combine_versions([None, None], [2.0, 3.0]))
    with self.assertRaises(InvalidVersionException):
      combine_versions([2.0, None], [None, 3.0])
    with self.assertRaises(InvalidVersionException):
      combine_versions([None, 3.0], [2.0, None])
    self.assertEqual([0, 3.0], combine_versions([0, 3.0], [0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([0, 3.0], [2.0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 3.0], [0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 0], [2.0, 3.0]))
    self.assertEqual([2.0, 3.0], combine_versions([2.0, 3.0], [2.0, 0]))

  def test_detect_min_version(self):
    self.assertEqual([2.6, 3.0], detect("import abc"))

    # (2.6, 3.0) vs. (2.7, 3.2) = (2.7, 3.2)
    self.assertEqual([2.7, 3.2], detect("import abc, argparse"))

    # (2.6, 3.0) vs. (None, 3.4) = (None, 3.4)
    self.assertEqual([None, 3.4], detect("import abc\nfrom abc import ABC"))

    # (2.0, None) vs. (2.0, 3.0) = (2.0, None)
    self.assertEqual([2.0, None], detect("import repr\nfrom sys import getdefaultencoding"))

    # (2.0, None) vs. (None, 3.0) = both exclude the other major version -> exception!
    with self.assertRaises(InvalidVersionException):
      detect("import copy_reg, http")

  def test_reverse_range(self):
    self.assertEqual(list(reverse_range([1, 2, 3])), [2, 1, 0])
    self.assertEqual(list(reverse_range([1, 2])), [1, 0])
    self.assertEqual(list(reverse_range([])), [])

  def test_dotted_name(self):
    self.assertEqual(dotted_name(["hello", "world"]), "hello.world")
    self.assertEqual(dotted_name(["foo", ["bar", "baz"], "boom"]), "foo.bar.baz.boom")
    self.assertEqual(dotted_name(["foo", ("bar", "baz"), "boom"]), "foo.bar.baz.boom")
    self.assertEqual(dotted_name([1, 2, 3]), "1.2.3")
    self.assertEqual(dotted_name("right"), "right")

  def test_assign_rvalue_attribute(self):
    self.assertEqual([None, 3.3], detect("import bz2\nv = bz2.BZ2File\nv.writable"))

  def test_user_defined(self):
    visitor = visit("def hello(): pass\nhello2()\nclass foo(): pass")
    self.assertOnlyIn(["hello", "foo"], visitor.user_defined())

  def test_ignore_members_when_user_defined_funcs(self):
    # `next()` was builtin from 2.6.
    visitor = visit("def next(): pass\nnext()")
    self.assertOnlyIn("next", visitor.user_defined())
    self.assertEmpty(visitor.members())

  def test_ignore_members_when_user_defined_classes(self):
    # `bytearray` was builtin from 2.6.
    visitor = visit("class bytearray: pass\nba = bytearray()")
    self.assertOnlyIn(["bytearray", "ba"], visitor.user_defined())
    self.assertEmpty(visitor.members())

  def test_ignore_modules_when_user_defined_funcs(self):
    # This test relies on the rule for "SimpleXMLRPCServer" module.

    # Ignore module due to class def.
    visitor = visit("import SimpleXMLRPCServer\n"
                    "def SimpleXMLRPCServer(): pass\n"
                    "src = SimpleXMLRPCServer()")
    self.assertOnlyIn(["SimpleXMLRPCServer", "src"], visitor.user_defined())
    self.assertEmpty(visitor.modules())

  def test_ignore_modules_when_user_defined_classes(self):
    # This test relies on the rule for "SimpleXMLRPCServer" module.

    # Ignore module due to class def.
    visitor = visit("import SimpleXMLRPCServer\n"
                    "class SimpleXMLRPCServer: pass\n"
                    "src = SimpleXMLRPCServer()")
    self.assertOnlyIn(["SimpleXMLRPCServer", "src"], visitor.user_defined())
    self.assertEmpty(visitor.modules())

  def test_str_from_type(self):
    visitor = visit("\"\".zfill(1)")
    self.assertIn("str.zfill", visitor.members())
    visitor = visit("str().zfill(1)")
    self.assertIn("str.zfill", visitor.members())

  def test_unicode_from_type(self):
    if current_version() < 3.0:
      visitor = visit("u\"\".isdecimal()")
      self.assertIn("unicode.isdecimal", visitor.members())
      visitor = visit("unicode().isdecimal()")
      self.assertIn("unicode.isdecimal", visitor.members())

  def test_list_from_type(self):
    visitor = visit("[].clear()")
    self.assertIn("list.clear", visitor.members())
    visitor = visit("list().clear()")
    self.assertIn("list.clear", visitor.members())

  def test_dict_from_type(self):
    visitor = visit("{}.pop()")
    self.assertIn("dict.pop", visitor.members())
    visitor = visit("dict().pop()")
    self.assertIn("dict.pop", visitor.members())

  def test_set_from_type(self):
    visitor = visit("{1}.isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())
    visitor = visit("set().isdisjoint()")
    self.assertIn("set.isdisjoint", visitor.members())

  def test_frozenset_from_type(self):
    visitor = visit("frozenset().isdisjoint()")
    self.assertIn("frozenset.isdisjoint", visitor.members())

  def test_int_from_type(self):
    visitor = visit("(1).bit_length()")
    self.assertIn("int.bit_length", visitor.members())
    visitor = visit("int().bit_length()")
    self.assertIn("int.bit_length", visitor.members())

  def test_long_from_type(self):
    if current_version() < 3.0:
      visitor = visit("(1L).bit_length()")
      self.assertIn("long.bit_length", visitor.members())
      visitor = visit("long().bit_length()")
      self.assertIn("long.bit_length", visitor.members())

  def test_float_from_type(self):
    visitor = visit("(4.2).hex()")
    self.assertIn("float.hex", visitor.members())
    visitor = visit("float().hex()")
    self.assertIn("float.hex", visitor.members())

  def test_mod_inverse_pow(self):
    # All arguments must be ints.
    visitor = visit("pow(1.1, -1, 3)")
    self.assertFalse(visitor.modular_inverse_pow())
    visitor = visit("pow(1, -1.0, 3)")
    self.assertFalse(visitor.modular_inverse_pow())
    visitor = visit("pow(1, -1, 3.0)")
    self.assertFalse(visitor.modular_inverse_pow())

    # The second argument can be negative to yield modular inverse calculation.
    visitor = visit("pow(1, -2, 3)")
    self.assertTrue(visitor.modular_inverse_pow())
    self.assertOnlyIn(3.8, visitor.minimum_versions())
