class Animal:
    def speak(self):
        print("Animal makes a sound.")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks!")
        super().speak()  # Calling the parent class method

# Create an instance of Dog class
dog = Dog()

dog.speak()
