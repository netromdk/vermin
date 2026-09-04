import ast

from vermin.fstring_detector import FStringDetector

from .testutils import VerminTest


def joined_strs(source):
  tree = ast.parse(source)
  return [n for n in ast.walk(tree) if isinstance(n, ast.JoinedStr)]


class FStringDetectorTests(VerminTest):
  def assert_self_doc(self, source, expected):
    detector = FStringDetector(source)
    nodes = joined_strs(source)
    self.assertTrue(nodes, "no f-string in: " + source)
    self.assertEqual(expected, any(detector.is_self_doc(n) for n in nodes), source)

  def assert_pep701(self, source, expected):
    """Assert the source's f-strings trigger the named PEP 701 violation. `None` expectation means
    "no violation", not "no f-string", which is asserted separately.
    """
    detector = FStringDetector(source)
    nodes = joined_strs(source)
    self.assertTrue(nodes, "no f-string in: " + source)
    if expected is None:
      self.assertTrue(all(detector.pep701_violation(n) is None for n in nodes), source)
    else:
      self.assertTrue(any(detector.pep701_violation(n) == expected for n in nodes), source)

  def test_none_source(self):
    detector = FStringDetector(None)
    node = joined_strs('f"{x}"')[0]
    self.assertFalse(detector.is_self_doc(node))
    self.assertIsNone(detector.pep701_violation(node))
    # pylint: disable=W0212
    self.assertIsNone(detector._read_fstring_token(node, None))

  def test_input_guards(self):
    detector = FStringDetector('f"{x}"')
    bare = ast.JoinedStr()
    const = ast.Constant(value="a")
    self.assertIsNone(detector.pep701_violation(bare))
    self.assertFalse(detector.is_self_doc(const))
    self.assertIsNone(detector.pep701_violation(const))
    # pylint: disable=W0212
    self.assertIsNone(detector._read_fstring_token(bare, 'f"{x}"'.splitlines()))
    self.assertIsNone(detector._read_fstring_token(bare, []))

  @VerminTest.skipUnlessVersion(3, 8)
  @VerminTest.parameterized_args([
    ("f'{a=}'", True),
    ("f'hello {name=}'", True),
    ("f'{b=}={a}'", True),
    ("f'{a =}'", True),
    ("f'{ a=}'", True),
    ("f'{a= }'", True),
    ("f'{ a = }'", True),
    ("f'{1+1=}'", True),
    ("f'{a+b=}'", True),
    ("f'{-5=}'", True),
    ("f'{(1,2,3)=}'", True),
    ("f'{ {1,2,3}=}'", True),
    ("f'{[x for x in [1,2,3]]=}'", True),
    ("f'{0==1=}'", True),
    ("f'{3.14=:10.10}'", True),
    ("f'{3.14=!s:10.10}'", True),
    ("f'{x=!r}'", True),
    ("f'{x=:.2f}'", True),
    ("f'{f\"{3.1415=:.1f}\":*^20}'", True),
    ("f'{{literal}}{a=}'", True),
    ("f'''{\n3\n=}'''", True),
    ("f'{f(a=4)=}'", True),
    ("f\"\\N{EXCLAMATION MARK}{a=}\"", True),
    ("f\"{x = :.2f}\"", True),
    ("f\"{(x) = :.2f}\"", True),
    ("f\"{     2      +     2    =    }\"", True),
    ("f\"{''=}\"", True),
    ('f"""{1=: "this" is fine}"""', True),

    # CRLFs must not shift the byte offsets of nodes on later lines.
    ("x = 1\r\ns = f\"{x=}\"\r\n", True),
    ("x = 1\r\ns = f\"{x=!r}\"\r\n", True),

    # Bare `\r` endings and parser-only separators, like `\v` and `\f`, in string literals must not
    # shift offsets either.
    ("x = 1\rs = f\"{x=}\"\r", True),
    ("y = \"\v\f\"\ns = f\"{x=}\"\n", True),

    ("a = 1\nf'a={a}'", False),
    ("a = 1\nf'={a}'", False),
    ("f'{a != b}'", False),
    ("f'{a == b}'", False),
    ("f'{a >= b}'", False),
    ("f'{a <= b}'", False),
    ("f'{x:=10}'", False),
    ("f'hello {name!r}'", False),
    ("f'{x!r}'", False),
    ("f'{x!s}'", False),
    ("f'{x!a}'", False),
    ("f'{x:.2f}'", False),
    ("f'val={val:.2f}'", False),
    ("f'{(a+b)}={x!r}'", False),
    ("f'{{x={a}}}'", False),
    ("f'{x}'", False),
    ("f'{x:{width}}'", False),
    ("f'={cos(radians(theta)):.3f}'", False),
    ("x = 1\r\ns = f\"{x+1}\"\r\n", False),
    ("x = 1\rs = f\"{x+1}\"\r", False),
  ])
  def test_self_doc(self, source, expected):
    self.assert_self_doc(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ('f"{\n1+2\n}"', "multi_line"),
    ('f"{\n  x +\n  y\n}"', "multi_line"),
    ("f\"{\n'''a'''\n}\"", "multi_line"),
    ("'''lit''' f\"{x\n+y}\"", "multi_line"),
    ('f"{a \\\n}"', "multi_line"),
    ("f'abc {\nx\n}'", "multi_line"),

    ('f"{x}"', None),
    ('f"{x:10}"', None),
    ("f'''{\n3\n}'''", None),
    ('f"\\N{EXCLAMATION MARK}{x}"', None),
    ('s = (f"got {x}: "\n     f"done")', None),
    ('s = f"{a}" f"{b}"', None),
    ('s = f"lit {a}" f"""{b\n+ c}"""', None),
    ('s = (f"got {x}: "\n     f"""done\n{p\n+ q}""")', None),
  ])
  def test_pep701_multi_line(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ('f"outer {f"inner"}"', "nested_same_quote"),
    ("f'outer {f'inner'}'", "nested_same_quote"),
    ('f"""outer {f"""inner"""}"""', "nested_same_quote"),
    ('f"outer {f"""inner"""}"', "nested_same_quote"),
    ('f"{x:{f".2f"}}"', "nested_same_quote"),
    ('f"1 {f"2 {f"3"}"}"', "nested_same_quote"),
    ('f"normal {f"{a=}"} normal"', "nested_same_quote"),
    ('f"normal {f"{a:.3f}"} normal"', "nested_same_quote"),
    ('f"normal { {f"{ { [1, 2] } }" } } normal"', "nested_same_quote"),
    ('f"foo {f"bar {x}"} baz"', "nested_same_quote"),
    ('value = f"{f"\\{1}"}"', "nested_same_quote"),
    ('value = rf"{f"\\{1}"}"', "nested_same_quote"),
    ('value = f"{rf"\\{1}"}"', "nested_same_quote"),
    ('_ = "a" f"b {f"c" f"d"} e" "f"', "nested_same_quote"),
    ('f"\\"foo\\" {f"\\"foo\\""} \\"\\""', "nested_same_quote"),

    ('f"""outer {f"inner"}"""', None),
    ('f"outer {f\'inner\'}"', None),
    ("f'outer {f\"inner\"}'", None),
  ])
  def test_pep701_nested_same_quote(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ("'lit' f\"{f\"{x}\"}\"", "nested_same_quote"),
    ('"""lit""" f"{f"{x}"}"', "nested_same_quote"),
    ("'''lit''' f\"{f\"{x}\"}\"", "nested_same_quote"),
    ("f'{\"lit\" f'{x}'}'", "nested_same_quote"),
    ('f"""{rf"""{x}"""}"""', "nested_same_quote"),
    ('f"{fr"""{x}"""}"', "nested_same_quote"),
    ("f'outer {rf'''{x}'''}'", "nested_same_quote"),
    ('f"{F"e{fr"""{x}"""}config"}"', "nested_same_quote"),
    ("('lit'\n# comment between\n f\"{f\"{x}\"}\")", "nested_same_quote"),

    ("'pre' f\"{f'{x}'}\"", None),
    ("'''pre''' f\"{f'{x}'}\"", None),

    # Format-spec nested f-strings are valid pre-3.12 even when same-quoted.
    ("f\"{x:{f'{y}'}}\"", None),
    ('f"""{x:{f"{y}"}}"""', None),
  ])
  def test_pep701_nested_same_quote_implicit_concat(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ("f\"{'\\n'.join(x)}\"", "backslash"),
    ("f\"{r'\\n'}\"", "backslash"),
    ("f\"{'\\''}\"", "backslash"),
    ("t = f\"{'\\InHere'=}\"", "backslash"),
    ('f"{"\\xFF\\N{space}"=}"', "backslash"),
    ('f"{r"\\xFF"=}"', "backslash"),

    ("f\"{chr(10)}\"", None),
    ("f'hello\\nworld'", None),
  ])
  def test_pep701_backslash(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  def test_pep701_backslash_line_continuation(self):
    source = 'f"{a \\\n}"'
    node = joined_strs(source)[0].values[0]
    detector = FStringDetector(source)
    # pylint: disable=W0212
    self.assertTrue(detector._has_pep701_backslash(node, source.splitlines()))

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ('f"""{x  # comment\n}"""', "comment"),
    ('f"""{x\n# comment\n}"""', "comment"),

    ("f\"{'#notacomment'}\"", None),
    ('f"{x}"', None),

    # `#` in a format spec is spec filler text, valid since 3.6.
    ('f"""{x:>3  # c\n}"""', None),
    ('f"""{x:{w}  # c\n}"""', None),
    ('f"""{x!r:>3  # c\n}"""', None),

    # A comment before the format spec is a PEP 701 comment.
    ('f"""{x  # c\n:>3}"""', "comment"),
  ])
  def test_pep701_comment(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ("('lit' f\"{x}\")", ('"', False)),
    ("('''lit''' f'{x}')", ("'", False)),
    ('(f"lit {a}" f"""{b\n+ c}""")', ('"', False)),
    ('f"{f"{x}"}"', ('"', False)),
    ('f"""{rf"""{x}"""}"""', ('"', True)),
    ('rf"raw {x}"', ('"', False)),
    ("(f'lit' f\"{x}\")", ("'", False)),
  ])
  def test_read_fstring_token(self, source, expected):
    detector = FStringDetector(source)
    nodes = joined_strs(source)
    self.assertTrue(nodes, "no f-string in: " + source)
    # pylint: disable=W0212
    got = detector._read_fstring_token(nodes[0], source.splitlines())
    self.assertEqual(expected, got, source)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ('f"""{x:>3  # c\n}"""', False),
    ('f"""{x:{w}  # c\n}"""', False),
    ('f"""{x!r:>3  # c\n}"""', False),
    ('f"""{x  # c\n:>3}"""', True),
    ('f"""{x\n# comment\n}"""', True),
    ("f\"{'#notacomment'}\"", False),
  ])
  def test_pep701_comment_region(self, source, expected):
    detector = FStringDetector(source)
    node = joined_strs(source)[0].values[0]
    # pylint: disable=W0212
    got = detector._has_pep701_comment(node, source.splitlines())
    self.assertEqual(expected, got, source)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    ("x = 1\r\ns = f\"{f\"{x}\"}\"\r\n", "nested_same_quote"),
    ("x = 1\r\ns = f\"{\r\nx\r\n}\"\r\n", "multi_line"),
    ("x = 1\r\ns = f\"{x  # c\r\n}\"\r\n", "multi_line"),
    ("x = 1\r\ns = f\"\"\"{x  # c\r\n}\"\"\"\r\n", "comment"),
    ("x = 1\r\n'''lit''' f\"{x\n+y}\"\r\n", "multi_line"),
    ("x = 1\r\ns = f\"{x!r}\"\r\n", None),
  ])
  def test_pep701_crlf(self, source, expected):
    self.assert_pep701(source, expected)

  @VerminTest.skipUnlessVersion(3, 12)
  @VerminTest.parameterized_args([
    # Bare `\r` endings and parser-only separators, like `\v` and `\f`, in string literals must not
    # shift offsets of nodes on later lines.
    ("x = 1\rs = f\"{f\"{x}\"}\"\r", "nested_same_quote"),
    ("y = \"\v\f\"\ns = f\"{f\"{x}\"}\"\n", "nested_same_quote"),
    ("x = 1\rs = f\"{x}\"\r", None),
    ("y = \"\v\f\"\ns = f\"{x}\"\n", None),
  ])
  def test_pep701_parser_line_breaks(self, source, expected):
    self.assert_pep701(source, expected)
