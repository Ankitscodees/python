class Display:
    # Overloaded method: show
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print("Two arguments:", a, "and", b)
        elif a is not None:
            print("One argument:", a)
        else:
            print("No arguments provided")

# Creating an instance of Display
display = Display()

# Calling the show method with no arguments
display.show()  # Output: No arguments provided

# Calling the show method with one argument
display.show(10)  # Output: One argument: 10

# Calling the show method with two arguments
display.show(10, 20)  # Output: Two arguments: 10 and 20
