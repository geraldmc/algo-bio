import pytest

from hashtable.ChainHash import ChainHash
from hashtable.LinProbeHash import LinProbeHash
from hashtable.QuadHash import QuadHash

SLOTS=120

def test_chain_none_values_when_created():
    assert None in ChainHash(capacity=SLOTS).values

def test_linear_none_values_when_created():
    assert None in LinProbeHash(capacity=SLOTS).values

def test_quad_none_values_when_created():
    assert None in QuadHash(capacity=SLOTS).values