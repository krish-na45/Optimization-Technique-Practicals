# Critical Point Finder and Classification using SymPy

## Overview

This Python program finds and classifies the critical points of a two-variable function using symbolic differentiation provided by the SymPy library.

The program:

* Accepts a function of two variables (`x` and `y`) from the user.
* Computes first-order partial derivatives.
* Finds critical (stationary) points by solving the system:

  * ∂f/∂x = 0
  * ∂f/∂y = 0
* Computes second-order partial derivatives.
* Evaluates the Hessian determinant at each critical point.
* Classifies each critical point as:

  * Local Minimum
  * Local Maximum
  * Saddle Point
  * Inconclusive

---

## Features

* Symbolic differentiation using SymPy.
* Automatic detection of critical points.
* Hessian-based classification.
* Supports a wide range of algebraic functions.
* User-friendly command-line interface.

---

## Requirements

* Python 3.7 or later
* SymPy

Install SymPy using:

```bash
pip install sympy
```

---

## How to Run

1. Save the program as `critical_point_finder.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run:

```bash
python critical_point_finder.py
```

5. Enter a function when prompted.

Example:

```text
Enter the two-variable function in terms of x and y:
x**2 + y**2 - 4*x - 6*y + 13
```

---

## Example

### Input

```text
x**2 + y**2 - 4*x - 6*y + 13
```

### Output

```text
The function is:
x**2 - 4*x + y**2 - 6*y + 13

First partial derivative with respect to x:
2*x - 4

First partial derivative with respect to y:
2*y - 6

Critical Points:
{x: 2, y: 3}

Second partial derivative fxx:
2

Second partial derivative fyy:
2

Mixed second partial derivative fxy:
0

Classification of Critical Points:

Critical Point: (2, 3)
fxx = 2
fyy = 2
fxy = 0
Hessian Determinant D = 4

→ Local Minimum
```

---

## Mathematical Background

For a function:

```text
f(x, y)
```

### Step 1: Find Critical Points

Solve:

```text
∂f/∂x = 0
∂f/∂y = 0
```

### Step 2: Compute Second Derivatives

```text
fxx = ∂²f/∂x²
fyy = ∂²f/∂y²
fxy = ∂²f/(∂x∂y)
```

### Step 3: Hessian Determinant

```text
D = fxx * fyy - (fxy)²
```

### Classification Rules

| Condition         | Classification |
| ----------------- | -------------- |
| D > 0 and fxx > 0 | Local Minimum  |
| D > 0 and fxx < 0 | Local Maximum  |
| D < 0             | Saddle Point   |
| D = 0             | Inconclusive   |

---

## Project Structure

```text
project/
│
├── critical_point_finder.py
├── README.md
└── requirements.txt
```

---

## Author

Developed using Python and SymPy for symbolic computation and multivariable calculus analysis.
