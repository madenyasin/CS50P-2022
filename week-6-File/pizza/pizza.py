# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    pizza.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/6/pizza/

from tabulate import tabulate
import csv
import sys


def main():
    # argüman kontrolleri
    arg_len = len(sys.argv)
    if arg_len == 1:
        sys.exit("Too few command-line arguments")
    elif arg_len > 2:
        sys.exit("Too many command-line arguments")
    else:
        # dosya adının son 4 harfi kırpılıyor
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")

    file_path = sys.argv[1]
    headers, table = get_data_csv(file_path)
    print(tabulate(table, headers, tablefmt="grid"))


def get_data_csv(file_path):
    try:
        headers = []
        table = []
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            headers = reader.fieldnames
            for row in reader:
                table.append([row[headers[0]], row[headers[1]], row[headers[2]]])
        return headers, table
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()


# >>> table = [["spam",42],["eggs",451],["bacon",0]]
# >>> headers = ["item", "qty"]
# >>> print(tabulate(table, headers, tablefmt="grid"))
