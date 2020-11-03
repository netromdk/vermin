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
