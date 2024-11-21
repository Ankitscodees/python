def largest_prime_factor(n):
    """
    This function finds the largest prime factor of a given number n.
    """
    if n <= 1:
        return "Number must be greater than 1."
    
    largest_factor = None
    # Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Check odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is still greater than 2, it's a prime factor
    if n > 2:
        largest_factor = n

    return largest_factor

# Test the function
number = 13195
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")
