import sympy as sp

# Define variables
x, lam = sp.symbols('x lam', nonnegative=True)

# Objective and constraint
f = x**2
g = 2 - x   # inequality constraint: x <= 2

# Lagrangian
L = f + lam * g

# KKT conditions
eq1 = sp.diff(L, x)       # stationarity: ∂L/∂x = 0
eq2 = lam * g             # complementary slackness: λ * g(x) = 0

# Solve system
solutions = sp.solve((eq1, eq2), (x, lam), dict=True)

print("Possible Solutions:")
print(solutions)

# Check feasibility and optimality
for sol in solutions:
    x_val = sol[x]
    lam_val = sol[lam]

    if x_val <= 2 and lam_val >= 0:   # primal feasibility & dual feasibility
        print("\nOptimal Solution")
        print("x =", x_val)
        print("Lambda =", lam_val)
        print("Objective Value =", f.subs(x, x_val))
