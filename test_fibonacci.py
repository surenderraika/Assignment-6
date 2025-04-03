import pytest
from fibonacci import Fibonacci

def test_non_integer_input():
    with pytest.raises(ValueError):
        Fibonaci("not a number")

def test_zero_input():
    assert list(Fibonacci(0)) == [0]

def test_one_input():
    assert list(Fibonacci(1)) == [0, 1]

def test_two_input():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_four_input():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]

def test_ten_input():
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_negatve_input():
    assert list(Fibonaci(-1)) == []
