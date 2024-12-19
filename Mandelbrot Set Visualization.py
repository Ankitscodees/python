import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Create image
rows, cols = 800, 800
image = np.zeros((rows, cols))
for x in range(rows):
    for y in range(cols):
        real = -2 + (x / rows) * 4
        imag = -2 + (y / cols) * 4
        c = complex(real, imag)
        color = mandelbrot(c, 100)
        image[x, y] = color

plt.imshow(image, cmap='hot')
plt.colorbar()
plt.show()
