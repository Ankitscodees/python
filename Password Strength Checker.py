import re

def check_password_strength(password):
    strength = 0
    conditions = [
        (r'[a-z]', 'Lowercase letter'),
        (r'[A-Z]', 'Uppercase letter'),
        (r'[0-9]', 'Digit'),
        (r'[!@#$%^&*(),.?":{}|<>]', 'Special character')
    ]

    for pattern, condition in conditions:
        if re.search(pattern, password):
            strength += 1

    if len(password) >= 8:
        strength += 1

    return ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"][strength]

# Example usage
password = "P@ssw0rd123"
print(f"Password Strength: {check_password_strength(password)}")
