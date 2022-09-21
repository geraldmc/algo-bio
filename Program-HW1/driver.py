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
from filehandler.io import dual_matrix_print_stdout, single_matrix_print_stdout
from data.matrix_maker import create_random_matrix
from bruteforce import impl as bf 
from strassen import impl as st

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """

import argparse

def prompt_file_input():
    # Everything required to support inputing a file
    p = input("Enter input path: ")
    return (p)

def prompt_file_output(out, A, B):
  for i, matrix in enumerate([A, B]):
    if i != 0:
      pass
    for line in matrix:
      out.write(" ".join(map(str, line)) + "\n")

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
group.add_argument('-plot', action='store', 
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
      dual_matrix_print_stdout(A,B)
      C = bf.standard_matrix_product(A,B)
      print()
      single_matrix_print_stdout(C)
elif args.create:
    order, r = prompt_matrix_creation()
    A = create_random_matrix(order, r)
    B = create_random_matrix(order, r)
    C = bf.standard_matrix_product(A,B)
    dual_matrix_print_stdout(A,B)
    print()
    single_matrix_print_stdout(C)

else:
  A=[[2, 1], [1, 5]]
  B=[[6, 7], [4, 3]]
  prompt_file_output(args.output, A,B)