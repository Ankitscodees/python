def find_second_largest(numbers):
    return sorted(set(numbers))[-2]

# Example usage
numbers = [10, 20, 4, 45, 99]
print("The second largest number is:", find_second_largest(numbers))
