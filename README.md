# CS50P: Introduction to Programming with Python

My journey learning Python from scratch by following **CS50's Introduction to Programming with Python (CS50P)**, taught by **David J. Malan** at Harvard University.

This repository contains my solution for **every problem set** from the course, with one folder per week. At the end, I built a **Rock, Paper, Scissors** game that runs in the terminal.

## About This Repo

- **Goal:** Learn Python step by step and build a real project
- **Course:** [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) by Harvard CS50
- **Language:** Python
- **Author:** [tk857021-lab](https://github.com/tk857021-lab)

## Project Structure

```
cs50python-/
├── week-0-functions-variables/
├── week-1-conditionals/
├── week-2-loops/
├── week-3-exceptions/
├── week-4-libraries/
├── week-5-unit-tests/
├── week-6-file-io/
├── week-7-regular-expressions/
├── week-8-oop/
├── week-9-et-cetera/
├── rock-paper-scissors/
│   ├── project.py
│   └── test_project.py
└── README.md
```

Each week folder holds my submitted solutions for that week's problem set. The `rock-paper-scissors` folder holds the final project.

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
   python week-0-functions-variables/indoor.py
   ```
5. To play the game:
   ```bash
   cd rock-paper-scissors
   python project.py
   ```
6. To run the tests (if you wrote them):
   ```bash
   pip install pytest
   pytest test_project.py
   ```

## What I Learned

- Functions, variables, and data types
- Conditionals and loops
- Exceptions and error handling
- Using libraries and modules
- Writing unit tests with `pytest`
- Reading and writing files
- Regular expressions
- Object-oriented programming
- Building a full project from scratch

## Progress

- [x] Started the course
- [x] Finished all problem sets
- [x] Built the Rock, Paper, Scissors project

## Credits

All credit for the course goes to **David J. Malan** and the **CS50 team at Harvard**. This repo is only my personal practice while learning.

Course link: [CS50P](https://cs50.harvard.edu/python/)

## Contact

- GitHub: [@tk857021-lab](https://github.com/tk857021-lab)
- LinkedIn: [Tushar Katara](https://www.linkedin.com/in/tushar-katara-80b20343b/)
- Gmail: [tk857021@gmail.com](mailto:tk857021@gmail.com)

---

⭐ If you are learning Python too, feel free to look around!
