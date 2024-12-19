def adventure_game():
    print("Welcome to the haunted forest!")
    choice1 = input("Do you go left or right? (left/right): ").strip().lower()

    if choice1 == "left":
        print("You encounter a friendly wolf. It shows you the way out. You win!")
    elif choice1 == "right":
        choice2 = input("You find a treasure chest. Open it? (yes/no): ").strip().lower()
        if choice2 == "yes":
            print("Congratulations! You found a hidden treasure. You win!")
        else:
            print("You walk away, but get lost in the forest. Game over!")
    else:
        print("Invalid choice. The game ends here.")

adventure_game()
