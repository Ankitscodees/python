import turtle
import random
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rotating Galaxy Effect")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the turtle
galaxy = turtle.Turtle()
galaxy.speed(0)
galaxy.hideturtle()

# Function to draw a single star
def draw_star(x, y, size, color):
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.dot(size, color)

# Galaxy animation loop
angle = 0
while True:
    galaxy.clear()
    hue = 0  # Starting hue for colors
    for i in range(200):  # Number of stars in the galaxy
        distance = random.randint(50, 300)  # Distance from the center
        angle_offset = random.uniform(0, 360)  # Random angle
        x = distance * turtle.cos((angle + angle_offset) * turtle.pi / 180)
        y = distance * turtle.sin((angle + angle_offset) * turtle.pi / 180)
        size = random.randint(2, 6)  # Random star size
        color = colorsys.hsv_to_rgb(hue, 1, 1)  # Create rainbow colors
        draw_star(x, y, color)
        hue += 1 / 200  # Gradually change hue

    angle += 2  # Rotate the galaxy slightly for the animation
    screen.update()
