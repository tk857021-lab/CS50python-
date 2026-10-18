

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0


def test_h():
    assert value("h") == 20
    assert value("Hi") == 20
    assert value("How you doing?") == 20


def test_other():
    assert value("bye") == 100
    assert value("What's happening?") == 100


