# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    taqueria.py                                       #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/3/taqueria/


def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    menu = make_key_lower(menu)
    amount = 0

    while True:
        try:
            item = input("Item: ").lower()
            if item in menu:
                amount += menu[item]
                print("Total: ${:.2f}".format(amount))
        except EOFError:  # catch (CTRL + D)
            return


def make_key_lower(dic):
    new_dic = {}
    for key in dic:
        new_dic[key.lower()] = dic[key]
    return new_dic


if __name__ == "__main__":
    main()
