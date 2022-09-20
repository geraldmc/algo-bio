#!/usr/bin/env python

"""Create random integer matrices."""

# Core Library modules
import random

random.seed(1234)

def create_random_matrix(n, limit):
  """Create a square matrix using randomly generated positive integers.
     The variable 'n' is the order of the matrix.
     The variable 'limit' is the range of positive integers used.
  """
  assert type(n) is int and n > 0 and n < 100
  matrix = []
  for i in range(n):
      matrix.append([random.randint(0, limit) for el in range(n)])
  return matrix

def save_matrix(A, B, filename):
  """FIXME
  """
  f = open(filename, "w")
  for i, matrix in enumerate([A, B]):
      if i != 0:
          f.write("\n")
      for line in matrix:
          f.write("\t".join(map(str, line)) + "\n")