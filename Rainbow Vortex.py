import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Vortex")

# Turtle setup
vortex = turtle.Turtle()
vortex.speed(0)  # Fastest speed
vortex.hideturtle()
vortex.width(2)

# Draw the vortex
hue = 0  # Starting color hue
vortex.pensize(2)  # Thickness of the lines

for i in range(360):
    # Change color for each iteration
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    vortex.color(color)

    # Draw the spiral
    vortex.forward(i * 2)
    vortex.right(59)  # The angle creates the vortex effect

    # Adjust the hue for rainbow transition
    hue += 0.005
    if hue > 1:  # Reset hue to loop through colors
        hue = 0

# Keep the window open
screen.mainloop()
