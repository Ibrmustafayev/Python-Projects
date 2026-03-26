import json

class Transaction:
    def __init__(self, amount, category, description, type):
        self.amount = amount
        self.category = category
        self.description = description
        self.type = type

    def to_dict(self):
        return {"amount" : self.amount, "category" : self.category, "description" : self.description, "type" : self.type}

class Tracker:
    def __init__(self):
        self.transactions = []
        self.load()

    def load(self):
        try:
            with open("finances.json", "r") as f:
                self.transactions = json.load(f)
        except:
            self.transactions = []

    def save(self):
        with open("finances.json", "w") as f:
            json.dump(self.transactions, f)
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction.to_dict())
        self.save()

    def view_all(self):
        if self.transactions:
            for i, transaction in enumerate(self.transactions):
                print(f"{i + 1}. [{transaction["type"].capitalize()}] ${transaction["amount"]:.2f} - {transaction["description"]} ({transaction["category"]})")
        else:
            print("None to display.")

    def summary(self):
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        total_expense = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        print(f"Total Income:   ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Net Balance:    ${(total_income - total_expense):.2f}")         
    
    def filter_by_category(self, category):
        filtered = [transaction for transaction in self.transactions if transaction["category"].lower() == category.lower()]
        if filtered:
            for i, transaction in enumerate(filtered):
                print(f"{i + 1}. [{transaction["type"].capitalize()}] ${transaction["amount"]:.2f} - {transaction["description"]} ({transaction["category"]})")
        else:
            print("None to display.")

def run():
    tracker = Tracker()
    while True:
        print("\n=== Finance Tracker ===\n")
        print("1. Add transaction")
        print("2. View all")
        print("3. Summary")
        print("4. Filter by category")
        print("5. Exit")
        choice = input("\nChoice: ")
        if choice == "5":
            print("Goodbye!!!")
            break
        elif choice == "1":
            try:
                amount = float(input("\nAmount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                category = input("Category: ")
                description = input("Description: ")
                type = input("type (income / expense): ").lower()
                if type not in ("income", "expense"):
                    print("Type must be either 'income' or 'expense'.")
                    continue
                tracker.add_transaction(Transaction(amount, category, description, type))
                print("Transaction added.")
            except ValueError:
                print("Error: Invalid amount.")
        elif choice == "2":
            tracker.view_all()
        elif choice == "3":
            tracker.summary()
        elif choice == "4":
            category = input("Category: ")
            tracker.filter_by_category(category)
        else:
            print("Error: invalid choice option.")

run()
