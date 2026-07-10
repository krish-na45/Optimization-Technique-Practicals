# Polynomial Extrema Finder

A Python program that allows users to define a single-variable polynomial function, compute its derivatives symbolically, identify critical points, and determine whether those points represent local maxima or local minima using the Second Derivative Test.

## Features

* **Interactive Polynomial Input**

  * Enter the degree of the polynomial.
  * Provide coefficients for each term from the highest degree to the constant term.

* **Symbolic Differentiation**

  * Uses the **SymPy** library to calculate the first and second derivatives symbolically.

* **Critical Point Detection**

  * Finds all values of (x) where the first derivative equals zero.

* **Extrema Classification**

  * Applies the Second Derivative Test to determine whether each critical point is a local maximum, local minimum, or inconclusive.

* **Detailed Output**

  * Displays:

    * The original polynomial function
    * First derivative
    * Second derivative
    * Critical points
    * Coordinates of local maxima and minima

---

## Technologies Used

* **Python**
* **SymPy** – Symbolic mathematics library for differentiation and equation solving

---

## Prerequisites

Before running the program, ensure that Python is installed on your system.

Install the required dependency:

```bash
pip install sympy
```

---

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
cd Polynomial-Extrema-Finder
```

2. Run the Python script:

```bash
python your_script_name.py
```

> If you are using Jupyter Notebook or Google Colab, simply execute the notebook cells.

---

## Usage

The program will prompt you to:

1. Enter the degree of the polynomial.
2. Enter the coefficient for each term, starting from the highest power down to the constant term.

### Example Input

For the polynomial:

[
f(x) = x^3 - 6x^2 + 9x + 1
]

```text
Degree of the function : 3
Enter coefficient for x^3: 1
Enter coefficient for x^2: -6
Enter coefficient for x^1: 9
Enter coefficient for x^0: 1
```

---

## Example Output

```text
The function is:
x**3 - 6*x**2 + 9*x + 1

The first derivative of the function is:
3*x**2 - 12*x + 9

Critical points (x where first derivative is 0):
x = 1
x = 3

The second derivative of the function is:
6*x - 12

Points of local maxima/minima:

Local Maximum: at x = 1, value of f(x) = 5
The Point is : (1, 5)

Local Minimum: at x = 3, value of f(x) = 1
The Point is : (3, 1)
```

---

## Mathematical Approach

### Step 1: Define the Polynomial

The user provides the polynomial degree and coefficients, and the program constructs the symbolic expression.

### Step 2: Compute the First Derivative

The first derivative (f'(x)) is calculated using SymPy.

### Step 3: Find Critical Points

Critical points are obtained by solving:

[
f'(x) = 0
]

### Step 4: Compute the Second Derivative

The second derivative (f''(x)) is calculated.

### Step 5: Apply the Second Derivative Test

For each critical point:

* If (f''(x) > 0), the point is a **local minimum**.
* If (f''(x) < 0), the point is a **local maximum**.
* If (f''(x) = 0), the test is **inconclusive**.

---

## Sample Results

For:

[
f(x) = x^3 - 6x^2 + 9x + 1
]

The program identifies:

* Local Maximum at **(1, 5)**
* Local Minimum at **(3, 1)**

---

## Future Improvements

* Support for plotting the polynomial and its critical points.
* Identification of points of inflection.
* Handling of higher-degree polynomials with complex roots.
* Graphical User Interface (GUI) version.
* Export results to text or PDF reports.

---

## License

This project is open-source and available for educational and learning purposes.
