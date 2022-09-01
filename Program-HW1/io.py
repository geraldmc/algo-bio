#!/usr/bin/env python

from math import ceil, log
from optparse import OptionParser

# Decorator for counting function calls.
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

if __name__ == "__main__":
  """MAIN
  """
  filename = "./data/LabStrassenInput-2.txt"
  n, A, B = read_matrix_file(filename)
  matrix_print(A)
  print()
  matrix_print(B)
  print()
  print(matrix_product(A,B))
  print()