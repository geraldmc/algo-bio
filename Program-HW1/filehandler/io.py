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
  m_dict = {}
  m = break_on_lf(filename)
  n = len(m) # n = number of individual matrices in the file read.
  for idx in range(0,n):
    m_dict[int(m[idx][:1][0])] = m[idx][1:].split('\n')[1:] # first element is key, values are matrix values
  return m_dict

def matrix_print(m):
  """FIXME
  """
  for key, value in m.items():
      print(key, value)