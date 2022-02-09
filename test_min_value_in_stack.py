import pytest
from min_value_in_stack import min_stack

def test_min_stack_many():
    assert min_stack([1,2,3,-17,4]) == -17

def test_single_item():
    assert min_stack([1]) == 1

def test_empty():
    with pytest.raises(IndexError):
        min_stack([])
