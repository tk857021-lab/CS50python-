# Rock Paper Scissors

#### Video Demo: <https://youtu.be/6QNSO7eu43I>

#### Description:

This is a terminal version of Rock, Paper, Scissors, written in Python as my CS50P final project. You play against the computer. Each round you type `rock`, `paper` or `scissors`, the computer picks one at random, and the program prints both choices and tells you who won. After every round it asks whether you want to play again, so you can keep playing without restarting the program.

I picked this project because the rules are simple enough to finish, but the game still needs real decisions: validating what the player types, choosing at random, deciding the winner, and looping until the player quits. Each of those became its own function, which also made them easy to test.

#### How to run it:

```
python project.py
```

To run the tests:

```
pip install -r requirements.txt
pytest test_project.py
```

The game itself uses only Python's standard library (`random`). `pytest` is only needed for the tests.

#### Files:

- **`project.py`**: the game. It contains `main` and four other functions:
  - `get_player_choice()` asks the player for a move and keeps asking until the answer is `rock`, `paper` or `scissors`. It ignores capital letters and extra spaces, so ` ROCK ` counts as `rock`.
  - `get_computer_choice()` returns a random move from the list of choices.
  - `result(computer, player)` takes the two moves and returns who won, or that it was a tie.
  - `play_again()` asks `y` or `n` and returns `True` or `False`.
- **`test_project.py`**: tests for those functions, run with `pytest`.
- **`requirements.txt`**: lists `pytest`.

#### Design choices:

**A dictionary decides the winner.** My first version used a long chain of `and`/`or` conditions, and it had a bug: when the computer won, the function returned nothing, so the program printed `None`. I replaced the chain with a dictionary, `BEATS`, that says what each move defeats (`rock` beats `scissors`, `paper` beats `rock`, `scissors` beats `paper`). `result` now has three cases: a tie, the player's move beats the computer's, or otherwise the computer wins. Every combination is covered, so nothing can fall through.

**Input is checked in its own function.** Validation lives in `get_player_choice` instead of `main`. Anything that isn't a valid move, like `banana` or an empty line, just asks again, so the game never crashes or counts a typo as a loss.

**Small functions that each do one job.** Separating the pieces keeps `main` short and readable, and it let me test them one at a time. `result` and `get_computer_choice` can be tested directly. The two functions that read input are tested by replacing `input()` with `pytest`'s `monkeypatch`, so the tests don't wait for a keyboard.

**The `if __name__ == "__main__":` guard.** This lets the test file import the functions without starting a game.

#### Possible improvements:

- Keep score across rounds and show a running total.
- Add a "best of three" mode.
- Add Rock, Paper, Scissors, Lizard, Spock as a variant. The `BEATS` dictionary would need to hold more than one beaten move per entry.
