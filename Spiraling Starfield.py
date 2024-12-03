import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiraling Starfield")

# Create the turtle
star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.penup()

# Function to draw a star
def draw_star(x, y, size, color):
    star.goto(x, y)
    star.color(color)
    star.begin_fill()
    for _ in range(5):  # Draw a 5-pointed star
        star.forward(size)
        star.right(144)
    star.end_fill()

# Spiral starfield animation
angle = 0
distance = 5
colors = ["white", "yellow", "blue", "purple", "red", "orange"]

for _ in range(200):
    # Calculate star position in a spiral
    x = distance * turtle.cos(angle)
    y = distance * turtle.sin(angle)
    
    # Randomize star size and color
    size = random.randint(5, 15)
    color = random.choice(colors)
    
    # Draw the star
    draw_star(x, y, size, color)
    
    # Increment angle and distance for spiral effect
    angle += 15
    distance += 2

# Keep the window open
screen.mainloop()
