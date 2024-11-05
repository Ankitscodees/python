a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
try:
    c = a/b
    print  ("Result",c)
except:
    print(" can't divide by zero:")
else:
    print("Try blocked is sucessfully executed:")
