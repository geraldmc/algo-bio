#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pre_process(f):
  """Preprocess input.
  """
  l2 = ''
  try:
    with open(f) as reader:
      try:
        contents = reader.read()
        l1 = contents.split('\n\n')
        l2 = [l.split('\n') for l in l1]
      except (IOError, OSError):
        print("Error reading from file")
  except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file. Please try again.")
  return l2[:-1] 
