import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spinning Flower")

# Create the turtle
flower = turtle.Turtle()
flower.speed(0)  # Fastest speed
flower.width(2)  # Pen thickness
flower.hideturtle()

# Number of petals and colors
num_petals = 36
num_colors = 36
hue = 0

# Draw the flower
for i in range(num_petals):
    # Set the color of the petal
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
    flower.color(color)
    # Draw a petal (arc)
    flower.circle(100, 60)  # Radius = 100, extent = 60 degrees
    flower.left(120)  # Turn to create a petal shape
    flower.circle(100, 60)
    flower.left(360 / num_petals)  # Rotate to position the next petal
    hue += 1 / num_colors  # Change hue for the next petal

# Keep the window open
screen.mainloop()
