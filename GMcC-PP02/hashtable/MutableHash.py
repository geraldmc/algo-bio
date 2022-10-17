try:
  from collections.abc import MutableMapping
except ImportError:
  from collections import MutableMapping

class MutableHash(MutableMapping):
  """Base class extends Python's MutableMapping."""
  def __init__(self):
    super().__init__()

  def __delitem__ (self):
    pass

  def __getitem__ (self):
    pass

  def __iter__ (self):
    pass

  def __len__ (self):
    pass

  def __setitem__ (self):
    pass

  class _Item:
    """Stores key-value pairs private."""
    
    __slots__ = '_key', '_value'
  
    def __init__(self, k, v): 
      self._key = k
      self._value = v
  
    def __eq__(self, other): # compare items based on their keys
      return self._key == other._key
  
    def __ne__(self, other):  # opposite of __eq__
      return not (self == other)
  
    def __lt__(self, other):
      return self._key < other._key # compare items based on their keys