# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    um.py                                             #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/um/


import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\w*um\w*"
    matches = re.findall(pattern, s, re.IGNORECASE)
    i = 0
    for match in matches:
        if match.lower() == "um":
            i += 1
    return i


if __name__ == "__main__":
    main()


# import re
# import sys
# import re

# def main():


#     # s = "um"
#     # pattern = r"^um$" # metin sadece um ise eşleşme olur
#     # matches = re.findall(pattern, s)
#     # print(matches)

#     # s = "amanın"
#     # pattern = r"um" # str'de 'um' metninin geçtiği her noktada eşleşir
#     # matches = re.findall(pattern, s)
#     # print(matches)


#     # s = "umumraniye"
#     # pattern = r"^um" # yalnızca başlangıc um ile başlarsa eşleşme var
#     # matches = re.findall(pattern, s)
#     # print(matches)


#     # s = "umarımum um"
#     # pattern = r"um$"
#     # matches = re.findall(pattern, s)
#     # print(matches)


# if __name__ == "__main__":
#     main()
