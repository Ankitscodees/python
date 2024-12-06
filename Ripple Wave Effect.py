import turtle
import math
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Ripple Wave Effect")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the turtle
ripple = turtle.Turtle()
ripple.hideturtle()
ripple.speed(0)
ripple.width(2)

# Draw a ripple wave
def draw_ripple(radius, color):
    ripple.penup()
    ripple.goto(0, -radius)
    ripple.pendown()
    ripple.color(color)
    ripple.circle(radius)

# Ripple animation loop
hue = 0
radius_step = 10
while True:
    ripple.clear()
    hue = 0  # Reset hue for each frame
    for radius in range(10, 300, radius_step):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        draw_ripple(radius, color)
        hue += 0.05  # Shift the hue for the next ripple
        if hue > 1:
            hue = 0
    radius_step += 1  # Gradually expand the ripples
    screen.update()
