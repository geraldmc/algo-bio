import pytest

from hashtable.Simple import *
from hashtable.ChainHash import *
from hashtable.LinProbeHash import *
from hashtable.QuadHash import *

SLOTS=120

def test_simple_none_values_when_created():
    assert None not in Simple(capacity=SLOTS).values

def test_simple_none_values_when_created():
    assert None not in ChainHash(capacity=SLOTS).values

def test_simple_none_values_when_created():
    assert None not in LinProbeHash(capacity=SLOTS).values

def test_simple_none_values_when_created():
    assert None not in QuadHash(capacity=SLOTS).values