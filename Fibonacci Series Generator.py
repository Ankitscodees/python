def fibonacci_series():
    try:
        n = int(input("Enter the number of terms for the Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        a, b = 0, 1
        count = 0

        print("Fibonacci Series:")
        while count < n:
            print(a, end=" ")
            a, b = b, a + b
            count += 1
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

fibonacci_series()
