expenses = []
expenseList = []
expenseDescriptions = []

print("Hello! Welcome to Gastos Galleon.")
name = input("Enter your name: ")

def addExpense():
    try:
        amount = float(input("Enter expense amount: PHP"))
        description = input("Enter a description for the expense: ")
        if amount <= 0:
            print("Invalid input. Expense amount must be greater than 0.")
        else:
            expenses.append({"amount": amount, "description": description})
            expenseList.append(amount)
            expenseDescriptions.append(description)
            print("Expense added.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def showExpenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print()
        print("===== Your Expenses =====")
        for i in range(len(expenses)):
            print(expenseDescriptions[i] + ": PHP" + str(round(expenseList[i], 2)))

        totalExpenses = sum(expenseList)
        print()
        print("Total Expenses: PHP" + str(round(totalExpenses, 2)))
        print("=========================")

def expenseTracker():
    print()
    print("Hello, " + name + "!")
    while True:
        print()
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            addExpense()
        elif choice == "2":
            showExpenses()
        elif choice == "3":
            print("Thank you for using Gastos Galleon!")
            break
        else:
            print("Invalid input. Please choose an option from 1 to 3.")

expenseTracker()