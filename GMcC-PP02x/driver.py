#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
from hashtables.LinearProbing import LinearProbing
from hashtables.QuadraticProbing import QuadraticProbing
from hashtables.SeparateChaining import SeparateChaining

from filehandler.io import pre_process

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

SLOTS=120

def default():
  # Support file input.
  try:
    inp = input("Enter file input path: ")
  except (FileNotFoundError, IsADirectoryError):
    print('File not found.')
  return (inp.strip())

def ChainHash(data):
  sch = SeparateChaining()

def LinProbeHash(data):
  lph = LinearProbing()

def QuadHash(data):
  qph = QuadraticProbing()

if __name__ == "__main__":
  """ Main driver for interacting with other modules. 
  """
  parser = argparse.ArgumentParser(description='Exercise in hashing.')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-file', action="store_true",
                      help='provide a path to a file containing hash input.')
  args = parser.parse_args()

  if args.file: # the default path for the assignment!
    inp_data = []
    inp = default()
    raw_input = pre_process(inp)
    for s in raw_input:
      inp_data.append([int(i) for i in s]) # convert to ints
    flat_list = [item for sub in inp_data for item in sub]
    lph = LinearProbing()
    qph = QuadraticProbing()
    sch = SeparateChaining()

    for element in flat_list:
      lph.insert(element)
      #qph.insert(element)
      #sch.insert(element)

    