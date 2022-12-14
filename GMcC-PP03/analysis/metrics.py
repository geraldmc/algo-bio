#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
from random import choice

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