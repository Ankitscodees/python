class Calculator:
    # Overloaded method: addition
    def add(self, a, b, c=0):
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Using the add method with two arguments
result1 = calc.add(10, 20)
print("Addition of two numbers:", result1)  # Output: 30

# Using the add method with three arguments
result2 = calc.add(10, 20, 30)
print("Addition of three numbers:", result2)  # Output: 60
