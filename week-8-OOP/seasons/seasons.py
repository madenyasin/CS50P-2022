# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    seasons.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/8/seasons/

from datetime import date
import inflect
import sys


def main():
    try:
        print(age_calculate(input("Date of Birth: ").strip()))
    except ValueError:
        sys.exit("Invalid Date")


def age_calculate(birth_date):
    birth_date = date.fromisoformat(birth_date)
    today = date.today()
    difference = today - birth_date
    return convert_to_words(difference.days * 24 * 60)


def convert_to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
