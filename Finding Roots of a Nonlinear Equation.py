from scipy.optimize import root

# Define the nonlinear function
def func(x):
    return x**3 - 5 * x + 3

# Find the root
solution = root(func, x0=0)  # Initial guess
print("Root of the equation:", solution.x)
