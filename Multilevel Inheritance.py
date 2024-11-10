class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        self.display()

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def show_manager_details(self):
        print(f"Department: {self.department}")
        self.show_employee_details()

# Create an instance of the Manager class
manager = Manager("Alice", 40, "MGR123", "Sales")

# Manager has access to methods from all levels of the inheritance chain
manager.show_manager_details()
