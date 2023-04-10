# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    meal.py                                           #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/1/meal/


def main():
    time = input("What time is it? ").lower()
    time_f = convert(time)
    time = time_f
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes) / 60
    time = "{:.2f}".format(time)
    return float(time)


if __name__ == "__main__":
    main()
