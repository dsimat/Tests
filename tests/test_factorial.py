import pytest

from test_package.factorial import factorial


def test_positive():
    """5! == 120"""
    assert factorial(5) == 120


def test_zero():
    """0! == 1"""
    assert factorial(0) == 1


def test_negative():
    """Factorial of negative number raises ValueError"""
    with pytest.raises(ValueError):
        factorial(-1)
