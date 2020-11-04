from .testutils import VerminTest

class VerminBytesDirectiveTests(VerminTest):
  @VerminTest.skipUnlessVersion(3.0)
  def test_b_directive(self):
    self.assertOnlyIn((3, 5), self.detect("b'%b'"))

  @VerminTest.skipUnlessVersion(3.0)
  def test_a_directive(self):
    self.assertOnlyIn((3, 5), self.detect("b'%a'"))

  @VerminTest.skipUnlessVersion(3.0)
  def test_r_directive(self):
    self.assertOnlyIn(((2, 7), (3, 5)), self.detect("b'%r'"))
