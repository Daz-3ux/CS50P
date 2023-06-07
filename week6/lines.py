import sys

def main():
    is_valid()
    cnt = cnt_lines()
    print(cnt)

def is_valid():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        exit(1)
    elif len(sys.argv) != 2:
        print("Too many command-line arguments")
        exit(1)
    elif sys.argv[1].endswith(".py") == False:
        print("Not a Python file")
        exit(1)

def cnt_lines():
    cnt = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#"):
                    continue
                elif line == "":
                    continue
                else:
                    cnt += 1
    except FileNotFoundError:
        print("File does not exist")
        exit(1)
    return cnt

main()
