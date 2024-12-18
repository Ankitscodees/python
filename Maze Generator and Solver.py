import random

# Generate a maze
def create_maze(size):
    maze = [['#'] * size for _ in range(size)]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            if random.choice([True, False]):
                maze[i][j] = ' '
    maze[1][1] = 'S'  # Start point
    maze[size - 2][size - 2] = 'E'  # End point
    return maze

# Display the maze
def display_maze(maze):
    for row in maze:
        print("".join(row))

# Solve the maze using recursion
def solve_maze(maze, x, y):
    if maze[x][y] == 'E':  # End point reached
        return True
    if maze[x][y] != ' ' and maze[x][y] != 'S':  # Invalid move
        return False

    maze[x][y] = '.'  # Mark as part of the path

    # Explore neighbors: up, right, down, left
    if solve_maze(maze, x - 1, y) or solve_maze(maze, x, y + 1) or solve_maze(maze, x + 1, y) or solve_maze(maze, x, y - 1):
        return True

    maze[x][y] = ' '  # Backtrack
    return False

# Main program
size = 10  # Maze size
maze = create_maze(size)
print("Generated Maze:")
display_maze(maze)

if solve_maze(maze, 1, 1):
    print("\nSolved Maze:")
    display_maze(maze)
else:
    print("\nNo solution found!")
