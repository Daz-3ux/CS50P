from working import convert
import pytest

def test_singal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_complex():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_night():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_wired():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_noto():
    with pytest.raises(ValueError):
        convert("12 AM 12 PM")

def test_outofrange():
    with pytest.raises(ValueError):
        convert("12:00 AM to 25:60 PM")