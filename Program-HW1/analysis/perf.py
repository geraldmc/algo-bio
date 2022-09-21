#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""perf.py: Functions for analyzing performance."""

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 1"
__class__       = "605.620"
__semester__    = "Fall, 2022"

def call_counter(f):
    """
    Adds a ".calls" variable to the function that increments w/every call.
    Must be set it to zero between iterations.  
    Example:
        @call_counter
        def sumallbelow(x):
          if x<1:
            return 0
          return x + sumallbelow(x-1)
    """
    def wrapped(*args, **kwargs): # deal with any/all arguments
        wrapped.calls += 1
        return f(*args, **kwargs) # call the real function here
    wrapped.calls = 0
    return wrapped