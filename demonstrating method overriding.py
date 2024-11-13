# Parent class
class Animal:
    def sound(self):
        return "Some generic animal sound"

# Child class
class Dog(Animal):
    # Overriding the sound method
    def sound(self):
        return "Bark"

# Child class
class Cat(Animal):
    # Overriding the sound method
    def sound(self):
        return "Meow"

# Creating instances of each class
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Calling the sound method on each instance
print("Animal sound:", generic_animal.sound())  # Output: Some generic animal sound
print("Dog sound:", dog.sound())  # Output: Bark
print("Cat sound:", cat.sound())  # Output: Meow
