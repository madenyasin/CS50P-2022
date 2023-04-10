# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    tip.py                                            #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/0/tip/


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):  # $##.## to ##.#
    # TODO
    # return float(d.replace("$", ""))
    return float(d.strip("$"))


def percent_to_float(p):  #  ##% to 0.##
    # TODO
    # return float(p.replace("%", "")) / 100
    return float(p.strip("%")) / 100


main()
