from .testutils import VerminTest

class VerminCodecsErrorHandlerTests(VerminTest):
  @VerminTest.parameterized_args([
    ("""import codecs
codecs.encode('test', 'utf-8', 'surrogateescape')
""", (3, 1)),
    ("""import codecs
codecs.encode('test', 'utf-8', errors='surrogateescape')
""", (3, 1)),
    ("""from codecs import encode
encode('test', 'utf-8', 'surrogateescape')
""", (3, 1)),
  ])
  def test_handler_surrogateescape(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("""import codecs
codecs.decode('test', 'utf-8', 'surrogatepass')
""", (3, 1)),
    ("""import codecs
codecs.decode('test', 'utf-8', errors='surrogatepass')
""", (3, 1)),
    ("""from codecs import decode
decode('test', 'utf-8', 'surrogatepass')
""", (3, 1)),
  ])
  def test_handler_surrogatepass(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("""import codecs
codecs.EncodedFile('test', 'utf-8', 'utf-8', 'namereplace')
""", (3, 5)),
    ("""import codecs
codecs.EncodedFile('test', 'utf-8', errors='namereplace')
""", (3, 5)),
    ("""from codecs import EncodedFile
EncodedFile('test', 'utf-8', 'utf-8', 'namereplace')
""", (3, 5)),
  ])
  def test_handler_namereplace(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  def test_function_encode(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import encode\n"
                                  "encode('test', 'utf-8', 'namereplace')"))

  def test_function_decode(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import decode\n"
                                  "decode('test', 'utf-8', 'namereplace')"))

  def test_function_open(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import open\n"
                                  "open('test', errors='namereplace')"))

  def test_function_EncodedFile(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import EncodedFile\n"
                                  "EncodedFile('test', 'utf-8', errors='namereplace')"))

  def test_function_iterencode(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import iterencode\n"
                                  "iterencode([], 'utf-8', 'namereplace')"))

  def test_function_iterdecode(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import iterdecode\n"
                                  "iterdecode([], 'utf-8', 'namereplace')"))

  def test_function_IncrementalEncoder(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import IncrementalEncoder\n"
                                  "IncrementalEncoder('namereplace')"))

  def test_function_IncrementalDecoder(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import IncrementalDecoder\n"
                                  "IncrementalDecoder('namereplace')"))

  def test_function_StreamWriter(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import StreamWriter\n"
                                  "from sys import stdout\n"
                                  "StreamWriter(stdout, 'namereplace')"))

  def test_function_StreamReader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import StreamReader\n"
                                  "from sys import stdin\n"
                                  "StreamReader(stdin, 'namereplace')"))

  def test_function_StreamReaderWriter(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import StreamReaderWriter as SRW\n"
                                  "SRW(open('hello.txt'), None, None, 'namereplace')"))

  def test_function_StreamRecorder(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from codecs import StreamRecorder as SR, encode, decode\n"
      "SR(open('hello.txt'), encode, decode, None, None, 'namereplace')"))
