import random

def word_scramble():
    words = ["python", "developer", "coding", "puzzle", "algorithm"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    print("Welcome to Word Scramble!")
    print(f"Scrambled word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word:
            print("Congratulations! You guessed it right!")
            return
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
    print(f"Game over! The correct word was: {word}")

word_scramble()
