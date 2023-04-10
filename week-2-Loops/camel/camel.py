# ----------------------------------------------- #
#  Course: CS50P                                  #
#  https://cs50.harvard.edu/python/2022/          #
# ----------------------------------------------- #
#  File Name: camel.py                            #
#  By: Yasin Maden <maden.yasin@hotmail.com>      #
# ----------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/2/camel/


def main():
    camel_case = input("camelCase: ")
    print(convert_snake_case(camel_case))


def convert_snake_case(veriable_name):
    snake_case = ""
    for ch in veriable_name:
        if ch.isupper():
            snake_case += "_"
            snake_case += ch.lower()
        else:
            snake_case += ch
    return snake_case


if __name__ == "__main__":
    main()
