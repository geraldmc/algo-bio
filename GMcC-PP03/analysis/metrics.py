#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
from random import choice
import time

# https://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna

def weightedchoice(items): # this doesn't require the numbers to add up to 100
	return choice("".join(x * y for x, y in items))

def dna_str(length, weighted=False):
  dna=""
  CHOICE1 = [('C', 10), ('G', 30), ('A', 30), ('T', 30)]
  for count in range(length):
    if weighted:
      dna+=weightedchoice(CHOICE1)
    else:
      dna+=choice("CGTA")
  return dna

def profile(f):
  ''' Function to profile a possibly recursive function
  '''
  is_evaluating = False
  def g(x,y):
      nonlocal is_evaluating
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
          print('Elapsed time (sec): {time}'.format(time=end_time-start_time))
          return value
  return g