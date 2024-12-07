import turtle
import colorsys
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Infinite Waves")
screen.tracer(0)

# Create the wave turtle
wave = turtle.Turtle()
wave.hideturtle()
wave.speed(0)

# Wave properties
amplitude = 100
frequency = 10
phase = 0
hue = 0

# Animation loop
while True:
    wave.clear()
    wave.penup()
    wave.goto(-400, 0)

    # Draw the wave
    for x in range(-400, 401, 5):
        y = amplitude * math.sin(math.radians(x * frequency + phase))
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        wave.pendown()
        wave.color(color)
        wave.goto(x, y)

    # Update properties for animation
    phase += 5
    hue += 0.01
    if hue > 1:
        hue = 0

    screen.update()
