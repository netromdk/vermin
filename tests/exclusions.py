from vermin import Config, SourceVisitor, parse_source

from .testutils import VerminTest

def visit(source):
  visitor = SourceVisitor()
  visitor.visit(parse_source(source))
  return visitor

class VerminExclusionsTests(VerminTest):
  def __init__(self, methodName):
    super(VerminExclusionsTests, self).__init__(methodName)
    self.config = Config.get()

  def setUp(self):
    self.config.reset()

  def tearDown(self):
    self.config.reset()

  def test_module(self):
    self.config.add_exclusion("email.parser.FeedParser")
    visitor = visit("from email.parser import FeedParser")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_kwarg(self):
    self.config.add_exclusion("argparse")  # module
    self.config.add_exclusion("argparse.ArgumentParser(allow_abbrev)")  # kwarg
    visitor = visit("from argparse import ArgumentParser\nArgumentParser(allow_abbrev=False)")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_codecs_error_handler(self):
    self.config.add_exclusion("ceh=surrogateescape")
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', 'surrogateescape')")
    self.assertEqual([0, 0], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', 'utf-8', errors='surrogateescape')")
    self.assertEqual([0, 0], visitor.minimum_versions())

  def test_codecs_encoding(self):
    self.config.add_exclusion("ce=koi8_t")
    visitor = visit("import codecs\ncodecs.encode('test', 'koi8_t')")
    self.assertEqual([0, 0], visitor.minimum_versions())
    visitor = visit("import codecs\ncodecs.encode('test', data_encoding='koi8_t')")
    self.assertEqual([0, 0], visitor.minimum_versions())
