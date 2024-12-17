def atm_simulator():
    balance = 1000  # Initial balance
    print("Welcome to the ATM Machine!")

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Your current balance is: ₹{balance}")
            elif choice == 2:
                amount = int(input("Enter amount to withdraw: ₹"))
                if amount > balance:
                    print("Insufficient balance!")
                elif amount <= 0:
                    print("Enter a valid amount.")
                else:
                    balance -= amount
                    print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
            elif choice == 3:
                amount = int(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Enter a valid amount.")
                else:
                    balance += amount
                    print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1-4.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

atm_simulator()
