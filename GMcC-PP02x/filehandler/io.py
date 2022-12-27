#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 

def pre_process(f):
  ''' Handle file input. '''
  
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

def divide_chunks(l, n):
  ''' Yield generator objects to print'''
  for i in range(0, len(l), n):
    yield l[i:i+n]

def print_5iter(generator):
  ''' Print a generator in fives.'''
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
  ''' Print a generator in threes. '''
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