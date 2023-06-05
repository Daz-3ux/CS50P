import random

while True:
    try:
        n = int(input("Level: "))
        if(n < 1):
            pass
        else:
            break
    except ValueError:
        continue


num = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < num:
            if guess < 1:
                pass
            else:
                print("Too small!")
        elif guess > num:
            if guess > n:
                pass
            else:
                print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue