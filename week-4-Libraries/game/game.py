# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    game.py                                           #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/game/

import random


def main():
    n = get_int("Level: ")
    destination = random.randint(1, n)  # 1 <= x <= n
    while True:
        guess = get_int("Guess: ")
        if guess < destination:
            print("Too small!")
        elif guess > destination:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_int(prompt=""):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
