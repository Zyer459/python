from database import add_expense, get_expense
from reports import get_total_spent, get_spending_by_category

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Reports")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Transport, etc.): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = get_expense()
            print("\nExpenses:")
            for exp in expenses:
                print(exp)

        elif choice == "3":
            total = get_total_spent()
            categories = get_spending_by_category()
            print(f"\nTotal Spent: ${total}")
            print("Spending by Category:")
            for category, amount in categories:
                print(f"{category}: ${amount}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
