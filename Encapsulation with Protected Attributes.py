class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Protected attribute
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance!")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

# Create an object
account = BankAccount("John", 1000)

# Access protected attribute indirectly
print(account.get_balance())  # Output: 1000

# Access protected attribute directly (not recommended but possible)
print(account._balance)  # Output: 1000
