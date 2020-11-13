from .testutils import VerminTest

class VerminLaxModeTests(VerminTest):
  def setUp(self):
    self.config.set_lax_mode(True)

  def test_if(self):
    visitor = self.visit("if False:\n\timport ssl")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_elif(self):
    visitor = self.visit("if True:\n\tpass\nelif False:\n\timport ssl")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_ifexp(self):
    visitor = self.visit("print('ok') if True else (lambda: print(f'no'))()")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    self.config.set_lax_mode(False)
    visitor = self.visit("print('ok') if True else (lambda: print(f'no'))()")
    self.assertEqual([None, (3, 6)], visitor.minimum_versions())

  def test_for(self):
    visitor = self.visit("for a in []:\n\timport ssl")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_async_for(self):
    visitor = self.visit("""async def foo():
  async for a in []:
    import ssl
""")
    self.assertOnlyIn((3, 5), visitor.minimum_versions())

  def test_while(self):
    visitor = self.visit("while False:\n\timport ssl")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_try(self):
    visitor = self.visit("try:\n\tpass\nexcept:\n\timport ssl")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  @VerminTest.skipUnlessVersion(3, 6)
  def test_boolop(self):
    visitor = self.visit("True or (lambda: print(f'no'))()")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
    visitor = self.visit("False and (lambda: print(f'no'))()")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_with(self):
    visitor = self.visit("""with 1 as a:
  import ssl
""")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
