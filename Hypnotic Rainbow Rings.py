import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hypnotic Rainbow Rings")
screen.tracer(0)

# Turtle setup
ring = turtle.Turtle()
ring.speed(0)
ring.hideturtle()

# Draw expanding rainbow rings
hue = 0
radius = 10
while True:
    ring.clear()
    for i in range(10):  # Number of rings
        color = colorsys.hsv_to_rgb(hue + i * 0.1, 1, 1)
        ring.penup()
        ring.goto(0, -radius * (i + 1))
        ring.pendown()
        ring.pensize(2)
        ring.color(color)
        ring.circle(radius * (i + 1))
    radius += 5
    hue += 0.01
    if hue > 1:
        hue = 0
    screen.update()
