import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Shooting Stars")

# Turtle setup
star = turtle.Turtle()
star.speed(0)
star.hideturtle()

# Function to draw a single shooting star
def draw_shooting_star(x, y, length):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color("white")
    star.width(2)
    for i in range(5):  # Trail effect
        star.forward(length)
        star.penup()
        star.goto(x - i * 10, y - i * 10)
        star.pendown()
    star.clear()

# Animation loop
while True:
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    length = random.randint(50, 150)
    draw_shooting_star(x, y, length)
