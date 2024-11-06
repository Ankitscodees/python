# Function that prints multiplication table from 1 to 10.
def mul_table(num):
    for i in range(1, 11):
       print(f"{num} x {i} = {num * i}")
       
# Example call
mul_table(16)
