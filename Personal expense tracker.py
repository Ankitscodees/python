def expense_tracker():
    print("Welcome to the Personal Expense Tracker!")
    expenses = []
    
    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Total expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                expenses.append({"amount": amount, "description": description})
                print("Expense added successfully!")
            except ValueError:
                print("Invalid amount. Please try again.")
        elif choice == "2":
            if not expenses:
                print("No expenses recorded.")
            else:
                print("\nYour Expenses:")
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}. {expense['description']}: ${expense['amount']:.2f}")
        elif choice == "3":
            total = sum(expense["amount"] for expense in expenses)
            print(f"\nTotal expenses: ${total:.2f}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the expense tracker
expense_tracker()
