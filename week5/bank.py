def main():
    greeting = input("Greeting: ").lower().lstrip()
    money = value(greeting)
    match money:
        case 0:
            print("$0")
        case 20:
            print("$20")
        case 100:
            print("$100")

def value(greeting):
    if greeting.find("hello", 0, 5) != -1:
        return 0
    elif greeting.find("h", 0, 1) != -1:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

