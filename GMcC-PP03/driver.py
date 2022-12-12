#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
from analysis.metrics import *
from filehandler.io import *
from algos.algorithms import *

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 3"
__class__       = "605.620"
__semester__    = "Fall, 2022"

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser(description='Exercise in longest common subsequence.')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-file', action="store_true",
                      help='provide a path to a file containing sequence input.')
  args = parser.parse_args()

  S1 = 'ACCGGTCGACTGCGCGGAAGCCGGCCGAA'
  S2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
  S3 = 'ATTGCATTGCATGGGCGCGATGCATTTGGTTAATTCCTCG'
  S4 = 'CTTGCTTAAATGTGCA'
  
  sequences = [S1, S2, S3, S4]
  for idx, seq in enumerate(sequences):
    print(LCS1(S1, S2)) 
    print(LCS2(S1, S2)) 