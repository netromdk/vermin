from vermin import detect

from .testutils import VerminTest

class VerminBuiltinConstantsTests(VerminTest):
  def test_obj_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').obj"))

  def test_nbytes_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').nbytes"))

  def test_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').contiguous"))

  def test_c_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').c_contiguous"))

  def test_f_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').f_contiguous"))
