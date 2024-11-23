class Robot:
    def __init__(self, name):
        self.__name = name

    def __display_name(self):  # Private method
        print(f"The robot's name is {self.__name}")

    def reveal_name(self):  # Public method to access the private method
        self.__display_name()

# Create an object
robot = Robot("Robo")

# Access private method through public method
robot.reveal_name()  # Output: The robot's name is Robo

# Direct access to private method will raise an AttributeError
# robot.__display_name()  # Uncommenting this line will raise an error
