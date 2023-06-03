str = input("Item: ").strip().lower()

calorie = 0

if str == "apple":
    calorie = 130
elif str == "avocado":
    calorie = 50
elif str == "kiwifruit":
    calorie = 90
elif str == "pear":
    calorie = 100
elif str == "sweet cherries":
    calorie = 100

if calorie != 0:
    print("Calories:", calorie)