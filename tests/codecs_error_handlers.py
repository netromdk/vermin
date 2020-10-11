from .testutils import VerminTest

class VerminCodecsErrorHandlerTests(VerminTest):
  def test_handler_surrogateescape(self):
    self.assertOnlyIn((3, 1),
                      self.detect("import codecs\n"
                                  "codecs.encode('test', 'utf-8', 'surrogateescape')"))
    self.assertOnlyIn((3, 1),
                      self.detect("import codecs\n"
                                  "codecs.encode('test', 'utf-8', errors='surrogateescape')"))
    self.assertOnlyIn((3, 1),
                      self.detect("from codecs import encode\n"
                                  "encode('test', 'utf-8', 'surrogateescape')"))

  def test_handler_surrogatepass(self):
    self.assertOnlyIn((3, 1),
                      self.detect("import codecs\n"
                                  "codecs.decode('test', 'utf-8', 'surrogatepass')"))
    self.assertOnlyIn((3, 1),
                      self.detect("import codecs\n"
                                  "codecs.decode('test', 'utf-8', errors='surrogatepass')"))
    self.assertOnlyIn((3, 1),
                      self.detect("from codecs import decode\n"
                                  "decode('test', 'utf-8', 'surrogatepass')"))

  def test_handler_namereplace(self):
    self.assertOnlyIn((3, 5),
                      self.detect("import codecs\n"
                                  "codecs.EncodedFile('test', 'utf-8', 'utf-8', 'namereplace')"))
    self.assertOnlyIn((3, 5),
                      self.detect("import codecs\n"
                                  "codecs.EncodedFile('test', 'utf-8', errors='namereplace')"))
    self.assertOnlyIn((3, 5),
                      self.detect("from codecs import EncodedFile\n"
                                  "EncodedFile('test', 'utf-8', 'utf-8', 'namereplace')"))

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
