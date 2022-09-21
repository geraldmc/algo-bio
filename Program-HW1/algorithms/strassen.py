# -*- coding: utf-8 -*-

from math import ceil, log
from algorithms import bruteforce as bf

def matrix_add(A, B):
  """ Sum of two square matrices.
  """
  n = len(A)
  C = [[0 for j in range(0, n)] for i in range(0, n)]
  for i in range(0, n):
    for j in range(0, n):
      C[i][j] = A[i][j] + B[i][j]
  return C

def matrix_subtract(A, B):
  """ Difference of two square matrices.
  """
  n = len(A)
  C = [[0 for j in range(0, n)] for i in range(0, n)]
  for i in range(0, n):
    for j in range(0, n):
      C[i][j] = A[i][j] - B[i][j]
  return C

def strassen(A, B):
  """ Strassen's Algorithm
  [[2, 1], [1, 5]]
  [[6, 7], [4, 3]]

  [[3, 2, 1, 4], [-1, 2, 0, 1], [2, 3, -1, -2], [5, 1, 1, 0]]
  [[-1, 2, -1, 0], [3, -1, 0, 2], [-4, 0, -3, 1], [0, -2, 1, 2]]

  """
  assert len(A) == len(B)
  small = 3
  if len(A) <= small:
    return bf.standard_matrix_product(A, B) # more efficient for small n
  else:
    # initialize sub-matrices
    sub_size = len(A) // 2
    a11 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    a12 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    a21 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    a22 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]

    b11 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    b12 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    b21 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    b22 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]

    aResult = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
    bResult = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]

    # dividing the matrices in 4 sub-matrices:
    for i in range(0, sub_size):
      for j in range(0, sub_size):
        a11[i][j] = A[i][j]  # top left
        a12[i][j] = A[i][j + sub_size]  # top right
        a21[i][j] = A[i + sub_size][j]  # bottom left
        a22[i][j] = A[i + sub_size][j + sub_size]  # bottom right

        b11[i][j] = B[i][j]  # top left
        b12[i][j] = B[i][j + sub_size]  # top right
        b21[i][j] = B[i + sub_size][j]  # bottom left
        b22[i][j] = B[i + sub_size][j + sub_size]  # bottom right

    # Calculating p1 to p7:
    aResult = matrix_add(a11, a22)
    bResult = matrix_add(b11, b22)
    p1 = strassen(aResult, bResult)  # p1 = (a11+a22) * (b11+b22)

    aResult = matrix_add(a21, a22)  # a21 + a22
    p2 = strassen(aResult, b11)  # p2 = (a21+a22) * (b11)

    bResult = matrix_subtract(b12, b22)  # b12 - b22
    p3 = strassen(a11, bResult)  # p3 = (a11) * (b12 - b22)

    bResult = matrix_subtract(b21, b11)  # b21 - b11
    p4 = strassen(a22, bResult)  # p4 = (a22) * (b21 - b11)

    aResult = matrix_add(a11, a12)  # a11 + a12
    p5 = strassen(aResult, b22)  # p5 = (a11+a12) * (b22)

    aResult = matrix_subtract(a21, a11)  # a21 - a11
    bResult = matrix_add(b11, b12)  # b11 + b12
    p6 = strassen(aResult, bResult)  # p6 = (a21-a11) * (b11+b12)

    aResult = matrix_subtract(a12, a22)  # a12 - a22
    bResult = matrix_add(b21, b22)  # b21 + b22
    p7 = strassen(aResult, bResult)  # p7 = (a12-a22) * (b21+b22)

    # calculating c21, c21, c11 e c22:
    c12 = matrix_add(p3, p5)  # c12 = p3 + p5
    c21 = matrix_add(p2, p4)  # c21 = p2 + p4

    aResult = matrix_add(p1, p4)  # p1 + p4
    bResult = matrix_add(aResult, p7)  # p1 + p4 + p7
    c11 = matrix_subtract(bResult, p5)  # c11 = p1 + p4 - p5 + p7

    aResult = matrix_add(p1, p3)  # p1 + p3
    bResult = matrix_add(aResult, p6)  # p1 + p3 + p6
    c22 = matrix_subtract(bResult, p2)  # c22 = p1 + p3 - p2 + p6

    # Grouping the results obtained in a single matrix:
    C = [[0 for j in range(0, len(A))] for i in range(0, len(A))]

    for i in range(0, sub_size):
      for j in range(0, sub_size):
        C[i][j] = c11[i][j]
        C[i][j + sub_size] = c12[i][j]
        C[i + sub_size][j] = c21[i][j]
        C[i + sub_size][j + sub_size] = c22[i][j]
  return C