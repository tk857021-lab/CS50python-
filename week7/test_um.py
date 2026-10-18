from um import count


def test_single():
    assert count("um") == 1
    assert count("hello, um, world") == 1


def test_case():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("Um, um, UM?") == 3


def test_inside_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("Um, thanks for the album") == 1


def test_none():
    assert count("hello") == 0
    assert count("") == 0


def test_punctuation():
    assert count("um?") == 1
    assert count("um, um.") == 2
