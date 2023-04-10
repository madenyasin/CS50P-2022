# ---------------------------------------------------- #
#    Course: CS50P                                     #
#    https://cs50.harvard.edu/python/2022/             #
# ---------------------------------------------------- #
#    grocery.py                                        #
#    By: Yasin Maden <maden.yasin@hotmail.com>         #
# ---------------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/3/grocery/


def main():
    grocery_list = []

    while True:
        try:
            item = input().upper()
            grocery_list.append(item)
        except EOFError:
            #  sözlükler başlatıldı
            grocery_dic = {}
            sorted_dic = {}

            #  sadece farklı ögeleri yeni sözlüğe ata
            for item in grocery_list:
                if not item in grocery_dic:
                    grocery_dic[item] = grocery_list.count(item)

            # sözlükteki anahtarları alfabetik sıralayıp yeni listeye ata
            sorted_list = sorted(grocery_dic.keys())

            #  sıralı listeyi sözlüğe çevirip eski sözlükten değerleri aldık
            for item in sorted_list:
                if item in grocery_dic:
                    sorted_dic[item] = grocery_dic[item]

            #  yazdır
            for item in sorted_dic:
                print("{} {}".format(sorted_dic[item], item))

            return


if __name__ == "__main__":
    main()
