#!/usr/bin/env python

from math import ceil, log
import argparse, os, sys

def matrix_product(A, B):
  """ A brute force method of calculating the product of two matrices.
  """
  n = len(A)
  C = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      for k in range(n):
          for j in range(n):
              C[i][j] += A[i][k] * B[k][j]
  return C

def matrix_add(A, B):
  """ Add two square matrices.
  """
n = len(A)
C = [[0 for j in range(0, n)] for i in range(0, n)]
for i in range(0, n):
    for j in range(0, n):
        C[i][j] = A[i][j] + B[i][j]
return C


def matrix_subtract(A, B):
  """ Subtract two square matrices.
  """
n = len(A)
C = [[0 for j in range(0, n)] for i in range(0, n)]
for i in range(0, n):
    for j in range(0, n):
        C[i][j] = A[i][j] - B[i][j]
return C


def strassen():
  """ An implementation of Strassen's Algorithm.
  """
    pass