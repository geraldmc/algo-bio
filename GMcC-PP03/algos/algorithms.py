# -*- coding: utf-8 -*-

def LCS1(X,Y):
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
# end LCS1 -------------------

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

def print_LCS(X,Y):
  # Create a string variable to store the lcs string
  lcs = ""

  # Start from the right-most-bottom-most corner and
  # one by one store characters in lcs[]
  i = m
  j = n
  while i > 0 and j > 0:
      # If current character in X[] and Y are same, then
      # current character is part of LCS
      if X[i-1] == Y[j-1]:
          lcs += X[i-1]
          i -= 1
          j -= 1
      # If not same, then find the larger of two and
      # go in the direction of larger value
      elif L[i-1][j] > L[i][j-1]:
          i -= 1
      else:
          j -= 1
  # We traversed the table in reverse order
  # LCS is the reverse of what we got
  lcs = lcs[::-1]
  print("LCS of " + X + " and " + Y + " is " + lcs)