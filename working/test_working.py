from working import convert
import pytest

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("17 PM to 13 AM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("11:60 AM to 10:67 PM")

def test_correct():
    assert convert("12:45 AM to 7 PM")