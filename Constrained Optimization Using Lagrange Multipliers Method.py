import sympy as sp

# Define variables
x, y, lam = sp.symbols('x y lam')

# Objective function
f = x * y

# Constraint function
g = x + y - 10

# Lagrangian Function
L = f + lam * g

# Partial derivatives
eq1 = sp.diff(L, x)   # ∂L/∂x
eq2 = sp.diff(L, y)   # ∂L/∂y
eq3 = sp.diff(L, lam) # ∂L/∂λ

# Solve equations
solution = sp.solve((eq1, eq2, eq3), (x, y, lam))

print("Optimal Solution:")
print(solution)

# Objective function value
x_val = solution[x]
y_val = solution[y]

optimal_value = f.subs({x: x_val, y: y_val})

print("\nMaximum Value of Objective Function:")
print(optimal_value)
