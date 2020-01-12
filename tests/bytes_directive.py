from .testutils import VerminTest, detect, current_version

class VerminBytesDirectiveTests(VerminTest):
  def test_b_directive(self):
    if current_version() >= 3.5:
      self.assertOnlyIn((3, 5), detect("b'%b' % 10"))

  def test_a_directive(self):
    if current_version() >= 3.5:
      self.assertOnlyIn((3, 5), detect("b'%a' % 'x'"))

  def test_r_directive(self):
    v = current_version()
    if v < 3 or v >= 3.5:
      self.assertOnlyIn(((2, 7), (3, 5)), detect("b'%r' % 'x'"))
