def main():
    while True:
        try:
            fuel_level = input("Fraction: ")
            percentage = convert(fuel_level)
            print(gauge(percentage))
            return
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        # split ile gelen elemanlar int'e çevrilip değişkenlere atanır
        first, second = map(int, fraction.split("/"))
        if second == 0:
            raise ZeroDivisionError
        elif first > second:
            raise ValueError

        return round((first / second) * 100)

    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + "%"
    except (ValueError, TypeError):
        return None


if __name__ == "__main__":
    main()
