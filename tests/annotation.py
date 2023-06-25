from .testutils import VerminTest

class VerminModuleTests(VerminTest):
  def test_return_annotation(self):
    self.assertOnlyIn((3, 0), self.detect("def foo() -> str:\n\treturn ''"))

  def test_arg_annotation(self):
    self.assertOnlyIn((3, 0), self.detect("def foo(bar: int):\n\tpass"))

  @VerminTest.skipUnlessVersion(3, 6)
  def test_var_annotation(self):
    self.assertOnlyIn((3, 6), self.detect("a: int = 5"))

  @VerminTest.skipUnlessVersion(3, 6)
  def test_Final_annotation(self):
    self.config.set_eval_annotations(True)
    self.assertOnlyIn((3, 8), self.detect("a: Final = 5"))
    self.assertOnlyIn((3, 8), self.detect("a: Final[int] = 5"))
    self.assertOnlyIn((3, 8), self.detect("a: typing.Final[int] = 5"))

  @VerminTest.skipUnlessVersion(3, 6)
  def test_Literal_annotation(self):
    self.config.set_eval_annotations(True)

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

  @VerminTest.skipUnlessVersion(3, 6)
  def test_maybe_Literal_annotation(self):
    self.config.set_eval_annotations(False)
    visitor = self.visit("def only_four(x: Literal[4]):\n\treturn x")
    self.assertFalse(visitor.literal_annotations())
    self.assertTrue(visitor.maybe_annotations())
    self.assertOnlyIn((3, 0), visitor.minimum_versions())
