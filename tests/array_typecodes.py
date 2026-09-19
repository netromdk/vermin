from .testutils import VerminTest

class VerminArrayTypecodeTests(VerminTest):
  @VerminTest.parameterized_args([
    ("from array import array\narray('q')", (3, 3)),
    ("import array\narray.array('q')", (3, 3)),
    ("from array import array\narray('q', [1, 2])", (3, 3)),
    ("from array import array as a\na('q', [1, 2])", (3, 3)),
  ])
  def test_typecode_q(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("from array import array\narray('Q')", (3, 3)),
    ("import array\narray.array('Q')", (3, 3)),
    ("from array import array\narray('Q', [1, 2])", (3, 3)),
    ("from array import array as a\na('Q', [1, 2])", (3, 3)),
  ])
  def test_typecode_Q(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("from array import array\narray('w')", (3, 13)),
    ("import array\narray.array('w')", (3, 13)),
    ("from array import array\narray('w', [1, 2])", (3, 13)),
    ("from array import array as a\na('w', [1, 2])", (3, 13)),
  ])
  def test_typecode_w(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("from array import array\narray('e')", (3, 15)),
    ("import array\narray.array('e')", (3, 15)),
    ("from array import array\narray('e', [1, 2])", (3, 15)),
    ("from array import array as a\na('e', [1, 2])", (3, 15)),
  ])
  def test_typecode_e(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("from array import array\narray('Zf')", (3, 15)),
    ("import array\narray.array('Zf')", (3, 15)),
    ("from array import array\narray('Zf', [1 + 2j, 3 - 4j])", (3, 15)),
    ("from array import array as a\na('Zf', [1 + 2j, 3 - 4j])", (3, 15)),
  ])
  def test_typecode_Zf(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("from array import array\narray('Zd')", (3, 15)),
    ("import array\narray.array('Zd')", (3, 15)),
    ("from array import array\narray('Zd', [1 + 2j, 3 - 4j])", (3, 15)),
    ("from array import array as a\na('Zd', [1 + 2j, 3 - 4j])", (3, 15)),
  ])
  def test_typecode_Zd(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)
