def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() != True:
        return False
    size = len(s)
    if size < 2 or size > 6:
        return False
    flag = False
    flagFirst = True
    for i in range(size):
        if s[i].isnumeric():
            flag = True
            if s[i] == "0" and flagFirst:
                return False
            flagFirst = False
        if s[i].isalpha() and flag:
            return False
        if s[i] == "." or s[i] == " ":
            return False
    return True

if __name__ == "__main__":
    main()