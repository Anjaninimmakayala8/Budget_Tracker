import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Data structure to store income/expense data
data = {
    'income': [],
    'expenses': []
}

# File to save/load data
file_name = "budget_data.json"

# Load data from file
def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': [], 'expenses': []}

# Save data to file
def save_data():
    with open(file_name, "w") as file:
        json.dump(data, file)

# Add income
def add_income(amount, description):
    income_entry = {
        'amount': amount,
        'description': description,
        'date': str(datetime.now())
    }
    data['income'].append(income_entry)
    save_data()

# Add expense
def add_expense(amount, category):
    expense_entry = {
        'amount': amount,
        'category': category,
        'date': str(datetime.now())
    }
    data['expenses'].append(expense_entry)
    save_data()

# View summary
def view_summary():
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = total_income - total_expenses

    print(f"\n--- Monthly Budget Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")
    print(f"-----------------------------")

# Visualize Income vs Expenses
def plot_income_vs_expenses():
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])

    labels = ['Income', 'Expenses']
    amounts = [total_income, total_expenses]
    colors = ['green', 'red']

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Income vs Expenses")
    plt.show()

# Visualize Expense Categories
def plot_expense_categories():
    categories = [item['category'] for item in data['expenses']]
    if not categories:
        print("No expenses to show.")
        return

    category_counts = {category: categories.count(category) for category in set(categories)}
    labels = list(category_counts.keys())
    values = list(category_counts.values())

    plt.figure(figsize=(8, 6))
    sns.barplot(x=values, y=labels, palette="muted")
    plt.xlabel("Number of Transactions")
    plt.ylabel("Expense Categories")
    plt.title("Expenses by Category")
    plt.show()

# Main function
def main():
    global data
    data = load_data()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Visualize Income vs Expenses")
        print("5. Visualize Expense Categories")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            description = input("Enter income description: ")
            add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category (e.g., Food, Rent): ")
            add_expense(amount, category)
        elif choice == "3":
            view_summary()
        elif choice == "4":
            plot_income_vs_expenses()
        elif choice == "5":
            plot_expense_categories()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
