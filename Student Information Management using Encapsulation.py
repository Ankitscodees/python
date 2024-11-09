class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private variable to store marks

    # Getter method to access marks
    def get_marks(self):
        return self.__marks

    # Setter method to set marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

    # Method to display student details
    def display_student_info(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.__marks}")

# Example of encapsulation in use
student1 = Student("Ankit", 85)

# Display student info using method
student1.display_student_info()

# Update marks using setter method
student1.set_marks(92)
student1.display_student_info()

# Trying to set invalid marks
student1.set_marks(105)  # Invalid, will show an error message

# Access marks using getter method
print("Updated Marks:", student1.get_marks())

 print(student1.__marks)
