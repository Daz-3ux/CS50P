from plates import is_valid

def main():
    test_head()
    test_length()
    test_number()
    test_punc()
    test_zero()

def test_head():
    assert is_valid("C50") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("CS5000000") == False

def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_punc():
    assert is_valid("CS.") == False

def test_zero():
    assert is_valid("AS001") == False