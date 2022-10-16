# QuadHash.py

BLANK = object()

class QuadHash:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]