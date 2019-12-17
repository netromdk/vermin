from vermin import Backports

from .testutils import VerminTest

class VerminBackportsTests(VerminTest):
  def test_modules(self):
    self.assertEqualItems((
      "argparse",
      "configparser",
      "enum",
      "faulthandler",
      "typing",
    ), Backports.modules())

  def test_is_backport(self):
    for mod in Backports.modules():
      self.assertTrue(Backports.is_backport(mod))

  def test_str(self):
    self.assertEqual("""   argparse     - https://pypi.org/project/argparse/
   configparser - https://pypi.org/project/configparser/
   enum         - https://pypi.org/project/enum34/
   faulthandler - https://pypi.org/project/faulthandler/
   typing       - https://pypi.org/project/typing/""", Backports.str(3))
