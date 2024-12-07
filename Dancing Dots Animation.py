import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dancing Dots")

# Create the dots
dots = [turtle.Turtle() for _ in range(20)]
for dot in dots:
    dot.shape("circle")
    dot.color(random.random(), random.random(), random.random())
    dot.penup()
    dot.speed(0)
    dot.goto(random.randint(-300, 300), random.randint(-200, 200))

# Movement logic
speeds = [random.uniform(1, 3) for _ in range(20)]
angles = [random.randint(0, 360) for _ in range(20)]

while True:
    for i, dot in enumerate(dots):
        dot.setheading(angles[i])
        dot.forward(speeds[i])

        # Bounce off the walls
        x, y = dot.position()
        if x < -390 or x > 390:
            angles[i] = 180 - angles[i]
        if y < -290 or y > 290:
            angles[i] = -angles[i]
