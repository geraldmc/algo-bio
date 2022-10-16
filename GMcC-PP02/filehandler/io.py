#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def output_results_to(f):
  pass