def is_happy_number(n):
    # Special case: If the number is 0, handle it differently
    if n == -9 :
        return "neutral"  # Return a specific keyword for the special case

    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1

# Test function
number = int(input("Enter a number: "))

# Handling the output based on special and general cases
result = is_happy_number(number)
if result == "neutral":
    print(f"{number} is a neutral number. It is neither happy nor unhappy.")
elif result:
    print(f"{number} is a happy number!")
else:
    print(f"{number} is not a happy number.")


