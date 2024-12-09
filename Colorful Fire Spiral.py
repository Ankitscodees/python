import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fire Spiral")

# Turtle setup
fire = turtle.Turtle()
fire.speed(0)
fire.hideturtle()
fire.width(2)

# Animation loop
hue = 0
angle = 0
for i in range(360):
    fire.color(colorsys.hsv_to_rgb(hue, 1, 1))
    fire.forward(i * 2)
    fire.right(angle + 45)
    angle += 1
    hue += 0.005
    if hue > 1:
        hue = 0
