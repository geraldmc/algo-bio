#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""driver.py
"""
import argparse, sys
from hashtables.LinearProbing import LinearProbing
from hashtables.QuadraticProbing import QuadraticProbing
from hashtables.SeparateChaining import SeparateChaining
from analysis.metrics import *
from filehandler.io import *

__author__      = "Gerald McCollam"
__assignment__  = "Programming Problem 2"
__class__       = "605.620"
__semester__    = "Fall, 2022"

NUM_BINS = 6 # for hash distribution map

class Tee(object):
  ''' Class object that allows printing  output to console AND to a file.
  '''
  def __init__(self, *files):
    self.files = files
  def write(self, obj):
    for f in self.files:
      f.write(obj)
      f.flush() # If you want the output to be visible immediately
  def flush(self) :
    for f in self.files:
      f.flush()

def is_valid_file(parser, arg):
  ''' Minimum error check on file'''
  if not os.path.exists(arg):
    parser.error("The file %s does not exist! Use the --help flag for input options." % arg)
  else:
    return arg

#def default():
#  # Support file input/ouput.
#  try:
#    inp = input("Enter file input path: ")
#  except (FileNotFoundError, IsADirectoryError):
#    print('File not found.')
#  return (inp.strip())

def LinProbeHash(data, mod, depth, hash_method=1, size=120):
  lph = LinearProbing(modulus=mod, slot_depth=depth, 
                      slot_size=size, hash_method=hash_method)
  for item in data:
    lph.insert(item)
  lph_table = ['-----' if i is None else i for i in lph.table]
  print(end='\n')
  if hash_method==1:
    print('LINEAR PROBING, hash map (mod={}, depth={}, size={}, method={})'
                                      .format(mod, depth, size, 1))
  else:
    print('LINEAR PROBING, hash map (mod={}, depth={}, size={}, method={})'
                                      .format(mod, depth, size, 2))
  if depth==3:
    lph_flat_table = lph.flatten(lph.table)
    lph_table = ['-----' if i is None else i for i in lph_flat_table]
    lph_iter = divide_chunks(lph_table, 3)
    print_3iter(lph_iter)
  else:
    lph_iter = divide_chunks(lph_table, 5)
    print_5iter(lph_iter)
  print('LINEAR hash distribution ({} bins, mod={}, depth={}, size={}).'
                                                 .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=lph, num_containers=NUM_BINS))
  print()
  print('Misc statistics:')
  print('Primary collisions: {}'.format(lph.collision_count(data)))
  print('Slots remaining: {}'.format(lph.slots_remaining))
  print('Slots used: {}'.format(lph.items_count))
  print(end='\n')
  print('--------------------------------------------------------------------END')

def QuadHash(data, mod, depth, size=120, hash_method=1):
  qph = QuadraticProbing(modulus=mod, slot_depth=depth, 
              slot_size=size, hash_method=hash_method)
  for item in data:
    qph.insert(item)
  qph_table = ['-----' if i is None else i for i in qph.table]
  print(end='\n')
  if hash_method==1:
    print('QUADRATIC PROBING, hash map (mod={}, depth={}, size={}, method={})'
                                      .format(mod, depth, size, 1))
  else:
    print('QUADRATIC PROBING, hash map (mod={}, depth={}, size={}, method={})'
                                      .format(mod, depth, size, 2))
  if depth==3:
    qph_flat_table = qph.flatten(qph.table)
    qph_table = ['-----' if i is None else i for i in qph_flat_table]
    qph_iter = divide_chunks(qph_table, 3)
    print_3iter(qph_iter)
  else:
    qph_iter = divide_chunks(qph_table, 5)
    print_5iter(qph_iter)
  print('QUADRATIC hash distribution ({} bins, mod={}, depth={}, size={}).'
                                                        .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=qph, num_containers=NUM_BINS))
  print()
  print('Misc statistics:')
  print('Primary collisions: {}'.format(qph.collision_count(data)))
  print('Slots remaining: {}'.format(qph.slots_remaining))
  print('Slots used: {}'.format(qph.items_count))
  print(end='\n')
  print('--------------------------------------------------------------------END')

def ChainHash(data, mod, depth, size, hash_method):
  sch = SeparateChaining(modulus=mod, slot_size=size, hash_method=hash_method)
  for item in data:
    sch.insert(item)
  sch_table = ['-----' if i is None else i for i in sch.table]
  print(end='\n')
  print('METHOD: Chaining, hash map (mod={}, depth={}, size={})'.format(mod, depth, size))
  sch_iter = divide_chunks(sch_table, 5)
  print_5iter(sch_iter)
  print('METHOD: Chaining hash distribution ({} bins, mod={}, depth={}, size={}).'
                                                        .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=sch, num_containers=NUM_BINS))
  print()
  print('Misc statistics:')
  print('\tPrimary collisions: {}'.format(sch.collision_count(data)))
  print('\tSlots remaining: {}'.format(sch.slots_remaining))
  print('\tSlots used: {}'.format(sch.items_count))

  print(end='\n')
  print('--------------------------------------------------------------------END')

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", dest="infile", required=True,
                    help="input file", type=lambda f: open(f)) 
  parser.add_argument("--output", help = "output file name")
  args = parser.parse_args()
  inp_data = []
  raw_input = pre_process(args.infile.name)
  for s in raw_input:
    inp_data.append([int(i) for i in s]) # convert to ints
  input_list = [item for sub in inp_data for item in sub]

# ------ this `tees` stdout to print also to a file.  
  f = open(args.output, 'w')
  original = sys.stdout # 
  sys.stdout = Tee(sys.stdout, f)
# ------ to use the original filehandle...  
# sys.stdout = original
# print ("This won't appear in file")
# f.close()

# Division modulo 120, bucket size=1 -----------------------------------------
  LinProbeHash(input_list, mod=120, depth=1)            #1
  QuadHash(input_list, mod=120, depth=1)                #2
  ChainHash(input_list, mod=120, depth=1, 
                        hash_method=1, size=120)        #3
# Division modulo 113, bucket size=1 -----------------------------------------
  LinProbeHash(input_list, mod=113, depth=1)            #4
  QuadHash(input_list, mod=113, depth=1)                #5
  ChainHash(input_list, mod=113, depth=1, 
                        hash_method=1, size=120)        #6
# Division modulo 41, bucket size=3 ------------------------------------------
  LinProbeHash(input_list, mod=41, depth=3, size=40)    #7
  QuadHash(input_list, mod=41, depth=3, size=40)        #8
# Division modulo 120, bucket size=1, hash_method=multiplicative (2) ---------
  LinProbeHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                           #9
  QuadHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                           #10
  ChainHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                           #11
# ----------------------------------- FIN -----------------------------------

