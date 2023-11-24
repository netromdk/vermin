from .testutils import VerminTest

class VerminBuiltinFunctionsMemberTests(VerminTest):
  def test_all(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("all()"))

  def test_any(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("any()"))

  def test_basestring(self):
    self.assertOnlyIn((2, 3), self.detect("basestring()"))

  def test_bin(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("bin()"))

  def test_callable(self):
    self.assertOnlyIn(((2, 0), (3, 2)), self.detect("callable()"))

  def test_classmethod(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("classmethod()"))

  def test_enumerate(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("enumerate()"))

  def test_file(self):
    self.assertOnlyIn((2, 0), self.detect("file()"))

  def test_format(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("format()"))

  def test_help(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("help()"))

  def test_iter(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("iter()"))

  def test_next(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("next()"))

  def test_property(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("property()"))

  def test_sorted(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("sorted()"))

  def test_staticmethod(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("staticmethod()"))

  def test_sum(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("sum()"))

  def test_super(self):
    # Calling without arguments requires v3 (`SourceVisitor.super_no_args()`).
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("super(SomeType)"))

  def test_type(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("type()"))

  def test_unichr(self):
    self.assertOnlyIn((2, 0), self.detect("unichr()"))

  def test_unicode(self):
    self.assertOnlyIn((2, 0), self.detect("unicode()"))

  def test_breakpoint(self):
    self.assertOnlyIn((3, 7), self.detect("breakpoint()"))
    self.assertOnlyIn((3, 7), self.detect("x=[]\nx[breakpoint()]"))

  @VerminTest.parameterized_args([
    ("d={}\nd.has_key('a')", (2, 2)),
    ("{}.has_key('a')", (2, 2)),
    ("d=dict()\nd.has_key('a')", (2, 2)),
    ("dict().has_key('a')", (2, 2)),
  ])
  def test_has_key_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.iteritems()", (2, 2)),
    ("{}.iteritems()", (2, 2)),
    ("d=dict()\nd.iteritems()", (2, 2)),
    ("dict().iteritems()", (2, 2)),
  ])
  def test_iteritems_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.iterkeys()", (2, 2)),
    ("{}.iterkeys()", (2, 2)),
    ("d=dict()\nd.iterkeys()", (2, 2)),
    ("dict().iterkeys()", (2, 2)),
  ])
  def test_iterkeys_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.itervalues()", (2, 2)),
    ("{}.itervalues()", (2, 2)),
    ("d=dict()\nd.itervalues()", (2, 2)),
    ("dict().itervalues()", (2, 2)),
  ])
  def test_itervalues_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.viewitems()", (2, 7)),
    ("{}.viewitems()", (2, 7)),
    ("d=dict()\nd.viewitems()", (2, 7)),
    ("dict().viewitems()", (2, 7)),
  ])
  def test_viewitems_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.viewkeys()", (2, 7)),
    ("{}.viewkeys()", (2, 7)),
    ("d=dict()\nd.viewkeys()", (2, 7)),
    ("dict().viewkeys()", (2, 7)),
  ])
  def test_viewkeys_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.viewvalues()", (2, 7)),
    ("{}.viewvalues()", (2, 7)),
    ("d=dict()\nd.viewvalues()", (2, 7)),
    ("dict().viewvalues()", (2, 7)),
  ])
  def test_viewvalues_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={}\nd.fromkeys()", ((2, 3), (3, 0))),
    ("{}.fromkeys()", ((2, 3), (3, 0))),
    ("d=dict()\nd.fromkeys()", ((2, 3), (3, 0))),
    ("dict().fromkeys()", ((2, 3), (3, 0))),
  ])
  def test_fromkeys_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("d={1: 2}\nd.pop(1)", ((2, 3), (3, 0))),
    ("{1: 2}.pop(1)", ((2, 3), (3, 0))),
    ("d=dict({1: 2})\nd.pop(1)", ((2, 3), (3, 0))),
    ("dict({1: 2}).pop(1)", ((2, 3), (3, 0))),
  ])
  def test_pop_of_dict(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    # set literals require 2.7, 3.0
    ("s={1,2}\ns.isdisjoint({3,4})", ((2, 7), (3, 0))),
    ("{1,2}.isdisjoint({3,4})", ((2, 7), (3, 0))),
    ("s=set()\ns.isdisjoint(set([3,4]))", ((2, 6), (3, 0))),
    ("set().isdisjoint(set([3,4]))", ((2, 6), (3, 0))),
  ])
  def test_isdisjoint_of_set(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=frozenset()\ns.isdisjoint(set([3,4]))", ((2, 6), (3, 0))),
    ("frozenset().isdisjoint(set([3,4]))", ((2, 6), (3, 0))),
  ])
  def test_isdisjoint_of_frozenset(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("l=[]\nl.clear()", (3, 0)),
    ("[].clear()", (3, 0)),
    ("l=list()\nl.clear()", (3, 0)),
    ("list().clear()", (3, 0)),
  ])
  def test_clear_of_list(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("l=[]\nl.copy()", (3, 0)),
    ("[].copy()", (3, 0)),
    ("l=list()\nl.copy()", (3, 0)),
    ("list().copy()", (3, 0)),
  ])
  def test_copy_of_list(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.decode()", (2, 2)),
    ("\"\".decode()", (2, 2)),
    ("s=str()\ns.decode()", (2, 2)),
    ("str().decode()", (2, 2)),
  ])
  def test_decode_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.encode()", ((2, 0), (3, 0))),
    ("\"\".encode()", ((2, 0), (3, 0))),
    ("s=str()\ns.encode()", ((2, 0), (3, 0))),
    ("str().encode()", ((2, 0), (3, 0))),
  ])
  def test_encode_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.casefold()", (3, 3)),
    ("\"\".casefold()", (3, 3)),
    ("s=str()\ns.casefold()", (3, 3)),
    ("str().casefold()", (3, 3)),
  ])
  def test_casefold_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.format()", ((2, 6), (3, 0))),
    ("\"\".format()", ((2, 6), (3, 0))),
    ("s=str()\ns.format()", ((2, 6), (3, 0))),
    ("str().format()", ((2, 6), (3, 0))),
  ])
  def test_format_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.format_map()", (3, 2)),
    ("\"\".format_map()", (3, 2)),
    ("s=str()\ns.format_map()", (3, 2)),
    ("str().format_map()", (3, 2)),
  ])
  def test_format_map_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.isascii()", (3, 7)),
    ("\"\".isascii()", (3, 7)),
    ("s=str()\ns.isascii()", (3, 7)),
    ("str().isascii()", (3, 7)),
  ])
  def test_isascii_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.isidentifier()", (3, 0)),
    ("\"\".isidentifier()", (3, 0)),
    ("s=str()\ns.isidentifier()", (3, 0)),
    ("str().isidentifier()", (3, 0)),
  ])
  def test_isidentifier_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.isprintable()", (3, 0)),
    ("\"\".isprintable()", (3, 0)),
    ("s=str()\ns.isprintable()", (3, 0)),
    ("str().isprintable()", (3, 0)),
  ])
  def test_isprintable_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.isdecimal()", (3, 0)),
    ("\"\".isdecimal()", (3, 0)),
    ("s=str()\ns.isdecimal()", (3, 0)),
    ("str().isdecimal()", (3, 0)),
  ])
  def test_isdecimal_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.isnumeric()", (3, 0)),
    ("\"\".isnumeric()", (3, 0)),
    ("s=str()\ns.isnumeric()", (3, 0)),
    ("str().isnumeric()", (3, 0)),
  ])
  def test_isnumeric_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.maketrans()", (3, 0)),
    ("\"\".maketrans()", (3, 0)),
    ("s=str()\ns.maketrans()", (3, 0)),
    ("str().maketrans()", (3, 0)),
  ])
  def test_maketrans_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.removeprefix()", (3, 9)),
    ("\"\".removeprefix()", (3, 9)),
    ("s=str()\ns.removeprefix()", (3, 9)),
    ("str().removeprefix()", (3, 9)),
  ])
  def test_removeprefix_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.removesuffix()", (3, 9)),
    ("\"\".removesuffix()", (3, 9)),
    ("s=str()\ns.removesuffix()", (3, 9)),
    ("str().removesuffix()", (3, 9)),
  ])
  def test_removesuffix_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.partition('a')", ((2, 5), (3, 0))),
    ("\"\".partition('a')", ((2, 5), (3, 0))),
    ("s=str()\ns.partition('a')", ((2, 5), (3, 0))),
    ("str().partition('a')", ((2, 5), (3, 0))),
  ])
  def test_partition_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.rpartition('a')", ((2, 5), (3, 0))),
    ("\"\".rpartition('a')", ((2, 5), (3, 0))),
    ("s=str()\ns.rpartition('a')", ((2, 5), (3, 0))),
    ("str().rpartition('a')", ((2, 5), (3, 0))),
  ])
  def test_rpartition_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.rsplit('a')", ((2, 4), (3, 0))),
    ("\"\".rsplit('a')", ((2, 4), (3, 0))),
    ("s=str()\ns.rsplit('a')", ((2, 4), (3, 0))),
    ("str().rsplit('a')", ((2, 4), (3, 0))),
  ])
  def test_rsplit_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  @VerminTest.parameterized_args([
    ("s=\"\"\ns.zfill(2)", ((2, 2), (3, 0))),
    ("\"\".zfill(2)", ((2, 2), (3, 0))),
    ("s=str()\ns.zfill(2)", ((2, 2), (3, 0))),
    ("str().zfill(2)", ((2, 2), (3, 0))),
  ])
  def test_zfill_of_str(self, source, min_versions):
    self.assertDetectMinVersions(source, min_versions)

  def test_as_integer_ratio_of_int(self):
    self.assertOnlyIn((3, 8), self.detect("(42).as_integer_ratio()"))
    self.assertOnlyIn((3, 8), self.detect("n=42\nn.as_integer_ratio()"))

  def test_bit_length_of_int(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("(42).bit_length()"))
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("n=42\nn.bit_length()"))

  def test_bit_count_of_int(self):
    self.assertOnlyIn((3, 10), self.detect("(42).bit_count()"))
    self.assertOnlyIn((3, 10), self.detect("n=42\nn.bit_count()"))

  def test_is_integer_of_int(self):
    self.assertOnlyIn((3, 12), self.detect("(42).is_integer()"))
    self.assertOnlyIn((3, 12), self.detect("n=42\nn.is_integer()"))

  def test_to_bytes_of_int(self):
    self.assertOnlyIn((3, 2), self.detect("(42).to_bytes()"))
    self.assertOnlyIn((3, 2), self.detect("n=42\nn.to_bytes()"))

  def test_from_bytes_of_int(self):
    self.assertOnlyIn((3, 2), self.detect("int.from_bytes([42])"))

  def test_as_integer_ratio_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("(42.0).as_integer_ratio()"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("n=42.0\nn.as_integer_ratio()"))

  def test_next_of_file(self):
    self.assertOnlyIn((2, 3), self.detect("file('name').next()"))

  def test_xreadlines_of_file(self):
    self.assertOnlyIn((2, 1), self.detect("file('name').xreadlines()"))

  def test_is_integer_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("(42.0).is_integer()"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("n=42.0\nn.is_integer()"))

  def test_hex_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("(42.0).hex()"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("n=42.0\nn.hex()"))

  def test_fromhex_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("(42.0).fromhex()"))
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("n=42.0\nn.fromhex()"))

  def test_hex_of_bytes(self):
    self.assertOnlyIn((3, 5), self.detect("b'\x10'.hex()"))
    self.assertOnlyIn((3, 5), self.detect("b=b'\x10'\nb.hex()"))

  def test_isascii_of_bytes(self):
    self.assertOnlyIn((3, 7), self.detect("b'\x10'.isascii()"))
    self.assertOnlyIn((3, 7), self.detect("b=b'\x10'\nb.isascii()"))

  def test_maketrans_of_bytes(self):
    self.assertOnlyIn((3, 1), self.detect("bytes.maketrans(b'a', b'b')"))

  def test_removeprefix_of_bytes(self):
    self.assertOnlyIn((3, 9), self.detect("bytes.removeprefix(b'a')"))

  def test_removesuffix_of_bytes(self):
    self.assertOnlyIn((3, 9), self.detect("bytes.removesuffix(b'a')"))

  def test_hex_of_bytearray(self):
    self.assertOnlyIn((3, 5), self.detect("bytearray(b'\x10').hex()"))
    self.assertOnlyIn((3, 5), self.detect("b=bytearray(b'\x10')\nb.hex()"))

  def test_isascii_of_bytearray(self):
    self.assertOnlyIn((3, 7), self.detect("bytearray(b'\x10').isascii()"))
    self.assertOnlyIn((3, 7), self.detect("b=bytearray(b'\x10')\nb.isascii()"))

  def test_maketrans_of_bytearray(self):
    self.assertOnlyIn((3, 1), self.detect("bytearray.maketrans(b'a', b'b')"))

  def test_removeprefix_of_bytearray(self):
    self.assertOnlyIn((3, 9), self.detect("bytearray.removeprefix(b'a')"))

  def test_removesuffix_of_bytearray(self):
    self.assertOnlyIn((3, 9), self.detect("bytearray.removesuffix(b'a')"))

  def test_hex_of_memoryview(self):
    self.assertOnlyIn((3, 5), self.detect("memoryview(b'1').hex()"))

  def test_release_of_memoryview(self):
    self.assertOnlyIn((3, 2), self.detect("memoryview(b'1').release()"))

  def test_cast_of_memoryview(self):
    self.assertOnlyIn((3, 3), self.detect("memoryview(b'1').cast()"))

  def test_toreadonly_of_memoryview(self):
    self.assertOnlyIn((3, 8), self.detect("memoryview(b'1').toreadonly()"))

  def test_deleter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("property.deleter()"))

  def test_getter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("property.getter()"))

  def test_setter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("property.setter()"))

  def test_indices_of_slice(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("slice.indices()"))

  def test_aiter(self):
    self.assertOnlyIn((3, 10), self.detect("aiter()"))

  def test_anext(self):
    self.assertOnlyIn((3, 10), self.detect("anext()"))

  def test_zip(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("zip()"))
