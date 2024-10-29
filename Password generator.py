import string,random

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits+ string. punctuation ) for _ in range(length))

user_length = int(input("Enter the desired password length (between 4 and 10): "))
if 4 <= user_length <= 10:
    print("Generated password:", generate_password(user_length))
else:
    print("Invalid length, must be between 4 and 10.")
