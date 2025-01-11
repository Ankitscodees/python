from scipy.optimize import minimize
import numpy as np

# Define the function to minimize: f(x) = (x - 2)^2 + 3
def func(x):
    return (x - 2)**2 + 3

# Initial guess
x0 = [0]

# Minimize the function
result = minimize(func, x0)

# Print the result
print("Optimal value of x:", result.x[0])
print("Minimum value of the function:", result.fun)
