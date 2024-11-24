class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, message="Age must be between 0 and 120"):
        self.message = message
        super().__init__(self.message)

def set_age(age):
    """Set the age of a user after validation."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Please provide a value between 0 and 120.")
    print(f"Age set to {age}.")

# Example usage
try:
    set_age(-5)  # Invalid age
except InvalidAgeError as e:
    print(f"Custom exception caught: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
