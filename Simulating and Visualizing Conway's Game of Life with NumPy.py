import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_grid(size, prob=0.2):
    """Initialize a random grid with live cells."""
    return np.random.choice([0, 1], size=size, p=[1 - prob, prob])

def update_grid(grid):
    """Apply the rules of Conway's Game of Life to update the grid."""
    neighbors = sum(
        np.roll(np.roll(grid, i, 0), j, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (i, j) != (0, 0)
    )
    return (neighbors == 3) | ((grid == 1) & (neighbors == 2))

def animate(frame):
    """Update the grid and display each frame."""
    global grid
    grid = update_grid(grid)
    mat.set_data(grid)
    return [mat]

# Parameters
grid_size = (50, 50)
probability = 0.3
frames = 100

# Initialize the grid
grid = initialize_grid(grid_size, prob=probability)

# Set up the plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap="binary")
ax.axis("off")

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=frames, interval=100, blit=True
)

plt.show()
