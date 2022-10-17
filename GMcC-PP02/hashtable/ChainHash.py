# ChainHash.py

from hashtable.BaseHash import BaseHash 

class ChainHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    pass

  def output(self):
    print("printing from ChainHash...")