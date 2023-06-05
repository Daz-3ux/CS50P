import random


def main():
    level = get_level()
    flag = 0
    score = 0
    for i in range(10):
        left, right = generate_integer(level)
        sum = left + right
        while True:
            try:
                input_num = input(f"{left} + {right} = ").strip()
                if sum == int(input_num):
                    flag = 0
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                flag += 1
                if flag == 3:
                    print(f"{left} + {right} = {sum}")
                    flag = 0
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        min_value = 0;
    else:
        min_value = 10 ** (level - 1)
    max_value = (10**level) - 1
    left = random.randint(min_value, max_value)
    right = random.randint(min_value, max_value)
    return left, right


if __name__ == "__main__":
    main()
