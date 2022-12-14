#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
import itertools
from analysis.metrics import *
from filehandler.io import *
from algos.algorithms import *

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 3"
__class__       = "605.620"
__semester__    = "Fall, 2022"

def default():
  # Support file input.
  try:
    inp = input("Enter file input path: ")
  except (FileNotFoundError, IsADirectoryError):
    print('File not found.')
  return (inp.strip())

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser(description='Exercise in longest common subsequence.')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-file', action="store_true",
                      help='provide a path to a file containing sequences.')
  args = parser.parse_args()

  if args.file: # the default path
    inp = default()
    seq_input = pre_process(inp)
  
  sequences = []
  for k in list(seq_input.keys()):
    sequences.append(seq_input[k])

# Compare every element (sequence) to every other element (sequence), only once. 
# Compare order (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
  for s1, s2 in itertools.combinations(sequences, 2):
    print(LCS2(s1, s2))

