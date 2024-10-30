def is_armstrong(number):
    # Convert the number to a string to count its digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits each raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == number

# Test with an example
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
