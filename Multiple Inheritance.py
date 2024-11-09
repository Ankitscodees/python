class Father:
    def work(self):
        print("Father is working.")
        
class Mother:
    def cook(self):
        print("Mother is cooking.")
        
class Child(Father, Mother):
    def play(self):
        print("Child is playing.")

# Create an instance of Child class
child = Child()

# Child class can access methods from both Father and Mother classes
child.work()  # Output: Father is working.
child.cook()  # Output: Mother is cooking.
child.play()  # Output: Child is playing.
