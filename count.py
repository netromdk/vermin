#!/usr/bin/env python
from vermin import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS, ARRAY_TYPECODE_REQS,\
  CODECS_ERROR_HANDLERS, CODECS_ENCODINGS
(mods, mems, kwargs, dirs, typecodes, codecshandlers, codecsencs) =\
  (len(MOD_REQS), len(MOD_MEM_REQS), len(KWARGS_REQS), len(STRFTIME_REQS),
   len(ARRAY_TYPECODE_REQS), len(CODECS_ERROR_HANDLERS), len(CODECS_ENCODINGS))
print("Rules:\n{:>4} modules\n{:>4} members\n{:>4} kwargs\n{:>4} strftime directives\n{:>4} array"
      " typecodes\n{:>4} codecs error handlers\n{:>4} codecs encodings\n{:>4} total".
      format(mods, mems, kwargs, dirs, typecodes, codecshandlers, codecsencs,
             mods + mems + kwargs + dirs + typecodes + codecshandlers + codecsencs))
