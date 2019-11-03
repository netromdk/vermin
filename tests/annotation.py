from .testutils import VerminTest, detect, current_version

class VerminModuleTests(VerminTest):
  def test_return_annotation(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), detect("def foo() -> str:\n\treturn ''"))

  def test_arg_annotation(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), detect("def foo(bar: int):\n\tpass"))

  def test_var_annotation(self):
    if current_version() >= 3.6:
      self.assertOnlyIn((3, 6), detect("a: int = 5"))
