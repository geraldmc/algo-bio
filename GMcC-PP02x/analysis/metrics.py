# metrics.py

from collections import Counter
import time
from functools import wraps

def profile(my_func):
  @wraps(my_func)
  def timed(*args, **kw):
    tstart = time.time()
    output = my_func(*args, **kw)
    tend = time.time()
    
    print('\tExecution Time: {:.3f} ms\n'.format((tend - tstart) * 1000))
    return output
  return timed

def distribute(items, num_containers, hash_function):
    return Counter([hash_function.hash_func(item) % num_containers for item in items])

def plot(histogram):
  for key in sorted(histogram):
    count = histogram[key]
    padding = (max(histogram.values()) - count) * " "
    print(f"{key:3} {'■' * count}{padding} ({count})")

def state_diff(s1, s2):
  print('Index', '   Diff')
  for idx, (a, b) in enumerate(zip(s1.state, s2.state)):
    if a != b:
      print(idx, '\t', a, '/', b)