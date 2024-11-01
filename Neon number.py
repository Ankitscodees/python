def is_neon_number(num):
    square = num ** 2
    sum_of_digits = sum(int(digit) for digit in str(square))
    return sum_of_digits == num

# Example usage
number = 9
if is_neon_number(number):
    print(f"{number} is a neon number")
else:
    print(f"{number} is not a neon number")
