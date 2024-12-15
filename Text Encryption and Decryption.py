def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
message = "Hello, Python!"
shift = 4
encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
