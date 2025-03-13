from database import add_expense, get_expense
from reports import *

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Reports")
        print("4. Visualize data")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Transport, etc.): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")

        elif choice == 2:
            expenses = get_expense()
            print("\nExpenses:")
            for exp in expenses:
                print(exp)

        elif choice == 3:
            total = get_total_spent()
            categories = get_spending_by_category()
            print(f"\nTotal Spent: ${total}")
            print("Spending by Category:")
            for category, amount in categories:
                print(f"{category}: ${amount}")

        elif choice == 4:
        	print('\n1. pie-chart: spending by category')
        	print('2. bar-chart: spending trend over time')
        	viz_choice = int(input('select an option: '))
        	
        	if viz_choice == 1:
        		plot_spending_by_category()
        	elif viz_choice == 2:
        		plot_spending_trend()
        	else:
        		print('invalid choice')        
        
        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
