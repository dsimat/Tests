from test_package.factorial import factorial
import pytest


def test_positive():
    assert factorial(5) == 120


def test_zero():
    assert factorial(0) == 1


def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)
