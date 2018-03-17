def reverse_range(object):
  """Yields reverse range of object: list(reverse_range([1, 2, 3])) -> [2, 1, 0]."""
  return range(len(object) - 1, -1, -1)

def dotted_name(names):
  """Returns a dotted name of a list of strings, integers, lists, and tuples."""

  # It will just return the value instead of "b.a.d" if input was "bad"!
  if isinstance(names, str):
    return names

  resolved = []
  for name in names:
    if isinstance(name, str):
      resolved.append(name)
    elif isinstance(name, int):
      resolved.append(str(name))
    elif isinstance(name, list) or isinstance(name, tuple):
      resolved += name
    else:
      assert False
  return ".".join(resolved)
