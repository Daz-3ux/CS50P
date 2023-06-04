def main():
    left = get_left()
    if left <= 0.01:
        print("E")
    elif left >= 0.99:
        print("F")
    else:
        print(f"{round(left*100)}%")
        
    

def get_left():
    while True:
        str = input("Fraction: ")
        str_split = str.split("/")
        try:
            x = int(str_split[0])
            y = int(str_split[1])
            if x > y:
              continue
            else:
              return float(x/y)
        except (ValueError, ZeroDivisionError):
            print("fuck u")
            pass
        
main()