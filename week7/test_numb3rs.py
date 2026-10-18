from numb3rs import validate


def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_number_too_big():
    assert validate("256.1.1.1") == False
    assert validate("1.1.1.300") == False


def test_wrong_count():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False


def test_not_numbers():
    assert validate("cat") == False
    assert validate("1.2.3.cat") == False
    assert validate("") == False
