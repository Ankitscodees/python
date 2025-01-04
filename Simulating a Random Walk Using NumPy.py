import numpy as np
import matplotlib.pyplot as plt

# Parameters
steps = 1000  # Number of steps in the walk
dimensions = 2  # Number of dimensions for the walk (e.g., 2D)

# Generate random steps (-1, 0, or 1) for each dimension
random_steps = np.random.choice([-1, 1], size=(steps, dimensions))

# Cumulative sum to get the positions at each step
positions = np.cumsum(random_steps, axis=0)

# Plot the random walk
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0], positions[:, 1], alpha=0.8, lw=2)
plt.scatter(positions[0, 0], positions[0, 1], color='red', label='Start', zorder=5)
plt.scatter(positions[-1, 0], positions[-1, 1], color='blue', label='End', zorder=5)
plt.title("Random Walk Simulation (2D)")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
