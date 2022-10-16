# ChainHash.py

BLANK = object()

class ChainHash:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]