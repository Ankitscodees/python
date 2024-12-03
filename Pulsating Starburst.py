import turtle
import random
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pulsating Starburst Animation")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the turtle
starburst = turtle.Turtle()
starburst.hideturtle()
starburst.speed(0)

# Number of rays and colors
num_rays = 36
num_colors = 36
hue = 0

# Animation loop
while True:
    # Draw a starburst
    for size in range(20, 200, 10):  # Pulsating sizes
        starburst.clear()
        hue = random.random()  # Random starting hue
        for i in range(num_rays):
            # Set the color for each ray
            color = colorsys.hsv_to_rgb(hue, 1, 1)
            starburst.color(color)
            starburst.penup()
            starburst.goto(0, 0)
            starburst.pendown()
            starburst.forward(size)  # Draw a ray
            starburst.backward(size)  # Draw backward
            starburst.right(360 / num_rays)  # Rotate for the next ray
            hue += 1 / num_colors  # Change hue slightly

        screen.update()

