# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    faces.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/0/faces/


def main():
    text = input("Enter text: ")
    convert(text)


def convert(s):
    s = s.replace(":)", "🙂").replace(":(", "🙁")
    print(s)


main()
