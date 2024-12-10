import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Kaleidoscope Animation")
screen.tracer(0)

# Turtle setup
kaleidoscope = turtle.Turtle()
kaleidoscope.speed(0)
kaleidoscope.hideturtle()

# Animation loop
hue = 0
while True:
    kaleidoscope.clear()
    for i in range(12):  # Number of mirrored patterns
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        kaleidoscope.color(color)
        kaleidoscope.penup()
        kaleidoscope.goto(0, 0)
        kaleidoscope.pendown()
        kaleidoscope.forward(100)
        kaleidoscope.right(30)

        for _ in range(4):  # Nested shapes
            kaleidoscope.circle(50, steps=6)
            kaleidoscope.right(90)
    hue += 0.01
    if hue > 1:
        hue = 0
    screen.update()
