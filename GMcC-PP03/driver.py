#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
import itertools
from analysis.metrics import *
from filehandler.io import *
from algos.algorithms import *

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 3"
__class__       = "605.620"
__semester__    = "Fall, 2022"

RUN_ALL = False

class Tee(object):
  ''' Class object that allows printing program output to console AND TO A FILE.
  '''
  def __init__(self, *files):
    self.files = files
  def write(self, obj):
    for f in self.files:
      f.write(obj)
      f.flush() # If you want the output to be visible immediately
  def flush(self) :
    for f in self.files:
      f.flush()

#def default():
  # Support file input.
#  try:
#    inp = input("Enter file input path: ")
#    print()
#  except (FileNotFoundError, IsADirectoryError):
#    print('File not found.')
#  return (inp.strip())

if __name__ == "__main__":
  """ Driver. 
  """
  #parser = argparse.ArgumentParser(description='Exercise in longest common subsequence.')
  #group = parser.add_mutually_exclusive_group(required=True)
  #group.add_argument('-file', action="store_true",
  #                    help='provide a path to a file containing sequences.')
  #args = parser.parse_args()

  #if args.file: # the default path
  #  inp = default()
  #  seq_input = pre_process(inp)

  parser = argparse.ArgumentParser()
  parser.add_argument("--input", dest="infile", required=True,
                    help="input file", type=lambda f: open(f)) 
  parser.add_argument("--output", help = "output file name")
  args = parser.parse_args()
  
  inp_data = []
  seq_input = pre_process(args.infile.name)

  sequences = []
  for k in list(seq_input.keys()):
    sequences.append(seq_input[k])

# ------ this `tees` stdout to print to a file also.  
  f = open(args.output, 'w')
  original = sys.stdout # 
  sys.stdout = Tee(sys.stdout, f)
# ------ to get the original filehandle back...  
# sys.stdout = original
# print ("This won't appear in file")
# f.close()

# Run the base DNA string comparison from the supplied input file --------------
# Compare every element (sequence) to every other element (sequence), once. 
# Compare order (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
  print()

  print('Running LCS1 (recursive) on provided data...')
  print()
  results = []
  for s1, s2 in itertools.combinations(sequences, 2):
    results.append(call_LCS1(s1, s2))
  lcd_a = max(results, key=len)

  print()
  print('\tLCD of all input DNA strings: ' + lcd_a + ' ' + str(len(lcd_a)))
  print()
  print('Running LCS2 (DP/iterative, first try) on provided data...')
  print()
  results = []
  for s1, s2 in itertools.combinations(sequences, 2):
    results.append(LCS2(s1, s2))
  lcd_b = max(results, key=len)
  print()
  print('\tLCD of all input DNA strings: ' + lcd_b + ' ' + str(len(lcd_b)))
  print()
  print('Running LCS3 (DP/iterative, second try) on provided data...')
  print()
  results = []
  for s1, s2 in itertools.combinations(sequences, 2):
    results.append(LCS3(s1, s2))
  lcd_c = max(results, key=len)
  print()
  print('\tLCD of all input DNA strings: ' + lcd_c + ' ' + str(len(lcd_c)))
  print()
  print('------------------------generated---------------------------')
  print()

if RUN_ALL:
  # Run generated DNA string comparisons
    idx1 = [5, 6, 7, 8, 9] #,10,11,12,13,14,15,16,17,19,20]
    idx2 = [2728,3004,3280,3556] #,3832,4108,4384,4660,4936,5212,5488,5764,6040,6316,6592]

    print('Running LCS1 on generated data...')
    print()
    for i in idx1:
        S1 = dna_str(i) # generate a random ACTG string of length i.
        S2 = dna_str(i)
        LCS1(S1, S2)
    print()
    print('Running LCS2 on generated data...')
    print()
    for i in idx2:
        S1 = dna_str(i)
        S2 = dna_str(i)
        LCS2(S1, S2)
    print()    
    print('Running LCS3 on generated data...')
    print()
    for i in idx2:
        S1 = dna_str(i)
        S2 = dna_str(i)
        LCS3(S1, S2)
    print()
    print('--------------------------fin-------------------------------')
    print()