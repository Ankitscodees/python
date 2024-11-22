def is_armstrong_number(number):
    """
    This function checks if a given number is an Armstrong number.
    """
    # Convert the number to a string to iterate over its digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == number

# Test the function
test_number = 153
if is_armstrong_number(test_number):
    print(f"{test_number} is an Armstrong number!")
else:
    print(f"{test_number} is NOT an Armstrong number.")
