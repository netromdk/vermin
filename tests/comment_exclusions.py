from .testutils import VerminTest, current_version

class VerminCommentsExclusionsTests(VerminTest):
  def test_import(self):
    visitor = self.visit("# novm\nimport email.parser.FeedParser")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Comment "novm" or "novermin" on its own refers to the next line.
    self.assertIn(2, visitor.no_lines())

    visitor = self.visit("# novermin\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing at end of line w/o spacing.
    visitor = self.visit("import email.parser.FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  #novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser#novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing multiple comment segments.
    visitor = self.visit("import email.parser.FeedParser  # noqa # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # novm # noqa")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser  # noqa # novermin # nolint")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("import email.parser.FeedParser "
                         "# type: ignore[attr-defined] # novm # pylint: disable=no-member")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Testing multiple comment segments on its own refers to the next line.
    visitor = self.visit("# noqa # novm # nolint\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# noqa # novermin # nolint\nimport email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# type: ignore[attr-defined] # novm # pylint: disable=no-member\n"
                         "import email.parser.FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    # Detect comments on line that are indented, i.e. col != 0 but the comment is alone on the line.
    visitor = self.visit("if 1:\n # novermin\n import email.parser.FeedParser")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if 1:\n\t# novermin\n\timport email.parser.FeedParser")
    self.assertIn(3, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if 1:\n\tif 1:\n\t\t# novermin\n\t\timport email.parser.FeedParser")
    self.assertIn(4, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_from_import(self):
    visitor = self.visit("# novm\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("# novermin\nfrom email.parser import FeedParser")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("from email.parser import FeedParser  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

    visitor = self.visit("from email.parser import FeedParser  # novermin")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_function(self):
    visitor = self.visit("# novm\ndef foo():\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("def foo(): # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_async_function(self):
    if current_version() >= 3.5:
      visitor = self.visit("# novm\nasync def foo():\n\tall([])")
      self.assertIn(2, visitor.no_lines())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
      visitor = self.visit("async def foo():  #novm\n\tall([])")
      self.assertIn(1, visitor.no_lines())
      self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_class(self):
    visitor = self.visit("# novm\nclass foo():\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("class foo(): # novm\n\tdef __init__(self):\n\t\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_if(self):
    visitor = self.visit("# novm\nif True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("if True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_for(self):
    visitor = self.visit("# novm\nfor a in [1,2,3]:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("for a in [1,2,3]:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_while(self):
    visitor = self.visit("# novm\nwhile True:\n\tall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("while True:  # novm\n\tall([])")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_boolop(self):
    visitor = self.visit("# novm\nFalse or all([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("False or all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_call(self):
    visitor = self.visit("# novm\nall([])")
    self.assertIn(2, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("all([])  # novm")
    self.assertIn(1, visitor.no_lines())
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
