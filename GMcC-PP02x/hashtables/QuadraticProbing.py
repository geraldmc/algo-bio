#!/usr/bin/env python
# -*- coding: utf-8 -*-

# QuadraticProbing.py
__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

class QuadraticProbing:
  ''' Collision handling via quadratic probing.
     State key: 1 = occupied, 0 = empty and -1 = deleted
  '''
  def __init__(self, hash_method=1, modulus=120, slot_size=120, 
               slot_depth=1):
    self.items_count = 0
    self.modulus = modulus
    self.slot_size = slot_size
    self.slot_depth = slot_depth
    if self.slot_depth>1: # either 1 or 3
      self.table = [[None for i in range(slot_depth)] for _ in range(slot_size)]
      self.state = [[0 for i in range(slot_depth)] for _ in range(slot_size)]
      self.slot_size = self.slot_size*self.slot_depth
    else:
      self.table = [None] * slot_size
      self.state = [0] * slot_size
    self.hash_method = hash_method
    self.collisions = 0

  def hash_func(self, key):
    import math
    if self.modulus not in [120, 113, 41]:
      raise ValueError('Modulus value is limited to 120, 113, 41.')
    if not self.slot_size:  self.slot_size = len(self.table)
    if self.hash_method==1: # simple division hashing
      return key % self.modulus
    elif self.hash_method==2: # multiplicative hashing
      return math.floor(self.slot_size*(key*0.357840 % 1)) 

  def quadratic(self, index, table):
    ''' '''
    found = False
    # the limit variable restricts function from entering an infinite loop
    limit = len(table)-5
    i = 1
    while i <= limit:
      # quadratically probe
      newIndex = index + (i**2)
      newIndex = newIndex % self.slot_size
      # if newIndex is available then break
      if table[newIndex] == 0:
        found = True
        break
      else:
        # as the position is not empty increase i
        i += 1
    return newIndex

  def __insert(self, key, table=None, state=None):
    if not table: table = self.table
    if not state: state = self.state
    if self.slot_depth>1:
      index, h = self.hash_func(key), 1
      table = self.flatten(self.table)
      state = self.flatten(self.state)
      while state[index] == 1: # occupied
        self.collisions += 1 
        index = self.quadratic(index, state)
      table[index], state[index] = key, 1
      self.table = self.unflatten(table, self.slot_depth)
      self.state = self.unflatten(state, self.slot_depth)
    else:
      index, h = self.hash_func(key), 1
      while self.state[index] == 1: # occupied
        self.collisions += 1 
        index = self.quadratic(index, self.state)
      table[index], state[index] = key, 1

  def insert(self, key):
    self.items_count += 1
    load_factor = self.items_count / len(self.table)
    if self.slots_remaining == -1:
      raise IndexError('Table is full. Enable rehashing?') 
      # REHASH AND EXPAND TABLE, DISABLED.
      #if load_factor > self.load_factor:
      #  self.table, self.state = self.__rehash()
      #  self.load_factor = load_factor
    else:
      self.__insert(key)

  def search(self, key):
    index, h = self.hash_func(key), 1
    while (self.table[index] != key or \
      self.state[index] == -1) and \
        self.state[index] == 1:
      index = (index + h * h) % self.modulus
      h += 1
    if self.table[index] == key:
      return index
    return -1

  def delete(self, key):
    index = self.search(key)
    if index > -1:
      self.state[index] = -1

  def flatten(self, arr):
    ''' Convert a multi-dimensional array to single dimension'''
    return [item for sub in arr for item in sub]

  def unflatten(self, arr, cols):
    ''' Convert a single dimension array to multi-dimensional.'''
    return [arr[i:i + cols] for i in range(0, len(arr), cols)]

  def collision_count(self, keys):
    ''' Return count of all collisions
    '''
    hashed_items = []
    for k in keys:
      hashed_items.append(self.hash_func(k))
    unique = set(hashed_items)
    return len(hashed_items)-len(unique) # diff of

  @property
  def slots_remaining(self):
    if self.slot_depth>1:
      return len(self.table)*self.slot_depth - self.items_count
    else:
      return len(self.table) - self.items_count

  @property
  def load_factor(self):
    if self.slot_depth>1:
      return round(1-self.slots_remaining/len(self.table)/self.slot_depth,3)
    else:
      return round(1 - self.slots_remaining/len(self.table), 3)

  def __rehash(self):
    ''' NOT CURRENTLY IN USE'''
    new_table = [None] * len(self.table) * 2
    new_state = [0] * len(self.table) * 2
    for bucket in self.table:
      if not bucket: continue
      self.__insert(bucket, new_table, new_state)
    return new_table, new_state

if __name__ == "__main__":
  """ Driver 
  """
  import sys
  import os
  # required to manage relative imports for testing
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))

  from filehandler import io

  data = []
  data_path = '../data/Input.txt'
  raw_input = io.pre_process(data_path)
  for s in raw_input:
    data.append([int(i) for i in s]) # convert to ints  
  data = [item for sub in data for item in sub]

  qdp = QuadraticProbing()
  for k in data:
    qdp.insert(k)