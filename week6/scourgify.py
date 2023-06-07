import sys
import csv

def main():
    is_valid()
    csv1 = get_csv1()
    sort_csv1(csv1)

def is_valid():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) != 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".csv") == False or \
          sys.argv[2].endswith(".csv") == False:
        print("Not a CSV file")
        sys.exit(1)

def get_csv1():
    csv1 = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv1.append({"name": row["name"], "house": row["house"]})
            return csv1
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

def sort_csv1(csv1):
    with open(sys.argv[2], "w") as file:
        header = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in csv1:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})

main()