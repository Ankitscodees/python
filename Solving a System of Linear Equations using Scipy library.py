from scipy.linalg import solve

# Coefficients of the equations
A = [[3, 1], [1, 2]]  # Coefficients matrix
b = [9, 8]  # Constants

# Solve Ax = b
solution = solve(A, b)
print("Solution to the system of equations:", solution)
