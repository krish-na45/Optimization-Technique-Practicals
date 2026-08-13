import sympy as sp

# Define variables
x = sp.Symbol('x')
y = 10 - x   # Constraint: x + y = 10

# Objective function
f = x**2 + y**2

print("Objective Function after substitution:")
print(sp.expand(f))

# First derivative
f_prime = sp.diff(f, x)
print("\nFirst Derivative:")
print(f_prime)

# Critical point
critical_points = sp.solve(f_prime, x)

# Second derivative
f_double = sp.diff(f_prime, x)

for point in critical_points:
    y_value = y.subs(x, point)

    print("\nOptimal Point:")
    print("x =", point)
    print("y =", y_value)

    if f_double.subs(x, point) > 0:
        print("Minimum Point")
    elif f_double.subs(x, point) < 0:
        print("Maximum Point")
    else:
        print("Test Inconclusive")

    print("Objective Function Value =", f.subs(x, point))
