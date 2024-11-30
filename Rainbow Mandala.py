import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Mandala")

# Create the turtle
mandala = turtle.Turtle()
mandala.speed(0)  # Fastest speed
mandala.width(2)  # Line thickness
mandala.hideturtle()

# Number of circles in the mandala
num_circles = 36
num_colors = 36
hue = 0

# Draw the mandala
for i in range(num_circles):
    # Set the color of each circle
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
    mandala.color(color)
    mandala.circle(100)  # Draw a circle
    mandala.right(360 / num_circles)  # Rotate to make the mandala
    hue += 1 / num_colors  # Change hue for the next circle

# Keep the window open
screen.mainloop()
