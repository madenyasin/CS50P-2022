# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    extensions.py                                     #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/1/extensions/


def main():
    file_name = input("File name: ").strip().lower()
    extension_name, name = find_extension(file_name)

    match extension_name:
        case "gif" | "jpg" | "jpeg" | "png":
            print("image/" + extension_name, sep="")
        case "pdf" | "zip":
            print("application/" + extension_name, sep="")
        case "txt":
            print("text/" + name, sep="")
        case _:
            print("application/octet-stream")


def find_extension(file_name):
    file_name = file_name.split(".")
    extension_name = file_name[len(file_name) - 1]
    if extension_name == "jpg":
        extension_name = "jpeg"
    return extension_name, file_name[0]


main()
