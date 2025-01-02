import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initialize the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2, color="blue")

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Update function for the animation
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

# Generate the frames for animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50, blit=True)

plt.show()
