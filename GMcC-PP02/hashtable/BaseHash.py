# Simple.py
from abc import ABC, abstractmethod

class BaseHash(ABC):
  def __init__(self, capacity):
    self.values = capacity * [None]

  @abstractmethod
  def __insert__(self):
      pass