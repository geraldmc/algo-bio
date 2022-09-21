#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py: Main driver class for Strassen/Brute force comparison.
"""
__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 1"
__class__       = "605.620"
__semester__    = "Fall, 2022"

from math import ceil, log
import argparse, os, sys
from filehandler.io import read_matrices, process_input_matrix
from filehandler.io import print_dual_stdout, print_single_stdout
from data.matrix_maker import create_random_matrix
from algorithms import bruteforce as bf 
from algorithms import strassen as st

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """

import argparse

def prompt_file_input():
    # Everything required to support inputing a file
    p = input("Enter input path: ")
    return (p)

def prompt_file_output(out, A, B, order):
  print('OK. Writing output to file: {}. Done!'.format(out.name))
  out.write(str(order) + "\n") 
  for i, matrix in enumerate([A, B]):
    if i != 0:
      pass
    for line in matrix:
      out.write(" ".join(map(str, line)) + "\n")
  out.write("\n")

def prompt_matrix_creation():
    # Everything required to support matrix creation
    n = int(input("Enter matrix order: "))
    r = int(input("Enter matrix value range (0,n): "))
    return(n, r)

parser = argparse.ArgumentParser(description='Apply Strassen\'s algorithm. \
                                  Compare with brute force algorithm.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-file', action="store_true",
                    help='provide a path to a file containing one or \
                    more paired matrices.')
group.add_argument('-create', action="store_true",
                    help='provide the order and an interval range to \
                      create a new paired matrix.')
group.add_argument('-write', action='store', 
                    type=argparse.FileType('w'), dest='output',
                    help="direct a plot to a named output file")

args = parser.parse_args()

if args.file:
    p = prompt_file_input()
    m = read_matrices(p)
    result = process_input_matrix(m)
    print()
    print('Read {} matrix pairs from file {}'.format(len(result), p))
    for idx in range(0,len(result)):
      A = result[idx][0]
      B = result[idx][1]
      print_dual_stdout(A,B)
      C = bf.standard_matrix_product(A,B)
      D = st.strassen(A, B)
      print()
      print_single_stdout(C)
elif args.create:
    order, r = prompt_matrix_creation()
    A = create_random_matrix(order, r)
    B = create_random_matrix(order, r)
    C = bf.standard_matrix_product(A,B)
    D = st.strassen(A, B)
    print_dual_stdout(A,B)
    print()
    print_single_stdout(C)

else:
  order, r = prompt_matrix_creation()
  A = create_random_matrix(order, r)
  B = create_random_matrix(order, r)
  prompt_file_output(args.output, A, B, order)