#!/usr/bin/env python
from vermin import Config, MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS, BYTES_REQS,\
  ARRAY_TYPECODE_REQS, CODECS_ERROR_HANDLERS, CODECS_ENCODINGS, BUILTIN_GENERIC_ANNOTATION_TYPES,\
  DICT_UNION_SUPPORTED_TYPES, DICT_UNION_MERGE_SUPPORTED_TYPES, DECORATOR_USER_FUNCTIONS
config = Config()
(mods, mems, kwargs, dirs, bdirs, typecodes, codecshandlers, codecsencs, builtinanntypes,
 dictuniontypes, dictunionmergetypes, decouserfuncs) =\
  (len(MOD_REQS(config)), len(MOD_MEM_REQS(config)), len(KWARGS_REQS), len(STRFTIME_REQS),
   len(BYTES_REQS), len(ARRAY_TYPECODE_REQS), len(CODECS_ERROR_HANDLERS), len(CODECS_ENCODINGS),
   len(BUILTIN_GENERIC_ANNOTATION_TYPES), len(DICT_UNION_SUPPORTED_TYPES),
   len(DICT_UNION_MERGE_SUPPORTED_TYPES), len(DECORATOR_USER_FUNCTIONS))
print("Rules:\n{:>4} modules\n{:>4} members\n{:>4} kwargs\n{:>4} strftime directives\n{:>4} bytes "
      "format directives\n{:>4} array typecodes\n{:>4} codecs error handlers\n{:>4} codecs "
      "encodings\n{:>4} builtin generic annotation types\n{:>4} builtin dict union types\n{:>4} "
      "builtin dict union merge types\n{:>4} user function decorators\n{:>4} total".
      format(mods, mems, kwargs, dirs, bdirs, typecodes, codecshandlers, codecsencs,
             builtinanntypes, dictuniontypes, dictunionmergetypes, decouserfuncs,
             mods + mems + kwargs + dirs + bdirs + typecodes + codecshandlers + codecsencs +
             builtinanntypes + dictuniontypes + dictunionmergetypes + decouserfuncs))
