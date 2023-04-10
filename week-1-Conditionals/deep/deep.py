# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    deep.py                                           #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/1/deep/


def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything?\n"
    )
    answer = formatter(answer)
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")
    else:
        print("No")


def formatter(s):
    return s.strip().lower()


main()
