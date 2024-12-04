import random

def roll_dice():
    return random.randint(1, 6)

def dice_game():
    print("Welcome to the Digital Dice Game!")
    while True:
        input("\nPress Enter to roll your die...")
        player_roll = roll_dice()
        computer_roll = roll_dice()
        
        print(f"\nYou rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")
        
        if player_roll > computer_roll:
            print("You win!")
        elif player_roll < computer_roll:
            print("Computer wins!")
        else:
            print("It's a tie!")
        
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
dice_game()
