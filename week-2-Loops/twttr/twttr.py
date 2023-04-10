# ----------------------------------------------- #
#  Course: CS50P                                  #
#  https://cs50.harvard.edu/python/2022/          #
# ----------------------------------------------- #
#  File Name: twttr.py                            #
#  By: Yasin Maden <maden.yasin@hotmail.com>      #
# ----------------------------------------------- #

#  https://cs50.harvard.edu/python/2022/psets/2/twttr/


def main():
    user_text = input("Input: ")
    print("Output:", remove_vowel_char(user_text))


def remove_vowel_char(s):
    edited_text = ""
    for ch in s:
        if not isvowel(ch):
            edited_text += ch
    return edited_text


def isvowel(ch):
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
