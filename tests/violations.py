from vermin import InvalidVersionException

from .testutils import VerminTest

class VerminViolationsTests(VerminTest):
  def setUp(self):
    self.config.set_only_show_violations(True)
    self.config.set_verbose(3)  # Verbosity to get output text to validate.
    # NOTE: Each test must define one or two targets to test for violations against. Exactness
    # doesn't play any role in determiniting violations, only the exit code of the program.

  def test_issue_57_example(self):
    self.config.add_target((2, 6))
    self.config.add_target((3, 2))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    # "(version)" comments mark the results.
    visitor = self.visit("""# file 1:
import enum        # 2.4, (3.3)
bytes.maketrans()  # (!2), 3.1
all()              # 2.5, 3.0

# file 2:
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3: 'bytes.maketrans' member requires !2, 3.1
""", visitor.output_text())

  def test_v2_3_target(self):
    self.config.add_target((2, 3))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, (3.3)
bytes.maketrans()  # (!2), 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3: 'bytes.maketrans' member requires !2, 3.1
L4 C0: 'all' member requires 2.5, 3.0
""", visitor.output_text())

  def test_v2_3_target_no_v2_incomp(self):
    self.config.add_target((2, 3))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, (3.3)
all()              # (2.5), 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([(2, 5), (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3 C0: 'all' member requires 2.5, 3.0
""", visitor.output_text())

  def test_v2_4_target(self):
    self.config.add_target((2, 4))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, 3.3
bytes.maketrans()  # (!2), (3.1)
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L3: 'bytes.maketrans' member requires !2, 3.1
L4 C0: 'all' member requires 2.5, 3.0
""", visitor.output_text())

  def test_v2_4_target_no_v2_incomp(self):
    self.config.add_target((2, 4))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, 3.3
all()              # (2.5), (3.0)
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([(2, 5), (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L3 C0: 'all' member requires 2.5, 3.0
""", visitor.output_text())

  def test_v2_1_v3_1_targets(self):
    self.config.add_target((2, 1))
    self.config.add_target((3, 1))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, (3.3)
bytes.maketrans()  # (!2), 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3: 'bytes.maketrans' member requires !2, 3.1
L4 C0: 'all' member requires 2.5, 3.0
L5 C0: 'enumerate' member requires 2.3, 3.0
""", visitor.output_text())

  def test_v2_1_v3_1_targets_no_v2_incomp(self):
    self.config.add_target((2, 1))
    self.config.add_target((3, 1))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # 2.4, (3.3)
all()              # (2.5), 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([(2, 5), (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3 C0: 'all' member requires 2.5, 3.0
L4 C0: 'enumerate' member requires 2.3, 3.0
""", visitor.output_text())

  def test_v3_1_target(self):
    self.config.add_target((3, 1))
    self.config.add_backport("enum")  # !2, 3.4 -> 2.4, 3.3

    visitor = self.visit("""
import enum        # (2.4), (3.3)
bytes.maketrans()  # !2, 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
""", visitor.output_text())

  def test_2_incomp_3_match_show_no_rules(self):
    # !2, == 3.4
    self.config.add_target((3, 4))

    visitor = self.visit("""
import enum        # !2, 3.4  <- match version
bytes.maketrans()  # !2, 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 4)], visitor.minimum_versions())
    self.assertEmpty(visitor.output_text())

  def test_2_incomp_above_3_show_violations(self):
    # !2, > 3.1
    self.config.add_target((3, 1))

    visitor = self.visit("""
import enum        # !2, 3.4  <- is > 3.1
bytes.maketrans()  # !2, 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 4)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires !2, 3.4
""", visitor.output_text())

  def test_2_incomp_below_3_show_no_rules(self):
    # !2, < 3.5
    self.config.add_target((3, 5))

    visitor = self.visit("""
import enum        # !2, 3.4
bytes.maketrans()  # !2, 3.1
all()              # 2.5, 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([None, (3, 4)], visitor.minimum_versions())
    self.assertEmpty(visitor.output_text())

  def test_2_maybe_3_incomp_show_violations(self):
    # ~2, !3
    self.config.add_target((3, 1))

    visitor = self.visit("""
import hotshot  # 2.2, !3  <- Incomp with 3.1 requirement
""")
    self.assertEqual([(2, 2), None], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'hotshot' module requires 2.2, !3
""", visitor.output_text())

  def test_2_incomp_3_incomp_show_incomp(self):
    # !2, !3
    self.config.add_target((3, 1))

    with self.assertRaises(InvalidVersionException):
      self.visit("""
import enum     # !2, 3.4
import hotshot  # 2.2, !3
""")

  def test_two_targets_above_both(self):
    # >2.3, >3.0
    self.config.add_target((2, 3))
    self.config.add_target((3, 0))
    self.config.add_backport("enum")

    visitor = self.visit("""
import enum        # 2.4, (3.3)
all()              # (2.5), 3.0
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([(2, 5), (3, 3)], visitor.minimum_versions())
    self.assertEqual("""L2 C7: 'enum' module requires 2.4, 3.3
L3 C0: 'all' member requires 2.5, 3.0
""", visitor.output_text())

  def test_two_targets_above_2_below_3(self):
    # >2.2, <3.1
    self.config.add_target((2, 2))
    self.config.add_target((3, 1))

    visitor = self.visit("""
all()              # (2.5), (3.0)
enumerate()        # 2.3, 3.0
""")
    self.assertEqual([(2, 5), (3, 0)], visitor.minimum_versions())
    self.assertEqual("""L2 C0: 'all' member requires 2.5, 3.0
L3 C0: 'enumerate' member requires 2.3, 3.0
""", visitor.output_text())

  def test_two_targets_below_2_above_3(self):
    # <2.4, >3.0
    self.config.add_target((2, 4))
    self.config.add_target((3, 0))
    self.config.add_backport("argparse")

    visitor = self.visit("""
enumerate()        # 2.3, 3.0
import argparse    # (2.3), (3.1)
""")
    self.assertEqual([(2, 3), (3, 1)], visitor.minimum_versions())
    self.assertEqual("""L3 C7: 'argparse' module requires 2.3, 3.1
""", visitor.output_text())

  def test_two_targets_below_both(self):
    # <2.4, <3.3
    self.config.add_target((2, 4))
    self.config.add_target((3, 3))
    self.config.add_backport("argparse")

    visitor = self.visit("""
enumerate()        # 2.3, 3.0
import argparse    # 2.3, 3.1
""")

    # All below targets so no violations: no rules shown.
    self.assertEqual([(2, 3), (3, 1)], visitor.minimum_versions())
    self.assertEmpty(visitor.output_text())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_violate_variable_annotations(self):
    # Violation.
    self.config.add_target((3, 5))

    code = "x: int"
    visitor = self.visit(code)
    self.assertEqual("""L1: variable annotations require !2, 3.6
""", visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((3, 6))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

  def test_violate_unpacking_assignment(self):
    # Violation.
    self.config.add_target((2, 7))

    code = "*a, b = [1, 2, 3]"
    visitor = self.visit(code)
    self.assertEqual("""L1: unpacking assignment requires !2, 3.0
""", visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((3, 0))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

  @VerminTest.skipUnlessVersion(3, 5)
  def test_violate_generalized_unpacking(self):
    # Violation.
    self.config.add_target((3, 4))

    code = "(*range(4), 4)"
    visitor = self.visit(code)
    self.assertEqual("""L1: generalized unpacking requires !2, 3.5
""", visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((3, 5))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

  def test_violate_mod_inv(self):
    # Violation.
    self.config.add_target((3, 7))

    code = "pow(1, -2, 3)"
    visitor = self.visit(code)
    self.assertEqual("""L1: modular inverse pow() requires !2, 3.8
""", visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((3, 8))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

  def test_violate_format27(self):
    # Violation.
    self.config.add_target((2, 6))

    code = "'hello {}!'.format('world')"
    txt = """L1: `"..{}..".format(..)` requires 2.7, 3.0
"""
    visitor = self.visit(code)
    self.assertEqual(txt, visitor.output_text())

    self.config.clear_targets()
    self.config.add_target((2, 6))
    self.config.add_target((3, 0))
    visitor = self.visit(code)
    self.assertEqual(txt, visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((2, 7))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

    self.config.clear_targets()
    self.config.add_target((3, 0))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

    self.config.clear_targets()
    self.config.add_target((2, 7))
    self.config.add_target((3, 0))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())

  def test_violate_bytesv3(self):
    # Violation.
    self.config.add_target((2, 5))

    code = "a = b'42'"
    visitor = self.visit(code)
    self.assertEqual("""L1: byte string (b'..') or `str` synonym requires 2.6, 3.0
""", visitor.output_text())

    # No violation.
    self.config.clear_targets()
    self.config.add_target((3, 0))
    visitor = self.visit(code)
    self.assertEmpty(visitor.output_text())
