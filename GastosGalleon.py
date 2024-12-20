# Creates empty lists to store information about the user’s input.
expenses = []
expenseList = []
expenseDescriptions = []

# Greets the user, asks for their name, and saves it in the variable for later use.
print("Hello! Welcome to Gastos Galleon.")
name = input("Enter your name: ")

# Input expense amount and description, validates input, stores it in lists, and asks  for corrections if the input is invalid.
def addExpense():
    try:
        # Take the expense amount and description
        amount = float(input("Enter expense amount: PHP"))
        description = input("Enter a description for the expense: ")
        # Check if the value entered is valid
        if amount <= 0:
            print("Invalid input. Expense amount must be greater than 0.")
        else:
            # Add the information to their respective lists
            expenses.append({"amount": amount, "description": description})
            expenseList.append(amount)
            expenseDescriptions.append(description)
            print("Expense added.")
    except ValueError:
        # Deals with invalid input for expense amount
        print("Invalid input. Please enter a valid amount.")
        
# Checks for recorded expenses, displays each one with its description and amount, and shows the total sum.
def showExpenses():
    if not expenses: # Check if there are no recorded expenses
        print("No expenses recorded.")
    else:
        print()
        print("===== Your Expenses =====")
        # Print all the recorded expenses along with the descriptions
        for i in range(len(expenses)):
            print(expenseDescriptions[i] + ": PHP" + str(round(expenseList[i], 2)))
        # Find and show the total amount of all costs
        totalExpenses = sum(expenseList)
        print()
        print("Total Expenses: PHP" + str(round(totalExpenses, 2)))
        print("=========================")

# Looping through options to add or view expenses, or exit the program, until the user chooses to exit.
def expenseTracker():
    print()
    print("Hello, " + name + "!")
    while True:
        print()
        print("1. Add Expense") 
        print("2. Show Expenses")
        print("3. Exit")
        # Get the user's input
        choice = input("Choose an option: ")
        
        if choice == "1":
            addExpense() # Call the addExpense function
        elif choice == "2":
            showExpenses() # Call the showExpenses function
        elif choice == "3":
            print("Thank you for using Gastos Galleon!")
            break # Exit the loop and terminate the program
        else:
            print("Invalid input. Please choose an option from 1 to 3.")
# Start the expense tracking process
expenseTracker()
