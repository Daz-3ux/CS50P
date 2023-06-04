def main():
    list = dict(sorted(upper_list().items()))
    
    for item in list:
        print(f"{list[item]} {item.upper()}")

def upper_list():
    list = {}
    while True:
        try:
            item = input("").lower()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            return list
        except ValueError:
            continue
        
main()