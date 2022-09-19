#!/usr/bin/env python

"""driver.py: Driver class.
"""
__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 1"
__class__       = "605.620"
__semester__    = "Fall, 2022"


from math import ceil, log
import argparse, os, sys
from filehandler.io import read_matrices, matrix_print, matrix_print_from_input
from data.matrix_maker import create_random_matrix

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """

import argparse

def prompt_file_input():
    # do everything required to support inputing a file
    p = input("Enter input path: ")
    return (p)

def prompt_matrix_creation():
    # do everything required to support matrix creation
    n = int(input("Enter matrix size: "))
    return(n)

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
    print(p)
    m = read_matrices(p)
    matrix_print(m)
else:
    order = prompt_matrix_creation()
    A = create_random_matrix(order, 2)
    B = create_random_matrix(order, 2)
    matrix_print_from_input(A,B)