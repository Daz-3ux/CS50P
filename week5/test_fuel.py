from fuel import convert, gauge
import pytest

def test_Val():
    with pytest.raises(ValueError):
        assert convert("5/4")

    with pytest.raises(ValueError):
        assert convert("cat/dog")
        assert convert("dd")
        assert convert("s/20")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")

def test_combain_E():
    assert convert("0/1") == 0
    assert gauge(1) == "E"
    assert convert("2/3") == 67

def test_combain_F():
    assert convert("1/1") == 100
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(12) == "12%"