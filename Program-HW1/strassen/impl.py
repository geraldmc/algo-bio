#!/usr/bin/env python

from math import ceil, log
import argparse, os, sys

# Decorator for counting function calls (from R. Fink).
# See: https://stackoverflow.com/a/21717396/8542716

def call_counter(f):
    """
    Adds a ".calls" variable to the function that increments w/every call.
    Must be set it to zero between iterations.  
    Example:
        @call_counter
        def sumallbelow(x):
          if x<1:
            return 0
          return x + sumallbelow(x-1)
    """
    def wrapped(*args, **kwargs): # deal with any/all arguments
        wrapped.calls += 1
        return f(*args, **kwargs) # call the real function here
    wrapped.calls = 0
    return wrapped

def break_on_lf(filename):
  with open(filename) as reader:
    contents = reader.read()
    matrices = contents.split('\n\n') # FIXME: this might fail
    matrices = matrices[:-1] # remove trailing newline
    return matrices

def read_matrices(filename):
  """FIXME
  """
  m_dict = {}
  m = break_on_lf(filename)
  n = len(m) # n = number of individual matrices in the file read.
  for idx in range(0,n):
    m_dict[int(m[idx][:1][0])] = m[idx][1:].split('\n')[1:] # first element is key, values are matrix values
    #m_list.append(m[idx].split('\n'))
  return m_dict

def read_matrix_file(filename):
  """FIXME
  """
  A = []
  B = []
  n = 0
  with open(filename) as reader:
    n = reader.readline()
    for idx in range(0, int(n)):
      line = reader.readline()
      if line != "":
        A.append([int(el) for el in line.strip().split()])
    for idx in range(0, int(n)):
      line = reader.readline()
      if line != "":
        B.append([int(el) for el in line.strip().split()])
    return int(n.strip()), A, B

def matrix_print(m):
  """FIXME
  """
  for line in m:
      print("\t".join(map(str, line)))

def matrix_print(m):
  """FIXME
  """
  for key, value in m.items():
      print(key, value)

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