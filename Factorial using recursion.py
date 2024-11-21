def factorial(n):
    """
    This function calculates the factorial of a number using recursion.
    Factorial of n (n!) is the product of all positive integers up to n.
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
