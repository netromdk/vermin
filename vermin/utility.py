def reverse_range(object):
  """Yields reverse range of object: list(reverse_range([1, 2, 3])) -> [2, 1, 0]."""
  return range(len(object) - 1, -1, -1)
