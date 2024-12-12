import random

class Maze3D:
    def __init__(self, size):
        self.size = size
        self.maze = [[[1 for _ in range(size)] for _ in range(size)] for _ in range(size)]
        self.path = []

    def generate_maze(self, x, y, z):
        directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        random.shuffle(directions)
        self.maze[x][y][z] = 0  # Mark current cell as path

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 < nx < self.size - 1 and 0 < ny < self.size - 1 and 0 < nz < self.size - 1:
                if self.maze[nx][ny][nz] == 1:  # Check for walls
                    if self.is_valid(nx, ny, nz):
                        self.generate_maze(nx, ny, nz)

    def is_valid(self, x, y, z):
        count = 0
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < self.size and 0 <= ny < self.size and 0 <= nz < self.size:
                if self.maze[nx][ny][nz] == 0:
                    count += 1
        return count < 2

    def solve_maze(self, x, y, z):
        if not (0 <= x < self.size and 0 <= y < self.size and 0 <= z < self.size):
            return False
        if (x, y, z) == (self.size - 2, self.size - 2, self.size - 2):
            self.path.append((x, y, z))
            return True
        if self.maze[x][y][z] == 1:
            return False

        self.maze[x][y][z] = 2  # Mark as visited
        self.path.append((x, y, z))

        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if self.solve_maze(x + dx, y + dy, z + dz):
                return True

        self.path.pop()
        return False

    def display(self):
        for z in range(self.size):
            print(f"Level {z + 1}")
            for y in range(self.size):
                print("".join(" " if self.maze[x][y][z] == 0 else "#" for x in range(self.size)))
            print()

# Example usage
size = 5
maze = Maze3D(size)
maze.generate_maze(1, 1, 1)
maze.solve_maze(1, 1, 1)

print("Maze:")
maze.display()

print("Path to Solve:")
print(maze.path)
