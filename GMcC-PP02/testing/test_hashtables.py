import pytest

from hashtables import SimpleHashTable

BUCKET=100

def test_should_not_contain_none_value_when_created():
    assert None not in SimpleHashTable(capacity=BUCKET).values