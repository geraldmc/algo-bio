#!/usr/bin/env python

"""io.py: Functions for handling I/O."""

__author__      = "Gerald McCollam"
__copyright__   = "Copyright 2022, Planet Earth"

def break_on_lf(filename):
  """FIXME
  """
  with open(filename) as reader:
    contents = reader.read()
    matrices = contents.split('\n\n') # FIXME: this could easily fail
    matrices = matrices[:-1] # remove trailing newline
    return matrices

def read_matrices(filename):
  """FIXME
  """
  A = []
  B = []
  #m_dict = {}
  m = break_on_lf(filename)
  n = len(m) # n = number of matrices read.
  # in following dict assignment, the order is the dict key, 
  # the value is the matrix itself.
  for idx in range(0,n):
    #m_dict[int(m[idx][:1][0])] = m[idx][1:].split('\n')[1:] 
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
  for key, value in m.items():
      print(key, value)

def matrix_print_from_input(a,b):
  """FIXME
  """
  print(a)
  print(b)