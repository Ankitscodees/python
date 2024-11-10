class Electronics:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} electronic device is now powered on.")

class Computer(Electronics):
    def __init__(self, brand, cpu):
        super().__init__(brand)
        self.cpu = cpu

    def boot(self):
        print(f"{self.brand} computer with {self.cpu} CPU is booting up.")

class Laptop(Computer):
    def __init__(self, brand, cpu, battery_life):
        super().__init__(brand, cpu)
        self.battery_life = battery_life

    def show_specs(self):
        print(f"{self.brand} laptop with {self.cpu} CPU and battery life of {self.battery_life} hours.")

# Create an instance of the Laptop class
my_laptop = Laptop("Asus", "Intel i7", 10)

# Laptop has access to methods from all levels of the inheritance chain
my_laptop.power_on()      
my_laptop.boot()          
my_laptop.show_specs()     
