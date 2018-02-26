from testutils import MinpyTest, detect, current_version, current_major_version

class MinpyLanguageTests(MinpyTest):
  def test_printv2(self):
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn(2.0, detect("print 'hello'"))

  def test_printv3(self):
    """Allowed in both v2 and v3."""
    self.assertOnlyIn(current_major_version(), detect("print('hello')"))

  def test_print_v2_v3_mixed(self):
    """When using both v2 and v3 style it must return v2 because v3 is allowed in v2."""
    # Before 3.4 it just said "invalid syntax" and didn't hint at missing parentheses.
    if current_version() >= 3.4:
      self.assertOnlyIn(2.0, detect("print 'hello'\nprint('hello')"))

  def test_format(self):
    vers = detect("'hello {}!'.format('world')")
    self.assertOnlyIn((2.7, 3.0), vers)
