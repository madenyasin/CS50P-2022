# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    test_jar.py                                       #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/8/jar/

from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-4)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(15)
