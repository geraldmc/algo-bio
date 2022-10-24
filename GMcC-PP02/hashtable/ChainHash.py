#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ChainHash.py

from BaseHash import BaseHash 

class ChainHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    print('Executing the __insert__ method from ChainHash.')

  def output(self):
    print(self)

if __name__ == "__main__":
  """ Driver for test. 
  """
  ch = ChainHash(capacity=10)
  ch.__insert__()