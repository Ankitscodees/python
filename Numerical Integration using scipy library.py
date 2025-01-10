from scipy.integrate import quad
import numpy as np

# Define the function to integrate
def func(x):
    return np.sin(x) ** 2

# Perform integration over the interval [0, π]
result, error = quad(func, 0, np.pi)
print(f"Integral result: {result}, Estimated error: {error}")
