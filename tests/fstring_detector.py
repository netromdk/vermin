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
    ("f'{(x)=}'", True),
    ("f'{a[0]=}'", True),

    # CRLFs must not shift the byte offsets of nodes on later lines.
    ("x = 1\r\ns = f\"{x=}\"\r\n", True),
    ("x = 1\r\ns = f\"{x=!r}\"\r\n", True),

    # Bare `\r` endings and parser-only separators, like `\v` and `\f`, in string literals must not
    # shift offsets either.
    ("x = 1\rs = f\"{x=}\"\r", True),
    ("y = \"\v\f\"\ns = f\"{x=}\"\n", True),

    # Implicit concat merging a leading plain string part must not misdirect the self-doc `{`-anchor
    # onto that part.
    ('"{" f"{x=}"', True),
    ('"{x}" f"{y=}"', True),
    ('("{\\n" f"{x=}")', True),
    ('"}" f"{x=}"', True),

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
    ('f"abc {a["x"]} def"', "same_quote_string"),
    ("f'ab {a['x']} cd'", "same_quote_string"),
    ('f"{d["k"]=}"', "same_quote_string"),
    ('f"{ {"a": k} }"', "same_quote_string"),
    ('f"t{ ["a"] }"', "same_quote_string"),
    ('f"{a["x"]["y"]}"', "same_quote_string"),
    ('f"{x:{"ab"}}"', "same_quote_string"),
    ('f"{x:{w["y"]}}"', "same_quote_string"),
    ("f'{ {'k': v} }'", "same_quote_string"),

    # A different quote is valid since 3.6.
    ('f"abc {a[\'x\']} def"', None),
    ("f'abc {a[\"x\"]} def'", None),
    ('f"{x:{w[\'y\']}}"', None),
    ('f"{x:>a\'b}"', None),
    ("f'{x:{w[\"y\"]}}'", None),

    # Triple-quoted f-strings allow the single-character reuse natively.
    ('f"""abc {a["x"]} def"""', None),
    ('f"""abc {a[\'x\']} def"""', None),
    ("f'''abc {a['x']} def'''", None),

    ('f"{chr(34)}"', None),
    ('f"{x:10}"', None),
    ('f"{f\'x\'}"', None),
  ])
  def test_pep701_same_quote_string(self, source, expected):
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
    ("f\"\"\"{a + 'x'  # c\n}\"\"\"", "comment"),

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

    # A `#` before the format spec is a comment, but after the `:` it is literal text.
    ('q = "zz" + f"""{a  # c\n}"""', True),
    ('q = "zz" + f"""{x:>3  # c\n}"""', False),
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


def _set_span(node, span):
  node.lineno, node.col_offset, node.end_lineno, node.end_col_offset = span
  return node


def _name(identifier, span):
  return _set_span(ast.Name(id=identifier, ctx=ast.Load()), span)


def _joined(values, span):
  return _set_span(ast.JoinedStr(values=values), span)


def _formatted(value, span):
  return _set_span(ast.FormattedValue(value=value, conversion=-1, format_spec=None), span)


class FStringDetectorParityTests(VerminTest):
  """PEP 701 parity tests that run on every interpreter, covering analysis the 3.12-gated suite
  never reaches.
  """

  # pylint: disable=protected-access

  def setUp(self):
    super().setUp()
    self.none_detector = FStringDetector(None)

    # The source code is inert on purpose, being short and single-line with no braces, quotes, or
    # backslashes. And thus the fabricated spans have nothing to find and must always miss.
    self.detector = FStringDetector("xyz")

  def assert_pep701_none(self, source, span, token):
    detector = FStringDetector(source)
    nodes = joined_strs(source)
    self.assertTrue(nodes, "no f-string in: " + source)

    # Re-apply the 3.12+ top-level span, since pre-3.12 parsers pin it to the whole f-string.
    for val in nodes[0].values:
      if isinstance(val, ast.FormattedValue):
        _set_span(val, span)
        break

    for node in nodes:
      self.assertIsNone(detector.pep701_violation(node), source)

    got = detector._read_fstring_token(nodes[0], source.splitlines())
    self.assertEqual(token, got, source)

  # Spans as 3.12+ reports them, re-applied where pre-3.12 parsers pin fields to the f-string.
  @VerminTest.parameterized_args([
    ('f"{{lit}}{x}"', (1, 9, 1, 12), ('"', False)),
    ('f"{a[\'x\']}"', (1, 2, 1, 10), ('"', False)),
    ('f"{x:{f\'{y}\'}}"', (1, 2, 1, 14), ('"', False)),
    ("f'outer {f\"mid\"}'", (1, 8, 1, 16), ("'", False)),
    ('f"\\N{EXCLAMATION MARK}{x}"', (1, 22, 1, 25), ('"', False)),
    ('r"lit" f"{x}"', (1, 9, 1, 12), ('"', False)),
    ('("lit"\n# c\n f"{y}")', (3, 3, 3, 6), ('"', False)),
    ("('''lit''' f'{x}')", (1, 13, 1, 16), ("'", False)),
    ("f\"\"\"{a + '#'}\"\"\"", (1, 4, 1, 13), ('"', True)),
    ('f"\\\\{x}"', (1, 4, 1, 7), ('"', False)),
  ])
  def test_pep701_cross_version(self, source, spans, token):
    self.assert_pep701_none(source, spans, token)

  def test_codepoint_helpers(self):
    """Codepoint helpers on a truncated UTF-8 column and out-of-range spans."""
    self.assertEqual(1, self.detector._codepoint_col(["é"], 1, 1))
    self.assertIsNone(self.detector._span_offset(self.detector._lines, 4, 0))
    self.assertEqual(0, self.detector._codepoint_length(["a"], 9, 0, 9, 0))

    # A `lineno` in range for the char count but beyond the actual line count must return `None`
    # rather than index past the per-line offset array.
    single_line = FStringDetector("abc")
    self.assertIsNone(single_line._span_offset(single_line._lines, 2, 0))

  def test_scanner_guards(self):
    """String/brace scanners that run past their end without a closing token."""
    self.assertEqual(3, self.detector._skip_string("f\"ab", 1, 3, 4))
    self.assertEqual(4, self.detector._fstring_body_end("f\"ab", 1, 4, '"', False, None, None))
    self.assertEqual(4, self.detector._field_end("f\"{x", 3, 4))

  def test_token_span_guards(self):
    # A joined span past the source.
    self.assertIsNone(
      self.detector._read_fstring_token(_joined([], (9, 0, 9, 1)), self.detector._lines))

    # An end span past the source.
    self.assertIsNone(
      self.detector._read_fstring_token(_joined([], (1, 0, 9, 1)), self.detector._lines))

    # A field span past the source.
    bad_fv = _formatted(_name("x", (1, 1, 1, 2)), (9, 1, 9, 2))
    self.assertIsNone(
      self.detector._read_fstring_token(_joined([bad_fv], (1, 0, 1, 5)), self.detector._lines))

  def test_build_field_contexts_guards(self):
    # A node without `end_col_offset`, like it was pre-3.8, yields no contexts.
    class BareStringNode:
      def __init__(self, values):
        self.values = values
        self.lineno = 1
        self.col_offset = 0
        self.end_lineno = 1
    truncated = BareStringNode([])
    self.assertEqual({}, self.detector._build_field_contexts(truncated, self.detector._lines)[0])

    # A joined span past the source yields no contexts.
    self.assertEqual({}, self.detector._build_field_contexts(
      _joined([], (1, 0, 9, 1)), self.detector._lines)[0])

    # Real literals re-scanned under an empty joined node resolve nothing.
    for source, span in (("f\"a{b}c\"", (1, 2, 1, 7)),
                         ("f\"{{x}}\"", (1, 2, 1, 6)),
                         ("f\"ab\\N{SPACE}cd\"", (1, 2, 1, 13))):
      fabricated = FStringDetector(source)
      contexts = fabricated._build_field_contexts(_joined([], span), [source])[0]
      self.assertEqual({}, contexts)

    # A brace outside any f-string literal falls back to the default context.
    mid = FStringDetector("f\"a\" {x} f\"b\"")
    contexts, default = mid._build_field_contexts(_joined([], (1, 0, 1, 13)), ["f\"a\" {x} f\"b\""])
    self.assertEqual({5: ('"', False)}, contexts)
    self.assertEqual(('"', False), default)

  def test_resolve_field_context_fallback(self):
    no_pos = ast.FormattedValue(value=_name("x", (1, 1, 1, 2)), conversion=-1, format_spec=None)
    default = ("'", True)
    self.assertEqual(default, self.detector._resolve_field_context(no_pos, {}, default))

  def test_self_doc_walk_guards(self):
    candidate = \
      ast.FormattedValue(value=_name("a", (1, 1, 1, 2)), conversion=ord("r"), format_spec=None)

    # An empty f-string has no fields to walk.
    self.assertFalse(self.none_detector.is_self_doc(_joined([], (1, 0, 1, 3))))

    # A joined span past the source triggers the out-of-range guard.
    self.assertFalse(self.detector.is_self_doc(_joined([candidate], (9, 0, 9, 3))))

    # A normal `!r` field is simply not self-documenting.
    self.assertFalse(FStringDetector("f\"x\"").is_self_doc(_joined([candidate], (1, 0, 1, 4))))

    # Value node lacking end offsets, so the walk can't read past its span.
    value_no_end = ast.Name(id="a")
    value_no_end.lineno, value_no_end.col_offset = 1, 3
    fv_no_end = ast.FormattedValue(value=value_no_end, conversion=ord("r"), format_spec=None)
    fv_no_end.lineno, fv_no_end.col_offset = 1, 2
    fv_no_end.end_lineno, fv_no_end.end_col_offset = 1, 4
    self.assertFalse(FStringDetector("f\"{x}\"").is_self_doc(_joined([fv_no_end], (1, 0, 1, 5))))

    # Value truncated at the span's edge, where no `=` can follow.
    truncated_fv = _formatted(_name("x", (1, 3, 1, 4)), (1, 2, 1, 4))
    self.assertFalse(FStringDetector("f\"{x}\"").is_self_doc(_joined([truncated_fv], (1, 0, 1, 4))))

  def test_violation_scan_guards(self):
    sample = _formatted(_name("x", (1, 2, 1, 5)), (1, 2, 1, 6))
    self.assertFalse(self.none_detector._has_same_quote_string(sample, '"'))
    self.assertFalse(self.none_detector._has_pep701_backslash(sample, None))
    self.assertFalse(self.none_detector._has_pep701_comment(sample, None))

    bad_span = _formatted(_name("x", (1, 1, 1, 2)), (9, 0, 9, 1))
    self.assertFalse(self.detector._has_same_quote_string(bad_span, '"'))
    self.assertFalse(self.detector._has_pep701_comment(bad_span, self.detector._lines))

  def test_backslash_scan(self):
    cont = FStringDetector("f\"{a \\\n}\"")
    cont_fv = _formatted(_name("a", (1, 3, 1, 4)), (1, 2, 2, 1))
    self.assertTrue(cont._has_pep701_backslash(cont_fv, cont._lines))

    token_error = FStringDetector("f\"ab'\\\nc}\"")
    token_fv = _formatted(_name("x", (1, 3, 1, 6)), (1, 2, 1, 6))
    self.assertFalse(token_error._has_pep701_backslash(token_fv, token_error._lines))
