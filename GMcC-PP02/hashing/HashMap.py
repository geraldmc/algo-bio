#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TableMap.py

from random import randrange
from MutableHash import MutableHash
from abc import abstractmethod

class HashMap(MutableHash):
  """Map implementation using an unordered list."""

  def __init__ (self, capacity):
    '''Create an empty hash-table map.''' 
    self._table = capacity * [ None ]
    self._n = 0         # number of current entries in the map
    self._capacity = capacity # number of possible entries in the map
    super().__init__()
    #self._prime = p     # prime for MAD compression
    #self._scale = 1 + randrange(p-1) # scale from 1 to p-1 for MAD
    #self._shift = randrange(p) # shift from 0 to p-1 for MAD

  def _hash_MOD(self, k):
    ''' Simple MOD hash'''
    MOD_VALS = [121, 127] # size of table (120) +1, or the first prime (127).
    if len(self._table) == 120:
      return hash(k) % MOD_VALS[1]
    else:
      pass # should raise an exception

  def _hash_MAD(self, k):
    '''Unused
    '''
    pass #  return (hash(k) * self._scale + self._shift) 
         # % self._prime % len(self._table)

  def __len__(self): # how many elements are present
    return self._n

  def _capacity(self): # how many slots.
    return self._capacity

  @abstractmethod
  def _bucket_setitem(self, j, k):
    pass

  @abstractmethod
  def _bucket_getitem(self, j, k, v):
    pass

  def __getitem__(self, k):
    j = self._hash_MOD(k) 
    return self._bucket_getitem(j, k) # can raise KeyError

  def __setitem__(self, k, v):
    j = self._hash_MOD(k)
    print('setting hash MOD')
    self._bucket_setitem(j, k, v)
    if self._n > len(self._table) // 2:
      self._resize(2 * len(self._table) - 1)

  def __delitem__(self, k):
    j = self._hash_MOD(k)
    self._bucket_delitem(j, k) # can raise KeyError
    self._n -= 1

  def _resize(self, capacity):
    ''' Resize bucket array to capacity'''
    old = list(self.items()) 
    self._table = self._capacity * [None] 
    self._n = 0
    for (k,v) in old:
      self[k] = v

if __name__ == "__main__":
  """ Driver for test. Note: The operations _bucket_setitem and _bucket_getitem
  make this class abstract. 
  """
  try:
    hm = HashMap()
  except TypeError:
    print('HashMap is an abstract class. You must subclass to instantiate it.')