from .testutils import VerminTest

class VerminCodecsEncodingTests(VerminTest):
  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'cp273')", (3, 4)),
    ("import codecs\ncodecs.encode('test', '273')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'ibm273')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'csibm273')", (3, 4)),
  ])
  def test_encoding_german(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'cp1125')", (3, 4)),
    ("import codecs\ncodecs.encode('test', '1125')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'ibm1125')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'cp866u')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'ruscii')", (3, 4)),
  ])
  def test_encoding_ukrainian(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  def test_encoding_windows_cp_utf8(self):
    self.assertOnlyIn((3, 3), self.detect("import codecs\ncodecs.encode('test', 'cp65001')"))

  def test_encoding_tajik(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.encode('test', 'koi8_t')"))

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'kz1048')", (3, 5)),
    ("import codecs\ncodecs.encode('test', 'kz_1048')", (3, 5)),
    ("import codecs\ncodecs.encode('test', 'strk1048_2002')", (3, 5)),
    ("import codecs\ncodecs.encode('test', 'kz-1048')", (3, 5)),
    ("import codecs\ncodecs.encode('test', 'strk1048-2002')", (3, 5)),
    ("import codecs\ncodecs.encode('test', 'rk1048')", (3, 5)),
  ])
  def test_encoding_kazakh(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  def test_encoding_windows_owm(self):
    self.assertOnlyIn((3, 6), self.detect("import codecs\ncodecs.encode('test', 'oem')"))

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'base64_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'base64-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'base64')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'base_64')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'base-64')", (3, 4)),
  ])
  def test_encoding_base64(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'bz2_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'bz2-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'bz2')", (3, 4)),
  ])
  def test_encoding_bz2(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'hex_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'hex-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'hex')", (3, 4)),
  ])
  def test_encoding_hex(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'quopri_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'quopri-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'quopri')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'quotedprintable')", (3, 4)),
    ("""import codecs
codecs.encode('test', 'quoted_printable')
""", (3, 4)),
    ("""import codecs
codecs.encode('test', 'quoted-printable')
""", (3, 4)),
  ])
  def test_encoding_quopri(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'uu_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'uu-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'uu')", (3, 4)),
  ])
  def test_encoding_uu(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'zip_codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'zip-codec')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'zip')", (3, 4)),
    ("import codecs\ncodecs.encode('test', 'zlib')", (3, 4)),
  ])
  def test_encoding_zip(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.encode('test', 'rot_13')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'rot-13')", (3, 2)),
    ("import codecs\ncodecs.encode('test', 'rot13')", (3, 4)),
  ])
  def test_encoding_rot13(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  def test_function_encode(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.encode('test', 'koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("""import codecs
codecs.encode('test', encoding='koi8_t')
"""))

  def test_function_decode(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.decode('test', 'koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("""import codecs
codecs.decode('test', encoding='koi8_t')
"""))

  def test_function_lookup(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.lookup('koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.lookup(encoding='koi8_t')"))

  def test_function_getencoder(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getencoder('koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getencoder(encoding='koi8_t')"))

  def test_function_getdecoder(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getdecoder('koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getdecoder(encoding='koi8_t')"))

  def test_function_getincrementalencoder(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getincrementalencoder('koi8_t')"))
    self.assertOnlyIn((3, 5),
                      self.detect("import codecs\ncodecs.getincrementalencoder(encoding='koi8_t')"))

  def test_function_getincrementaldecoder(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getincrementaldecoder('koi8_t')"))
    self.assertOnlyIn((3, 5),
                      self.detect("import codecs\ncodecs.getincrementaldecoder(encoding='koi8_t')"))

  def test_function_getreader(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getreader('koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getreader(encoding='koi8_t')"))

  def test_function_getwriter(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getwriter('koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.getwriter(encoding='koi8_t')"))

  def test_function_open(self):
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.open('f.txt', 'r', 'koi8_t')"))
    self.assertOnlyIn((3, 5), self.detect("import codecs\ncodecs.open('f.txt', encoding='koi8_t')"))

  @VerminTest.parameterized_args([
    ("import codecs\ncodecs.EncodedFile('f.txt', 'koi8_t')", (3, 5)),
    ("""import codecs
codecs.EncodedFile('f.txt', data_encoding='koi8_t')
""", (3, 5)),
    ("""import codecs
codecs.EncodedFile('f.txt', 'utf-8', file_encoding='koi8_t')
""", (3, 5)),
    ("""from codecs import EncodedFile as EF
EF('f.txt', data_encoding='koi8_t', file_encoding='utf-8')
""", (3, 5)),
  ])
  def test_function_EncodedFile(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)
