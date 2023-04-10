# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    figlet.py                                         #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
from pyfiglet import Figlet


def main():
    # argümanlar gerekli koşulları sağlıyor mu kontrol ediliyor
    arg_len = len(sys.argv)
    if arg_len != 1:
        if arg_len != 3 or sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

    figlet = Figlet()
    fonts = figlet.getFonts()
    if arg_len != 1:
        f = sys.argv[2]  # font name
        # font geçerli mi kontrol ediliyor
        if f in fonts:
            figlet.setFont(font=f)
        else:
            sys.exit("Invalid usage")

    user_input = input("Input: ")

    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()
