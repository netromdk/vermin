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
      "mock",
      "statistics",
      "typing",
      "typing_extensions==4.0",
      "typing_extensions==4.3",
      "typing_extensions",
      "zoneinfo",
    ), Backports.modules())

  def test_is_backport(self):
    for mod in Backports.modules():
      self.assertTrue(Backports.is_backport(mod))

  def test_str(self):
    self.assertEqual("""   argparse               - https://pypi.org/project/argparse/ (2.3, 3.1)
   asyncio                - https://pypi.org/project/asyncio/ (!2, 3.3)
   configparser           - https://pypi.org/project/configparser/ (2.6, 3.0)
   contextvars            - https://pypi.org/project/contextvars/ (!2, 3.5)
   dataclasses            - https://pypi.org/project/dataclasses/ (!2, 3.6)
   enum                   - https://pypi.org/project/enum34/ (2.4, 3.3)
   faulthandler           - https://pypi.org/project/faulthandler/ (2.6, 3.0)
   importlib              - https://pypi.org/project/importlib/ (2.3, 3.0)
   ipaddress              - https://pypi.org/project/ipaddress/ (2.6, 3.2)
   mock                   - https://pypi.org/project/mock/ (!2, 3.6)
   statistics             - https://pypi.org/project/statistics/ (2.6, 3.4)
   typing                 - https://pypi.org/project/typing/ (2.7, 3.2)
   typing_extensions==4.0 - https://pypi.org/project/typing-extensions/4.0.0/ (!2, 3.6)
   typing_extensions==4.3 - https://pypi.org/project/typing-extensions/4.3.0/ (!2, 3.7)
   typing_extensions      - https://pypi.org/project/typing-extensions/4.3.0/ (!2, 3.7)
   zoneinfo               - https://pypi.org/project/backports.zoneinfo/ (!2, 3.6)""",
                     Backports.str(3))

  def test_version_filter(self):
    self.assertEqual("somemodule", Backports.version_filter("somemodule==1.2"))
    self.assertEqual("some_module", Backports.version_filter("some_module==1.2"))
    self.assertEqual("some.module", Backports.version_filter("some.module==1.2"))
    self.assertEqual("somemodule", Backports.version_filter("somemodule==string"))
    self.assertEqual("somemodule", Backports.version_filter("somemodule"))

  def test_unversioned_filter(self):
    self.assertEqualItems([
      "argparse",
      "asyncio",
      "configparser",
      "contextvars",
      "dataclasses",
      "enum",
      "faulthandler",
      "importlib",
      "ipaddress",
      "mock",
      "statistics",
      "typing",
      "typing_extensions",
      "zoneinfo",
    ], Backports.unversioned_filter(Backports.modules()))

  def test_expand_versions(self):
    self.assertEqual([
      ("typing_extensions",
       ["https://pypi.org/project/typing-extensions/4.3.0/"],
       (None, (3, 7))),
      ("typing_extensions==4.3",
       ["https://pypi.org/project/typing-extensions/4.3.0/"],
       (None, (3, 7))),
      ("typing_extensions==4.0",
       ["https://pypi.org/project/typing-extensions/4.0.0/"],
       (None, (3, 6))),
    ], Backports.expand_versions("typing_extensions"))
    self.assertEqual([
      ("enum",
       ["https://pypi.org/project/enum34/"],
       ((2, 4), (3, 3))),
    ], Backports.expand_versions("enum"))
