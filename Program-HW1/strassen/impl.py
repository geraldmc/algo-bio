#!/usr/bin/env python

from math import ceil, log
import argparse, os, sys

def matrix_product(A, B):
  """FIXME
  """
  n = len(A)
  C = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      for k in range(n):
          for j in range(n):
              C[i][j] += A[i][k] * B[k][j]
  return C