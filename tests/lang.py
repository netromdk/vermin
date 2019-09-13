from .testutils import VerminTest, detect, current_version, current_major_version

class VerminLanguageTests(VerminTest):
  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn(2.0, detect("print 'hello'"))

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    self.assertIn(current_major_version(), detect("print('hello')"))

  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn(2.0, detect("print 'hello'\nprint('hello')"))

  def test_format(self):
    vers = detect("'hello {}!'.format('world')")
    self.assertOnlyIn((2.7, 3.0), vers)

  def test_longv2(self):
    self.assertOnlyIn(2.0, detect("v = long(42)"))
    self.assertOnlyIn(2.0, detect("isinstance(42, long)"))

  def test_bytesv3(self):
    if current_major_version() >= 3:
      self.assertOnlyIn(3.0, detect("v = b'hello'"))
      self.assertOnlyIn(3.0, detect("v = B'hello'"))

  def test_fstrings(self):
    if current_version() >= 3.6:
      self.assertOnlyIn(3.6, detect("name = 'world'\nf'hello {name}'"))

  def test_coroutines_async(self):
    if current_version() >= 3.5:
      self.assertOnlyIn(3.5, detect("async def func():\n\tpass"))

  def test_coroutines_await(self):
    if current_version() >= 3.5:
      self.assertOnlyIn(3.5, detect("async def func():\n\tawait something()"))

  def test_async_generator(self):
    if current_version() >= 3.6:
      self.assertOnlyIn(3.6, detect("async def func():\n\tyield 42\n\tawait something()"))

  def test_async_comprehension(self):
    if current_version() >= 3.6:
      self.assertOnlyIn(3.6, detect("[i async for i in aiter() if i % 2]"))

