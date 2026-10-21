# test_calculator.py
import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(1,2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5,2) == 3

def test_mul():
    assert mul(3,4) ==12

def test_div():
    assert div(6,2) ==3
    with pytest.raises(ZeroDivisionError):
        div(1,0)
