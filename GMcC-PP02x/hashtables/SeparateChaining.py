#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SeparateChaining.py

class Node:
  ''' Node class is required for chaining within table. '''
  def __init__(self, key):
    self.key = key
    self.next = None

  def __repr__(self):
    return str(self.key)

class SeparateChaining:
  ''' '''
  def __init__(self, modulus=120, slot_size=120, slot_depth=1):
    if slot_depth > 1:
      raise ValueError('Only single bucket size allowed.')
    if slot_size != 120:
      raise ValueError('Slot size must be 120.')
    self.items_count = 0
    self.modulus = modulus
    self.slot_size = slot_size
    self.slot_depth = slot_depth
    self.table = [None] * slot_size
    self.first_collisions = 0
    self.second_collisions = 0

  def hash_func(self, key, slot_size=None):
    if self.modulus not in [120, 113]:
      raise ValueError('Modulus value limited to 120, 113.')
    if not slot_size: slot_size = len(self.table)
    return key % self.modulus

  def __insert_last(self, index, key):
    ''' Always insert new nodes following next.
    '''
    new_node = Node(key)
    if not self.table[index]:
      self.table[index] = new_node
      return
    current = self.table[index]
    while current.next:
      current = current.next
    current.next = new_node
    
  def insert(self, key):
    self.items_count += 1
    load_factor = self.items_count / len(self.table)
    if self.slots_remaining == -1:
      raise IndexError('Table is full. Enable rehashing?') 
    #if load_factor > self.load_factor:
    #  self.table = self.__rehash()
    #  self.slot_size *= 2
    #  self.load_factor = self.items_count /self.slot_size
    index = self.hash_func(key)
    self.__insert_last(index, key)

  def find(self, key):
    index = self.hash_func_mod(key)
    current = self.table[index]
    while current or current.key != key:
      current = current.next
    if not current:
      raise Exception(f"key = {key} doesn't exist in the list")
    return current.key

  def __remove(self, index, key):
    if not self.table[index]:
      raise Exception(f"List is Empty. key = {key} doesn't exist.")
    if self.table[index].key == key:
      self.table[index] = self.table[index].next
      return
    current, previous = self.table[index], self.table[index]
    while current and current.next != key:
      previous, current = current, current.next

    if not current:
      raise Exception(f"Key = {key} doesn't exist.")
    previous.next = current.next

  def remove(self, key):
    index = self.hash_func(key)
    self.__remove(index, key)

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
    return len(self.table) - self.items_count

  def __rehash(self):
    ''' NOT CURRENTLY IN USE'''
    new_table = [None] * (self.slot_size * 2)
    for bucket in self.table:
  #    if not bucket: continue
      index = self.hash_func_mod(bucket.key, len(new_table))
      new_table[index] = bucket
    return new_table

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

  sch = SeparateChaining(modulus=113)
  for k in data:
    sch.insert(k)