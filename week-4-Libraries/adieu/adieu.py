# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    adieu.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/4/adieu/

import inflect


def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:  # crtl + d
            main_text = "Adieu, adieu, to "
            p = inflect.engine()
            print(main_text + p.join(name_list))
            break


if __name__ == "__main__":
    main()

# def main():
#     name_list = []
#     while True:
#         try:
#             name = input("Name: ")
#             name_list.append(name)
#         except EOFError: # crtl + d
#             main_text = "Adieu, adieu, to"
#             if len(name_list) == 1:
#                 print(main_text + ' ' + name_list[0])
#             elif len(name_list) == 2:
#                 print(main_text + ' ' + name_list[0] + ' and ' + name_list[1])
#             elif len(name_list) > 2:
#                 for name in name_list[:-1]:
#                     main_text += (' ' + name + ',')
#                 main_text += " and " + name_list[-1]
#                 print(main_text)
#             break
