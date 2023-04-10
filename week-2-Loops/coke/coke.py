# ----------------------------------------------- #
#  Course: CS50P                                  #
#  https://cs50.harvard.edu/python/2022/          #
# ----------------------------------------------- #
#  File Name: coke.py                             #
#  By: Yasin Maden <maden.yasin@hotmail.com>      #
# ----------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/2/coke/


def main():
    amount = 50
    total_coin = 0
    while total_coin < amount:
        print("Amount Due:", amount - total_coin)
        insert = int(input("Insert Coin: "))
        if insert in [5, 10, 25]:
            total_coin += insert
    print("Change Owed:", total_coin - amount)


if __name__ == "__main__":
    main()
