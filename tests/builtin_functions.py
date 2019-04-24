from .testutils import VerminTest, detect

class VerminBuiltinFunctionsMemberTests(VerminTest):
  def test_all(self):
    self.assertOnlyIn((2.5, 3.0), detect("all()"))

  def test_any(self):
    self.assertOnlyIn((2.5, 3.0), detect("any()"))

  def test_basestring(self):
    self.assertOnlyIn((2.3, 3.0), detect("basestring()"))

  def test_bin(self):
    self.assertOnlyIn((2.6, 3.0), detect("bin()"))

  def test_classmethod(self):
    self.assertOnlyIn((2.2, 3.0), detect("classmethod()"))

  def test_enumerate(self):
    self.assertOnlyIn((2.3, 3.0), detect("enumerate()"))

  def test_file(self):
    self.assertOnlyIn((2.2, 3.0), detect("file()"))

  def test_format(self):
    self.assertOnlyIn((2.6, 3.0), detect("format()"))

  def test_help(self):
    self.assertOnlyIn((2.2, 3.0), detect("help()"))

  def test_iter(self):
    self.assertOnlyIn((2.2, 3.0), detect("iter()"))

  def test_next(self):
    self.assertOnlyIn((2.6, 3.0), detect("next()"))

  def test_sorted(self):
    self.assertOnlyIn((2.4, 3.0), detect("sorted()"))

  def test_staticmethod(self):
    self.assertOnlyIn((2.2, 3.0), detect("staticmethod()"))

  def test_sum(self):
    self.assertOnlyIn((2.3, 3.0), detect("sum()"))

  def test_super(self):
    self.assertOnlyIn((2.2, 3.0), detect("super()"))

  def test_unichr(self):
    self.assertOnlyIn((2.0, 3.0), detect("unichr()"))

  def test_unicode(self):
    self.assertOnlyIn((2.0, 3.0), detect("unicode()"))

  def test_zip(self):
    self.assertOnlyIn((2.0, 3.0), detect("zip()"))

  def test_breakpoint(self):
    self.assertOnlyIn(3.7, detect("breakpoint()"))
