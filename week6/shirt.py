import sys
from PIL import Image, ImageOps

def main():
    is_valid()
    make_image()

def is_valid():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) != 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[2][-4:] not in [".jpg", ".png", "jpeg"]:
        print("Invalid output")
        sys.exit(1)
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        print("Input and output have different extensions")
        sys.exit(1)

def make_image():
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("1")

if __name__ == "__main__":
    main()