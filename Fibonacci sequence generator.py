def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to n terms.
    The Fibonacci sequence is a series of numbers where each number
    is the sum of the two preceding ones, starting from 0 and 1.
    """
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the sequence
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Test the function
num_terms = 10
result = fibonacci(num_terms)
print(f"The first {num_terms} terms of the Fibonacci sequence are: {result}")
