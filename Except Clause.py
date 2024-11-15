try:
    # Attempting risky operations
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of division is: {result}")
except ValueError:
    # Handling invalid input
    print("Invalid input! Please enter integers only.")
except ZeroDivisionError:
    # Handling division by zero
    print("Division by zero is not allowed.")
except Exception as e:
    # Catching any other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
