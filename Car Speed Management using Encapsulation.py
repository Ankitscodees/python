class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.__speed = speed  # Private variable to store speed

    # Getter method to access speed
    def get_speed(self):
        return self.__speed

    # Setter method to set speed
    def set_speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
            print(f"Speed is set to {self.__speed} km/h")
        else:
            print("Invalid speed! Speed should be between 0 and 200 km/h.")

    # Method to accelerate the car
    def accelerate(self, increment):
        if self.__speed + increment <= 200:
            self.__speed += increment
            print(f"Car accelerated! New speed: {self.__speed} km/h")
        else:
            print("Cannot accelerate! Speed will exceed 200 km/h.")

    # Method to apply brakes
    def apply_brakes(self, decrement):
        if self.__speed - decrement >= 0:
            self.__speed -= decrement
            print(f"Brakes applied! New speed: {self.__speed} km/h")
        else:
            print("Speed cannot be negative. Brakes applied to stop the car.")

    # Method to display car details
    def display_car_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Current Speed: {self.__speed} km/h")

# Example of encapsulation in use
car1 = Car("Toyota", "Corolla", 50)

# Display car details
car1.display_car_info()

# Accelerate the car
car1.accelerate(30)

# Apply brakes
car1.apply_brakes(20)

# Update speed using setter method
car1.set_speed(120)

# Trying to set invalid speed
car1.set_speed(220)  # Invalid, will show an error message

# Access speed using getter method
print("Current Speed:", car1.get_speed())
