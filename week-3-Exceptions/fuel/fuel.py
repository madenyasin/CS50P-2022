# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    fuel.py                                           #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/3/fuel/


def main():
    while True:
        try:
            fuel_level = input("Fraction: ")

            # split ile gelen elemanlar int'e çevrilip değişkenlere atanır
            first, second = map(int, fuel_level.split("/"))
            if first > second:
                continue

            fuel_percentage = round((first / second) * 100)
            if fuel_percentage <= 1:
                print("E")
            elif fuel_percentage >= 99:
                print("F")
            else:
                print(str(fuel_percentage) + "%")

            break

        # catch exceptions
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
