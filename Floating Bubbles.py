import turtle
import random
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Floating Bubbles")

# Create the bubble turtle
bubble = turtle.Turtle()
bubble.hideturtle()
bubble.speed(0)
bubble.pensize(2)

# Function to draw a bubble
def draw_bubble(x, y, radius, color):
    bubble.penup()
    bubble.goto(x, y - radius)  # Start at the bottom of the circle
    bubble.pendown()
    bubble.color(color)
    bubble.circle(radius)

# Generate initial bubbles
bubbles = []
for _ in range(20):  # Number of bubbles
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    radius = random.randint(20, 50)
    hue = random.random()
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    bubbles.append([x, y, radius, color, random.randint(1, 3)])  # Add speed for floating

# Animation loop
while True:
    bubble.clear()
    for i in range(len(bubbles)):
        x, y, radius, color, speed = bubbles[i]

        # Draw the bubble
        draw_bubble(x, y, radius, color)

        # Move the bubble upward
        bubbles[i][1] += speed

        # Reset bubble when it goes off-screen
        if bubbles[i][1] - radius > 300:
            bubbles[i][1] = -300
            bubbles[i][0] = random.randint(-300, 300)
            bubbles[i][2] = random.randint(20, 50)
            hue = random.random()
            bubbles[i][3] = colorsys.hsv_to_rgb(hue, 1, 1)
            bubbles[i][4] = random.randint(1, 3)

    # Update the screen
    screen.update()
