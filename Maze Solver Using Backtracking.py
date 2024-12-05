def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == " "

def solve_maze(maze, x, y, solution):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:  # Reached the destination
        solution[x][y] = "X"
        return True
    
    if is_safe(maze, x, y):
        solution[x][y] = "X"
        
        # Move down
        if solve_maze(maze, x + 1, y, solution):
            return True
        
        # Move right
        if solve_maze(maze, x, y + 1, solution):
            return True
        
        # Backtrack
        solution[x][y] = " "
        return False
    
    return False

def maze_solver():
    maze = [
        ["#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#"]
    ]

    solution = [[" " for _ in row] for row in maze]
    print("Maze:")
    print_maze(maze)
    
    if solve_maze(maze, 1, 1, solution):  # Start at (1,1)
        print("\nSolved Maze:")
        print_maze(solution)
    else:
        print("\nNo solution exists for the maze.")

# Solve the maze
maze_solver()
