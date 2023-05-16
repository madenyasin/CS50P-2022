# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    response.py                                       #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/7/response/

import validators

def main():
    result = validators.email(input("email: ").strip())
    if result:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()