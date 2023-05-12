# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    shirt.py                                          #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/6/shirt/

import os
import sys
from PIL import Image, ImageOps


def main():
    # argüman kontrolleri
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    elif arg_len > 3:
        sys.exit("Too many command-line arguments")
    else:
        in_extension = os.path.splitext(sys.argv[1])[1]
        out_extension = os.path.splitext(sys.argv[2])[1]
        # dosya formatı kontrolü
        valid_format = [".jpg", ".jpeg", ".png"]
        if not in_extension in valid_format:
            sys.exit("Invalid input")
        if not out_extension in valid_format:
            sys.exit("Invalid output")
        # dosya formatları birbirinden farklı mı kontrol ediliyor
        if in_extension != out_extension:
            sys.exit("Input and output have different extensions")

    input = sys.argv[1]
    output = sys.argv[2]

    paste_shirt(input, output)


def paste_shirt(input, output):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(input) as input_img:
                # gorselin boyutu shirt.png boyutuna eşitleniyor
                input_img = ImageOps.fit(input_img, shirt.size)
                # shirt.png görsele yapıştırılıyor
                input_img.paste(shirt, shirt)
                # yeni görsel diske kaydediliyor
                input_img.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
