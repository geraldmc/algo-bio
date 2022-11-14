#!/usr/bin/env python
# -*- coding: utf-8 -*-

# QuadraticProbing.py
# in state list: 1 means occupied, 0 means empty and -1 means deleted

class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class QuadraticProbing:
  def __init__(self, hash_method=1, modulus=120, slot_size=120, 
               slot_depth=1, load_factor=1.00):
    self.items_count = 0
    self.load_factor = load_factor
    self.modulus = modulus
    self.slot_size = slot_size
    self.slot_depth = slot_depth
    if self.slot_depth>1: # either 1 or 3 for this assignment
      self.table = [[None for i in range(slot_depth)] for _ in range(slot_size)]
      self.state = [[0 for i in range(slot_depth)] for _ in range(slot_size)]
    else:
      self.table = [None] * slot_size
      self.state = [0] * slot_size
    self.hash_method = hash_method
    self.first_collisions = 0
    self.second_collisions = 0

  def hash_func_mod(self, key, slot_size=None):
    if self.modulus not in [120, 113, 41]:
      raise ValueError('Modulus value is limited to 120, 113, 41.')
    if not slot_size: slot_size = len(self.table)
    return key % self.modulus

  def hash_func(self, key):
    import math
    if self.modulus not in [120, 113, 41]:
      raise ValueError('Modulus value is limited to 120, 113, 41.')
    if not self.slot_size:  self.slot_size = len(self.table)
    if self.hash_method==1:
      return key % self.modulus # simple modulus
    elif self.hash_method==2:
      return math.floor(self.slot_size*(key*0.357840 % 1)) # multiplicative
    
  def __rehash(self):
    new_table = [None] * len(self.table) * 2
    new_state = [0] * len(self.table) * 2
    for bucket in self.table:
      if not bucket: continue
      self.__insert(bucket, new_table, new_state)
    return new_table, new_state

  def __insert(self, key, table=None, state=None):
    if not table: table = self.table
    if not state: state = self.state
    index, h = self.hash_func(key), 1
    while self.state[index] == 1:
      index = (index + h * h) % self.modulus # quadratic probing
      h += 1
    table[index], state[index] = key, 1
    
  def insert(self, key):
    self.items_count += 1
    load_factor = self.items_count / len(self.table)
    if load_factor > self.load_factor:
      self.table, self.state = self.__rehash()
      self.load_factor = load_factor
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

  def collision_count(self, keys):
    ''' Return count of all collisions
    '''
    hashed_items = []
    for k in keys:
      hashed_items.append(self.hash_func_mod(k))
    unique = set(hashed_items)
    return len(hashed_items)-len(unique) # diff of

  @property
  def slots_remaining(self):
    if self.slot_depth>1:
      return len(self.table)*self.slot_depth - self.items_count
    else:
      return len(self.table) - self.items_count

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

  # Testing ----------------------------------------------------------------

  qdp = QuadraticProbing()
  for k in data:
    qdp.insert(k)

    # Quick tests
  if qdp.modulus == 120:
    assert qdp.collision_count(data) == 17
  elif qdp.modulus == 113:
    assert qdp.collision_count(data) == 14
  elif qdp.modulus == 41:
    assert qdp.collision_count(data) == 27

  assert qdp.hash_func(55555) == 115

  if qdp.slot_size ==120:
    assert qdp.slots_remaining == 60
    assert qdp.state[115] == 1
    assert qdp.state[60] == 0
    assert qdp.state[61] == 0