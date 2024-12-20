import turtle
import math

def draw_spirograph(radius, step, color):
    turtle.speed(0)
    turtle.color(color)
    for angle in range(0, 360, step):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(10)

draw_spirograph(200, 10, "blue")
turtle.done()
