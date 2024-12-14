def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark forest.")
    choice1 = input("Do you ENTER the forest or RUN away? (enter/run): ").lower()

    if choice1 == "enter":
        print("You step into the forest. It's dark and eerie.")
        choice2 = input("You see a glowing object. Do you PICK it up or IGNORE it? (pick/ignore): ").lower()
        
        if choice2 == "pick":
            print("The object grants you magical powers. You win!")
        else:
            print("You ignore the object, but a wild beast finds you. Game over!")
    else:
        print("You run away safely but miss an amazing adventure. Game over!")

adventure_game()
