import sys
from tabulate import tabulate
import csv

def main():
    is_valid()
    table = get_table()
    headers = table[0]
    print(tabulate(table[1:], headers, tablefmt="grid"))

def is_valid():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) != 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".csv") == False:
        print("Not a CSV file")
        sys.exit(1)

def get_table():
    table = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            return table
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)










main()