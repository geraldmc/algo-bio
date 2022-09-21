# -*- coding: utf-8 -*-

def standard_matrix_product(A, B):
  """ Product of two square matrices.
  """
  n = len(A)
  C = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    for k in range(n):
      for j in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C