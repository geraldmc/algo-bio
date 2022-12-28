#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashtables.LinearProbing import LinearProbing
from hashtables.QuadraticProbing import QuadraticProbing
from hashtables.SeparateChaining import SeparateChaining
from analysis.metrics import *
from filehandler.io import *

f = './data/hundred_ten.txt'

lph = LinearProbing()
qdp = QuadraticProbing()
sch = SeparateChaining()

assert len(lph.table) == 120
assert len(qdp.table) == 120
assert len(sch.table) == 120

inp_data = []
raw_input = pre_process(f)

for s in raw_input:
  inp_data.append([int(i) for i in s])
data = [item for sub in inp_data for item in sub]

print('Number of data elements to be entered into table: {}'.format(len(data)))
print()
print('slots remaining for linear scheme before data entry: {}'.format(lph.slots_remaining))
print('slots remaining for quadratic scheme before data entry: {}'.format(qdp.slots_remaining))
print('slots remaining for separate chain before data entry: {}'.format(sch.slots_remaining))
for item in data:
  lph.insert(item)
  qdp.insert(item)
  sch.insert(item)
print()
print('slots remaining for linear scheme after data entry: {}'.format(lph.slots_remaining))
print('slots remaining for quadratic scheme after data entry: {}'.format(qdp.slots_remaining))
print('slots remaining for separate scheme after data entry: {}'.format(sch.slots_remaining))