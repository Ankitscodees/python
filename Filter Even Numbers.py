# A function that filters even numbers
def filter_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


# Example run
numbers = [17, 22, 83, 41, 50, 63, 72, 89, 92, 10]

even_nums = filter_even(numbers)

print(even_nums)
