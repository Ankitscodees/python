def check_number(num):
    if num < 0:
        # Raise an exception explicitly
        raise ValueError("The number cannot be negative.")
    elif num == 0:
        # Raise a different exception explicitly
        raise ZeroDivisionError("The number cannot be zero.")
    else:
        print(f"The number {num} is valid.")

# Main code
try:
    number = int(input("Enter a number: "))
    check_number(number)
except ValueError as ve:
    print(f"ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")
finally:
    print("Program completed.")
