#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""

from filehandler.io import pre_process

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

import argparse

if __name__ == "__main__":
  """ Main driver for interacting with other modules. 
  """

import argparse

def default():
  # Support file input.
  try:
    inp = input("Enter file input path: ")
  except (FileNotFoundError, IsADirectoryError):
    print('File not found.')
  return (inp.strip())

parser = argparse.ArgumentParser(description='Exercise in hashing.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-file', action="store_true",
                    help='provide a path to a file containing hash input.')
args = parser.parse_args()

if args.file: # the default path for the assignment!
    inp = default()
    raw_input = pre_process(inp)
    for s in raw_input:
      print (s)
else:
  print('no other option yet...')