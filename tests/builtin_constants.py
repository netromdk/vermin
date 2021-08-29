from .testutils import VerminTest

class VerminBuiltinConstantsTests(VerminTest):
  def test_obj_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').obj"))

  def test_nbytes_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').nbytes"))

  def test_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').contiguous"))

  def test_c_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').c_contiguous"))

  def test_f_contiguous_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').f_contiguous"))

  def test_mapping_of_dict_view(self):
    self.assertOnlyIn((3, 10), self.detect("{}.items().mapping"))
    self.assertOnlyIn((3, 10), self.detect("{}.keys().mapping"))
    self.assertOnlyIn((3, 10), self.detect("{}.values().mapping"))

    self.assertOnlyIn((3, 10), self.detect("dict().items().mapping"))
    self.assertOnlyIn((3, 10), self.detect("dict().keys().mapping"))
    self.assertOnlyIn((3, 10), self.detect("dict().values().mapping"))

    self.assertOnlyIn((3, 10), self.detect("""
d = {}
d.items().mapping
"""))
    self.assertOnlyIn((3, 10), self.detect("""
d = {}
d.keys().mapping
"""))
    self.assertOnlyIn((3, 10), self.detect("""
d = {}
d.values().mapping
"""))

    self.assertOnlyIn((3, 10), self.detect("""
d = {}
i = d.items()
i.mapping
"""))
    self.assertOnlyIn((3, 10), self.detect("""
d = {}
i = d.keys()
i.mapping
"""))
    self.assertOnlyIn((3, 10), self.detect("""
d = {}
i = d.values()
i.mapping
"""))
