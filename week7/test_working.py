import pytest
from working import convert


def test_hours_only():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_with_minutes():
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("8:45 AM to 12:15 PM") == "08:45 to 12:15"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_bad_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_bad_times():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
