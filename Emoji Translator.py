# Emoji dictionary
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "python": "🐍",
    "fire": "🔥",
    "cool": "😎",
    "pizza": "🍕",
    "cat": "🐱",
    "dog": "🐶",
    "rocket": "🚀",
}

# Function to translate text to emojis
def text_to_emoji(text):
    words = text.split()
    translated = [emoji_dict.get(word.lower(), word) for word in words]
    return " ".join(translated)

# Main program
print("Welcome to the Emoji Translator!")
while True:
    text = input("\nEnter a sentence (or type 'quit' to exit): ")
    if text.lower() == "quit":
        print("Goodbye!")
        break
    print("Translated:", text_to_emoji(text))
