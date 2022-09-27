# -*- coding: utf-8 -*-

"""io.py: Functions for handling I/O."""

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 1"
__class__       = "605.620"
__semester__    = "Fall, 2022"

def break_on_lf(filename):
  """Preprocess the input file to extract an
     arbitrary number of square matrices.
  """
  with open(filename) as reader:
    contents = reader.read()
    matrices = contents.split('\n\n')
    matrices = matrices[:-1] # FIXME: remove trailing newlines?
    return matrices

def read_matrices(filename):
  """ Read the matrices from file.
      This function calls the preprocess function break_on_lf().
      Returns a dictionary object keyed on the order of the matrix.
  """
  A = []
  B = []
  m_dict = {}
  m = break_on_lf(filename)
  n = len(m) # n = number of matrices read.

  # In following dict assignment, the order is the dict key, 
  # the value is the matrix itself. This is wrapped in a try block 
  # as the input file prvioded for testing has changed several times.
  try:
    for idx in range(0,n):
      m_dict[int(m[idx][:1][0])] = m[idx][1:].split('\n')[1:] 
  except Exception as e:
    print("WARNING! An ", e.__class__, "exception has occurred. Please continue...")
    print()
  return m_dict

def process_input_matrix(m):
  """ Process the matrix dictionary object produced by read_matrices(f).
      This dict contains the order of a matrix and its contents. 
      For each dict in the series, it extracts matrix values in their proper
      order. It returns a dictionary object keyed on a count of the number
      of matrices read. The output dictionary values are lists.
  """   
  k = list(m.keys())
  C = {}
  for key,val in enumerate(k):
    A = []
    B = []
    d = m[val]
    for idx in range(0,int(len(d)/2)): # first half of list
      A.append([int(i) for i in d[idx].split(' ') if i])
    mid = idx+1
    for idx in range(mid, len(d)): # second half of list
      B.append([int(i) for i in d[idx].split(' ') if i])
    C[key] = A, B
  return C

def input_stdout(A,B,C,count,index):
  """ Convenience function for printing input 
      and multiplication results to the console. 
  """
  print()
  print('Matrix Input ({}):'.format(index))
  print(A)
  print(B)
  print('Matrix Product ({}):'.format(index))
  print(C)
  print('Number of naive multiplications ({}):'.format(count))

def file_output(A, B, order, handle):
  """FIXME
  """
  handle.write(str(order) + "\n") 
  for i, matrix in enumerate([A, B]):
    if i != 0:
      pass
    for line in matrix:
      handle.write(" ".join(map(str, line)) + "\n")
  handle.write("\n")
  print('OK. Wrote output to file: {}. Done!'.format(handle.name))
  handle.close()