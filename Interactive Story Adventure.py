def start_adventure():
    print("Welcome to the Enchanted Forest!")
    print("You find yourself at a crossroads.")
    choice1 = input("Do you go left towards the dark cave or right towards the sunny meadow? (left/right): ").strip().lower()

    if choice1 == "left":
        print("You cautiously enter the dark cave.")
        choice2 = input("Inside, you see a treasure chest and a sleeping dragon. Do you open the chest or sneak away? (open/sneak): ").strip().lower()
        if choice2 == "open":
            print("You open the chest and find a pile of gold! You're rich!")
        elif choice2 == "sneak":
            print("You sneak away quietly, escaping the dragon's lair safely.")
        else:
            print("Invalid choice! The dragon wakes up and you have to run!")
    elif choice1 == "right":
        print("You walk into the sunny meadow and see a beautiful unicorn.")
        choice3 = input("Do you approach the unicorn or stay back? (approach/stay): ").strip().lower()
        if choice3 == "approach":
            print("The unicorn lets you ride it, and you have a magical adventure!")
        elif choice3 == "stay":
            print("You enjoy the peaceful scenery and feel at one with nature.")
        else:
            print("Invalid choice! The unicorn vanishes into the woods.")
    else:
        print("Invalid choice! You wander around aimlessly.")

start_adventure()
