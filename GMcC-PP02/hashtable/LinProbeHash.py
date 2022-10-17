#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LinProbeHash.py

from hashtable.BaseHash import BaseHash 

class LinProbeHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    pass

  def output(self):
    print("printing from LinProbeHash...")

  if __name__ == "__main__":
    """ Driver for debugging. 
    """
    pass