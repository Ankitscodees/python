import random

def dungeon_treasure_hunt():
    print("Welcome to Dungeon Treasure Hunt!")
    print("Your goal is to find treasure without falling into traps.")
    dungeon = [["T", " ", "X", " "],
               [" ", "X", " ", " "],
               [" ", " ", " ", "X"],
               ["X", " ", " ", "T"]]

    player_pos = [0, 0]
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    treasures_found = 0

    while True:
        print(f"Current Position: {player_pos}")
        for row in dungeon:
            print(" ".join(row))

        move = input("Move (up, down, left, right): ").lower()
        if move not in moves:
            print("Invalid move! Try again.")
            continue

        new_pos = [player_pos[0] + moves[move][0], player_pos[1] + moves[move][1]]
        if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
            player_pos = new_pos
            cell = dungeon[player_pos[0]][player_pos[1]]
            if cell == "T":
                treasures_found += 1
                print(f"🎉 You found a treasure! Total treasures: {treasures_found}")
                dungeon[player_pos[0]][player_pos[1]] = " "
            elif cell == "X":
                print("💀 You fell into a trap! Game over.")
                break
            else:
                print("You moved safely.")
        else:
            print("You hit a wall! Try a different direction.")

        if treasures_found == 2:
            print("🏆 You collected all treasures! You win!")
            break

dungeon_treasure_hunt()
