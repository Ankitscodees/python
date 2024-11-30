import turtle
import colorsys

def colorful_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed

    n = 36  # Number of colors in the palette
    h = 0  # Initial hue
    t.width(2)

    for i in range(360):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB
        t.color(c)  # Set the turtle's color
        t.forward(i * 2)
        t.right(59)
        h += 1 / n  # Increment hue for the next color

    turtle.done()

colorful_spiral()
