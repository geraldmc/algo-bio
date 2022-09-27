# -*- coding: utf-8 -*-

def zero_matrix(r, c):
  """Creates a matrix filled with zeros.
  """
  matrix = [[0 for row in range(r)] for col in range(c)]
  return matrix

def naive_matrix_product(A, B):
  """ Returns the product of two square matrices.
      This implementation represents a 'brute force' algorithm
      with time complexity of O(n^3).
  """
  #assert len(A[0]) == len(B)
  n = len(A)
  count=0
  # initialize a sq. matrix w/ zeroes
  C = [[0 for i in range(n)] for j in range(n)]

  for i in range(n): # loop n times...
    for k in range(n): # times n times...
      for j in range(n): # times n times = n^3
        C[i][j] += A[i][k] * B[k][j] # multiply
        count+=1
  return C, count