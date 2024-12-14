def mandelbrot(width, height, max_iterations):
    for y in range(height):
        for x in range(width):
            zx, zy = (x - width / 2) / (width / 4), (y - height / 2) / (height / 4)
            c = complex(zx, zy)
            z = 0
            iteration = 0

            while abs(z) < 2 and iteration < max_iterations:
                z = z * z + c
                iteration += 1

            if iteration == max_iterations:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage
mandelbrot(80, 24, 50)
