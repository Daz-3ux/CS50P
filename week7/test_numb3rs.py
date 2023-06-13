from numb3rs import validate
import pytest

def test_is_true():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True

def test_is_false():
    assert validate("1.2.3.1234") == False
    assert validate("0.0.0.256") == False

def test_yourself_mesrlf():
    assert validate("127.0.0.1") == True

def test_special():
    assert validate("0.1.1.1") == False