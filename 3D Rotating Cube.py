import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Rotating Cube")

# Turtle setup
cube = turtle.Turtle()
cube.hideturtle()
cube.speed(0)
cube.pensize(2)

# Cube vertices
vertices = [
    (-100, -100, -100),
    (-100, -100, 100),
    (-100, 100, -100),
    (-100, 100, 100),
    (100, -100, -100),
    (100, -100, 100),
    (100, 100, -100),
    (100, 100, 100),
]

# Edges connecting the vertices
edges = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5), (2, 3),
    (2, 6), (3, 7), (4, 5),
    (4, 6), (5, 7), (6, 7),
]

# Project 3D points to 2D
def project_3d_to_2d(x, y, z, angle):
    # Rotation matrix
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    # Rotate around Y-axis
    x_rot = x * cos_a - z * sin_a
    z_rot = x * sin_a + z * cos_a

    # Perspective projection
    factor = 200 / (200 + z_rot)
    x_proj = x_rot * factor
    y_proj = y * factor

    return x_proj, y_proj

# Draw the cube
def draw_cube(angle):
    cube.clear()
    projected = []

    # Project each vertex
    for vertex in vertices:
        x, y, z = vertex
        x_proj, y_proj = project_3d_to_2d(x, y, z, angle)
        projected.append((x_proj, y_proj))

    # Draw edges
    cube.color("cyan")
    for edge in edges:
        start, end = edge
        cube.penup()
        cube.goto(projected[start][0], projected[start][1])
        cube.pendown()
        cube.goto(projected[end][0], projected[end][1])

# Animation loop
angle = 0
while True:
    draw_cube(angle)
    angle += 0.02  # Rotate slowly
    screen.update()
    time.sleep(0.01)
