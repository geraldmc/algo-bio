#!/usr/bin/env python

"""driver.py: Driver class.
  Gerald McCollam
  605.620.FA22.
  Programming Project #1
  September 27th 2022

"""

__author__      = "Gerald McCollam"
__copyright__   = "Copyright 2022, Planet Earth"

from math import ceil, log
import argparse, os, sys
from filehandler.io import read_matrices, matrix_print

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """
  parser = argparse.ArgumentParser(description='Apply Strassen\'s algorithm. Compare with brute force algorithm.')
  parser.add_argument('Path', metavar='input file path:', type=str,
                       help='a path to a file containing matrices.')
  parser.add_argument('Matrix', metavar='Create paired matrices?:', type=str,
                      help='command to create paired matrices.')

  args = parser.parse_args()
  input_file = args.Path

  if not os.path.isfile(input_file):
      print('The file specified does not exist. Exiting...')
      sys.exit()

  filename = './data/LabStrassenInput.txt'
  m = read_matrices(filename)
  matrix_print(m)
  
  if args.makematrix = True
    A = create_random_matrix(n)
    B = create_random_matrix(n)
    save_matrix(A, B, "%i.in" % n)