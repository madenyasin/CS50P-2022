# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_working.py                                   #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/working/

import pytest
from working import convert


def test_limit_value():
    assert convert("12 am to 12 pm") == "00:00 to 12:00"
    assert convert("00 am to 12 pm") == "00:00 to 12:00"


def test_extra_minutes():
    with pytest.raises(ValueError):
        convert("12:61 to 12 pm")


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("11 am - 11 pm ")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("10:00 - 11:00")
