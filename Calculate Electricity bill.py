def calculate_electricity_bill(units):

    bill_amount = 0
    
    if units <= 100:
        bill_amount = 0
    elif units <= 200:
        bill_amount = (units - 100) * 5
    else:
        bill_amount = 100 * 5
        bill_amount += (units - 200) * 10
    
    return bill_amount

try:
    units = float(input("Enter the number of units: "))
    
    bill_amount = calculate_electricity_bill(units)
    
    print(f"Total electricity bill amount: Rs {bill_amount:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
