from .testutils import VerminTest, detect

class VerminModuleTests(VerminTest):

  def test_return_annotation(self):
    self.assertOnlyIn(3.5, detect("def foo() -> str:\n    return ''"))

  def test_arg_annotation(self):
    self.assertOnlyIn(3.5, detect("def foo(bar: int):\n    pass"))

  def test_var_annotation(self):
    self.assertOnlyIn(3.6, detect("a: int = 5"))
