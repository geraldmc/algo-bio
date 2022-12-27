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

NUM_BINS = 12 # for hash distribution map

class Tee(object):
  ''' Class object that allows printing program output to console AND TO A FILE.
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

@profile
def LinProbeHash(data, mod, depth, hash_method=1, size=120):
  lph = LinearProbing(modulus=mod, slot_depth=depth, 
                      slot_size=size, hash_method=hash_method)
  load_factor_array = []
  collisions_array = []
  for item in data:
    lph.insert(item)
    load_factor_array.append(round(lph.load_factor,3))
    collisions_array.append(str(lph.collisions))
  lph_table = ['-----' if i is None else i for i in lph.table]
  print(end='\n')
  if hash_method==1:
    print('HASH TABLE: modulus={}, slot depth={}, slot size={}, hashing method={}.'
                                      .format(mod, depth, size, 1))
  else:
    print('HASH TABLE: modulus={}, slot depth={}, slot size={}, hashing method={}.'
                                      .format(mod, depth, size, 2))
  if depth==3:
    lph_flat_table = lph.flatten(lph.table)
    lph_table = ['-----' if i is None else i for i in lph_flat_table]
    lph_iter = divide_chunks(lph_table, 3)
    print_3iter(lph_iter)
  else:
    lph_iter = divide_chunks(lph_table, 5)
    print_5iter(lph_iter)
  print('KEY DISTRIBUTION: {} bins, modulus={}, slot depth={}, slot size={}.'
                                                 .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=lph, num_containers=NUM_BINS))
  print()
  print('STATISTICS:')
  print('\tNumber of collisions: {}'.format(lph.collisions))
  print('\tLoad Factor: {}/1'.format(lph.load_factor))
  print('\tSlots occupied: {}'.format(lph.items_count))
  print('\tSlots remaining: {}'.format(lph.slots_remaining))
  print('\tSlot Depth: {}'.format(lph.slot_depth))
  print('\tSlot Size: {}'.format(lph.slot_size))

  print(end='\n')

@profile
def QuadHash(data, mod, depth, size=120, hash_method=1):
  qph = QuadraticProbing(modulus=mod, slot_depth=depth, 
              slot_size=size, hash_method=hash_method)
  load_factor_array = []
  collisions_array = []
  for item in data:
    qph.insert(item)
    load_factor_array.append(round(qph.load_factor,3))
    collisions_array.append(str(qph.collisions))
  qph_table = ['-----' if i is None else i for i in qph.table]
  print(end='\n')
  if hash_method==1:
    print('HASH TABLE: modulus={}, slot depth={}, slot size={}, hashing method={}.'
                                      .format(mod, depth, size, 1))
  else:
    print('HASH TABLE: modulus={}, slot depth={}, slot size={}, hashing method={}.'
                                      .format(mod, depth, size, 2))
  if depth==3:
    qph_flat_table = qph.flatten(qph.table)
    qph_table = ['-----' if i is None else i for i in qph_flat_table]
    qph_iter = divide_chunks(qph_table, 3)
    print_3iter(qph_iter)
  else:
    qph_iter = divide_chunks(qph_table, 5)
    print_5iter(qph_iter)
  print('KEY DISTRIBUTION: {} bins, modulus={}, slot depth={}, slot size={}.'
                                                        .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=qph, num_containers=NUM_BINS))
  print()
  print('STATISTICS:')
  print('\tNumber of collisions: {}'.format(qph.collisions))
  print('\tLoad Factor: {}/1'.format(qph.load_factor))
  print('\tSlots occupied: {}'.format(qph.items_count))
  print('\tSlots remaining: {}'.format(qph.slots_remaining))
  print('\tSlot Depth: {}'.format(qph.slot_depth))
  print('\tSlot Size: {}'.format(qph.slot_size))
  print(end='\n')

@profile
def ChainHash(data, mod, depth, size, hash_method):
  sch = SeparateChaining(modulus=mod, slot_size=size, hash_method=hash_method)
  load_factor_array = []
  collisions_array = []
  for item in data:
    sch.insert(item)
    load_factor_array.append(round(sch.load_factor,3))
    collisions_array.append(str(sch.collisions))
  sch_table = ['-----' if i is None else i for i in sch.table]
  print(end='\n')
  print('HASH TABLE: modulus={}, slot depth={}, slot size={}.'.format(mod, depth, size))
  sch_iter = divide_chunks(sch_table, 5)
  print_5iter(sch_iter)
  print('KEY DISTRIBUTION: {} bins, modulus={}, slot depth={}, slot size={}.'
                                        .format(NUM_BINS, mod, depth, size))
  print()
  plot(distribute(data, hash_function=sch, num_containers=NUM_BINS))
  print()
  print('STATISTICS:')
  print('\tNumber of collisions: {}'.format(sch.collisions))
  print('\tLoad Factor: {}/1'.format(sch.load_factor))
  print('\tSlots occupied: {}'.format(sch.items_count))
  print('\tSlots remaining: {}'.format(sch.slots_remaining))
  print('\tSlot Depth: {}'.format(sch.slot_depth))
  print('\tSlot Size: {}'.format(sch.slot_size))

  print(end='\n')

if __name__ == "__main__":
  """ Driver. 
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", dest="infile", required=True,
                    help="input file containing values to be hashed. ", 
                    type=lambda f: open(f)) 
  parser.add_argument("--output", help = "output file.")
  args = parser.parse_args()
  inp_data = []
  raw_input = pre_process(args.infile.name)
  for s in raw_input:
    inp_data.append([int(i) for i in s]) # convert to ints
  input_list = [item for sub in inp_data for item in sub]

# ------ this `tees` stdout to print to a file also.  
  f = open(args.output, 'w')
  original = sys.stdout # 
  sys.stdout = Tee(sys.stdout, f)
# ------ to get the original filehandle back...  
# sys.stdout = original
# print ("This won't appear in file")
# f.close()

# ----------------------- 11 Exercises from the Lab's Handout -----------------
  print('\n')
  print('=============== ++++++++++++++++++++++++++++++++++++ ================')
  print('=============== VARIATIONS ON HASHING - 11 EXERCISES ================')
  print('=============== ++++++++++++++++++++++++++++++++++++ ================')
  print('\n')

# Division modulo 120, bucket size=1
  print('#1 Linear Probe Grp 1 ---------------------------------------------- ')
  LinProbeHash(input_list, mod=120, depth=1)            #1
  print('-------------------------------------------------------------- end #1')
  print('#2 Quadratic Probe Grp 1 ------------------------------------------- ')
  QuadHash(input_list, mod=120, depth=1)                #2
  print('-------------------------------------------------------------- end #2')
  print('#3 Separate Chaining Grp 1------------------------------------------ ')
  ChainHash(input_list, mod=120, depth=1, 
                        hash_method=1, size=120)        #3
  print('-------------------------------------------------------------- end #3')

# Division modulo 113, bucket size=1
  print('#4 Linear Probe Grp 2 ---------------------------------------------- ')
  LinProbeHash(input_list, mod=113, depth=1)            #4
  print('-------------------------------------------------------------- end #4')
  print('#5 Quadratic Probe Grp 2 ------------------------------------------- ')
  QuadHash(input_list, mod=113, depth=1)                #5
  print('------------------------------------------------------------------ #5')
  print('#6 Separate Chaining Grp 2 ----------------------------------------- ')
  ChainHash(input_list, mod=113, depth=1, 
                        hash_method=1, size=120)        #6
  print('-------------------------------------------------------------- end #6')

# Division modulo 41, bucket size=3
  print('#7 Linear Probe Grp 3 ---------------------------------------------- ')
  LinProbeHash(input_list, mod=41, depth=3, size=40)    #7
  print('------------------------------------------------------------------ #7')
  print('#8 Quadratic Probe Grp 3 ------------------------------------------- ')
  QuadHash(input_list, mod=41, depth=3, size=40)        #8
  print('-------------------------------------------------------------- end #8')

# Division modulo 120, bucket size=1, hash_method=multiplicative (2)
  print('#9 Linear Probe Grp 4 ---------------------------------------------- ')
  LinProbeHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                          #9
  print('--------------------------------------------------------------end  #9')
  print('#10 Quadratic Probe Grp 4 ------------------------------------------ ')
  QuadHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                         #10
  print('------------------------------------------------------------- end #10')
  print('#10 Separate Chaining Grp 4 ---------------------------------------- ')
  ChainHash(input_list, mod=120, depth=1, size=120, 
                hash_method=2)                         #11
  print('------------------------------------------------------------- end #11')
