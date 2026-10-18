import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def main():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()
        print(f"computer: {computer}, player: {player}")
        print(result(computer, player))
        if not play_again():
            break


def get_player_choice():
    while True:
        choice = input("choice (rock, paper, scissors): ").strip().lower()
        if choice in CHOICES:
            return choice


def get_computer_choice():
    return random.choice(CHOICES)


def result(computer, player):
    if computer == player:
        return "player and computer tie"
    elif BEATS[player] == computer:
        return "player win"
    else:
        return "computer win"


def play_again():
    while True:
        answer = input("play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"


if __name__ == "__main__":
    main()