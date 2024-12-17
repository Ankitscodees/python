def is_prime():
    try:
        num = int(input("Enter a number to check if it is prime: "))
        if num <= 1:
            print(f"{num} is NOT a prime number.")
            return
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is NOT a prime number. Divisible by {i}.")
                return
        print(f"{num} is a Prime Number! 🎉")
    except ValueError:
        print("Invalid input! Please enter an integer.")

is_prime()
