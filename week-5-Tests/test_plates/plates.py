def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    results = []
    results.append(first_two_chars_are_letters(s))
    results.append(check_plate_len_rule(s))
    results.append(check_plate_number_rule(s))

    if False in results:
        return False
    else:
        return True


def first_two_chars_are_letters(s):
    if len(s) < 2:
        r = len(s)
    else:
        r = 2
    for i in range(r):
        if not s[i].isalpha():
            return False
    return True


def check_plate_len_rule(s):
    if s.isalnum() and 2 <= len(s) <= 6:
        return True
    return False


def check_plate_number_rule(s):
    i = 0
    for c in s:
        if c.isdigit():
            i += 1
            if i == 1 and c == "0":
                return False
        else:
            if i != 0:
                return False
    return True


if __name__ == "__main__":
    main()
