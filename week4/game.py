import random


def main():
    level = get_positive_int("Level: ")
    computer = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")
        if guess < computer:
            print("Too small!")
        elif guess > computer:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


main()
