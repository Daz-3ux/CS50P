from hello import hello

def main():
    test_default()
    test_arugment()

def test_default():
    assert hello() == "Hello, world"

def test_arugment():
    assert hello("David") == "Hello, David"

if __name__ == "__main__":
    main()