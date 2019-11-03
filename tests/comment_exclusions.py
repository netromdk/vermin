from .testutils import VerminTest, visit, current_version

class VerminCommentsExclusionsTests(VerminTest):
  def test_import(self):
    visitor = visit("# novm\nimport email.parser.FeedParser")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Comment "novm" or "novermin" on its own refers to the next line.
    self.assertIn(2, visitor.no_lines())

    visitor = visit("# novermin\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing at end of line w/o spacing.
    visitor = visit("import email.parser.FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("import email.parser.FeedParser  #novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("import email.parser.FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("import email.parser.FeedParser#novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_from_import(self):
    visitor = visit("# novm\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("# novermin\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("from email.parser import FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = visit("from email.parser import FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_function(self):
    visitor = visit("# novm\ndef foo():\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("def foo(): # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_async_function(self):
    if current_version() >= 3.5:
      visitor = visit("# novm\nasync def foo():\n\tall([])")
      self.assertIn(2, visitor.no_lines())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
      visitor = visit("async def foo():  #novm\n\tall([])")
      self.assertIn(1, visitor.no_lines())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_class(self):
    visitor = visit("# novm\nclass foo():\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("class foo(): # novm\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_if(self):
    visitor = visit("# novm\nif True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("if True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_for(self):
    visitor = visit("# novm\nfor a in [1,2,3]:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("for a in [1,2,3]:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_while(self):
    visitor = visit("# novm\nwhile True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("while True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_boolop(self):
    visitor = visit("# novm\nFalse or all([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("False or all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_call(self):
    visitor = visit("# novm\nall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = visit("all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
