# -*- coding: utf-8 -*-

def standard_matrix_product(A, B):
  """ Product of two square matrices.
      This represents a 'brute force' algorithm
      with time complexity of O(n^3).
  """
  n = len(A)
  # init sq. matrix w/ zero
  C = [[0 for i in range(n)] for j in range(n)]
  for i in range(n): # n...
    for k in range(n): # times n...
      for j in range(n): # times n = n^3
        C[i][j] += A[i][k] * B[k][j]
  return C