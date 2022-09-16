#!/usr/bin/env python

"""perf.py: Functions for analyzing performance."""

__author__      = "Gerald McCollam"
__copyright__   = "Copyright 2022, Planet Earth"

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