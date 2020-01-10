import json
from os.path import abspath

class FreqEntry:
  def __init__(self):
    self.__count = 0          # Frequency count.
    self.__triggered = False  # Whether triggered via rule.

  def count(self):
    return self.__count

  def inc(self):
    self.__count += 1

  def triggered(self):
    return self.__triggered

  def trigger(self):
    self.__triggered = True

  def unite(self, entry):
    self.__count += entry.count()
    self.__triggered |= entry.triggered()

  def data(self):
    return (self.count(), self.triggered())

class Frequencies:
  def __init__(self):
    self.__members = dict()
    self.__kwargs = dict()
    self.__strftime_dirs = dict()
    self.__array_typecodes = dict()
    self.__codecs_error_handlers = dict()
    self.__codecs_encodings = dict()

  def members(self):
    return self.__members

  def kwargs(self):
    return self.__kwargs

  def strftime_directives(self):
    return self.__strftime_dirs

  def array_typecodes(self):
    return self.__array_typecodes

  def codecs_error_handlers(self):
    return self.__codecs_error_handlers

  def codecs_encodings(self):
    return self.__codecs_encodings

  def data(self):
    return {
      "members": self.__entries_data(self.__members),
      "kwargs": self.__entries_data(self.__kwargs),
      "strftime_dirs": self.__entries_data(self.__strftime_dirs),
      "array_typecodes": self.__entries_data(self.__array_typecodes),
      "codecs_error_handlers": self.__entries_data(self.__codecs_error_handlers),
      "codecs_encodings": self.__entries_data(self.__codecs_encodings),
    }

  def unite(self, freq):
    self.__unite_dict(self.__members, freq.members())
    self.__unite_dict(self.__kwargs, freq.kwargs())
    self.__unite_dict(self.__strftime_dirs, freq.strftime_directives())
    self.__unite_dict(self.__array_typecodes, freq.array_typecodes())
    self.__unite_dict(self.__codecs_error_handlers, freq.codecs_error_handlers())
    self.__unite_dict(self.__codecs_encodings, freq.codecs_encodings())

  def record_member(self, member):
    self.__inc(self.__members, member)

  def trigger_member(self, member):
    self.__trigger(self.__members, member)

  def record_kwarg(self, kwarg):
    self.__inc(self.__kwargs, self.__kwarg_str(kwarg))

  def trigger_kwarg(self, kwarg):
    self.__trigger(self.__kwargs, self.__kwarg_str(kwarg))

  def record_strftime_directive(self, directive):
    self.__inc(self.__strftime_dirs, directive)

  def trigger_strftime_directive(self, directive):
    self.__trigger(self.__strftime_dirs, directive)

  def record_array_typecode(self, typecode):
    self.__inc(self.__array_typecodes, typecode)

  def trigger_array_typecode(self, typecode):
    self.__trigger(self.__array_typecodes, typecode)

  def record_codecs_error_handler(self, handler):
    self.__inc(self.__codecs_error_handlers, handler)

  def trigger_codecs_error_handler(self, handler):
    self.__trigger(self.__codecs_error_handlers, handler)

  def record_codecs_encoding(self, encoding):
    self.__inc(self.__codecs_encodings, encoding)

  def trigger_codecs_encoding(self, encoding):
    self.__trigger(self.__codecs_encodings, encoding)

  def save(self, path):
    with open(path, mode="w+") as fp:
      print("Writing frequencies to {}".format(abspath(path)))
      json.dump(self.data(), fp, sort_keys=True)

  def __prepare_entry(self, dictionary, key):
    dictionary.setdefault(key, FreqEntry())

  def __inc(self, dictionary, value):
    self.__prepare_entry(dictionary, value)
    dictionary[value].inc()

  def __trigger(self, dictionary, value):
    self.__prepare_entry(dictionary, value)
    dictionary[value].trigger()

  def __entries_data(self, dictionary):
    res = {}
    for key in dictionary:
      res[key] = dictionary[key].data()
    return res

  def __kwarg_str(self, kwarg):
    return "{}({})".format(kwarg[0], kwarg[1])

  def __unite_dict(self, ours, theirs):
    for key in theirs:
      entry = theirs[key]
      if key in ours:
        ours[key].unite(entry)
      else:
        ours[key] = entry
