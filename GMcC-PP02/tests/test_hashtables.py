import pytest

from hashtables.simple import SimpleHashTable

BUCKET=100

def test_simple_only_none_value_when_created():
    assert None not in SimpleHashTable(capacity=BUCKET).values