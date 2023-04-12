# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_bank.py                                      #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value


def test_number():
    assert value("0123456789") == 100
    assert value("01234 56789") == 100


def test_upper_case():
    assert value("HELLO SIR") == 0
    assert value("HEY") == 20
    assert value("WHAT") == 100


def test_lower_case():
    assert value("hello my name is") == 0
    assert value("her") == 20
    assert value("welcome") == 100


def test_punctuation():
    assert value("What's happening?") == 100
    assert value("Hello my name is...!;") == 0
    assert value("Her.,--") == 20
