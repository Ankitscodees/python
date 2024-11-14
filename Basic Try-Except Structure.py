def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return f"Result: {result}"
    finally:
        print("Execution completed.")

# Test cases
print(divide_numbers(10, 2))    # Expected output: Result: 5.0
print(divide_numbers(10, 0))    # Expected output: Error: Cannot divide by zero.
print(divide_numbers(10, "a"))  # Expected output: Error: Both inputs must be numbers.
