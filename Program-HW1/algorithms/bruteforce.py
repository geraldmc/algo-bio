# -*- coding: utf-8 -*-

def zero_matrix(r, c):
  """Creates a matrix filled with zeros.
  """
  matrix = [[0 for row in range(r)] for col in range(c)]
  return matrix

def standard_matrix_product(A, B):
  """ Product of two square matrices.
      This represents a 'brute force' algorithm
      with time complexity of O(n^3).
  """
  n = len(A)
  count=0
  # init sq. matrix w/ zeroes
  C = [[0 for i in range(n)] for j in range(n)]
  for i in range(n): # n...
    for k in range(n): # times n...
      for j in range(n): # times n = n^3
        C[i][j] += A[i][k] * B[k][j]
        count+=1
  return C, count

def direct_multiply(A, B):
  count=0
  if len(A[0]) != len(B):
    return "Matrix is not square. Exiting...!"
  else:
    C = zero_matrix(len(A), len(B[0]))
    for i in range(len(A)):
      for j in range(len(B[0])):
        for k in range(len(B)):
          C[i][j] += A[i][k] * B[k][j]
          count+=1
  return C, count