class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance is {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    # Method to get balance (read-only)
    def get_balance(self):
        return self.__balance

# Creating an instance of BankAccount
account = BankAccount("Ankit Singh", 5000)

# Accessing the account balance through the public method
print("Initial Balance:", account.get_balance()) 

# Depositing money
account.deposit(1500)  # Output: 1500 deposited. New balance is 6500

# Withdrawing money
account.withdraw(2000)  # Output: 2000 withdrawn. New balance is 4500

print("Accessing hidden balance:", account._BankAccount__balance)  # Output: 4500
