# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    numb3rs.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        numbers = list(map(int, ip.split(".")))

        # çeşitli kontroller
        if len(numbers) != 4:
            return False

        for number in numbers:
            if not 0 <= number <= 255:
                return False

        # ip adresi için gerekli kurala uyuyor mu?
        if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip, re.IGNORECASE):
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    main()
