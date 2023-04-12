# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_plates.py                                    #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/5/test_plates/


from plates import is_valid


def test_len():
    assert is_valid("AAAAAAA") == False
    assert is_valid("A") == False


def test_punctuation():
    assert is_valid("AA.AAA") == False


def test_start_with_zero():
    assert is_valid("YY01") == False


def test_number_location():
    assert is_valid("YY11MM") == False


def test_number():
    assert is_valid("123456") == False
