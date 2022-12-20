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

RUN_ALL = True

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
# Compare every element (sequence) to every other element (sequence), once. 
# Compare order (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
  print('NOTE: The recursive LCS1 function runs very slowly on sequences longer than')
  print('18 characters. It is run on generated test data specific to it, not on the ')
  print('provided test data (for time considerations).')
  print()
  time.sleep(6)  
  print('Running LCS2 on provided data...')
  print()
  for s1, s2 in itertools.combinations(sequences, 2):
    LCS2(s1, s2)
  print()
  print('Running LCS3 on provided data...')
  print()
  for s1, s2 in itertools.combinations(sequences, 2):
    LCS3(s1, s2)
  print()
  print('------------------------generated---------------------------')
  print()

if RUN_ALL:
  # Run generated DNA string comparisons
    idx1 = [5, 6, 7, 8, 9] #,10,11,12,13,14,15,16,17,19,20]
    idx2 = [2728,3004,3280,3556] #,3832,4108,4384,4660,4936,5212,5488,5764,6040,6316,6592]

    print('Running LCS1 on generated data...')
    print()
    for i in idx1:
        S1 = dna_str(i) # generate a random ACTG string of length i.
        S2 = dna_str(i)
        LCS1(S1, S2)
    print()
    print('Running LCS2 on generated data...')
    print()
    for i in idx2:
        S1 = dna_str(i)
        S2 = dna_str(i)
        LCS2(S1, S2)
    print()    
    print('Running LCS3 on generated data...')
    print()
    for i in idx2:
        S1 = dna_str(i)
        S2 = dna_str(i)
        LCS3(S1, S2)
    print()
    print('--------------------------fin-------------------------------')
    print()