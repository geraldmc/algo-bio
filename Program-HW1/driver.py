#!/usr/bin/env python

"""driver.py: Driver class.
"""
__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 1"
__class__       = "605.620"
__semester__    = "Fall, 2022"


from math import ceil, log
import argparse, os, sys
from filehandler.io import read_matrices, process_input_matrix, matrix_print_from_list
from data.matrix_maker import create_random_matrix

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """

import argparse

def prompt_file_input():
    # Everything required to support inputing a file
    p = input("Enter input path: ")
    return (p)

def prompt_matrix_creation():
    # Everything required to support matrix creation
    n = int(input("Enter matrix order: "))
    r = int(input("Enter matrix value range (0,n): "))
    return(n, r)

parser = argparse.ArgumentParser(description='Apply Strassen\'s algorithm. \
                                  Compare with brute force algorithm.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-file', action="store_true",
                    help='a path to a file containing matrices.')
group.add_argument('-create matrices', action="store_true",
                    help='command to create paired matrices.')

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
      matrix_print_from_list(A,B)
else:
    order, r = prompt_matrix_creation()
    A = create_random_matrix(order, r)
    B = create_random_matrix(order, r)
    matrix_print_from_list(A,B)