def gcd(a, b):
    """
    This function calculates the greatest common divisor (GCD)
    of two numbers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1 = 56
num2 = 98
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
