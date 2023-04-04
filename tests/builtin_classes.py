from .testutils import VerminTest

class VerminBuiltinClassesMemberTests(VerminTest):
  def test_bool(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("bool()"))

  def test_bytearray(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("bytearray()"))

  def test_frozenset(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("frozenset()"))

  def test_object(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("object()"))

  def test_reversed(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("reversed()"))

  def test_set(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("set()"))

  def test_dict(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("dict()"))

  def test_memoryview(self):
    self.assertOnlyIn(((2, 7), (3, 0)), self.detect("memoryview()"))

  def test_long(self):
    self.assertOnlyIn((2, 0), self.detect("long()"))

  def test_ExceptionGroup(self):
    self.assertOnlyIn((3, 11), self.detect("ExceptionGroup()"))

  def test_BaseExceptionGroup(self):
    self.assertOnlyIn((3, 11), self.detect("BaseExceptionGroup()"))
