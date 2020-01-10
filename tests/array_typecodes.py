from .testutils import VerminTest, detect

class VerminArrayTypecodeTests(VerminTest):
  def test_typecode_q(self):
    self.assertOnlyIn((3, 3), detect("from array import array\narray('q')"))
    self.assertOnlyIn((3, 3), detect("import array\narray.array('q')"))
    self.assertOnlyIn((3, 3), detect("from array import array\narray('q', [1, 2])"))
    self.assertOnlyIn((3, 3), detect("from array import array as a\na('q', [1, 2])"))

  def test_typecode_Q(self):
    self.assertOnlyIn((3, 3), detect("from array import array\narray('Q')"))
    self.assertOnlyIn((3, 3), detect("import array\narray.array('Q')"))
    self.assertOnlyIn((3, 3), detect("from array import array\narray('Q', [1, 2])"))
    self.assertOnlyIn((3, 3), detect("from array import array as a\na('Q', [1, 2])"))
