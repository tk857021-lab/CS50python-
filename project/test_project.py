from project import (
    CHOICES,
    get_computer_choice,
    get_player_choice,
    play_again,
    result,
)


def test_result_tie():
    for choice in CHOICES:
        assert result(choice, choice) == "player and computer tie"


def test_result_player_wins():
    assert result("rock", "paper") == "player win"
    assert result("paper", "scissors") == "player win"
    assert result("scissors", "rock") == "player win"


def test_result_computer_wins():
    assert result("rock", "scissors") == "computer win"
    assert result("paper", "rock") == "computer win"
    assert result("scissors", "paper") == "computer win"


def test_get_computer_choice():
    for _ in range(100):
        assert get_computer_choice() in CHOICES


def test_get_player_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: " ROCK ")
    assert get_player_choice() == "rock"


def test_get_player_choice_reprompts(monkeypatch):
    answers = iter(["banana", "", "paper"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert get_player_choice() == "paper"


def test_play_again(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert play_again() is True
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert play_again() is False
