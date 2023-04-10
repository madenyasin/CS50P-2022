# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    bitcoin.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import json
import sys


def main():
    # argüman sayısı kontrolleri
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) != 2:
        sys.exit("Too many argument!")

    # argümanın sayısal değer olduğundan emin oluyoruz
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        price = o["bpi"]["USD"]["rate_float"]  # veri ayıklama işlemi
        amount = price * number
        print(f"${amount:,.4f}")
    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
