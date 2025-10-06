class ExpenseTracker:
    def __init__(self):   # ✅ fixed constructor
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        print(f"Added expense: ₹{amount} in {category} - {description}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- All Expenses ---")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['description']}")

    def summary(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return
        print("\n--- Expense Summary ---")
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"Total Expenses: ₹{total}")

        category_summary = {}
        for exp in self.expenses:
            category_summary[exp['category']] = category_summary.get(exp['category'], 0) + exp['amount']

        for cat, amt in category_summary.items():
            percent = (amt / total) * 100
            print(f"{cat}: ₹{amt} ({percent:.2f}%)")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (Food, Travel, Shopping, etc.): ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please try again.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()