#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LinearProbing.py

class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class LinearProbing:
  '''Collision handling via linear probing.
  When a collision occurs, we add one to the hash function,
  and check to see if the location is free. State list key is:
  1 = occupied, 0 = empty and -1 = deleted
  '''
  def __init__(self, modulus=120, slot_size=120, slot_depth=1, load_factor=1.00):
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
    self.first_collisions = 0
    self.second_collisions = 0

  def hash_func_mod(self, key, slot_size=None):
    if self.modulus not in [120, 113, 41]:
      raise ValueError('Modulus value is limited to 120, 113, 41.')
    if not slot_size: slot_size = len(self.table)
    return key % self.modulus
  
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
    index = self.hash_func_mod(key)
    while self.state[index] == 1:
      index = (index + 1) % len(self.table) # probe
    table[index], state[index] = key, 1
  
  def insert(self, key):
    self.items_count += 1
    load_factor = self.items_count / len(self.table)
    if load_factor > self.load_factor:
      self.table, self.state = self.__rehash()
      self.load_factor = load_factor
    self.__insert(key)

  def search(self, key):
    index = self.hash_func_mod(key)
    while (self.table[index] != key or self.state[index] == -1) and \
        self.state[index] == 1:
      index = (index + 1) % self.modulus
    if self.table[index] == key:
      return index
    return -1

  def delete(self, key):
    index = self.search(key)
    if index > -1:
      self.state[index] = -1
 
  def collision_count(self, keys):
    ''' Return count of possible collisions
    '''
    hashed_items = []
    for k in keys:
      hashed_items.append(self.hash_func_mod(k))
    unique = set(hashed_items)
    return len(hashed_items)-len(unique) # diff=collisions

  @property
  def slots_remaining(self):
    ''' Used in chaining'''
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
  ht = LinearProbing(modulus=41)

  for k in data:
    ht.insert(k)

  # Quick tests
  if ht.modulus == 120:
    assert ht.collision_count(data) == 17
  elif ht.modulus == 113:
    assert ht.collision_count(data) == 14
  elif ht.modulus == 41:
    assert ht.collision_count(data) == 27
  
  if ht.slot_size ==120:
    assert ht.slots_remaining == 60
    assert ht.table[61] == None
    assert ht.state[60] == 0
    assert ht.state[61] == 0

  ht = LinearProbing() #  modulus = 120
  assert ht.hash_func_mod(55555) == 115
  assert ht.state[115] == 0
  ht.insert(55555)
  assert ht.state[115] == 1
  ht.delete(55555)
  assert ht.state[115] == -1

  print('Good!')

  #print(ht.slots_remaining)
  #for k in keys:
  #  ht.insert(k)
  #print(ht.slots_remaining)

  #      pairs = []
  #      for idx in range(self.slot_size):
  #       pairs.append(self.slots[self.hash_func(key)][idx])