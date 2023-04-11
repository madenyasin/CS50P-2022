def main():
    user_text = input("Input: ")
    print("Output:", shorten(user_text))


def shorten(s):
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
