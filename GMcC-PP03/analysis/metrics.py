#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
from random import choice

# https://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna

def dna_string(length):
	DNA=""
	for count in range(length):
		DNA+=choice("CGTA")
	return DNA

def weightedchoice(items): # this doesn't require the numbers to add up to 100
	return choice("".join(x * y for x, y in items))

# call weightedchoice instead of choice in the loop:
#DNA+=weightedchoice([("C", 10], ("G", 20), ("A", 40"), ("T", 30)])
