
import json
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "bank_accounts.json")

print("JSON file location:", FILE_NAME)

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.__balance = balance
        self.account_number = account_number
        self.transactions = []

    def check_balance(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: ₹{self.__balance}")

    def deposit(self):
        try:
            amount = int(input("Kitna deposit karna hai? ₹"))
        except ValueError:
            print("Please enter a valid number!")
            return

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        self.__balance += amount
        self.transactions.append(f"Deposited: ₹{amount}")
        print("Deposit successful!")
        self.check_balance()

    def withdraw(self):
        try:
            amount = int(input("Kitna withdraw karna hai? ₹"))
        except ValueError:
            print("Please enter a valid number!")
            return

        if amount <= 0:
            print("Amount must be greater than zero!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")
            print("Withdrawal successful!")
            self.check_balance()

    def transaction_history(self):
        print(f"\n--- {self.name}'s Transaction History ---")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.__balance,
            "account_number": self.account_number,
            "transactions": self.transactions
        }

    @classmethod
    def from_dict(cls, data):
        account = cls(
            data["name"],
            data["balance"],
            data["account_number"]
        )
        account.transactions = data.get("transactions", [])
        return account


accounts = {}


def save_accounts():
    data = {
        number: account.to_dict()
        for number, account in accounts.items()
    }

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Account data saved successfully!")
    except OSError:
        print("Error: Could not save account data!")


def load_accounts():
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        for number, details in data.items():
            accounts[number] = BankAccount.from_dict(details)

        print(f"{len(accounts)} account(s) loaded successfully!")

    except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
        print("Warning: Account file could not be loaded.")
        print("Please check the JSON file before continuing.")


def generate_account_number():
    while True:
        number = str(random.randint(10000000, 99999999))
        if number not in accounts:
            return number


def find_account():
    number = input("Enter your account number: ").strip()

    if number in accounts:
        return accounts[number]

    print("Account not found!")
    return None


# Load existing accounts when the program starts
load_accounts()


while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("What do you want to do? ").strip()

    if choice == "1":
        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        try:
            balance = int(input("Enter initial balance: ₹"))

            if balance < 0:
                print("Balance cannot be negative!")
                continue

            account_number = generate_account_number()

            accounts[account_number] = BankAccount(
                name, balance, account_number
            )

            print("\nAccount created successfully!")
            print(f"Name: {name}")
            print(f"Account Number: {account_number}")
            print(f"Initial Balance: ₹{balance}")
            print("Please save your account number!")

            save_accounts()

        except ValueError:
            print("Please enter a valid balance!")

    elif choice == "2":
        account = find_account()
        if account:
            account.check_balance()

    elif choice == "3":
        account = find_account()
        if account:
            account.deposit()
            save_accounts()

    elif choice == "4":
        account = find_account()
        if account:
            account.withdraw()
            save_accounts()

    elif choice == "5":
        account = find_account()
        if account:
            account.transaction_history()

    elif choice == "6":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please select 1-6.")
