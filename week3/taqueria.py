def main():
    menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }
    get_dish(menu)
    

def get_dish(menu):
    count = 0
    while True:
        try:
            dish = input("Item: ").lower()
            if dish in menu:
                count += float(menu[dish])
            else:
                continue
            print(f"Total: ${count:.2f}")
        except EOFError:
            print("\n")
            exit()
        except KeyError:
            continue

main()