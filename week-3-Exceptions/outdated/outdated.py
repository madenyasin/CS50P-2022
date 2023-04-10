# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    outdated.py                                       #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/3/outdated/


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    months_dic = {}
    i = 0

    # ayların sayısal karşılığını içeren bir sözlük oluşturuldu
    for month in months:
        i += 1
        if i <= 9:
            months_dic[month] = "0" + str(i)
        else:
            months_dic[month] = str(i)

    while True:
        try:
            date = input("Date: ")

            # tarih formatına göre ögelerine ayrıldı
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                month_and_day, year = date.split(",")
                month, day = month_and_day.split()
                month = months_dic[month]

            # ay ve gün sayısı sınırları kontrol ediliyor
            year, month, day = map(str.strip, [year, month, day])
            if not (0 < int(month) <= 12) or not (0 < int(day) <= 31):
                continue

            # sonuç
            year, month, day = map(int, [year, month, day])
            print(f"{year}-{month:02}-{day:02}")

            break

        # çeşitli hata yakalamalar
        except (ValueError, TypeError, UnboundLocalError, KeyError):
            pass
        except (EOFError, KeyboardInterrupt):
            quit("\n")


if __name__ == "__main__":
    main()
