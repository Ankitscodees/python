class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} {self.model} is being driven as a car.")

class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} {self.model} is being ridden as a bike.")

class Truck(Vehicle):
    def load_cargo(self):
        print(f"{self.brand} {self.model} is loading cargo.")

# Creating instances of each child class
car = Car("Toyota", "Camry")
bike = Bike("Yamaha", "MT-07")
truck = Truck("Ford", "F-150")

# All child classes have access to the parent class's methods
car.start_engine()         # Output: Toyota Camry's engine started.
car.drive()                # Output: Toyota Camry is being driven as a car.

bike.start_engine()        # Output: Yamaha MT-07's engine started.
bike.ride()                # Output: Yamaha MT-07 is being ridden as a bike.

truck.start_engine()       # Output: Ford F-150's engine started.
truck.load_cargo()         # Output: Ford F-150 is loading cargo.
