import json
from os.path import abspath

class Frequencies:
  def __init__(self):
    self.reset()

  def reset(self):
    self.__members = dict()

  def data(self):
    return {
      "members": self.__members
    }

  def unite(self, freq):
    other_data = freq.data()
    for mem in other_data["members"]:
      count = other_data["members"][mem]
      if mem in self.__members:
        self.__members[mem] += count
      else:
        self.__members[mem] = count

  def record_member(self, member):
    self.__inc(self.__members, member)

  def save(self, path):
    with open(path, mode="w+") as fp:
      print("Writing frequencies to {}".format(abspath(path)))
      json.dump(self.data(), fp, indent=2, sort_keys=True)

  def __inc(self, dictionary, value):
    if value not in dictionary:
      dictionary[value] = 0
    dictionary[value] += 1
