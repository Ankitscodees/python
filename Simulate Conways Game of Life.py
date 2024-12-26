import numpy as np
import matplotlib.pyplot as plt
import time

def update(grid):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1) 
                    for i, j in [(-1, -1), (-1, 0), (-1, 1),
                                 (0, -1), (0, 1), 
                                 (1, -1), (1, 0), (1, 1)])
    return (neighbors == 3) | ((grid == 1) & (neighbors == 2))

size = 50
grid = np.random.choice([0, 1], size=(size, size))

plt.ion()
while True:
    plt.imshow(grid, cmap="binary")
    plt.axis("off")
    plt.pause(0.1)
    grid = update(grid)
    plt.clf()
