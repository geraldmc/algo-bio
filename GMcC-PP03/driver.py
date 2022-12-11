#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
from analysis.metrics import *
from filehandler.io import *

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 3"
__class__       = "605.620"
__semester__    = "Fall, 2022"

def lcs(s1, s2):
  matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
  for i in range(len(s1)):
    for j in range(len(s2)):
      if s1[i] == s2[j]:
        if i == 0 or j == 0:
          matrix[i][j] = s1[i]
        else:
          matrix[i][j] = matrix[i-1][j-1] + s1[i]
      else:
        matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

  cs = matrix[-1][-1]

  return len(cs), cs

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser(description='Exercise in longest common subsequence.')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-file', action="store_true",
                      help='provide a path to a file containing sequence input.')
  args = parser.parse_args()
  
  print(lcs("abcdaf", "acbcf")) 