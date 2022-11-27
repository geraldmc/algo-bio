#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
from hashtables.LinearProbing import LinearProbing
from hashtables.QuadraticProbing import QuadraticProbing
from hashtables.SeparateChaining import SeparateChaining
from analysis.metrics import *
from filehandler.io import pre_process

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

def default():
  # Support file input.
  try:
    inp = input("Enter file input path: ")
  except (FileNotFoundError, IsADirectoryError):
    print('File not found.')
  return (inp.strip())

def LinProbeHash(data, mod, depth, size=120):
  lph = LinearProbing(modulus=mod, slot_depth=depth, slot_size=size)
  for item in data:
    lph.insert(item)
  plot(distribute(data, hash_function=lph, num_containers=12))
  print('-- Linear Probing: mod={}, depth={}, size={}'.format(mod, depth, size))
  print()

def QuadHash(data, mod, depth, size=120):
  qph = QuadraticProbing(modulus=mod, slot_depth=depth, slot_size=size)
  for item in data:
    qph.insert(item)
  plot(distribute(data, hash_function=qph, num_containers=12))
  print('-- Quadratic Probing: mod={}, depth={}, size={}'.format(mod, depth, size))
  print()

def ChainHash(data, mod, depth):
  sch = SeparateChaining(modulus=mod)
  for item in data:
    sch.insert(item)

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser(description='Exercise in hashing.')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-file', action="store_true",
                      help='provide a path to a file containing hash input.')
  args = parser.parse_args()

  if args.file: # the default path
    inp_data = []
    inp = default()
    raw_input = pre_process(inp)
    for s in raw_input:
      inp_data.append([int(i) for i in s]) # convert to ints
    input_list = [item for sub in inp_data for item in sub]

# Division modulo 120, bucket size = 1 ----------------------------------------
    LinProbeHash(input_list, mod=120, depth=1)            #1
    QuadHash(input_list, mod=120, depth=1)                #2
    ChainHash(input_list, mod=120, depth=1)               #3
# Division modulo 113, bucket size = 1 ----------------------------------------
    LinProbeHash(input_list, mod=113, depth=1)            #4
    QuadHash(input_list, mod=113, depth=1)                #5
    ChainHash(input_list, mod=113, depth=1)               #6
# Division modulo 41, bucket size = 3 ----------------------------------------
    LinProbeHash(input_list, mod=41, depth=3, size=40)    #7
    QuadHash(input_list, mod=41, depth=3, size=40)        #8
