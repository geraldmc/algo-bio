#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
from random import choice
import time

# https://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna

def weightedchoice(items): # doesn't require numbers to add up to 100
	return choice("".join(x * y for x, y in items))

def dna_str(length, weighted=False):
  ''' Generates a DNA string of user-defined length. 
      Use the keyword arg `weighted` to make it more biologically
      interesting.
  '''
  dna=""
  CHOICE1 = [('C', 10), ('G', 30), ('A', 30), ('T', 30)] # no relevance!
  for count in range(length):
    if weighted:
      dna+=weightedchoice(CHOICE1)
    else:
      dna+=choice("CGTA")
  return dna

def profile(f):
  ''' Function to profile a (possibly recursive) function. This uses
      Python's `nonlocal` keyword. The nonlocal keyword works with variables 
      inside nested functions, where the variable should not belong to the 
      inner function.
  ''' 
 
  is_evaluating = False # handles nested recursion
  def g(x,y):
    nonlocal is_evaluating # useful with variables inside nested functions
    if is_evaluating:
      return f(x,y)
    else:
      start_time = time.perf_counter()
      is_evaluating = True
      try:
          value = f(x,y)
      finally:
          is_evaluating = False
      end_time = time.perf_counter()
      print('Value {} had elapsed time (sec): {time}'.format(value, time=end_time-start_time))
      return value
  return g

def call_counter(f):
  """
  Adds a ".calls" variable to the function that increments w/every call.
  """
  def wrapped(*args, **kwargs): # deal with any/all arguments
      wrapped.calls += 1
      return f(*args, **kwargs) # call the real function here
  wrapped.calls = 0
  return wrapped

def print_LCS(X,Y,Z):
  ''' Function to print all sequence combinations
  '''
  print('LCS of {} and {} is: \n {} with length of: {}'.format(X, Y, Z[1], Z[0]))
  print()
  # end print_LCS --------------------------------------------------------------