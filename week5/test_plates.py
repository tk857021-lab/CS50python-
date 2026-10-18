
from plates import is_valid


def test_length():
    assert is_valid("CS") == True          # shortest allowed
    assert is_valid("CS50") == True
    assert is_valid("CS5050") == True      # longest allowed
    assert is_valid("C") == False          # too short
    assert is_valid("CS50P2X") == False    # too long


def test_starts_with_letters():
    assert is_valid("AAA222") == True
    assert is_valid("50CS") == False       # starts with digits
    assert is_valid("C5") == False         # only one leading letter


def test_numbers_at_end():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False      # letter after a digit
    assert is_valid("CS05") == False       # first digit is 0


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False      # a space
    assert is_valid("HELLO!") == False
