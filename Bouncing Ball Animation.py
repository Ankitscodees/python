import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Bouncing Ball Animation")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create a ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)

# Ball movement settings
ball.dx = random.uniform(2, 4) * random.choice([-1, 1])  # Random X direction
ball.dy = random.uniform(2, 4) * random.choice([-1, 1])  # Random Y direction

# Animation loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:  # Right or left wall
        ball.dx *= -1  # Reverse X direction
        ball.color(random.choice(["red", "blue", "green", "yellow", "purple"]))

    if ball.ycor() > 290 or ball.ycor() < -290:  # Top or bottom wall
        ball.dy *= -1  # Reverse Y direction
        ball.color(random.choice(["red", "blue", "green", "yellow", "purple"]))
