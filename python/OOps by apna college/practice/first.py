# class mobile:
#     def call(self):
#         print("calling.....")

# s1=mobile()
# s1.call()

# class Mobile:
#     def show_details(self):
#         print(self.brand)
#         print(self.price)

# s1=Mobile()
# s1.brand="Samsung"
# s1.price=20000

# s2=Mobile()
# s2.brand="Apple"
# s2.price=70000

# s1.show_details()
# s2.show_details()



class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.amount=amount
        if self.amount>0:
         self.__balance+=amount
         print(f"{self.amount} is successfully depostted in ur bank account")
         print(f"available balace is {self.__balance}")

        else:
           print("invalid amount")

    def withdraw(self,amount):
       if amount<=0:
          print("invalid amount")
       elif amount>=self.__balance:
          print("insufficient balace")
       
       else:
          withdraw=int(input("enter amount how much u want to withdraw"))
          self.__balance-=withdraw
          print(f"Available balance is {self.__balance}")


s1=BankAccount(10000)

s1.deposit(500)
s1.withdraw()






    
        
    