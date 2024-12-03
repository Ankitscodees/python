import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dynamic Starfield Animation")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the star turtle
star = turtle.Turtle()
star.hideturtle()
star.penup()
star.speed(0)

# Function to draw a glowing star
def draw_star(x, y, size, color):
    star.goto(x, y)
    star.dot(size, color)

# Starfield animation loop
while True:
    # Clear screen for dynamic effect
    star.clear()

    # Draw random stars
    for _ in range(50):  # Number of stars per frame
        x = random.randint(-390, 390)  # Random X coordinate
        y = random.randint(-290, 290)  # Random Y coordinate
        size = random.randint(2, 8)    # Random star size
        color = random.choice(["white", "yellow", "blue", "purple", "cyan"])
        draw_star(x, y, size, color)

    # Update the screen
    screen.update()

    # Delay to create a dynamic effect
    screen.delay(100)
