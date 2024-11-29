import random

# Function to roll dice
def roll_dice(num_dice=1):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

# Main program
print("Welcome to the Virtual Dice Roller!")
while True:
    try:
        num_dice = int(input("How many dice would you like to roll? (Enter 0 to quit): "))
        if num_dice == 0:
            print("Thanks for playing!")
            break
        results = roll_dice(num_dice)
        print(f"You rolled: {results}")
    except ValueError:
        print("Please enter a valid number.")
