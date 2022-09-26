#!/usr/bin/env python

"""Create random integer matrices."""

import random

random.seed(123)

def create_random_matrix(n, limit):
  """Create a square matrix using randomly generated positive integers.
     The variable 'n' is the order of the matrix.
     The variable 'limit' is the range of positive integers used.
  """
  assert type(n) is int and n > 0 and n <= 256
  matrix = []
  for i in range(n):
      matrix.append([random.randint(0, limit) for el in range(n)])
  return matrix