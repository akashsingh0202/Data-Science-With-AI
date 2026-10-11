class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def showBalance(self):
        print("Your balance is:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount


b = Bank(10000)

b.showBalance()
b.deposit(5000)
b.showBalance()