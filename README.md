# Scientific Calculator

## Overview

This is a menu-driven command-line scientific calculator written in Python. It provides common arithmetic and scientific operations, then displays the result in the terminal.

## Features

- Basic calculations: addition, subtraction, multiplication, and division
- Powers and real square roots
- Trigonometric functions: sine, cosine, and tangent (input angles in degrees)
- Logarithms with base 10 or base *e*
- Mean and median for a list of comma-separated numbers
- Square roots of complex numbers
- Input handling for invalid values and oversized results
- Division-by-zero protection

## Technologies and tools

- Python 3
- Python standard-library modules: `math`, `cmath`, and `statistics`
- A terminal or command prompt

No third-party packages are required.

## Installation and running

1. Install Python 3 if it is not already installed. Confirm it is available with `python --version` (on some systems, use `python3 --version`).
2. Save the calculator code in a file named `scientific_calculator.py`.
3. Open a terminal in the folder containing that file.
4. Run:

   ```bash
   python scientific_calculator.py
   ```

   On systems where the Python command is `python3`, run `python3 scientific_calculator.py` instead.
5. Choose an operation by entering its menu number. Enter `0` to exit.

## Testing instructions

Run the program and try the following manual checks:

| Check | Example input | Expected result |
| --- | --- | --- |
| Addition | Choose `1`, then `8`, `+`, `2` | `Answer: 10.0` |
| Division by zero | Choose `1`, then `8`, `/`, `0` | A division-by-zero message |
| Power | Choose `2`, then `2` and `3` | `Answer: 8.0` |
| Square root | Choose `3`, then `9` | `Answer: 3.0` |
| Negative real square root | Choose `3`, then `-4` | A message that a negative number has no real square root |
| Trigonometry | Choose `4`, then `30` and `sin` | `Answer: 0.5` |
| Logarithm | Choose `5`, then `100` and `10` | `Answer: 2.0` |
| Mean and median | Choose `6`, then `1, 2, 3` | Mean and median both `2.0` |
| Complex square root | Choose `7`, then `3+4j` | A complex square-root result |
| Invalid input | Enter text where a number is requested | An invalid-input message |

