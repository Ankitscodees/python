import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Animation")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create a turtle object for the fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.penup()
firework.speed(0)

def draw_firework(x, y, colors):
    firework.goto(x, y)
    firework.dot(10, random.choice(colors))  # Starting point
    for _ in range(20):  # Draw 20 lines radiating outward
        angle = random.randint(0, 360)
        distance = random.randint(50, 100)
        firework.setheading(angle)
        firework.forward(distance)
        firework.dot(8, random.choice(colors))  # Explosion dot
        firework.goto(x, y)  # Return to center

# Colors for the fireworks
colors = ["red", "yellow", "blue", "green", "purple", "white", "orange"]

# Fireworks animation loop
while True:
    x = random.randint(-300, 300)  # Random X position
    y = random.randint(-250, 250)  # Random Y position
    draw_firework(x, y, colors)
    screen.update()  # Update the screen
    screen.delay(100)  # Pause slightly to see the effect
