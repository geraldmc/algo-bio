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
    print()
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

# Run the base DNA string comparison from the supplied input file --------------
# Compare every element (sequence) to every other element (sequence), only once. 
# Compare order (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
  for s1, s2 in itertools.combinations(sequences, 2):
    print_LCS(s1, s2, LCS3(s1, s2))

# Run generated DNA string comparisons -------------------------------------
# NOTE: Don't try recursive solution here (no LCS1)!
  idx1 =  [212, 2980, 5959, 8938, 11916, 14895, 17874, 20853, 23831, 26810, 29789, 32768]
  idx2 =  [2980, 5959, 8938, 11916, 14895, 17874, 20853, 23831, 26810, 29789, 32768]
  idx3 =  [5959,11375,16791,22207,27623,33039,38455,43871,49287,54703,60119,65536]
  for i in idx1:
      S1 = dna_str(i)
      S2 = dna_str(i)
      LCS2(S1, S2)
