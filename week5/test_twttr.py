from twttr import shorten

def main():
    test_twitter()

def test_twitter():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWIttEr") == "TWttr"
    assert shorten("123") == "123"
    assert shorten("da.") == "d."