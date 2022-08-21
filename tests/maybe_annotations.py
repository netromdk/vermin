from .testutils import VerminTest

class VerminMaybeAnnotationsTests(VerminTest):
  def setUp(self):
    self.config.set_eval_annotations(False)

  @VerminTest.skipUnlessVersion(3, 6)
  def test_ann_assign(self):
    visitor = self.visit("a: b = 1")
    self.assertTrue(visitor.maybe_annotations())

  @VerminTest.skipUnlessVersion(3, 10)
  def test_ann_assign_union_type(self):
    visitor = self.visit("a: b | c = 1")
    self.assertTrue(visitor.maybe_annotations())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_lit_annotation(self):
    visitor = self.visit("a: Literal = 5")
    self.assertTrue(visitor.maybe_annotations())

    visitor = self.visit("a: Literal[int] = 5")
    self.assertTrue(visitor.maybe_annotations())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_builtin_generic_annotation(self):
    visitor = self.visit("dict[str, list[int]]")
    self.assertTrue(visitor.maybe_annotations())

    visitor = self.visit("l = list[str]()")
    self.assertTrue(visitor.maybe_annotations())
