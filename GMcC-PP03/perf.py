#!/usr/bin/env python
# -*- coding: utf-8 -*-

# perf.py

from analysis.metrics import *

if __name__ == "__main__":
  """ Driver 
  """
  import sys
  import os
  # required to manage relative imports for testing
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))

  data = []
  data_path = './data/Input.txt'