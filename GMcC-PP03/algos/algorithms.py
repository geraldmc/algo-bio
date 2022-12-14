# -*- coding: utf-8 -*-
"""A module-level docstring

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.
"""

def LCS1(X, Y):
  '''
    The first two functions (LCS1 and LCS2) are essentially equivalent. Each 
    takes as input sequences X[1..m] and Y[1..n], computes the LCS between 
    X[1..i] and Y[1..j] for all 1 ≤ i ≤ m and 1 ≤ j ≤ n, and stores it in C[i,j]. 
    C[m,n] will contain the length of the LCS of X and Y.
  '''
  lengths = [[0] * (len(Y)+1) for _ in range(len(X)+1)]
  for i, x in enumerate(X):
    for j, y in enumerate(Y):
      if x == y:
        lengths[i+1][j+1] = lengths[i][j] + 1
      else:
        lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    # read a substring from the matrix
    result = ''
    j = len(Y)
    for i in range(1, len(X)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += X[i-1]

    return result
# end LCS1 ---------------------------------------------------------------------

def LCS2(X, Y):
  ''' 

  '''
  m = [['' for x in range(len(Y))] for x in range(len(X))]
  for i in range(len(X)):
    for j in range(len(Y)):
      if X[i] == Y[j]:
        if i == 0 or j == 0:
          m[i][j] = X[i]
        else:
          m[i][j] = m[i-1][j-1] + X[i]
      else:
        m[i][j] = max(m[i-1][j], m[i][j-1], key=len)
  cs = m[-1][-1]
  return str(len(cs)), cs
# end LCS2 ---------------------------------------------------------------------

def LCS3(X,Y):
  ''' Dynamic programming example.
  '''
  n = len(X)
  m = len(Y)

	# Opt array stores the optimal solution value till ith and jth position for 2 strings
  opt = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
	# Pi array stores the direction when calculating the actual sequence
  pi = [[0 for i in range(0,m+1)] for j in range(0,n+1)]

	# Calculate the length of the longest common subsequence
  # in opt array, 
  for i in range(1,n+1):
    for j in range(1,m+1):
      if X[i-1] == Y[j-1]:
        opt[i][j] = opt[i-1][j-1] + 1
        pi[i][j] = 0
      elif opt[i][j-1] >= opt[i-1][j]:
        opt[i][j] = opt[i][j-1]
        pi[i][j] = 1
      else:
        opt[i][j] = opt[i-1][j]
        pi[i][j] = 2 

	# Calculate the longest common subsequence using the Pi array
  i = n
  j = m
  S = ''

  while i>0 and j>0:
    if pi[i][j] == 0:
      S = X[i-1] + S
      i-=1
      j-=1
    elif pi[i][j] == 2:
      i-=1
    else:
      j-=1
  return str(opt[n][m]),S
# end LCS1 ---------------------------------------------------------------------


def LCS4(X, Y):
  """
  Recursive approach that is quite slow. This returns the correct subsequence 
  but in reverse. To fix this apply [::-1] to resulting string. 
  https://rosettacode.org/wiki/Longest_common_subsequence#Recursion_7 
  """
  if not X or not Y:
    return ''
  x, xs, y, ys = X[0], X[1:], Y[0], Y[1:]

  if x == y:
    return str(LCS4(xs, ys)) + x
  else:
    return max(LCS4(X, ys), LCS4(xs, Y), key=len)
# end LCS4 ---------------------------------------------------------------------


def print_LCS(X,Y,Z):
  ''' Simple function to print all sequence combinations
  '''
  print()
  print('LCS of {} and {} is: \n {} with length of: {}'.format(X, Y, Z[1], Z[0]))
  print()
  # end print_LCS --------------------------------------------------------------
