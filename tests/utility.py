from vermin.utility import split_lines

from .testutils import VerminTest


class UtilityTests(VerminTest):
  def test_split_lines_lf(self):
    lines, offsets = split_lines("a\nb\n")
    self.assertEqual(["a", "b"], lines)
    self.assertEqual([0, 2, 4], offsets)

  def test_split_lines_lf_no_trailing_terminator(self):
    lines, offsets = split_lines("a\nb")
    self.assertEqual(["a", "b"], lines)
    self.assertEqual([0, 2, 3], offsets)

  def test_split_lines_crlf(self):
    lines, offsets = split_lines("a\r\nb\r\n")
    self.assertEqual(["a", "b"], lines)
    self.assertEqual([0, 3, 6], offsets)

  def test_split_lines_crlf_mixed(self):
    lines, offsets = split_lines("a\r\nb\nc\rd")
    self.assertEqual(["a", "b", "c", "d"], lines)
    self.assertEqual([0, 3, 5, 7, 8], offsets)

  def test_split_lines_bare_cr(self):
    lines, offsets = split_lines("a\rb\r")
    self.assertEqual(["a", "b"], lines)
    self.assertEqual([0, 2, 4], offsets)

  def test_split_lines_empty(self):
    lines, offsets = split_lines("")
    self.assertEqual([], lines)
    self.assertEqual([0], offsets)

  def test_split_lines_only_terminator(self):
    self.assertEqual(([""], [0, 1]), split_lines("\n"))
    self.assertEqual(([""], [0, 2]), split_lines("\r\n"))

  def test_split_lines_consecutive_terminators(self):
    lines, offsets = split_lines("a\n\n")
    self.assertEqual(["a", ""], lines)
    self.assertEqual([0, 2, 3], offsets)

  def test_split_lines_no_terminator(self):
    lines, offsets = split_lines("single")
    self.assertEqual(["single"], lines)
    self.assertEqual([0, 6], offsets)

  def test_split_lines_parser_separators_not_split(self):
    lines, offsets = split_lines("x = \"\v\f\"\nf\"{y}\"\n")
    self.assertEqual(["x = \"\v\f\"", "f\"{y}\""], lines)
    self.assertEqual([0, 9, 16], offsets)
