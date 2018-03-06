#!/usr/bin/env python
from vermin import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS
(mods, kwargs, dirs) = (len(MOD_REQS), len(KWARGS_REQS), len(STRFTIME_REQS))
mems = 0
for v in MOD_MEM_REQS.values():
  mems += len(v)
print("Rules:\n{:>4} modules\n{:>4} members\n{:>4} kwargs\n{:>4} strftime directives\n{:>4} total".
      format(mods, mems, kwargs, dirs, mods + mems + kwargs + dirs))
