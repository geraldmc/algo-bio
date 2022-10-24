# BaseHash.py
from abc import ABC, abstractmethod
from typing import NamedTuple, Any

class BaseHash(ABC):

  def __init__(self, capacity):
      self.pairs = capacity * [None]

  def __len__(self):
      return len(self.pairs)

  def __delitem__(self, key):
      if key in self:
          self.pairs[self._index(key)] = None
      else:
          raise KeyError(key)

  def __setitem__(self, key, value):
      self.pairs[self._index(key)] = Pair(key, value)

  def __getitem__(self, key):
      pair = self.pairs[self._index(key)]
      if pair is None:
          raise KeyError(key)
      return pair.value

  def __contains__(self, key):
      try:
          self[key]
      except KeyError:
          return False
      else:
          return True

  def get(self, key, default=None):
      try:
          return self[key]
      except KeyError:
          return default

  def __str__(self):
      pairs = []
      for key, value in self.pairs:
          pairs.append(f"{key!r}: {value!r}")
      return "{" + ", ".join(pairs) + "}"

  def _index(self, key):
      return hash(key) % len(self)

  @abstractmethod
  def __insert__(self):
      pass
  
  @classmethod
  def from_dict(cls, dictionary, capacity=None):
      hash_table = cls(capacity or len(dictionary))
      for key, value in dictionary.items():
          hash_table[key] = value
      return hash_table

class Pair(NamedTuple):
    key: Any
    value: Any