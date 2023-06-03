def main():
    print_square(3,5)

def print_square(height, width):
    for _ in range(height):
        print_row(width)
        
def print_row(width):
    print("#" * width)

main()