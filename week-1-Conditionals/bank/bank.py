# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    bank.py                                           #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/1/bank/


def main():
    speech = formatter(input("Greeting: "))
    if "hello" in speech:
        print("$0")
    elif speech[0] == "h":
        print("$20")
    else:
        print("$100")


def formatter(s):
    return s.strip().lower()


main()
