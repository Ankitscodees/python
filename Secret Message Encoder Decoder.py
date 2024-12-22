def caesar_cipher(text, shift, mode="encode"):
    result = ""
    shift = shift if mode == "encode" else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

choice = input("Do you want to encode or decode a message? (encode/decode): ").strip().lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift value (1-25): "))

if choice in ["encode", "decode"]:
    transformed = caesar_cipher(message, shift, mode=choice)
    print(f"Your {choice}d message is: {transformed}")
else:
    print("Invalid choice!")
