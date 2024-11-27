def tribonacci(n):
    """
    This function calculates the nth number in the Tribonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    # Initialize the first three terms
    t0, t1, t2 = 0, 1, 1
    
    # Compute the nth term iteratively
    for _ in range(3, n + 1):
        t_next = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t_next
    
    return t2

# Test the function
n = 10
result = tribonacci(n)
print(f"The {n}th number in the Tribonacci sequence is: {result}")
