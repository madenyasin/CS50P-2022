# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_um.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/um/

import pytest
from um import count


def test_null_text():
    assert count("") == 0


def test_only_numbers():
    assert count("0123456789") == 0


def test_valid_input():
    assert count("umarım ummm um merhaba mum") == 1
    assert count("gumruk memuru") == 0


def test_white_space():
    assert count("           um") == 1
    assert count("           um                 ") == 1
    assert count("           um   um  ") == 2


def test_ignore_case():
    assert count("UM aaa UM") == 2
    assert count("um umarım UM um") == 3
