from collections import defaultdict

def multidict(values):
  d = defaultdict(set)
  for k, v in values:
    d[k].add(v)
  return d
