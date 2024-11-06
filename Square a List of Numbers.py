# A function that squares a list of numbers
def square(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result


# Example run
numbers = [15, 25, 35]
squared = square(numbers)
print(squared)
