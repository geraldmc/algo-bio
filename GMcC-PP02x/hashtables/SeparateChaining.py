#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SeparateChaining.py
# in state list: 1 means occupied, 0 means empty and -1 means deleted

class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class SeparateChaining:
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

  # insertion:
  def __insert_last(self, index, key):
    new_node = Node(key)
    if not self.table[index]:
      self.table[index] = new_node
      return
    current = self.table[index]
    while current.next:
      current = current.next
    current.next = new_node

  def __rehash(self):
    new_table = [None] * (self.slot_size * 2)
    for bucket in self.table:
      if not bucket: continue
      index = self.hash_func_mod(bucket.key, len(new_table))
      new_table[index] = bucket
    return new_table
    
  def insert(self, key):
    self.items_count += 1
    load_factor = self.items_count / self.slot_size
    if load_factor > self.load_factor:
      self.table = self.__rehash()
      self.slot_size *= 2
      self.load_factor = self.items_count /self.slot_size
    index = self.hash_func_mod(key)
    self.__insert_last(index, key)

  # search:
  def find(self, key):
    index = self.hash_func_mod(key)
    current = self.table[index]
    while current or current.key != key:
      current = current.next
    if not current:
      raise Exception(f"key = {key} doesn't exist in the list")
    return current.key

  # remove:
  def __remove(self, index, key):
    if not self.table[index]:
      raise Exception(f"List is Empty!! key = {key} doesn't exist in the list")

    if self.table[index].key == key:
      self.table[index] = self.table[index].next
      return
    current, previous = self.table[index], self.table[index]
    while current and current.next != key:
      previous, current = current, current.next

    if not current:
      raise Exception(f"key = {key} doesn't exist in the list")
    previous.next = current.next

  def remove(self, key):
    index = self.hash_func_mod(key)
    self.__remove(index, key)

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
  """ Driver for debugging. 
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

  # Tests ----------------------------------------------------------------

  sch = SeparateChaining(modulus=41)
  for k in data:
    sch.insert(k)

  if sch.modulus == 120:
    assert sch.collision_count(data) == 17
  elif sch.hash_func_mod == 113:
    assert sch.collision_count(data) == 14
  elif sch.hash_func_mod == 41:
    assert sch.collision_count(data) == 27