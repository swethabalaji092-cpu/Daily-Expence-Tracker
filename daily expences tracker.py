expenses = []

while True:
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Total Expense")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})

    elif choice == "2":
        for e in expenses:
            print(e)

    elif choice == "3":
        total = sum(e["amount"] for e in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        break
