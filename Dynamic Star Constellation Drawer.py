import turtle
import random

def draw_constellation():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()
    for _ in range(15):  # Draw 15 random stars
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(2, 10)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("white")
        turtle.begin_fill()
        for _ in range(5):  # Draw a star
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

draw_constellation()
turtle.done()
