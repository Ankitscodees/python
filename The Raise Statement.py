# Define a user-defined exception
class AgeTooLowError(Exception):
    def __init__(self, message="Age is below the allowed limit."):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def validate_age(age):
    if age < 18:
        raise AgeTooLowError(f"Age {age} is too low. Minimum age is 18.")
    else:
        print("Age is valid.")

# Main code
try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except AgeTooLowError as e:
    print(f"Custom Exception: {e}")
except ValueError:
    print("Please enter a valid integer.")
finally:
    print("Age validation process completed.")
