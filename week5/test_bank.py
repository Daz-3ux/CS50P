from bank import value

def main():
    test_0()
    test_20()
    test_100()
    test_out()

def test_0():
    assert value("hello") == 0

def test_20():
    assert value("hi") == 20

def test_100():
    assert value("fuck u") == 100

def test_out():
    assert value("HELLo") == 0