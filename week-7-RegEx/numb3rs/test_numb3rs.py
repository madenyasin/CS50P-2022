# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_numb3rs.py                                   #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import pytest
from numb3rs import validate


def test_char_input():
    assert validate("a.a.a.a") == False


def test_negative():
    assert validate("-2.1.1.1") == False
    assert validate("2.-1.1.1") == False
    assert validate("-2.-1.1.1") == False


def test_limit_values():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("123.3.268.0") == False
