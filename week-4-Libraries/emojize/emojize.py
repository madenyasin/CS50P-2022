# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    emojize.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/emojize/

import emoji


def main():
    user_input = input("Input: ")
    print("Output: " + emoji.emojize(user_input))


if __name__ == "__main__":
    main()
