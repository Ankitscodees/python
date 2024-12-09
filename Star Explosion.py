import turtle
import random
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Explosion")

# Turtle setup
star = turtle.Turtle()
star.speed(0)
star.hideturtle()

# Function to draw a starburst
def draw_starburst(x, y):
    hue = random.random()
    star.penup()
    star.goto(x, y)
    star.pendown()

    for _ in range(36):  # Number of rays in the starburst
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        star.color(color)
        star.forward(random.randint(50, 150))
        star.backward(random.randint(50, 150))
        star.right(10)

# Animation loop
while True:
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_starburst(x, y)
    star.clear()
