import sympy as sp

x = sp.Symbol('x')

#Function
n = int(input("Degree of the function : "))
coefficients = []
for i in range(n + 1):
    coeff = int(input(f"Enter coefficient for x^{n-i}: "))
    coefficients.append(coeff)

f_x = 0
for i, coeff in enumerate(coefficients):
    f_x += coeff * (x**(n-i))

print("\nThe function is: ")
display(f_x)

#First derivative
f_x_first = sp.diff(f_x, x)
print("\nThe first derivative of the function is:")
display(f_x_first)

# Critical points
critical_points = sp.solve(f_x_first, x)
print("\nCritical points (x where first derivative is 0):")
for point in critical_points:
    print(f"x = {point}")

# Second derivative
f_x_double = sp.diff(f_x_first, x)
print("\nThe second derivative of the function is:")
display(f_x_double)

print("\nPoints of local maxima/minima:")
for point in critical_points:
    y_value = f_x.subs(x, point)
    second_value = f_x_double.subs(x, point)
    if second_value > 0:
        print(f"Local Minimum: at x = {point}, value of f(x) = {y_value},  The Point is : ({point}, {y_value})\n")
    elif second_value < 0:
        print(f"Local Maximum: at x = {point}, value of f(x) = {y_value},  The Point is : ({point}, {y_value})\n")
    else:
        print(f"Second derivative test inconclusive: at x = {point}, value of f(x) = {y_value},  The Point is : ({point}, {y_value})\n")
