def digital_root(n):
    """
    This function calculates the digital root of a number.
    """
    while n >= 10:  # Repeat until n becomes a single digit
        n = sum(int(digit) for digit in str(n))
    return n

# Test the function
number = 9875
result = digital_root(number)
print(f"The digital root of {number} is: {result}")
