import turtle

def drawing_app():
    print("Welcome to the Simple Drawing App!")
    print("Use your mouse or arrow keys to draw. Close the window to exit.")

    screen = turtle.Screen()
    screen.title("Drawing App")
    screen.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)
    
    # Functions to control the pen
    def move_up():
        pen.setheading(90)
        pen.forward(20)

    def move_down():
        pen.setheading(270)
        pen.forward(20)

    def move_left():
        pen.setheading(180)
        pen.forward(20)

    def move_right():
        pen.setheading(0)
        pen.forward(20)

    def clear_screen():
        pen.clear()

    # Keyboard bindings
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(clear_screen, "c")
    
    screen.mainloop()

# Run the drawing app
drawing_app()
