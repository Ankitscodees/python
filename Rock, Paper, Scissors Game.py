import random

choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Play the game
while True:
    print("\nChoose rock, paper, or scissors (or type 'quit' to exit):")
    player_choice = input("Your choice: ").lower()
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    if player_choice not in choices:
        print("Invalid choice. Try again!")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))
