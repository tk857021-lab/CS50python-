# CS50P: Introduction to Programming with Python

My journey through **Harvard's CS50P: Introduction to Programming with Python**, taught by **David J. Malan**. I completed the course, submitted every problem set, and built a final project: a **Rock, Paper, Scissors** game that runs in the terminal.

This repository contains my solutions for **every problem set** from the course, with one folder per week, plus my **final project**.

## About This Repo

- **Goal:** Learn Python step by step and build a real project
- **Course:** [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) by Harvard CS50
- **Language:** Python
- **Tools:** pytest, Git, GitHub, VS Code
- **Author:** [tk857021-lab](https://github.com/tk857021-lab)

## Project Structure

```
cs50python-/
├── week-0/    Functions, Variables
├── week-1/    Conditionals
├── week-2/    Loops
├── week-3/    Exceptions
├── week-4/    Libraries
├── week-5/    Unit Tests
├── week-6/    File I/O
├── week-7/    Regular Expressions
├── week-8/    Object-Oriented Programming
├── week-9/    Et Cetera
├── rock-paper-scissors/
│   ├── project.py
│   └── test_project.py
└── README.md
```

## Weekly Overview

| Week | Topic | What I Learned |
|------|-------|----------------|
| 0 | Functions, Variables | Writing functions, using variables, and working with strings and numbers |
| 1 | Conditionals | `if`, `elif`, `else`, boolean logic, and comparing values |
| 2 | Loops | `for` and `while` loops, lists, and dictionaries |
| 3 | Exceptions | Handling errors with `try` and `except`, and validating input |
| 4 | Libraries | Using modules such as `random`, `sys`, and `requests`, and installing packages with `pip` |
| 5 | Unit Tests | Testing code with `pytest` and `assert` |
| 6 | File I/O | Reading and writing files, CSV files, and working with images |
| 7 | Regular Expressions | Validating and cleaning text with the `re` module |
| 8 | Object-Oriented Programming | Classes, objects, methods, and decorators |
| 9 | Et Cetera | Sets, global variables, constants, type hints, and docstrings |

## Final Project: Rock, Paper, Scissors

A terminal game where you play Rock, Paper, Scissors against the computer, built with **Python only**.

**Features:**
- Play against the computer, which picks randomly using the `random` module
- Input validation, so wrong input does not crash the game
- Score tracking for you and the computer
- Clear win, lose, and draw messages for each round
- Option to play again or quit
- Functions written so they can be tested with `pytest`

**Example:**

```
Choose rock, paper, or scissors: rock
Computer chose: scissors
You win this round!

Score -> You: 1 | Computer: 0
Play again? (y/n):
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/tk857021-lab/cs50python-.git
   ```
2. Open the folder in a code editor such as VS Code.
3. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
4. Run any problem set file, for example:
   ```bash
   python week-0/indoor.py
   ```
5. To play the game:
   ```bash
   cd rock-paper-scissors
   python project.py
   ```
6. To run the tests:
   ```bash
   pip install pytest
   pytest test_project.py
   ```

## What I Learned

- Writing functions and organizing code
- Conditionals, loops, and data structures
- Handling errors and validating user input
- Using libraries and installing packages
- Writing unit tests with `pytest`
- Reading and writing files
- Cleaning and validating text with regular expressions
- Object-oriented programming
- Building a full project from scratch

## Progress

- [x] Completed all 10 weeks
- [x] Submitted every problem set
- [x] Finished the final project
- [x] Earned the CS50P certificate

## Credits

All credit for the course goes to **David J. Malan** and the **CS50 team at Harvard**. This repo is my personal work while learning.

Course link: [CS50P](https://cs50.harvard.edu/python/)

## Contact

- GitHub: [@tk857021-lab](https://github.com/tk857021-lab)
- LinkedIn: [Tushar Katara](https://www.linkedin.com/in/tushar-katara-80b20343b/)
- Gmail: [tk857021@gmail.com](mailto:tk857021@gmail.com)

---

⭐ If you are taking CS50P too, feel free to look around!
