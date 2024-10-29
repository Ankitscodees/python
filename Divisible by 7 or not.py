def is_divisible_by_7(number):
    return number % 7 == 0

try:
    A = int(input("Enter a number: "))
    
    if is_divisible_by_7(A):
        print(f"{A} is divisible by 7.")
    else:
        print(f"{A} is not divisible by 7.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
