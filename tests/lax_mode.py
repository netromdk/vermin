from vermin import Config, SourceVisitor, parse_source

from .testutils import VerminTest, current_version

def visit(source):
  visitor = SourceVisitor()
  visitor.visit(parse_source(source))
  return visitor

class VerminLaxModeTests(VerminTest):
  def __init__(self, methodName):
    super(VerminLaxModeTests, self).__init__(methodName)
    self.config = Config.get()

  def setUp(self):
    self.config.reset()
    self.config.set_lax_mode(True)

  def tearDown(self):
    self.config.reset()

  def test_if(self):
    visitor = visit("if False:\n\timport ssl")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_elif(self):
    visitor = visit("if True:\n\tpass\nelif False:\n\timport ssl")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_ifexp(self):
    if current_version() >= 3.6:
      visitor = visit("print('ok') if True else (lambda: print(f'no'))()")
      self.assertEqual([0, 0], visitor.minimum_versions())

  def test_for(self):
    visitor = visit("for a in []:\n\timport ssl")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_while(self):
    visitor = visit("while False:\n\timport ssl")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_try(self):
    visitor = visit("try:\n\tpass\nexcept:\n\timport ssl")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_boolop(self):
    if current_version() >= 3.6:
      visitor = visit("True or (lambda: print(f'no'))()")
      self.assertEqual([0, 0], visitor.minimum_versions())
      visitor = visit("False and (lambda: print(f'no'))()")
      self.assertEqual([0, 0], visitor.minimum_versions())
