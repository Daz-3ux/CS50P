def main():
    str = input("Fraction: ")
    try:
        out = convert(str)
        print(gauge(out))
    except (ValueError, ZeroDivisionError):
        pass


def convert(str):
    while True:
        str_split = str.split("/")
        x = int(str_split[0])
        y = int(str_split[1])
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            return round((x/y)*100)


def gauge(left):
    if left <= 1:
        return "E"
    elif left >= 99:
        return "F"
    else:
        return f"{left}%"


if __name__ == "__main__":
    main()
