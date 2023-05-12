# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    lines.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys


def main():
    # argüman kontrolleri
    arg_len = len(sys.argv)
    if arg_len == 1:
        sys.exit("Too few command-line arguments")
    elif arg_len > 2:
        sys.exit("Too many command-line arguments")
    else:
        # dosya adının son 3 harfi kırpılıyor
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")

    file_path = sys.argv[1]
    print(lines_with_code(file_path))


def lines_with_code(file_path):
    try:
        with open(file_path) as file:
            counter = 0
            for line in file:
                line = line.lstrip()
                # yorum satırları atlanır
                if line.startswith("#"):
                    continue
                # boş satırlar atlanır
                if line == "":
                    continue
                # yalnzıca kod içeren satırlar için sayaç çalışır
                counter += 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
