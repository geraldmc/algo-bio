# LinProbeHash.py

BLANK = object()

class LinProbeHash:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]