from vermin import reverse_string, edit_distance, edit_distance_relaxed

from .testutils import VerminTest

class VerminUtilityTests(VerminTest):
  @VerminTest.parameterized_args([
    ("abc", "cba"),
    ("test", "tset"),
    ("123", "321"),
  ])
  def test_reverse_string(self, s, rev):
    self.assertEqual(rev, reverse_string(s), msg="{} vs. {}".format(s, rev))

  @VerminTest.parameterized_args([
    ("test", "test", 0),
    ("test", "tast", 1),
    ("tes", "test", 1),
    ("test", "tes", 1),
    ("st", "test", 2),
    ("test", "st", 2),
    ("--nolint", "--no-lint", 4),
  ])
  def test_edit_distance(self, a, b, dist):
    self.assertEqual(dist, edit_distance(a, b), msg="{} vs. {}".format(a, b))

  @VerminTest.parameterized_args([
    ("--test", "test"),
    ("-test", "tast"),
    ("--tes", "test"),
    ("--test", "tes"),
    ("--st", "test"),
    ("--test", "st"),
    ("--nolint", "--no-lint"),
  ])
  def test_edit_distance_relaxed_no_ignore(self, a, b):
    self.assertEqual(edit_distance(a, b), edit_distance_relaxed(a, b), msg="{} vs. {}".format(a, b))

  @VerminTest.parameterized_args([
    ("--test", "--test", 0),
    ("--test", "--tast", 1),
    ("--tes", "--test", 1),
    ("--test", "--tes", 1),
    ("--st", "--test", 2),
    ("--test", "--st", 2),
    ("--nolint", "--no-lint", 0),
  ])
  def test_edit_distance_relaxed_ignore(self, a, b, dist):
    ignore = ["-"]
    self.assertEqual(dist, edit_distance_relaxed(a, b, ignore), msg="{} vs. {}".format(a, b))
