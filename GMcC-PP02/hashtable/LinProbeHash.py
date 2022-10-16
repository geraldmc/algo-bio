# LinProbeHash.py

from hashtable.BaseHash import BaseHash 

class LinProbeHash(BaseHash):
  def __init__(self, capacity):
    super().__init__(capacity)

  def __insert__(self):
    print('insert from LinProbeHash')