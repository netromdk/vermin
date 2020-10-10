from vermin import Config, visit

from .testutils import VerminTest

class VerminExclusionsTests(VerminTest):
  def __init__(self, methodName):
    super(VerminExclusionsTests, self).__init__(methodName)
    self.config = Config.get()

  def setUp(self):
    self.config.reset()

  def tearDown(self):
    self.config.reset()

  def test_module(self):
    visitor = visit("from email.parser import FeedParser")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

    self.config.add_exclusion("email.parser.FeedParser")
    visitor = visit("from email.parser import FeedParser")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_kwarg(self):
    visitor = visit("from argparse import ArgumentParser\nArgumentParser(allow_abbrev=False)")
    self.assertEqual([None, (3, 5)], visitor.minimum_versions())

    self.config.add_exclusion("argparse")  # module
    self.config.add_exclusion("argparse.ArgumentParser(allow_abbrev)")  # kwarg
    visitor = visit("from argparse import ArgumentParser\nArgumentParser(allow_abbrev=False)")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())

  def test_codecs_error_handler(self):
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', 'surrogateescape')")
    self.assertEqual([None, (3, 1)], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', errors='surrogateescape')")
    self.assertEqual([None, (3, 1)], visitor.minimum_versions())

    self.config.add_exclusion("ceh=surrogateescape")
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', 'surrogateescape')")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', errors='surrogateescape')")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

  def test_codecs_encoding(self):
    visitor = visit("import codecs\ncodecs.encode('test', 'koi8_t')")
    self.assertEqual([None, (3, 5)], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', data_encoding='koi8_t')")
    self.assertEqual([None, (3, 5)], visitor.minimum_versions())

    self.config.add_exclusion("ce=koi8_t")
    visitor = visit("import codecs\ncodecs.encode('test', 'koi8_t')")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', data_encoding='koi8_t')")
    self.assertEqual([(2, 4), (3, 0)], visitor.minimum_versions())

  def test_long(self):
    visitor = visit("a = long(1)")
    self.assertEqual([(2, 0), None], visitor.minimum_versions())

    self.config.add_exclusion("long")
    visitor = visit("a = long(1)")
    self.assertEqual([(0, 0), (0, 0)], visitor.minimum_versions())
