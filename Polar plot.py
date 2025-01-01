import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
r = 1 + np.sin(6 * theta)

plt.polar(theta, r, color='magenta')
plt.title("Polar Plot Example")
plt.show()
