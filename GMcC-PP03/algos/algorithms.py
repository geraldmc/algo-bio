# -*- coding: utf-8 -*-

def LCS1(s1,s2):
	n = len(s1)
	m = len(s2)

	# Opt array stores the optimal solution value till ith and jth position for 2 strings
	opt = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
	# Pi array stores the direction when calculating the actual sequence
	pi = [[0 for i in range(0,m+1)] for j in range(0,n+1)]

	# Calculate the length of the longest common subsequence
	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1] == s2[j-1]:
				opt[i][j] = opt[i-1][j-1] + 1
				pi[i][j] = 0
			elif opt[i][j-1] >= opt[i-1][j]:
				opt[i][j] = opt[i][j-1]
				pi[i][j] = 1
			else:
				opt[i][j] = opt[i-1][j]
				pi[i][j] = 2 #Length of the lcs is saved at opt[n][m]

	# Calculate the longest common subsequence using the Pi array
	i = n
	j = m
	S = ''

	while i>0 and j>0:
		if pi[i][j] == 0:
			S = s1[i-1] + S
			i-=1
			j-=1
		elif pi[i][j] == 2:
			i-=1
		else:
			j-=1
	return str(opt[n][m]),S

def LCS2(s1, s2):
  matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
  for i in range(len(s1)):
    for j in range(len(s2)):
      if s1[i] == s2[j]:
        if i == 0 or j == 0:
          matrix[i][j] = s1[i]
        else:
          matrix[i][j] = matrix[i-1][j-1] + s1[i]
      else:
        matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

  cs = matrix[-1][-1]

  return len(cs), cs