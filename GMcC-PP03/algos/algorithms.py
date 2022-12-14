# -*- coding: utf-8 -*-

def LCS1(X,Y):
  '''
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

def LCS2(X, Y):
  ''' Dynamic implementation of LCS problem
  '''
  m = [["" for x in range(len(Y))] for x in range(len(X))]
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


def print_LCS(X,Y,Z):
  ''' Simple function to print all sequence combinations
  '''
  print()
  print('LCS of {} and {} is: \n {} with length of: {}'.format(X, Y, Z[1], Z[0]))
  print()
  # end print_LCS --------------------------------------------------------------
