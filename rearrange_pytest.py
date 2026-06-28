import pytest
from arrange.py import rearrange_name

def test_rearrange_simple():
    assert rearrange_name("Turing, Alan") == "Alan Turing"
    assert rearrange_name("Curie, Marie") == "Marie Curie"
    assert rearrange_name("Einstein, Albert") == "Albert Einstein"

def test_no_comma():
    # If unsure about format, function should return the name unchanged
    assert rearrange_name("Ada Lovelace") == "Ada Lovelace"

def test_extra_spaces():
    # Ensures stripping works correctly
    assert rearrange_name("   Hopper,    Grace   ") == "Grace Hopper"
