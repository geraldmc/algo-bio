#!/usr/bin/env python
# -*- coding: utf-8 -*-

# QuadHash.py

#from hashtable.BaseHash import BaseHash 

class QuadHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    pass

  def output(self):
    print("printing from Quadhash...")

if __name__ == "__main__":
  """ Driver for debugging. 
  """
  from .BaseHash import BaseHash
  pass