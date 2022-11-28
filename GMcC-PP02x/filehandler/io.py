#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 

def pre_process(f):
  """Preprocess file input.
  """
  result = ''
  try:
    with open(f) as reader:
      try:
        contents = reader.read()
        l1 = contents.split('\n\n')
        result = [l.split('\n') for l in l1]
      except (OSError):
        print("Error reading from file")
  except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file. Please try again.")
  return result[:-1] 

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def divide_chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i+n]

def print_5iter(generator):
  try:
    assert next(generator, None) is not None
  except AssertionError:
    print('Iterator was exhausted when print statement called.')
  print()
  while True:
    try:
      a,b,c,d,e = next(generator)
    except (StopIteration, ValueError):
      break
    print(a,b,c,d,e)
  print()

def print_3iter(generator):
  try:
    assert next(generator, None) is not None
  except AssertionError:
    print('Iterator was exhausted when print statement called.')  
  print()
  while True:
    try:
      a,b,c = next(generator)
    except (StopIteration):
      break
    print(a,b,c)
  print()

def traverse(o, tree_types=(list, tuple)):
  ''' print(list(traverse(inp_data)))
  '''
  if isinstance(o, tree_types):
    for value in o:
      for subvalue in traverse(value, tree_types):
        yield subvalue
  else:
    yield o

def output_results_to(data, f=None):
  if f is None:
    pass
  else:
    pass