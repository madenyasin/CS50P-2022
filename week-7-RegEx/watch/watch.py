# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    watch.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    regex = (
        r'<iframe(?:.+)(?:http|https)://(?:www\.)?youtube\.com/embed/(\w+)"></iframe>'
    )
    if matches := re.search(regex, s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"

    return None


if __name__ == "__main__":
    main()
