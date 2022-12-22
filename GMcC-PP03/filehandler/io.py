#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os 

BASEPAIRS = {'A','C','T','G','U'}

def pre_process(f):
  ''' This function takes a file handle as input.
      It returns a dictionary of sequences from the file:
      {'S1': 'ACCGGTCGACTGCGCGGAAGCCGGCCGAA',
       'S2': 'GTCGTTCGGAATGCCGTTGCTCTGTAAA',
       'S3': 'ATTGCATTGCATGGGCGCGATGCATTTGGTTAATTCCTCG',
       'S4': 'CTTGCTTAAATGTGCA'}
      '''
  
  result = ''
  try:
    with open(f) as reader:
      try:
        contents = reader.read()
        l1 = contents.split('\n')
        result = [l.split('=') for l in l1]
        result_dict = {}
        for i in range(len(result)):
           # j is never > 2 so this is a reasonable nested loop
          for j in range(len(result[i])):
              if j == 0:
                  key = result[i][j].strip()
              else:
                  result_dict[key] = result[i][j].strip()
      except (OSError):
        print("Error reading from file")
  except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file. Please try again.")
  for l in list(result_dict.values()):
    if False in [x in BASEPAIRS for x in l]:
      raise ValueError("Found non-nucleotide character[s]. Please check the input file and try again")
  print()
  return result_dict


