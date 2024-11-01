def is_spy_number(num):
    digits = [int(digit) for digit in str(num)]
    sum_of_digits = sum(digits)
    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit
    return sum_of_digits == product_of_digits

# Example usage
number = 132
if is_spy_number(number):
    print(f"{number} is a spy number")
else:
    print(f"{number} is not a spy number")
