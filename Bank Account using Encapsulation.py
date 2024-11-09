class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable (encapsulated)

    # Getter method to access the balance
    def get_balance(self):
        return self.__balance

    # Setter method to update the balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example of encapsulation in use
account = BankAccount("Ankit", 1000)

# Access balance using getter method
print("Initial balance:", account.get_balance())

# Deposit and withdraw using methods
account.deposit(500)
account.withdraw(200)
