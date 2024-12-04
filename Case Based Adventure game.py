def start_adventure():
    print("\nWelcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark forest. What will you do?")
    print("1. Enter the forest")
    print("2. Walk away")
    
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        print("You decide to walk away, avoiding any potential dangers. Game Over!")
    else:
        print("Invalid choice. Try again!")
        start_adventure()

def forest_path():
    print("\nYou venture into the forest and come across a fork in the path.")
    print("1. Take the left path")
    print("2. Take the right path")
    
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        treasure_cave()
    elif choice == "2":
        wolf_encounter()
    else:
        print("Invalid choice. Try again!")
        forest_path()

def treasure_cave():
    print("\nYou follow the left path and discover a hidden cave filled with treasure!")
    print("Congratulations! You've found the treasure and won the game!")

def wolf_encounter():
    print("\nYou take the right path and encounter a hungry wolf!")
    print("1. Fight the wolf")
    print("2. Run away")
    
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("\nYou bravely fight the wolf but are overpowered. Game Over!")
    elif choice == "2":
        print("\nYou run away and escape safely. Game Over!")
    else:
        print("Invalid choice. Try again!")
        wolf_encounter()

# Start the adventure
start_adventure()
