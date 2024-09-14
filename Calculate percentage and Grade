def determine_grade(percentage):
    if percentage > 90:
        return 'A'
    elif 80 < percentage <= 90:
        return 'B'
    elif 60 <= percentage <= 80:
        return 'C'
    else:
        return 'D'

try:
    percentage = float(input("Enter the percentage: "))
    
    grade = determine_grade(percentage)
    
    print(f"The grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
