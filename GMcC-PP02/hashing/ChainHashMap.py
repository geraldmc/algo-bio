#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ChainHashMap.py

from HashMap import HashMap
from TableMap import TableMap
from abc import abstractmethod

class ChainHashMap(HashMap):
  """HashMap with separate chaining"""

  def _bucket_setitem(self, j, k, v): 
    if self._table[j] is None:
      self._table[j] = TableMap() 
    oldsize = len(self._table[j])
    self._table[j][k] = v
    if len(self._table[j]) > oldsize:
      self._n += 1

  def _bucket_getitem(self, j, k): 
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error:  ' + repr(k)) # no match
    return bucket[k] # can raise KeyError

  def _bucket_delitem(self, j, k): 
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error:  ' + repr(k)) 
    del bucket[k]
    
  def __iter__(self):
    for bucket in self._table:
      if bucket is not None: 
        for key in bucket:
          yield key

  def __str__(self):
      _items = []
      for key, value in self.items():
          _items.append(f"{key!r}: {value!r}")
      return "{" + ", ".join(_items) + "}"

if __name__ == "__main__":
  """ Driver for test. Note: The operations _bucket_setitem and _bucket_getitem
  make this class abstract. 
  """
  chm = ChainHashMap(capacity=120)
  chm[0] = chm._hash_MOD(12501)
  chm[1] = chm._hash_MOD(84763)
  chm[2] = chm._hash_MOD(22599)

  for k,v in enumerate(chm):
    print('Key: {}, Value: {}'.format(k,v))

  chm._output()