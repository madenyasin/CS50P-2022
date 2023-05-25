# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_seasons.py                                   #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/8/seasons/

import pytest
from seasons import age_calculate


def test_invalid_date():
    with pytest.raises(ValueError):
        age_calculate("February 6th, 1998")
