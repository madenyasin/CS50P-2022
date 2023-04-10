# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    interpreter.py                                    #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/1/interpreter/


def main():
    math_operation = input("Expression: ")

    first, operator, second = find_items(math_operation)
    match operator:
        case "+":
            print(first + second)
        case "-":
            print(first - second)
        case "*":
            print(first * second)
        case "/":
            print(first / second)


def find_items(operation):
    operation_items = operation.split(" ")
    # print(operation_items)
    return float(operation_items[0]), operation_items[1], float(operation_items[2])


main()
