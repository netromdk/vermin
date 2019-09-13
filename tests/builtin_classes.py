from .testutils import VerminTest, detect

class VerminBuiltinClassesMemberTests(VerminTest):
  def test_bool(self):
    self.assertOnlyIn((2.2, 3.0), detect("bool()"))

  def test_bytearray(self):
    self.assertOnlyIn((2.6, 3.0), detect("bytearray()"))

  def test_frozenset(self):
    self.assertOnlyIn((2.4, 3.0), detect("frozenset()"))

  def test_object(self):
    self.assertOnlyIn((2.2, 3.0), detect("object()"))

  def test_reversed(self):
    self.assertOnlyIn((2.4, 3.0), detect("reversed()"))

  def test_set(self):
    self.assertOnlyIn((2.4, 3.0), detect("set()"))

  def test_type(self):
    self.assertOnlyIn((2.2, 3.0), detect("type()"))

  def test_memoryview(self):
    self.assertOnlyIn((2.7, 3.0), detect("memoryview()"))
