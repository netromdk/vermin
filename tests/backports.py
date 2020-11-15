from vermin import Backports

from .testutils import VerminTest

class VerminBackportsTests(VerminTest):
  def test_modules(self):
    self.assertEqualItems((
      "argparse",
      "asyncio",
      "configparser",
      "contextvars",
      "dataclasses",
      "enum",
      "faulthandler",
      "importlib",
      "ipaddress",
      "statistics",
      "typing",
    ), Backports.modules())

  def test_is_backport(self):
    for mod in Backports.modules():
      self.assertTrue(Backports.is_backport(mod))

  def test_str(self):
    self.assertEqual("""   argparse     - https://pypi.org/project/argparse/
   asyncio      - https://pypi.org/project/asyncio/
   configparser - https://pypi.org/project/configparser/
   contextvars  - https://pypi.org/project/contextvars/
   dataclasses  - https://pypi.org/project/dataclasses/
   enum         - https://pypi.org/project/enum34/
   faulthandler - https://pypi.org/project/faulthandler/
   importlib    - https://pypi.org/project/importlib/
   ipaddress    - https://pypi.org/project/ipaddress/
   statistics   - https://pypi.org/project/statistics/
   typing       - https://pypi.org/project/typing/""", Backports.str(3))
