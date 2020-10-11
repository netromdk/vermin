from .testutils import VerminTest, current_version

class VerminModuleTests(VerminTest):
  def test_return_annotation(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), self.detect("def foo() -> str:\n\treturn ''"))

  def test_arg_annotation(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), self.detect("def foo(bar: int):\n\tpass"))

  def test_var_annotation(self):
    if current_version() >= 3.6:
      self.assertOnlyIn((3, 6), self.detect("a: int = 5"))

  def test_Final_annotation(self):
    if current_version() >= 3.6:
      self.assertOnlyIn((3, 8), self.detect("a: Final = 5"))
      self.assertOnlyIn((3, 8), self.detect("a: Final[int] = 5"))
      self.assertOnlyIn((3, 8), self.detect("a: typing.Final[int] = 5"))

  def test_Literal_annotation(self):
    if current_version() >= 3.6:
      visitor = self.visit("a: Literal = 5")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("a: Literal[int] = 5")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("def only_four(x: Literal[4]):\n\treturn x")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      visitor = self.visit("def foo(x: typing.Literal[4]):\n\treturn x")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())

      # Detect literal annotations after first annotation.
      visitor = self.visit("def foo(x: L[1], y: Literal[4]):\n\treturn y")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())
      visitor = self.visit("def foo(x: L[1], y: L[1], z: Literal[4]):\n\treturn z")
      self.assertTrue(visitor.literal_annotations())
      self.assertOnlyIn((3, 8), visitor.minimum_versions())
