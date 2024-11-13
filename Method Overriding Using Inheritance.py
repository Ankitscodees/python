# Base class
class Vehicle:
    def start_engine(self):
        return "Starting the engine of the vehicle"

# Subclass Car
class Car(Vehicle):
    # Overriding the start_engine method
    def start_engine(self):
        return "Starting the engine of the car"

# Subclass Bike
class Bike(Vehicle):
    # Overriding the start_engine method
    def start_engine(self):
        return "Starting the engine of the bike"

# Creating instances of each class
vehicle = Vehicle()
car = Car()
bike = Bike()

# Calling the start_engine method on each instance
print("Vehicle:", vehicle.start_engine())  # Output: Starting the engine of the vehicle
print("Car:", car.start_engine())          # Output: Starting the engine of the car
print("Bike:", bike.start_engine())        # Output: Starting the engine of the bike
