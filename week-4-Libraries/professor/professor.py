# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    professor.py                                      #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

right = 3
step = 0
first = None
second = None


def main():
    global right, step, first, second
    level = get_level()
    first, second = generate_integer(level)

    score = 0

    while step < 10:
        try:
            print_question(first[step], second[step])
            result = first[step] + second[step]
            answer = int(input())
            if result == answer:
                score += 1
                step += 1
            else:
                wrong_case()
        except ValueError:
            wrong_case()
            pass

    print("Score: " + str(score))


def wrong_case():
    global right, step
    right -= 1
    print("EEE")
    if right == 0:
        print_result(first[step], second[step])
        step += 1
        right = 3


def print_question(item_1, item_2):
    print(f"{item_1} + {item_2} = ", end="")


def print_result(item_1, item_2):
    print(f"{item_1} + {item_2} = {item_1 + item_2}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not 1 <= level <= 3:
                continue
            return level
        except ValueError:
            pass


def generate_integer(level):
    try:
        if not 1 <= level <= 3:
            raise ValueError("Invalid level")
        first_numbers = []
        second_numbers = []
        # levele göre sayıların aralığı belirleniyor
        if level == 1:
            min = 0
            max = 9
        elif level == 2:
            min = 10
            max = 99
        else:
            min = 100
            max = 999
        # toplama işleminin iki elemanı farklı listede tutuluyor
        for i in range(10):
            first_numbers.append(random.randint(min, max))
            second_numbers.append(random.randint(min, max))
        return first_numbers, second_numbers

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
