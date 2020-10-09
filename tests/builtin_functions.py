from vermin import detect

from .testutils import VerminTest, current_version

class VerminBuiltinFunctionsMemberTests(VerminTest):
  def test_all(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("all()"))

  def test_any(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("any()"))

  def test_basestring(self):
    self.assertOnlyIn((2, 3), detect("basestring()"))

  def test_bin(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("bin()"))

  def test_callable(self):
    self.assertOnlyIn(((2, 0), (3, 2)), detect("callable()"))

  def test_classmethod(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("classmethod()"))

  def test_enumerate(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("enumerate()"))

  def test_file(self):
    self.assertOnlyIn((2, 0), detect("file()"))

  def test_format(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("format()"))

  def test_help(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("help()"))

  def test_iter(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("iter()"))

  def test_next(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("next()"))

  def test_property(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("property()"))

  def test_sorted(self):
    self.assertOnlyIn(((2, 4), (3, 0)), detect("sorted()"))

  def test_staticmethod(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("staticmethod()"))

  def test_sum(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("sum()"))

  def test_super(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("super()"))

  def test_unichr(self):
    self.assertOnlyIn((2, 0), detect("unichr()"))

  def test_unicode(self):
    self.assertOnlyIn((2, 0), detect("unicode()"))

  def test_breakpoint(self):
    self.assertOnlyIn((3, 7), detect("breakpoint()"))

  def test_has_key_of_dict(self):
    self.assertOnlyIn((2, 2), detect("d={}\nd.has_key('a')"))
    self.assertOnlyIn((2, 2), detect("{}.has_key('a')"))
    self.assertOnlyIn((2, 2), detect("d=dict()\nd.has_key('a')"))
    self.assertOnlyIn((2, 2), detect("dict().has_key('a')"))

  def test_iteritems_of_dict(self):
    self.assertOnlyIn((2, 2), detect("d={}\nd.iteritems()"))
    self.assertOnlyIn((2, 2), detect("{}.iteritems()"))
    self.assertOnlyIn((2, 2), detect("d=dict()\nd.iteritems()"))
    self.assertOnlyIn((2, 2), detect("dict().iteritems()"))

  def test_iterkeys_of_dict(self):
    self.assertOnlyIn((2, 2), detect("d={}\nd.iterkeys()"))
    self.assertOnlyIn((2, 2), detect("{}.iterkeys()"))
    self.assertOnlyIn((2, 2), detect("d=dict()\nd.iterkeys()"))
    self.assertOnlyIn((2, 2), detect("dict().iterkeys()"))

  def test_itervalues_of_dict(self):
    self.assertOnlyIn((2, 2), detect("d={}\nd.itervalues()"))
    self.assertOnlyIn((2, 2), detect("{}.itervalues()"))
    self.assertOnlyIn((2, 2), detect("d=dict()\nd.itervalues()"))
    self.assertOnlyIn((2, 2), detect("dict().itervalues()"))

  def test_viewitems_of_dict(self):
    self.assertOnlyIn((2, 7), detect("d={}\nd.viewitems()"))
    self.assertOnlyIn((2, 7), detect("{}.viewitems()"))
    self.assertOnlyIn((2, 7), detect("d=dict()\nd.viewitems()"))
    self.assertOnlyIn((2, 7), detect("dict().viewitems()"))

  def test_viewkeys_of_dict(self):
    self.assertOnlyIn((2, 7), detect("d={}\nd.viewkeys()"))
    self.assertOnlyIn((2, 7), detect("{}.viewkeys()"))
    self.assertOnlyIn((2, 7), detect("d=dict()\nd.viewkeys()"))
    self.assertOnlyIn((2, 7), detect("dict().viewkeys()"))

  def test_viewvalues_of_dict(self):
    self.assertOnlyIn((2, 7), detect("d={}\nd.viewvalues()"))
    self.assertOnlyIn((2, 7), detect("{}.viewvalues()"))
    self.assertOnlyIn((2, 7), detect("d=dict()\nd.viewvalues()"))
    self.assertOnlyIn((2, 7), detect("dict().viewvalues()"))

  def test_fromkeys_of_dict(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("d={}\nd.fromkeys()"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("{}.fromkeys()"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("d=dict()\nd.fromkeys()"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("dict().fromkeys()"))

  def test_pop_of_dict(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("d={1: 2}\nd.pop(1)"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("{1: 2}.pop(1)"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("d=dict({1: 2})\nd.pop(1)"))
    self.assertOnlyIn(((2, 3), (3, 0)), detect("dict({1: 2}).pop(1)"))

  def test_isdisjoint_of_set(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("s={1,2}\ns.isdisjoint({3,4})"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("{1,2}.isdisjoint({3,4})"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("s=set()\ns.isdisjoint({3,4})"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("set().isdisjoint({3,4})"))

  def test_isdisjoint_of_frozenset(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("s=frozenset()\ns.isdisjoint({3,4})"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("frozenset().isdisjoint({3,4})"))

  def test_clear_of_list(self):
    self.assertOnlyIn((3, 0), detect("l=[]\nl.clear()"))
    self.assertOnlyIn((3, 0), detect("[].clear()"))
    self.assertOnlyIn((3, 0), detect("l=list()\nl.clear()"))
    self.assertOnlyIn((3, 0), detect("list().clear()"))

  def test_copy_of_list(self):
    self.assertOnlyIn((3, 0), detect("l=[]\nl.copy()"))
    self.assertOnlyIn((3, 0), detect("[].copy()"))
    self.assertOnlyIn((3, 0), detect("l=list()\nl.copy()"))
    self.assertOnlyIn((3, 0), detect("list().copy()"))

  def test_decode_of_str(self):
    self.assertOnlyIn((2, 2), detect("s=\"\"\ns.decode()"))
    self.assertOnlyIn((2, 2), detect("\"\".decode()"))
    self.assertOnlyIn((2, 2), detect("s=str()\ns.decode()"))
    self.assertOnlyIn((2, 2), detect("str().decode()"))

  def test_casefold_of_str(self):
    self.assertOnlyIn((3, 3), detect("s=\"\"\ns.casefold()"))
    self.assertOnlyIn((3, 3), detect("\"\".casefold()"))
    self.assertOnlyIn((3, 3), detect("s=str()\ns.casefold()"))
    self.assertOnlyIn((3, 3), detect("str().casefold()"))

  def test_format_of_str(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("s=\"\"\ns.format()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("\"\".format()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("s=str()\ns.format()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("str().format()"))

  def test_format_map_of_str(self):
    self.assertOnlyIn((3, 2), detect("s=\"\"\ns.format_map()"))
    self.assertOnlyIn((3, 2), detect("\"\".format_map()"))
    self.assertOnlyIn((3, 2), detect("s=str()\ns.format_map()"))
    self.assertOnlyIn((3, 2), detect("str().format_map()"))

  def test_isascii_of_str(self):
    self.assertOnlyIn((3, 7), detect("s=\"\"\ns.isascii()"))
    self.assertOnlyIn((3, 7), detect("\"\".isascii()"))
    self.assertOnlyIn((3, 7), detect("s=str()\ns.isascii()"))
    self.assertOnlyIn((3, 7), detect("str().isascii()"))

  def test_isidentifier_of_str(self):
    self.assertOnlyIn((3, 0), detect("s=\"\"\ns.isidentifier()"))
    self.assertOnlyIn((3, 0), detect("\"\".isidentifier()"))
    self.assertOnlyIn((3, 0), detect("s=str()\ns.isidentifier()"))
    self.assertOnlyIn((3, 0), detect("str().isidentifier()"))

  def test_isprintable_of_str(self):
    self.assertOnlyIn((3, 0), detect("s=\"\"\ns.isprintable()"))
    self.assertOnlyIn((3, 0), detect("\"\".isprintable()"))
    self.assertOnlyIn((3, 0), detect("s=str()\ns.isprintable()"))
    self.assertOnlyIn((3, 0), detect("str().isprintable()"))

  def test_isdecimal_of_unicode(self):
    if current_version() < 3.0:  # pragma: no cover
      self.assertOnlyIn((2, 0), detect("s=u\"\"\ns.isdecimal()"))
      self.assertOnlyIn((2, 0), detect("u\"\".isdecimal()"))
      self.assertOnlyIn((2, 0), detect("s=unicode()\ns.isdecimal()"))
      self.assertOnlyIn((2, 0), detect("unicode().isdecimal()"))

  def test_isnumeric_of_unicode(self):
    if current_version() < 3.0:  # pragma: no cover
      self.assertOnlyIn((2, 0), detect("s=u\"\"\ns.isnumeric()"))
      self.assertOnlyIn((2, 0), detect("u\"\".isnumeric()"))
      self.assertOnlyIn((2, 0), detect("s=unicode()\ns.isnumeric()"))
      self.assertOnlyIn((2, 0), detect("unicode().isnumeric()"))

  def test_isdecimal_of_str(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), detect("s=\"\"\ns.isdecimal()"))
      self.assertOnlyIn((3, 0), detect("\"\".isdecimal()"))
      self.assertOnlyIn((3, 0), detect("s=str()\ns.isdecimal()"))
      self.assertOnlyIn((3, 0), detect("str().isdecimal()"))

  def test_isnumeric_of_str(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 0), detect("s=\"\"\ns.isnumeric()"))
      self.assertOnlyIn((3, 0), detect("\"\".isnumeric()"))
      self.assertOnlyIn((3, 0), detect("s=str()\ns.isnumeric()"))
      self.assertOnlyIn((3, 0), detect("str().isnumeric()"))

  def test_maketrans_of_str(self):
    self.assertOnlyIn((3, 0), detect("s=\"\"\ns.maketrans()"))
    self.assertOnlyIn((3, 0), detect("\"\".maketrans()"))
    self.assertOnlyIn((3, 0), detect("s=str()\ns.maketrans()"))
    self.assertOnlyIn((3, 0), detect("str().maketrans()"))

  def test_removeprefix_of_str(self):
    self.assertOnlyIn((3, 9), detect("s=\"\"\ns.removeprefix()"))
    self.assertOnlyIn((3, 9), detect("\"\".removeprefix()"))
    self.assertOnlyIn((3, 9), detect("s=str()\ns.removeprefix()"))
    self.assertOnlyIn((3, 9), detect("str().removeprefix()"))

  def test_removesuffix_of_str(self):
    self.assertOnlyIn((3, 9), detect("s=\"\"\ns.removesuffix()"))
    self.assertOnlyIn((3, 9), detect("\"\".removesuffix()"))
    self.assertOnlyIn((3, 9), detect("s=str()\ns.removesuffix()"))
    self.assertOnlyIn((3, 9), detect("str().removesuffix()"))

  def test_partition_of_str(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("s=\"\"\ns.partition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("\"\".partition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("s=str()\ns.partition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("str().partition('a')"))

  def test_rpartition_of_str(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("s=\"\"\ns.rpartition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("\"\".rpartition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("s=str()\ns.rpartition('a')"))
    self.assertOnlyIn(((2, 5), (3, 0)), detect("str().rpartition('a')"))

  def test_rsplit_of_str(self):
    self.assertOnlyIn(((2, 4), (3, 0)), detect("s=\"\"\ns.rsplit('a')"))
    self.assertOnlyIn(((2, 4), (3, 0)), detect("\"\".rsplit('a')"))
    self.assertOnlyIn(((2, 4), (3, 0)), detect("s=str()\ns.rsplit('a')"))
    self.assertOnlyIn(((2, 4), (3, 0)), detect("str().rsplit('a')"))

  def test_zfill_of_str(self):
    self.assertOnlyIn(((2, 2), (3, 0)), detect("s=\"\"\ns.zfill(2)"))
    self.assertOnlyIn(((2, 2), (3, 0)), detect("\"\".zfill(2)"))
    self.assertOnlyIn(((2, 2), (3, 0)), detect("s=str()\ns.zfill(2)"))
    self.assertOnlyIn(((2, 2), (3, 0)), detect("str().zfill(2)"))

  def test_as_integer_ratio_of_int(self):
    self.assertOnlyIn((3, 8), detect("(42).as_integer_ratio()"))
    self.assertOnlyIn((3, 8), detect("n=42\nn.as_integer_ratio()"))

  def test_bit_length_of_int(self):
    self.assertOnlyIn(((2, 7), (3, 1)), detect("(42).bit_length()"))
    self.assertOnlyIn(((2, 7), (3, 1)), detect("n=42\nn.bit_length()"))

  def test_to_bytes_of_int(self):
    self.assertOnlyIn((3, 2), detect("(42).to_bytes()"))
    self.assertOnlyIn((3, 2), detect("n=42\nn.to_bytes()"))

  def test_from_bytes_of_int(self):
    self.assertOnlyIn((3, 2), detect("int.from_bytes([42])"))

  def test_bit_length_of_long(self):
    if current_version() < 3.0:  # pragma: no cover
      self.assertOnlyIn((2, 7), detect("(42L).bit_length()"))
      self.assertOnlyIn((2, 7), detect("n=42L\nn.bit_length()"))

  def test_as_integer_ratio_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("(42.0).as_integer_ratio()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("n=42.0\nn.as_integer_ratio()"))

  def test_next_of_file(self):
    self.assertOnlyIn((2, 3), detect("file('name').next()"))

  def test_xreadlines_of_file(self):
    self.assertOnlyIn((2, 1), detect("file('name').xreadlines()"))

  def test_is_integer_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("(42.0).is_integer()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("n=42.0\nn.is_integer()"))

  def test_hex_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("(42.0).hex()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("n=42.0\nn.hex()"))

  def test_fromhex_of_float(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("(42.0).fromhex()"))
    self.assertOnlyIn(((2, 6), (3, 0)), detect("n=42.0\nn.fromhex()"))

  def test_hex_of_bytes(self):
    if current_version() >= 3.0:
      self.assertOnlyIn((3, 5), detect("b'\x10'.hex()"))
      self.assertOnlyIn((3, 5), detect("b=b'\x10'\nb.hex()"))

  def test_isascii_of_bytes(self):
    self.assertOnlyIn((3, 7), detect("b'\x10'.isascii()"))
    self.assertOnlyIn((3, 7), detect("b=b'\x10'\nb.isascii()"))

  def test_maketrans_of_bytes(self):
    self.assertOnlyIn((3, 1), detect("bytes.maketrans(b'a', b'b')"))

  def test_removeprefix_of_bytes(self):
    self.assertOnlyIn((3, 9), detect("bytes.removeprefix(b'a')"))

  def test_removesuffix_of_bytes(self):
    self.assertOnlyIn((3, 9), detect("bytes.removesuffix(b'a')"))

  def test_hex_of_bytearray(self):
    self.assertOnlyIn((3, 5), detect("bytearray(b'\x10').hex()"))
    self.assertOnlyIn((3, 5), detect("b=bytearray(b'\x10')\nb.hex()"))

  def test_isascii_of_bytearray(self):
    self.assertOnlyIn((3, 7), detect("bytearray(b'\x10').isascii()"))
    self.assertOnlyIn((3, 7), detect("b=bytearray(b'\x10')\nb.isascii()"))

  def test_maketrans_of_bytearray(self):
    self.assertOnlyIn((3, 1), detect("bytearray.maketrans(b'a', b'b')"))

  def test_removeprefix_of_bytearray(self):
    self.assertOnlyIn((3, 9), detect("bytearray.removeprefix(b'a')"))

  def test_removesuffix_of_bytearray(self):
    self.assertOnlyIn((3, 9), detect("bytearray.removesuffix(b'a')"))

  def test_hex_of_memoryview(self):
    self.assertOnlyIn((3, 5), detect("memoryview(b'1').hex()"))

  def test_release_of_memoryview(self):
    self.assertOnlyIn((3, 2), detect("memoryview(b'1').release()"))

  def test_cast_of_memoryview(self):
    self.assertOnlyIn((3, 3), detect("memoryview(b'1').cast()"))

  def test_toreadonly_of_memoryview(self):
    self.assertOnlyIn((3, 8), detect("memoryview(b'1').toreadonly()"))

  def test_deleter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("property.deleter()"))

  def test_getter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("property.getter()"))

  def test_setter_of_property(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("property.setter()"))

  def test_indices_of_slice(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("slice.indices()"))
