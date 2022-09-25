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
from filehandler.io import input_stdout, output_stdout, file_output
from data.matrix_maker import create_random_matrix
from algorithms import bruteforce as bf 
from algorithms import strassen as st

# See: https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/

if __name__ == "__main__":
  """MAIN
  """

import argparse

def default():
    # Support input and output w/ file.
    inp = input("Enter input path: ")
    outp = input("Enter output path: ")
    return (inp, outp)

def prompt_matrix_creation():
    # Support matrix creation
    ord = int(input("Enter matrix order: "))
    rang = int(input("Enter value range (0,n): "))
    return(ord, rang)

parser = argparse.ArgumentParser(description='Apply Strassen\'s algorithm. \
                                  Compare it with a \'brute force\' algorithm.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-file', action="store_true",
                    help='provide a path to a file containing one or \
                    more paired matrices.')
group.add_argument('-create', action="store_true",
                    help='provide the order and an interval range to \
                      create a new paired matrix.')
group.add_argument('-test', action='store', 
                    type=argparse.FileType('w'), dest='output',
                    help="direct a matrix to a named output file")

args = parser.parse_args()

if args.file: # the default path for the assignment!
    inp, outp = default()
    m = read_matrices(inp)
    result = process_input_matrix(m)
    print()
    print('Read {} matrix pairs from file {}'.format(len(result), inp))
    response = input('Print the result[s] to a file? (Yes|No): ').lower()
    affirm = (lambda x: 0 if x.strip()=='no' else 1)(response)

    for idx in range(0,len(result)):
      A = result[idx][0]
      B = result[idx][1]
      C = bf.standard_matrix_product(A,B)
      D = st.strassen(A, B)
      if affirm:
        with open(outp, 'a+') as f: # this will *append*, if the file exists.
          f.write('[Matrix Input {}]'.format(idx+1) + '\n')
          f.write(str(len(A))+'\n')
          f.write('\n'.join(' '.join(map(str,sl)) for sl in A))
          f.write('\n')
          f.write('\n'.join(' '.join(map(str,sl)) for sl in B))
          f.write('\n\n')
          f.write('[Matrix Product {}]'.format(idx+1) + '\n')
          f.write('\n'.join(' '.join(map(str,sl)) for sl in C))
          f.write('\n\n')
      else: 
        input_stdout(A,B,C,(idx+1))
    print('Printed {} matrix pairs/products to file {}'.format(len(result), outp))

elif args.create: # for testing to console 
    order, r = prompt_matrix_creation()
    A = create_random_matrix(order, r)
    B = create_random_matrix(order, r)
    C = bf.standard_matrix_product(A,B)
    D = st.strassen(A, B)
    input_stdout(A,B,C,1)
    print()
else: # for testing to file.
  order, r = prompt_matrix_creation()
  A = create_random_matrix(order, r)
  B = create_random_matrix(order, r)
  file_output(A, B, order, args.output)