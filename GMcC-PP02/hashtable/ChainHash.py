#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ChainHash.py

from hashtable.BaseHash import BaseHash 

class ChainHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    pass

  def output(self):
    print("printing from ChainHash...")

if __name__ == "__main__":
  """ Driver for debugging. 
  """
  pass