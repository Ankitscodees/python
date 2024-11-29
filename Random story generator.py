import random

# Story elements
characters = ["a wizard", "an alien", "a pirate", "a robot", "a dragon"]
places = ["in a haunted castle", "on a distant planet", "on a pirate ship", "in a futuristic city", "in a dark forest"]
actions = ["found a hidden treasure", "discovered a magical spell", "saved the world", "fought an epic battle", "made a new friend"]

# Generate a random story
def generate_story():
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    return f"Once upon a time, {character} {place} {action}."

# Main program
print("Welcome to the Random Story Generator!")
while True:
    print("\nYour story:")
    print(generate_story())
    play_again = input("\nWant another story? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
