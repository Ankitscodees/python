from art import text2art

def ascii_art_generator():
    print("Welcome to the ASCII Art Generator!")
    while True:
        text = input("\nEnter text to convert to ASCII art (or type 'quit' to exit): ")
        if text.lower() == "quit":
            print("Goodbye!")
            break

        art_style = input("Enter a font style (press Enter for default): ").strip()
        try:
            art = text2art(text, font=art_style or None)
            print("\nYour ASCII Art:")
            print(art)
        except Exception as e:
            print(f"Error: {e}. Try a different font or text.")

# Run the ASCII Art Generator
ascii_art_generator()
