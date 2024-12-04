import random

def hangman():
    words = ["python", "programming", "hangman", "challenge", "developer", "keyboard"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0 and "_" in guessed_word:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print("Wrong!")
            attempts -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Start the game
hangman()
