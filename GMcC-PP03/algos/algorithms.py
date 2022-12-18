# -*- coding: utf-8 -*-
"""A module-level docstring

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.
"""
from analysis.metrics import profile

#https://www.enjoyalgorithms.com/blog/longest-common-subsequence
@profile
def LCS1(X, Y):
  '''
  A brute-force approach using recursion. This returns the correct subsequence 
  but in reverse. To fix, simply apply [::-1] to the resulting string.
  '''
  if not X or not Y:
    return ''
  x, xs, y, ys = X[0], X[1:], Y[0], Y[1:]

  if x == y:
    return str(LCS1(xs, ys)) + x
  else:
    return max(LCS1(X, ys), LCS1(xs, Y), key=len)

def call_LCS1(X,Y):
  S = LCS1(X, Y)[::-1]
  return str(len(S)), S
# end LCS1 ---------------------------------------------------------------------

@profile
def LCS2(X,Y):
  ''' An iterative DP example.
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
  S = m[-1][-1]
  return str(len(S)), S
# end LCS3 ---------------------------------------------------------------------

@profile
def LCS3(X,Y):
  ''' Return table such that L[j][k] is length of lcs for X[0:j] and Y[0:k].
  '''
  n,m = len(X), len(Y)
  result = []
  # Part I: --------
  L = [[0]* (m+1) for k in range(n+1)] # table: (n+1) x (m+1)
  for j in range(n):
    for k in range(m):
      if X[j]==Y[k]:
        L[j+1][k+1] = L[j][k] + 1
      else:
         L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
  # Part II: --------
  while L[n][m] > 0: # there are common characters in X and Y
    if X[n-1] == Y[m-1]:
      result.append(X[n-1])
      n -= 1
      m -= 1
    elif L[n-1][m] >= L[n][m-1]:
      n -= 1
    else:
      m -= 1
  S = ''.join(reversed(result)) 
  l = len(S)
  return l, S 
# end LCS3 ---------------------------------------------------------------------
