#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py: Main class for SHashing exercise
"""

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

import argparse

if __name__ == "__main__":
  """ Driver main function for interacting with all modules. 
  """

import argparse

def default():
    # Support input and output w/ file.
    inp = input("Enter input path: ")
    outp = input("Enter output path: ")
    return (inp, outp)


parser = argparse.ArgumentParser(description='Exercises with hashing.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-file', action="store_true",
                    help='provide a path to a file containing one or \
                    more paired matrices.')
args = parser.parse_args()

if args.file: # the default path for the assignment!
    inp, outp = default()
else:
  pass