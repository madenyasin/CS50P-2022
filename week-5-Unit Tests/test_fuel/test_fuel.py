# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_fuel.py                                      #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_float():
    with pytest.raises(ValueError):
        convert("1.5/1")


def test_str():
    with pytest.raises(ValueError):
        convert("three/four")


def test_number():
    assert convert("75/100") == 75


def test_percentage():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
