import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# Get user input
function_str = input(
    "Enter the two-variable function in terms of x and y\n"
    "(e.g., x**2 + y**2 - 4*x - 6*y + 13): "
)

# Convert string to SymPy expression
f = sp.sympify(function_str)

print("\nThe function is:")
print(f)

# First partial derivatives
fx = sp.diff(f, x)
fy = sp.diff(f, y)

print("\nFirst partial derivative with respect to x:")
print(fx)

print("\nFirst partial derivative with respect to y:")
print(fy)

# Find critical points
critical_points = sp.solve([fx, fy], [x, y], dict=True)

print("\nCritical Points:")
if critical_points:
    for point in critical_points:
        print(point)
else:
    print("No critical points found.")

# Second partial derivatives
fxx = sp.diff(fx, x)
fyy = sp.diff(fy, y)
fxy = sp.diff(fx, y)

print("\nSecond partial derivative fxx:")
print(fxx)

print("\nSecond partial derivative fyy:")
print(fyy)

print("\nMixed second partial derivative fxy:")
print(fxy)

# Classification
print("\nClassification of Critical Points:")

if critical_points:
    for point in critical_points:

        fxx_val = fxx.subs(point)
        fyy_val = fyy.subs(point)
        fxy_val = fxy.subs(point)

        D = fxx_val * fyy_val - (fxy_val ** 2)

        print(f"\nCritical Point: ({point[x]}, {point[y]})")
        print("fxx =", fxx_val)
        print("fyy =", fyy_val)
        print("fxy =", fxy_val)
        print("Hessian Determinant D =", D)

        # Convert to numerical values if possible
        D_num = float(D.evalf())
        fxx_num = float(fxx_val.evalf())

        if D_num > 0 and fxx_num > 0:
            print("→ Local Minimum")
        elif D_num > 0 and fxx_num < 0:
            print("→ Local Maximum")
        elif D_num < 0:
            print("→ Saddle Point")
        else:
            print("→ Test Inconclusive")
else:
    print("No critical points to classify.")
