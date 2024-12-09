import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral of Hearts")

# Turtle setup
heart = turtle.Turtle()
heart.speed(0)
heart.hideturtle()

# Draw a single heart
def draw_heart(size, color):
    heart.color(color)
    heart.begin_fill()
    heart.left(50)
    heart.forward(size)
    heart.circle(size * 0.4, 200)
    heart.right(140)
    heart.circle(size * 0.4, 200)
    heart.forward(size)
    heart.end_fill()

# Spiral of hearts
for i in range(36):  # Number of hearts in the spiral
    draw_heart(100, (1 - i / 36, 0.5, i / 36))  # Gradient of colors
    heart.right(10)  # Rotate for the spiral
