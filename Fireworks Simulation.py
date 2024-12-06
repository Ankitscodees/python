import turtle
import random
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Simulation")
screen.tracer(0)

# Create the turtle for fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)

# Function to draw a single firework burst
def draw_firework(x, y):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()

    # Generate random colors
    hue = random.random()
    for _ in range(36):  # 36 rays for the burst
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        firework.color(color)
        firework.forward(random.randint(50, 150))
        firework.backward(random.randint(50, 150))
        firework.right(10)  # Rotate for the next ray

# Animation loop
while True:
    firework.clear()

    # Random position for the firework
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)

    # Draw the firework burst
    draw_firework(x, y)

    # Update the screen
    screen.update()
    screen.delay(200)  # Pause before the next firework
