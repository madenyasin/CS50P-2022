# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_twttr.py                                     #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten


def test_lower_case():
    assert shorten("yasinmaden") == "ysnmdn"
    assert shorten("yasin maden") == "ysn mdn"


def test_upper_case():
    assert shorten("YASINMADEN") == "YSNMDN"
    assert shorten("YASIN MADEN") == "YSN MDN"


def test_number():
    assert shorten("0123456789") == "0123456789"


def test_punctuation():
    assert shorten("!-yasin, maden.") == "!-ysn, mdn."
