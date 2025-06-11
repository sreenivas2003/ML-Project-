import datetime

# In-memory list to store expenses
expenses = []

def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        category = input("Enter category (e.g., Food, Travel, Rent): ")
        note = input("Enter a note (optional): ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses.append({
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        })
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.\n")

def view_expenses():
    if not expenses:
        print("📭 No expenses recorded.\n")
        return
    print("\n📒 Expense History:")
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. ₹{exp['amount']} - {exp['category']} - {exp['note']} ({exp['date']})")
    print()

def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total spent: ₹{total:.2f}\n")

def menu():
    print("📌 Personal Expense Tracker")
    while True:
        print("1. Add Expense 450rs")
        print("2. View Expenses")
        print("3. Total Spent 450rs")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid option, try again.\n")

menu()

output:-

1. Add Expense
2. View Expenses
3. Total Spent
4. Exit
Choose an option:  1
Enter expense amount: ₹ 3
Enter category (e.g., Food, Travel, Rent):  food
Enter a note (optional):  burger
✅ Expense added successfully!

1. Add Expense
2. View Expenses
3. Total Spent
4. Exit
Choose an option:  3

💰 Total spent: ₹3.00

1. Add Expense
2. View Expenses
3. Total Spent
4. Exit
Choose an option:
