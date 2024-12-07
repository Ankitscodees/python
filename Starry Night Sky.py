import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Night")

# Create the turtle for stars
star = turtle.Turtle()
star.hideturtle()
star.speed(0)

# Function to draw a single star
def draw_star(x, y, size):
    star.penup()
    star.goto(x, y)
    star.dot(size, "white")

# Generate random stars
stars = [(random.randint(-400, 400), random.randint(-300, 300), random.randint(2, 5)) for _ in range(100)]

while True:
    star.clear()
    for x, y, size in stars:
        draw_star(x, y, size)
    screen.update()
    time.sleep(0.5)

    # Twinkle effect
    for i in range(len(stars)):
        if random.random() > 0.8:
            stars[i] = (stars[i][0], stars[i][1], random.randint(2, 5))
