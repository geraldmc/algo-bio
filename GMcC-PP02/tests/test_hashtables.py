import pytest

from hashtables.hash import SimpleHash1

BUCKET=100

def test_simple_only_none_value_when_created():
    assert None not in SimpleHash1(capacity=BUCKET).values