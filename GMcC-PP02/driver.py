#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse
from array import array # for contiguous typed arrays
#from hashing.TableMap import TableMap
#from hashing.HashMap import HashMap
#from hashing.MutableHash import MutableHash
from hashing.ChainHashMap import ChainHashMap
#from hashtable.ChainHash import ChainHash
#from hashtable.LinProbeHash import LinProbeHash
#from hashtable.QuadHash import QuadHash

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

def runChainHash(data):
  chm = ChainHashMap(capacity=SLOTS)
  for idx in range(len(data)):
    chm[idx] = chm._hash_MOD(data[idx])
  return chm

def runLinProbeHash(data):
  ph = LinProbeHash(capacity=SLOTS)
  ph.output()

def runQuadHash(data):
  qh = QuadHash(capacity=SLOTS)
  qh.output()

if __name__ == "__main__":
  """ Main driver for interacting with other modules. 
  """
  _items = []
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
    chm = runChainHash(flat_list)

    for key, value in chm.items():
      _items.append(f"{key!r}: {value!r}")


    print(_items)
    #runLinProbeHash(inp_data)
    #runQuadHash(inp_data)
    #print(inp_data)