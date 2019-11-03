from .testutils import VerminTest, detect

class VerminStrftimeDirectiveTests(VerminTest):
  def test_G_directive(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime.now().strftime('%G')"))

  def test_u_directive(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime.now().strftime('%u')"))

  def test_V_directive(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime.now().strftime('%V')"))

  def test_f_directive(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from datetime import datetime\ndatetime.now().strftime('%f')"))
