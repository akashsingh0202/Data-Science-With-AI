class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def check_balance(self):
        print(f"Available balance: ₹{self.__balance}")

    
    def deposit(self):
        amount=int(input("enter amount how much u want to deposit"))
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful avalable balance is {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount")
        elif amount>self.__balance:
            print("insufficient balance")
        else:
          withdraw=int(input("enter money how much u want to withdraw"))
          self.__balance-=withdraw
          print(f"withdraw successfully available balance={self.__balance}")


account = BankAccount("Akash", 5000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("what do u want? ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        account.deposit()

    elif choice == "3":
        account.withdraw()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice")