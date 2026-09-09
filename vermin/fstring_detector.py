import ast

from .utility import split_lines


BACKSLASH = "\\"
HASH = "#"
FSTRING_PREFIX_CHARS = "furb"
STRING_QUOTE_CHARS = "\"'"
NEWLINE = "\n"
OPEN_BRACE = "{"
CLOSE_BRACE = "}"
DOUBLE_BRACE = "{{"
TRIPLE_QUOTE_LEN = 3
SINGLE_QUOTE_LEN = 1
FSTRING_FLAG = "f"
FSTRING_TOKEN_PREFIX_CHARS = "rf"  # nosec
UNICODE_NAME_ESCAPE = BACKSLASH + "N"
CLOSING_TRAILERS = ")]"
WS_AND_NEWLINES = " \t\r" + NEWLINE
WS_AND_TRAILERS = WS_AND_NEWLINES + CLOSING_TRAILERS
SELF_DOC_MARKER = "="
SELF_DOC_FOLLOW_CHARS = "!:`}"
REPR_CONVERSION = ord("r")


class FStringDetector:
  def __init__(self, source):
    self._source = source
    if source is None:
      self._lines = None
      self._line_offsets = [0]
    else:
      self._lines, self._line_offsets = split_lines(source)

  def _codepoint_col(self, lines, lineno, col_offset):
    """Convert an AST byte-based column offset to a code-point column offset. CPython reports
    `col_offset`/`end_col_offset` as byte offsets into the UTF-8 encoded source, while slicing
    operates on code-point strings, so the two only differ after non-ASCII text on the same line.
    """
    if not lines or lineno < 1 or lineno > len(lines) or col_offset <= 0:
      return 0
    line = lines[lineno - 1]
    try:
      return len(line.encode("utf-8")[:col_offset].decode("utf-8"))
    except UnicodeDecodeError:
      return len(line)

  def _codepoint_length(self, lines, start_lineno, start_col_offset,
                        end_lineno, end_col_offset):
    src_len = len(self._source)
    start_off = self._span_offset(lines, start_lineno, start_col_offset, src_len)
    end_off = self._span_offset(lines, end_lineno, end_col_offset, src_len)
    if start_off is None or end_off is None:
      return 0
    return max(0, end_off - start_off)

  def is_self_doc(self, node):
    if not hasattr(node, "values") or self._source is None:
      return False
    values = node.values
    for idx, value in enumerate(values):
      if isinstance(value, ast.FormattedValue) and self._is_fstring_self_doc_candidate(values, idx):
        return self._self_doc_source_walk(node)
    return False

  def _is_fstring_self_doc_candidate(self, values, index):
    """Whether the FormattedValue at `index` may be self-documenting. A `{expr=}` field carries
    conversion 114 (`ord("r")`), while a `{literal=}` field, like `{3.14=:..}`, folds with
    conversion -1 and ends the preceding Constant's text in `=`.
    """
    val = values[index]
    if val.conversion == REPR_CONVERSION:
      return True
    return index > 0 and isinstance(values[index - 1], ast.Constant) and \
      isinstance(values[index - 1].value, str) and \
      values[index - 1].value.rstrip().endswith(SELF_DOC_MARKER)

  def _self_doc_source_walk(self, node):
    """Confirm self-doc by locating each `{..}` region in the source."""
    source = self._source
    lines = self._lines
    start = self._span_offset(lines, node.lineno, node.col_offset, len(source))
    end = self._span_offset(lines, node.end_lineno, node.end_col_offset, len(source))
    if start is None or end is None:
      return False

    # Locate the first f-string literal in the fused span. Implicit concat can merge a leading plain
    # string part, whose literal braces would otherwise misdirect the `{`-anchor.
    pos = self._fstring_opener_end(source, start, end, start)
    if pos is None:
      return False

    for idx, val in enumerate(node.values):
      if not isinstance(val, ast.FormattedValue):
        continue

      # Find the next non-escaped opening brace.
      while pos < end:
        if source[pos] == OPEN_BRACE:
          # Skip escaped `{{`.
          if source.startswith(DOUBLE_BRACE, pos):
            pos += len(DOUBLE_BRACE)
            continue

          # Skip to the closing brace of a `\N{..}` unicode name or a `\{` escaped literal.
          if (pos >= start + len(UNICODE_NAME_ESCAPE) and
              source[pos - len(UNICODE_NAME_ESCAPE):pos] == UNICODE_NAME_ESCAPE) or \
             (pos > start and source[pos - 1] == BACKSLASH):
            close = source.find(CLOSE_BRACE, pos, end)
            pos = close + 1 if close != -1 else end
            continue

          break  # Actual opening brace found.
        pos += 1
      if pos >= end:
        break

      # Skip non-candidates and consume region.
      if not self._is_fstring_self_doc_candidate(node.values, idx):
        close = source.find(CLOSE_BRACE, pos, end)
        if close == -1:
          break
        pos = close + 1
        continue

      # Nested f-strings get bogus positions on Python 3.8 because inner tokens are pinned to the
      # opening quote, so the `{`-anchor cannot locate their fields. A self-doc fold whose text
      # appears verbatim in the source with a `{` directly before it is self-locating, its trailing
      # `=` the marker.
      if idx > 0 and isinstance(node.values[idx - 1], ast.Constant) and \
         isinstance(node.values[idx - 1].value, str) and \
         node.values[idx - 1].value.rstrip().endswith(SELF_DOC_MARKER) and \
         not node.values[idx - 1].value.startswith(OPEN_BRACE):
        const_text = node.values[idx - 1].value
        match = start - 1
        while True:
          match = source.find(const_text, match + 1, end)
          if match == -1:
            break

          # Unescaped `{` directly before (not `{{`), and a valid self-doc follow char after `=`.
          after = match + len(const_text)
          if match - 1 >= start and source[match - 1] == OPEN_BRACE and \
             not (match - 2 >= start and source[match - 2] == OPEN_BRACE) and \
             (after >= end or source[after] in SELF_DOC_FOLLOW_CHARS):
            return True

      # Position is lost on 3.8 but the length survives, so the end is derivable.
      if not hasattr(val.value, "end_col_offset") or val.value.end_col_offset is None:
        return False

      # Skip leading whitespace in the field body.
      body = pos + 1
      while body < end and source[body] in WS_AND_NEWLINES:
        body += 1

      # Measure the expression via AST positions, then skip closing trailers (parens/brackets).
      length = self._codepoint_length(lines, val.value.lineno, val.value.col_offset,
                                      val.value.end_lineno, val.value.end_col_offset)
      expr_end = body + length
      while expr_end < end and source[expr_end] in CLOSING_TRAILERS:
        expr_end += 1

      # Skip trailing whitespace and look for the `=` self-doc marker.
      probe = expr_end
      while probe < end and source[probe] in WS_AND_NEWLINES:
        probe += 1
      if probe < end and source[probe] == SELF_DOC_MARKER:
        return True

      # Grouping-paren inclusion differs across node types and versions, so the span may land before
      # the actual end. Probe one char further on.
      if not (probe < end and source[probe] in SELF_DOC_FOLLOW_CHARS) and \
         expr_end + 1 < end:
        probe = expr_end + 1
        while probe < end and source[probe] in WS_AND_TRAILERS:
          probe += 1
        if expr_end + 1 < probe < end and source[probe] == SELF_DOC_MARKER:
          return True

      close = source.find(CLOSE_BRACE, body, end)
      if close == -1:
        break
      pos = close + 1
    return False

  def pep701_violation(self, node):
    """Return the first PEP 701 construct the JoinedStr `node` triggers, or None. All five are
    `SyntaxError` before 3.12.
    """
    if self._source is None:
      return None
    if not hasattr(node, "values") or not hasattr(node, "end_lineno"):
      return None

    # Pre-3.12 parsers pin internal `FormattedValue` positions to the whole span, so the scan bound
    # collapses onto the span start and no quote can be read. The analysis is skipped on such trees.
    lines = self._lines
    if self._read_fstring_token(node, lines) is None:
      return None
    contexts, default_context = self._build_field_contexts(node, lines)

    for val in node.values:
      if not isinstance(val, ast.FormattedValue):
        continue

      outer = self._resolve_field_context(val, contexts, default_context)
      if outer is None:
        continue
      outer_quote, outer_triple = outer

      # Check expression spanning lines in a single/double-quoted f-string. Triple-quoted f-strings
      # allow newlines natively (3.6+), and implicit concatenation that merges a triple-quoted part
      # (which the parser collapses, losing the triple-quote info in the AST) is excluded too.
      if not outer_triple and hasattr(val, "end_lineno") and \
         val.end_lineno is not None and hasattr(val, "lineno") and \
         val.end_lineno > val.lineno:
        return "multi_line"

      # Check same-quote nesting. A triple-quoted outer f-string allows a nested single-occurrence
      # inner quote natively, but nested triple-quote f-strings using the same character require
      # 3.12+.
      for inner_js in self._walk_joined_strs(val):
        if inner_js.lineno == node.lineno and \
           inner_js.col_offset == node.col_offset:
          # Pre-3.12 parsers pin inner `JoinedStr` nodes to the outer quote, which would falsely
          # read as same-quote nesting with itself.
          continue

        inner = self._read_fstring_token(inner_js, lines)
        if inner is None or inner[0] != outer_quote:
          continue
        if not outer_triple or inner[1]:
          return "nested_same_quote"

      # A string literal reusing the outer quote inside a field is only legal from 3.12. A
      # triple-quoted f-string natively allows the single-character reuse, so only single/double
      # quotes trigger this. The backslash check is ordered first so escaped same-quote literals
      # keep their backslash label.
      if self._has_pep701_backslash(val, lines):
        return "backslash"

      if not outer_triple and self._has_same_quote_string(val, outer_quote):
        return "same_quote_string"

      if self._has_pep701_comment(val, lines):
        return "comment"
    return None

  def _fstring_opener_end(self, source, pos, bound, lower_bound):
    """Return the offset just past the opening quote of the first f-string literal in `[pos,
    bound)`, skipping plain strings, comments, and non-f prefixes, or None if there is no f-string.
    """
    while pos < bound:
      ch = source[pos]

      if ch in STRING_QUOTE_CHARS:
        if self._match_fstring_quote(source, pos, lower_bound) is None:
          next_pos = self._skip_string(source, pos, bound, len(source))
          if next_pos >= bound:
            # No well-formed plain literal within bounds. Advance past the lone quote and keep
            # scanning so the `{`-anchor still finds the fields.
            pos += SINGLE_QUOTE_LEN
            continue
          pos = next_pos
          continue

        # F-string opener found. Return just past its quote(s).
        pos += (TRIPLE_QUOTE_LEN if source.startswith(ch * TRIPLE_QUOTE_LEN, pos)
                else SINGLE_QUOTE_LEN)
        return pos

      if ch == HASH:
        pos = self._skip_comment(source, pos, bound)
        continue

      pos += 1
    return None

  def _read_fstring_token(self, node, lines):
    """Return `(quote, is_triple)` of the f-string opening at `node`'s span, or None. On 3.12+
    implicit-concat, `col_offset` points at the leading part and raw prefixes at the `f`, so the
    opener is scanned forward to the first f-string literal. This also stops a nested same-quote
    literal like `f"{f'x'}"` from being misread as the opener.
    """
    source = self._source
    if source is None or lines is None or not lines:
      return None
    if not hasattr(node, "lineno") or not hasattr(node, "end_lineno") or \
       not hasattr(node, "col_offset"):
      return None

    # Map the byte-based span-start position to a code-point source offset.
    src_len = len(source)
    start = self._span_offset(lines, node.lineno, node.col_offset, src_len)
    if start is None:
      return None

    # Use end-of-source as the span end when the node has no end column.
    end = src_len
    if hasattr(node, "end_col_offset"):
      end = self._span_offset(lines, node.end_lineno, node.end_col_offset, src_len)
      if end is None:
        return None

    # Stop scanning at the first field to avoid misreading a nested same-quote literal as the
    # opener.
    bound = end
    for val in node.values:
      if not isinstance(val, ast.FormattedValue):
        continue
      if hasattr(val, "lineno") and hasattr(val, "col_offset"):
        offset = self._span_offset(lines, val.lineno, val.col_offset, src_len)
        if offset is None:
          return None
        bound = offset
      break

    # Skip plain strings, comments, and non-f prefix tokens to reach the f-string opener.
    pos = start
    while pos < bound:
      ch = source[pos]

      if ch in STRING_QUOTE_CHARS:
        pos = self._skip_string(source, pos, bound, src_len)
        continue

      if ch == HASH:
        pos = self._skip_comment(source, pos, bound)
        continue

      if ch.lower() in FSTRING_TOKEN_PREFIX_CHARS:
        prefix_end = pos
        while prefix_end < bound and source[prefix_end].lower() in FSTRING_TOKEN_PREFIX_CHARS:
          prefix_end += 1
        if prefix_end < bound and source[prefix_end] in STRING_QUOTE_CHARS:
          if FSTRING_FLAG in source[pos:prefix_end].lower():
            quote = source[prefix_end]
            is_triple = source.startswith(quote * TRIPLE_QUOTE_LEN, prefix_end)
            return (quote, is_triple)  # f-string opener found.

          # Skip plain non-fstring, like `r"lit"`.
          pos = self._skip_string(source, prefix_end, bound, src_len)
          continue

      pos += 1
    return None

  def _span_offset(self, lines, lineno, col_offset, src_len):
    """Return the source offset of a code-point line/column position, or None."""
    if lineno - 1 >= src_len:
      return None
    return self._line_offsets[lineno - 1] + self._codepoint_col(lines, lineno, col_offset)

  def _skip_string(self, source, pos, bound, src_len):
    """Skip a plain string literal starting at the quote at `pos` and return the offset past it."""
    quote = source[pos]
    is_triple = source.startswith(quote * TRIPLE_QUOTE_LEN, pos)
    scan = pos + (TRIPLE_QUOTE_LEN if is_triple else SINGLE_QUOTE_LEN)
    while scan < bound and scan < src_len:
      ch = source[scan]
      if ch == BACKSLASH:
        scan += 2
      elif is_triple:
        if source.startswith(quote * TRIPLE_QUOTE_LEN, scan):
          return scan + TRIPLE_QUOTE_LEN  # Closing triple quote found.
        scan += 1
      elif ch == quote:
        return scan + SINGLE_QUOTE_LEN
      else:
        scan += 1
    return min(bound, src_len)

  def _skip_comment(self, source, pos, bound):
    """Skip `#` comment to the end of its line and return the offset past the newline or `bound`."""
    nl_pos = source.find(NEWLINE, pos, bound)
    return bound if nl_pos == -1 else nl_pos + 1

  def _build_field_contexts(self, node, lines):
    """Map each top-level replacement-field `{` offset to the `(quote, is_triple)` of the f-string
    literal that contains it, plus a default context (the first f-string token) used when a field
    cannot be attributed. The source is scanned forward over the whole fused span, so leading plain
    strings and `#` comments between implicitly-concatenated parts are skipped before a part's quote
    is read, and single- and triple-quoted parts each contribute their own context.
    """
    source = self._source
    src_len = len(source)
    contexts = {}
    default = None
    if not hasattr(node, "end_col_offset"):
      return contexts, default

    start = self._span_offset(lines, node.lineno, node.col_offset, src_len)
    end = self._span_offset(lines, node.end_lineno, node.end_col_offset, src_len)
    if start is None or end is None:
      return contexts, default

    # Scan the fused span, attributing each `{` to the f-string literal that contains it.
    pos = start
    while pos < end:
      ch = source[pos]

      # Record f-string literals' quote and tripleness in their context.
      if ch in STRING_QUOTE_CHARS:
        fstr = self._match_fstring_quote(source, pos, start)
        if fstr is None:
          pos = self._skip_string(source, pos, end, src_len)
          continue
        quote, is_triple = fstr
        context = (quote, is_triple)
        if default is None:
          default = context
        pos = self._fstring_body_end(source, pos, end, quote, is_triple, context, contexts)
        continue

      # Skip escaped/nested braces and map each field to its context.
      if ch == OPEN_BRACE:
        if source.startswith(DOUBLE_BRACE, pos):
          pos += len(DOUBLE_BRACE)  # Escaped brace in a literal.
          continue

        # A `\N{` unicode name or a `\{` escaped literal is not a replacement field.
        if (pos >= start + len(UNICODE_NAME_ESCAPE) and
            source[pos - len(UNICODE_NAME_ESCAPE):pos] == UNICODE_NAME_ESCAPE) or \
           (pos > start and source[pos - 1] == BACKSLASH):
          close = source.find(CLOSE_BRACE, pos, end)
          pos = close + 1 if close != -1 else end
          continue

        if default is not None:
          contexts[pos] = default
        pos = self._field_end(source, pos + 1, end)
        continue

      # Skip comments between concatenated parts to the end of the line.
      if ch == HASH:
        pos = self._skip_comment(source, pos, end)
        continue

      pos += 1
    return contexts, default

  def _resolve_field_context(self, val, contexts, default_context):
    """Return the `(quote, is_triple)` context of the f-string literal enclosing a field."""
    lineno = getattr(val, "lineno", None)
    col = getattr(val, "col_offset", None)
    if lineno is None or col is None:
      return default_context
    offset = self._span_offset(self._lines, lineno, col, len(self._source))
    field_ctx = contexts.get(offset)
    return default_context if field_ctx is None else field_ctx

  def _match_fstring_quote(self, source, pos, lower_bound):
    """Return the quote and tripleness if `source[pos]` opens an f-string literal, else None."""
    prefix_start = pos - 1
    while prefix_start >= lower_bound and source[prefix_start].lower() in FSTRING_PREFIX_CHARS:
      prefix_start -= 1
    if FSTRING_FLAG not in source[prefix_start + 1:pos].lower():
      return None
    return (source[pos], source.startswith(source[pos] * TRIPLE_QUOTE_LEN, pos))

  def _fstring_body_end(self, source, pos, end, quote, is_triple, context, contexts):
    """Scan one f-string literal's body, starting at its opening quote at `pos`, and return the
    offset just past its closing quote. Replacement fields directly under the literal are mapped to
    `context` in `contexts` when that mapping is wanted.
    """
    pos += TRIPLE_QUOTE_LEN if is_triple else SINGLE_QUOTE_LEN
    while pos < end:
      ch = source[pos]

      # Skip escaped character.
      if ch == BACKSLASH:
        pos += 2
        continue

      if ch == OPEN_BRACE:
        # Skip escaped `{{`.
        if source.startswith(DOUBLE_BRACE, pos):
          pos += len(DOUBLE_BRACE)
          continue

        # Skip `\N{..}` unicode name escape.
        if pos >= len(UNICODE_NAME_ESCAPE) and \
           source[pos - len(UNICODE_NAME_ESCAPE):pos] == UNICODE_NAME_ESCAPE:
          close = source.find(CLOSE_BRACE, pos, end)
          pos = close + 1 if close != -1 else end
          continue

        # Skip a backslash-escaped nested brace.
        if pos > 0 and source[pos - 1] == BACKSLASH:
          pos += 1
          continue

        if contexts is not None:
          contexts[pos] = context
        pos = self._field_end(source, pos + 1, end)
        continue

      # Closing triple quote found.
      if is_triple:
        if source.startswith(quote * TRIPLE_QUOTE_LEN, pos):
          return pos + TRIPLE_QUOTE_LEN

      # Closing single quote found.
      elif ch == quote:
        return pos + SINGLE_QUOTE_LEN

      pos += 1
    return end

  def _field_end(self, source, pos, end):
    """Scan a replacement field's expression, just after its `{`, and return the offset just past
    the matching `}`. Braces, strings, escapes, and nested f-strings inside the expression are
    skipped, so the enclosing brace is found even when a nested f-string reuses the same quote.
    """
    depth = 1
    while pos < end:
      ch = source[pos]
      if ch in STRING_QUOTE_CHARS:
        fstr = self._match_fstring_quote(source, pos, 0)
        if fstr is None:
          pos = self._skip_string(source, pos, end, len(source))
          continue
        quote, is_triple = fstr
        pos = self._fstring_body_end(source, pos, end, quote, is_triple, None, None)
        continue

      # Skip escaped character.
      if ch == BACKSLASH:
        pos += 2
        continue

      # Nested field/brace.
      if ch == OPEN_BRACE:
        depth += 1
        pos += 1
        continue

      if ch == CLOSE_BRACE:
        depth -= 1
        if depth == 0:
          return pos + 1  # Matching closing brace found.

      pos += 1
    return end

  def _has_same_quote_string(self, node, outer_quote):
    """Whether a replacement field contains a string literal reusing the outer quote. Reusing the
    quote character only became legal within a field in 3.12, so the whole field body, expression
    and format spec, is scanned for a bare outer-quote character.
    """
    source = self._source
    lines = self._lines
    if source is None or lines is None or not hasattr(node, "end_lineno") or \
       not hasattr(node, "end_col_offset"):
      return False

    src_len = len(source)
    start = self._span_offset(lines, node.lineno, node.col_offset, src_len)
    end = self._span_offset(lines, node.end_lineno, node.end_col_offset, src_len)
    if start is None or end is None or end <= start + 2:
      return False

    # Exclude the enclosing braces, bounding the scan to the field body.
    if end > start and source[end - 1] == CLOSE_BRACE:
      end -= 1

    pos = start + 1
    while pos < end:
      ch = source[pos]
      if ch == outer_quote:
        return True
      if ch in STRING_QUOTE_CHARS:
        pos = self._skip_string(source, pos, end, src_len)
        continue
      pos += 1
    return False

  def _walk_joined_strs(self, node):
    for child in ast.iter_child_nodes(node):
      if isinstance(child, ast.JoinedStr):
        yield child
      yield from self._walk_joined_strs(child)  # novermin

  def _has_pep701_backslash(self, node, lines):
    """Whether a FormattedValue expression contains a backslash (PEP 701). Before 3.12, backslashes
    were forbidden in f-string expressions.
    """
    source = self._source
    if source is None or lines is None:
      return False

    # If the expression ends on a different line than the replacement field, scan the source between
    # them for a line-continuation backslash.
    expr = node.value
    if node.end_lineno != expr.end_lineno:
      expr_line = expr.end_lineno
      expr_col = self._codepoint_col(lines, expr.end_lineno, expr.end_col_offset)
      field_line = node.end_lineno
      field_col = self._codepoint_col(lines, node.end_lineno, node.end_col_offset)
      gap_parts = []
      if expr_line - 1 < len(lines):
        gap_parts.append(lines[expr_line - 1][expr_col:])
      for line_no in range(expr_line, field_line - 1):
        if line_no < len(lines):
          gap_parts.append(lines[line_no])
      if field_line - 1 < len(lines):
        gap_parts.append(lines[field_line - 1][:field_col])
      if any(BACKSLASH in part for part in gap_parts):
        return True

    # Escape sequence in a string literal within the expression. The single-line guard makes the
    # ASCII line slice a complete and cheap check, skipping `ast.get_source_segment()`.
    if expr.lineno == expr.end_lineno:
      line = lines[expr.lineno - 1]
      lo = self._codepoint_col(lines, expr.lineno, expr.col_offset)
      hi = self._codepoint_col(lines, expr.lineno, expr.end_col_offset)
      if BACKSLASH not in line[lo:hi]:
        return False

    # Tokenize the full expression source to confirm a backslash. Only reachable on Python 3.8+
    # because that's when `ast.get_source_segment()` was added
    if hasattr(ast, "get_source_segment"):
      expr_src = ast.get_source_segment(source, expr)  # novermin
      if expr_src and BACKSLASH in expr_src:
        import tokenize as _tokenize  # novermin, pylint: disable=import-outside-toplevel
        import io as _io  # novermin, pylint: disable=import-outside-toplevel
        try:
          tokens = list(_tokenize.generate_tokens(
            _io.StringIO(expr_src).readline))
          for tok in tokens:
            if tok.type == _tokenize.STRING and BACKSLASH in tok.string:
              return True
        except _tokenize.TokenError:
          pass
    return False

  def _has_pep701_comment(self, node, lines):
    """Whether a replacement field contains a comment (PEP 701). Before 3.12, comments were
    forbidden inside f-string expressions. The parser strips them, so the region between the opening
    `{` and the top-level format spec's `:`, or the closing `}`, is scanned for `#` characters that
    are outside string literals. A `#` in the format spec itself, after the `:`, is spec filler text
    and is valid since 3.6.
    """
    source = self._source
    if source is None or lines is None or not hasattr(node, "end_lineno"):
      return False

    src_len = len(source)
    start = self._span_offset(lines, node.lineno, node.col_offset, src_len)
    if start is None:
      return False

    # Bound the scan by the format-spec `:` when present, else the closing `}`.
    spec = node.format_spec if hasattr(node, "format_spec") else None
    if spec is not None and getattr(spec, "lineno", None) is not None:
      end = self._span_offset(lines, spec.lineno, spec.col_offset, src_len)
    else:
      end = self._span_offset(lines, node.end_lineno, node.end_col_offset, src_len)
      if end is not None and end > start and source[end - 1] == CLOSE_BRACE:
        end -= 1
    if end is None or end <= start:
      return False

    # Skip the scan below when the region contains no `#` at all.
    field = source[start:end]
    if HASH not in field:
      return False

    # Scan the region for `#` outside string literals.
    field_len = len(field)
    pos = 0
    while pos < field_len:
      ch = field[pos]
      if ch in STRING_QUOTE_CHARS:
        pos = self._skip_string(source, start + pos, start + end, src_len) - start
        continue
      if ch == HASH:
        return True
      pos += 1
    return False
