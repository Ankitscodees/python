try:
    # Prompt the user for input
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {num**2}")
except ValueError:
    # Handle the error if input is not a valid integer
    print("Oops! That's not a valid number. Please enter an integer.")
finally:
    # This block will execute no matter what
    print("Program execution completed.")
