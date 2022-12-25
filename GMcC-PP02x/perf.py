#!/usr/bin/env python
# -*- coding: utf-8 -*-

# perf.py

from analysis.metrics import *
from hashtables.LinearProbing import LinearProbing
from hashtables.QuadraticProbing import QuadraticProbing
from hashtables.SeparateChaining import SeparateChaining
from filehandler.io import pre_process

if __name__ == "__main__":
  """ Driver 
  """
  import sys
  import os
  # required to manage relative imports for testing
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))

  data = []
  data_path = './data/Extra.txt'
  raw_input = pre_process(data_path)
  for s in raw_input:
    data.append([int(i) for i in s]) # convert to ints  
  data = [item for sub in data for item in sub]

  ht = LinearProbing(hash_method=2, slot_depth=2, slot_size=120)
  
  plot(distribute(data, hash_function=ht, num_containers=12))