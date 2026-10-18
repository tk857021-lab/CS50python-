from datetime import date, timedelta
import pytest
from seasons import get_birthdate, minutes_in_words


def test_one_year():
    birth = date.today() - timedelta(days=365)
    assert minutes_in_words(birth) == "Five hundred twenty-five thousand, six hundred minutes"


def test_two_years():
    birth = date.today() - timedelta(days=730)
    assert minutes_in_words(birth) == "One million, fifty-one thousand, two hundred minutes"


def test_today():
    assert minutes_in_words(date.today()) == "Zero minutes"


def test_parse_valid():
    assert get_birthdate("2000-01-01") == date(2000, 1, 1)


def test_parse_invalid():
    with pytest.raises(SystemExit):
        get_birthdate("2000/01/01")
    with pytest.raises(SystemExit):
        get_birthdate("cat")
    with pytest.raises(SystemExit):
        get_birthdate("")
