from .config import Config

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

class InvalidVersionException(BaseException):
  pass

def combine_versions(list1, list2):
  assert len(list1) == len(list2)
  assert len(list1) == 2
  if not Config.get().ignore_incomp() and\
    ((list1[0] is None and list1[1] is not None and list2[0] is not None and list2[1] is None) or
     (list1[0] is not None and list1[1] is None and list2[0] is None and list2[1] is not None)):
    raise InvalidVersionException("Versions could not be combined: {} and {}".format(list1, list2))
  res = []
  for i in range(len(list1)):
    v1 = list1[i]
    v2 = list2[i]
    if v1 is 0 and v2 is 0:
      res.append(0)
    elif v1 is 0:
      res.append(v2)
    elif v2 is 0:
      res.append(v1)
    elif v1 is None or v2 is None:
      res.append(None)
    else:
      res.append(max(v1, v2))
  return res
