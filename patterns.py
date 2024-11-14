def validate_email(email):
    pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return "Valid email."
    else:
        return "Invalid email."

# Test cases
print(validate_email("test@example.com"))  # Output: Valid email.
print(validate_email("invalid-email"))     # Output: Invalid email.
