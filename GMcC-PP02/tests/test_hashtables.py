# test_hashtables.py

import pytest

from hashtable.ChainHash import ChainHash
from hashtable.LinProbeHash import LinProbeHash
from hashtable.QuadHash import QuadHash

SLOTS=120

@pytest.fixture
def hash_table():
  sample_data = ChainHash(capacity=10)
  sample_data[0] = 12501
  sample_data[1] = 84763
  sample_data[2] = 22599
  sample_data[3] = 55555
  sample_data[4] = 72501
  sample_data[5] = 99999
  sample_data[6] = 33975
  sample_data[7] = 62501
  sample_data[8] = 42501
  sample_data[9] = 11121
  return sample_data

#------------------------------------------------------------
def test_report_length_of_empty_hash_table():
    assert len(ChainHash(capacity=SLOTS)) == SLOTS
    assert len(LinProbeHash(capacity=SLOTS)) == SLOTS
    assert len(QuadHash(capacity=SLOTS)) == SLOTS
#------------------------------------------------------------
def test_none_values_when_created():
    assert None in ChainHash(capacity=SLOTS).pairs
    assert None in LinProbeHash(capacity=SLOTS).pairs
    assert None in QuadHash(capacity=SLOTS).pairs
#------------------------------------------------------------
def test_create_empty_value_slots():
  assert ChainHash(capacity=3).pairs == [None, None, None]
  assert LinProbeHash(capacity=3).pairs == [None, None, None]
  assert QuadHash(capacity=3).pairs == [None, None, None]
#------------------------------------------------------------
def test_should_insert_key_value_pairs():
  hash_chain = ChainHash(capacity=SLOTS)
  hash_probe = LinProbeHash(capacity=SLOTS)
  hash_quad = QuadHash(capacity=SLOTS)
  hash_chain[0] = 12501
  hash_probe[1] = 84763
  hash_quad[2] = 22599
  assert (0, 12501) in hash_chain.pairs
  assert (1, 84763) in hash_probe.pairs
  assert (2, 22599) in hash_quad.pairs
#------------------------------------------------------------
#@pytest.mark.skip
def test_find_value_by_key(hash_table):
  assert hash_table[0] == 12501
  assert hash_table[1] == 84763
  assert hash_table[1] != 22599
#------------------------------------------------------------

''' ----- GUTTER


'''