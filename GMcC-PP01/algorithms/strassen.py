#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Note:
# This file maye be run as a script. To do so enter the following at the 
# command prompt:

# >> python strassen.py

# See: https://stackoverflow.com/questions/52137431/strassens-algorithm-\
# bug-in-python-implementation
# ---------------------------------------------------------------------  

strassen_count = 0

def increment_global_by_one():
    global strassen_count    # Needed to modify global copy of strassen_count
    strassen_count += 1

def print_global():
    print("Number of Strassen Multiplications: ({})".format(strassen_count)) 

def zero_matrix(r, c):
  """Creates a matrix filled with zeros.
  """
  matrix = [[0 for row in range(r)] for col in range(c)]
  return matrix

def brute_multiply(x, y):
  if len(x[0]) != len(y):
    return "Multiplication is not possible!"
  else:
    p_matrix = zero_matrix(len(x), len(y[0]))
    for i in range(len(x)):
      for j in range(len(y[0])):
        for k in range(len(y)):
          p_matrix[i][j] += x[i][k] * y[k][j]
  return p_matrix

def split(matrix):
  """Split input matrix into 1/4's.
  """
  a = b = c = d = matrix
  while len(a) > len(matrix)/2:
    a = a[:len(a)//2]
    b = b[:len(b)//2]
    c = c[len(c)//2:]
    d = d[len(d)//2:]

  while len(a[0]) > len(matrix[0])//2:
    for i in range(len(a[0])//2):
      a[i] = a[i][:len(a[i])//2]
      b[i] = b[i][len(b[i])//2:]
      c[i] = c[i][:len(c[i])//2]
      d[i] = d[i][len(d[i])//2:]

  return a, b, c, d

def add_matrix(a, b):
  """FIXME
  """
  if type(a) == int:
    d = a + b
  else:
    d = []
    for i in range(len(a)):
      c = []
      for j in range(len(a[0])):
        c.append(a[i][j] + b[i][j])
      d.append(c)
  return d

def subtract_matrix(a, b):
  """FIXME
  """
  if type(a) == int:
    d = a - b
  else:
    d = []
    for i in range(len(a)):
      c = []
      for j in range(len(a[0])):
        c.append(a[i][j] - b[i][j])
      d.append(c)
  return d

def strassen(A, B, n):
  """FIXME
  """
  # base case: 1x1 matrix
  if n == 1:
    z = [[0]]
    z[0][0] = A[0][0] * B[0][0]
    return z
  else:
    # split matrices into 1/4th's
    a, b, c, d = split(A)
    e, f, g, h = split(B)

    # p1 = a*(f-h), multiplication occurs heredire
    p1 = strassen(a, subtract_matrix(f, h), n/2)
    increment_global_by_one()
    # p2 = (a+b)*h, multiplication occurs here
    p2 = strassen(add_matrix(a, b), h, n/2)
    increment_global_by_one()
    # p3 = (c+d)*e, multiplication occurs here
    p3 = strassen(add_matrix(c, d), e, n/2)
    increment_global_by_one()
    # p4 = d*(g-e), multiplication occurs here
    p4 = strassen(d, subtract_matrix(g, e), n/2)
    increment_global_by_one()
    # p5 = (a+d)*(e+h), multiplication occurs here
    p5 = strassen(add_matrix(a, d), add_matrix(e, h), n/2)
    increment_global_by_one()
    # p6 = (b-d)*(g+h), multiplication occurs here
    p6 = strassen(subtract_matrix(b, d), add_matrix(g, h), n/2)
    increment_global_by_one()
    # p7 = (a-c)*(e+f), multiplication occurs here
    p7 = strassen(subtract_matrix(a, c), add_matrix(e, f), n/2)
    increment_global_by_one()

    z11 = add_matrix(subtract_matrix(add_matrix(p5, p4), p2), p6)
    z12 = add_matrix(p1, p2)
    z21 = add_matrix(p3, p4)
    z22 = add_matrix(subtract_matrix(subtract_matrix(p5, p3), p7), p1)

    z = zero_matrix(len(z11)*2, len(z11)*2) # zero out a new matrix
    for i in range(len(z11)):
      for j in range(len(z11)):
        z[i][j] = z11[i][j]
        z[i][j+len(z11)] = z12[i][j]
        z[i+len(z11)][j] = z21[i][j]
        z[i+len(z11)][j+len(z11)] = z22[i][j]

    return z

if __name__ == "__main__":
  """ Run this as a script, to test.
  """
  A1 = [[2,1],[1,5,]]
  B1 = [[6,7],[4,3]]

  A2 = [[3,2,1,4],[-1,2,0,1],[2,3,-1,-2],[5,1,1,0]]
  B2 = [[-1,2,-1,0],[3,-1,0,2],[-4,0,-3,1],[0,-2,1,2]]

  A3 = [[1,0,1,2,0,-1,-1,-1], [-1,1,-1,1,2,0,0,3],
        [1,-1,2,-3,-1,1,1,0], [0,2,3,2,1,0,-1,-2],
        [2,3,-1,0,-1,0,-1,0], [1,2,2,1,0,1,1,2],
        [3,-1,0,2,2,2,2,1], [2,-2,1,-3,3,0,1,2] ]
  B3 = [[1,0,1,2,0,-1,-1,-1], [-1,1,-1,1,2,0,0,3],
        [1,-1,2,-3,-1,1,1,0], [0,2,3,2,1,0,-1,-2],
        [2,3,-1,0,-1,0,-1,0], [1,2,2,1,0,1,1,2],
        [3,-1,0,2,2,2,2,1], [2,-2,1,-3,3,0,1,2] ]

  print_global()
  print(f"Using Strassen's:\nA*B = {strassen(A1, B1, 2)}")
  print_global()
  print(f"A*B = {strassen(A2, B2, 4)}")
  print_global()
  print(f"A*B = {strassen(A3, B3, 8)}")
  print_global()