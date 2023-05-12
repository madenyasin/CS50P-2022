# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    scourgify.py                                      #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys
import csv


def main():
    # argüman kontrolleri
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    elif arg_len > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("Not a CSV file")
    before_csv = sys.argv[1]
    after_csv = sys.argv[2]

    edited_data = []  # sözlük listesi oluşturulacak

    # csv dosyasındaki verileri sözlük şeklinde listemize depoluyoruz
    with open(before_csv, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = parse_name(row["name"])
            edited_data.append({"first": first, "last": last, "house": row["house"]})

    # düzenlenmiş verilerle yeni csv dosyası oluşturuluyor
    with open(after_csv, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(edited_data)


# csv dosyasındaki isimleri ad-soyad şeklinde ayırıyoruz
def parse_name(full_name):
    last, first = full_name.split(",")
    return first.lstrip(), last


if __name__ == "__main__":
    main()
