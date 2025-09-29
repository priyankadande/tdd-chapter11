import pytest
from app import add, divide

def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_numbers():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
