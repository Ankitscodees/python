import random

def generate_maze(size):
    maze = [[' ' if random.choice([True, False]) else '#' for _ in range(size)] for _ in range(size)]
    maze[0][0] = 'S'  # Start
    maze[-1][-1] = 'E'  # End
    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(row))

maze = generate_maze(10)
display_maze(maze)
print("\nNavigate from 'S' to 'E'!")
