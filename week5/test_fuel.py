import pytest
from fuel import convert, gauge


def test_convert_normal():
    assert convert("3/4") == 75
    assert convert("1/3") == 33


def test_convert_edges():
    assert convert("0/4") == 0
    assert convert("4/4") == 100


def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
