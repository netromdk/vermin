from vermin import detect

from .testutils import VerminTest

class VerminCodecsEncodingTests(VerminTest):
  def test_encoding_german(self):
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'cp273')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', '273')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'ibm273')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'csibm273')"))

  def test_encoding_ukrainian(self):
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'cp1125')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', '1125')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'ibm1125')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'cp866u')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'ruscii')"))

  def test_encoding_windows_cp_utf8(self):
    self.assertOnlyIn((3, 3), detect("import codecs\ncodecs.encode('test', 'cp65001')"))

  def test_encoding_tajik(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'koi8_t')"))

  def test_encoding_kazakh(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'kz1048')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'kz_1048')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'strk1048_2002')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'kz-1048')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'strk1048-2002')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'rk1048')"))

  def test_encoding_windows_owm(self):
    self.assertOnlyIn((3, 6), detect("import codecs\ncodecs.encode('test', 'oem')"))

  def test_encoding_base64(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'base64_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'base64-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'base64')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'base_64')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'base-64')"))

  def test_encoding_bz2(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'bz2_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'bz2-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'bz2')"))

  def test_encoding_hex(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'hex_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'hex-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'hex')"))

  def test_encoding_quopri(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'quopri_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'quopri-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'quopri')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'quotedprintable')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'quoted_printable')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'quoted-printable')"))

  def test_encoding_uu(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'uu_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'uu-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'uu')"))

  def test_encoding_zip(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'zip_codec')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'zip-codec')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'zip')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'zlib')"))

  def test_encoding_rot13(self):
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'rot_13')"))
    self.assertOnlyIn((3, 2), detect("import codecs\ncodecs.encode('test', 'rot-13')"))
    self.assertOnlyIn((3, 4), detect("import codecs\ncodecs.encode('test', 'rot13')"))

  def test_function_encode(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', 'koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.encode('test', encoding='koi8_t')"))

  def test_function_decode(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.decode('test', 'koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.decode('test', encoding='koi8_t')"))

  def test_function_lookup(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.lookup('koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.lookup(encoding='koi8_t')"))

  def test_function_getencoder(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getencoder('koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getencoder(encoding='koi8_t')"))

  def test_function_getdecoder(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getdecoder('koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getdecoder(encoding='koi8_t')"))

  def test_function_getincrementalencoder(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getincrementalencoder('koi8_t')"))
    self.assertOnlyIn((3, 5),
                      detect("import codecs\ncodecs.getincrementalencoder(encoding='koi8_t')"))

  def test_function_getincrementaldecoder(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getincrementaldecoder('koi8_t')"))
    self.assertOnlyIn((3, 5),
                      detect("import codecs\ncodecs.getincrementaldecoder(encoding='koi8_t')"))

  def test_function_getreader(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getreader('koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getreader(encoding='koi8_t')"))

  def test_function_getwriter(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getwriter('koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.getwriter(encoding='koi8_t')"))

  def test_function_open(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.open('f.txt', 'r', 'koi8_t')"))
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.open('f.txt', encoding='koi8_t')"))

  def test_function_EncodedFile(self):
    self.assertOnlyIn((3, 5), detect("import codecs\ncodecs.EncodedFile('f.txt', 'koi8_t')"))
    self.assertOnlyIn((3, 5),
                      detect("import codecs\ncodecs.EncodedFile('f.txt', data_encoding='koi8_t')"))
    self.assertOnlyIn((3, 5),
                      detect("import codecs\n"
                             "codecs.EncodedFile('f.txt', 'utf-8', file_encoding='koi8_t')"))
    self.assertOnlyIn((3, 5),
                      detect("from codecs import EncodedFile as EF\n"
                             "EF('f.txt', data_encoding='koi8_t', file_encoding='utf-8')"))
