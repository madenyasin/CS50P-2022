# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    working.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/working/

import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM

    pattern = r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)"
    # pattern = r"(\d{1,2}):?([0-5][0-9])?\s+(AM|PM)\s+to\s+(\d{1,2}):?([0-5][0-9])?\s+(AM|PM)"

    # pattern = r"(\d{1,2}):?([0-5][0-9])? (AM|PM) to (\d{1,2}):?([0-5][0-9])? (AM|PM)"

    if matches := re.search(pattern, s, re.IGNORECASE):
        items = list(matches.groups())

        for i in range(len(items)):
            if items[i] == None:
                items[i] = "00"

        if int(items[0]) < 10 and int(items[0]) != 0:
            items[0] = "0" + items[0]

        if int(items[3]) < 10 and int(items[3]) != 0:
            items[3] = "0" + items[3]

        if not 0 <= int(items[1]) <= 59 or not 0 <= int(items[4]) <= 59:
            raise ValueError

        if items[2] == "PM":
            items[0] = int(items[0]) + 12
        if items[5] == "PM":
            items[3] = int(items[3]) + 12

        if items[0] == "12" and items[2].lower() == "am":
            items[0] = "00"
        if items[3] == 24 and items[5].lower() == "pm":
            items[3] = 12

        return f"{items[0]}:{items[1]} to {items[3]}:{items[4]}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
