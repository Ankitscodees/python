# Input student's marks
marks = int(input("Enter your marks: "))

if marks >= 40:  # Check if student passed
    if marks >= 90:
        print("Excellent")
    elif marks >= 75:
        print("Very Good")
    elif marks >= 60:
        print("Good")
    elif marks >= 50:
        print("Average")
    else:
        print("Pass")
else:
    print("Fail")
