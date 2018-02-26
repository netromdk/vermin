#!/usr/bin/env python
from minpy import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS
(mods, mems, kwargs) = (len(MOD_REQS), len(MOD_MEM_REQS), len(KWARGS_REQS))
print("{:>4} modules\n{:>4} members\n{:>4} kwargs\n{:>4} total".
      format(mods, mems, kwargs, mods + mems + kwargs))
