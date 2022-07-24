import re
from math import floor
from functools import reduce

def reverse_range(values):
  """Yields reverse range of values: list(reverse_range([1, 2, 3])) -> [2, 1, 0]."""
  return range(len(values) - 1, -1, -1)

def dotted_name(names):
  """Returns a dotted name of a list of strings, integers, lists, and tuples."""

  # It will just return the value instead of "b.a.d" if input was "bad"!
  if isinstance(names, str):
    return names
  if isinstance(names, (int, float)):
    return str(names)

  resolved = []
  for name in names:
    if isinstance(name, str):
      resolved.append(name)
    elif isinstance(name, int):
      resolved.append(str(name))
    elif isinstance(name, (list, tuple)):
      resolved += filter(lambda x: x is not None, name)
    elif name is None:
      continue
    else:
      assert False
  return ".".join(resolved)

def float_version(f):
  """Converts a float X.Y into (X, Y)."""
  assert(not f < 0)
  major = floor(f)
  minor = int((f - major) * 10)
  return (major, minor)

class InvalidVersionException(BaseException):
  pass

def __handle_incomp_versions(list1, list2, version_refs=None):
  v1, v2 = version_strings(list1), version_strings(list2)
  t1, t2 = tuple(list1), tuple(list2)
  if version_refs is None or t1 not in version_refs or t2 not in version_refs:
    raise InvalidVersionException("Versions could not be combined: {} and {}".format(v1, v2))

  def get_ref(key):
    ref = version_refs[key]
    if len(ref) == 1:
      ref = ref[0]
    return ref
  ref1, ref2 = get_ref(t1), get_ref(t2)
  raise InvalidVersionException("{} (requires {}) vs. {} (requires {})".format(ref1, v1, ref2, v2))

def combine_versions(list1, list2, config, version_refs=None):
  assert len(list1) == len(list2)
  assert len(list1) == 2
  if not config.ignore_incomp() and\
    ((list1[0] is None and list1[1] is not None and list2[0] is not None and list2[1] is None) or
     (list1[0] is not None and list1[1] is None and list2[0] is None and list2[1] is not None)):
    __handle_incomp_versions(list1, list2, version_refs)

  res = []

  # Convert integers and floats into version tuples.
  def fixup(v):
    if isinstance(v, int):
      return (v, 0)
    if isinstance(v, float):
      return float_version(v)
    return v

  for i in range(len(list1)):
    v1 = fixup(list1[i])
    v2 = fixup(list2[i])
    if v1 is None or v2 is None:
      res.append(None)
    else:
      res.append(max(v1, v2))
  return res

def version_strings(versions, separator=None):
  """Yields version strings of versions. If one value is 0, 0.0, or (0, 0) then either one or two
values can be specified, otherwise any number is allowed. A None separator means ', '."""
  separator = separator or ", "
  amount = len(versions)
  assert(amount > 0)
  if any(v in (0, (0, 0)) for v in versions):
    assert(amount < 3)
  res = []
  for i in range(amount):
    version = versions[i]
    # When versions aren't known, show something instead of nothing. It might run with any
    # version.
    if version in (0, (0, 0)):
      res.append("~{}".format(i + 2))
    elif version is None:
      res.append("!{}".format(i + 2))
    else:
      res.append(dotted_name(version))
  return separator.join(res)

def remove_whitespace(string, extras=None):
  extras = extras or []
  return re.sub("[ \t\n\r\f\v{}]".format("".join(extras)), "", string)

def bounded_str_hash(value):
  """Computes bounded hash value of string input that isn't randomly seeded, like `hash()` does
because we need the same hash value for every program execution.
  """
  h = reduce(lambda acc, ch: acc + 29 * ord(ch), value, 13)
  return float(h % 1000000) / 1000000

LINE_COL_REGEX = re.compile(r"L(\d+)(?:\s*C(\d+))?:(.*)")

def sort_line_column(key):
  """Sorts line and column numbers of input texts with format "LX[ CY]: ..". In order to
consistently sort texts of same line/column but with different subtext, the subtext is hashed and
included in the value. Text without line/column numbers is still hashed and thought of as having
line number 0. This function can be used with `list.sort(key=sort_line_column)`.
  """
  m = LINE_COL_REGEX.match(key)
  if not m:
    return bounded_str_hash(key)
  line = int(m.group(1))
  col = m.group(2)
  h = bounded_str_hash(m.group(3)) / 1000
  if col is None:
    return line + h
  return line + float(col) / 1000 + h

LINE_COL_PARSABLE_REGEX = re.compile(r"(?:.*?):(\d+):(\d*):(.*)")

def sort_line_column_parsable(key):
  m = LINE_COL_PARSABLE_REGEX.match(key)
  if not m:
    return bounded_str_hash(key)
  line = int(m.group(1))
  col = m.group(2)
  if len(col) == 0:
    col = 0
  h = bounded_str_hash(m.group(3)) / 1000
  if col == 0:
    return line + h
  return line + float(col) / 1000 + h

def format_title_descs(pairs, titles, indent=0):
  res = []
  longest = len(max(titles, key=len))
  for (name, desc) in pairs:
    title = "{}{:{fill}} - ".format(" " * indent, name, fill=longest)
    first_line = desc[0]
    res.append("{}{}".format(title, first_line))
    if len(desc) > 1:
      for line in desc[1:]:
        res.append("{}{}".format(" " * len(title), line))
  return "\n".join(res)

TARGETS_SPLIT = re.compile("[\\.,]")

def parse_target(target):
  exact = True
  if target.endswith("-"):
    exact = False
    target = target[:-1]

  # Parse target as a tuple separated by either commas or dots, which preserves support for old
  # float-number inputs.
  elms = TARGETS_SPLIT.split(target)
  if len(elms) != 1 and len(elms) != 2:
    return None

  for h in range(len(elms)):
    try:
      n = int(elms[h])
      if n < 0:
        return None
      elms[h] = n
    except ValueError:
      return None

  # When only specifying major version, use zero as minor.
  if len(elms) == 1:
    elms.append(0)

  elms = tuple(elms)
  if not ((2, 0) <= elms < (4, 0)):
    return None

  return (exact, elms)
