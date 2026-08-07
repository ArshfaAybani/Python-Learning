# Compound Interest Calculator

A simple command-line application written in Python that calculates the final balance using the **compound interest formula**. The program validates user input to ensure the principal amount, interest rate, and time are greater than zero before performing the calculation.

## Features

* Calculates compound interest
* Validates user input using `while` loops
* Prevents zero or negative values
* Uses Python's built-in `pow()` function
* Simple and beginner-friendly command-line interface

## Concepts Practiced

* Variables
* User input (`input()`)
* Type conversion (`float`, `int`)
* `while` loops
* Conditional statements (`if`)
* Input validation
* Mathematical calculations
* Formatted output (f-strings)

## Formula Used

```text
A = P × (1 + r/100)^t
```

Where:

* **A** = Final Amount
* **P** = Principal Amount
* **r** = Annual Interest Rate (%)
* **t** = Time (years)

## How to Run

1. Ensure Python 3 is installed.
2. Clone this repository.

```bash
git clone https://github.com/ArshfaAybani/Python-learning.git
```

3. Navigate to the project folder.

```bash
cd Compound Calculator
```

4. Run the program.

```bash
python compoundCalc.py
```

## Example

```text
Enter your principal amount: 10000
Enter your rate amount: 8
Enter your time(in yrs) amount: 5

Your Balance after 5 years is 14693.28
```

## Future Improvements

* Round the final balance to two decimal places
* Display the total interest earned separately
* Support different compounding frequencies (monthly, quarterly, annually)
* Add exception handling for non-numeric input
* Create a graphical user interface (GUI)
