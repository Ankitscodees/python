import random

# List of emojis to use in the art
emojis = ['🌟', '🔥', '💧', '🌈', '🌸', '🍀', '🎵', '🎲', '⚡', '🌙', '⭐', '🌀', '🍁']

# Function to generate random emoji art
def generate_emoji_art(rows, cols):
    art = ""
    for _ in range(rows):
        line = ''.join(random.choice(emojis) for _ in range(cols))
        art += line + "\n"
    return art

# Ask user for size of the art
try:
    rows = int(input("Enter the number of rows for the art: "))
    cols = int(input("Enter the number of columns for the art: "))
    print("\n🎨 Random Emoji Art 🎨\n")
    print(generate_emoji_art(rows, cols))
except ValueError:
    print("Please enter valid numbers for rows and columns.")
