import inflect
p = inflect.engine()

def main():
    names = get_names()
    names = p.join(names)
    print("Adieu, adieu, to",names)

def get_names():
    names = []
    while True:
        try:
            name = input("Input: ")
            names.append(name)
        except EOFError:
            return names
        
main()