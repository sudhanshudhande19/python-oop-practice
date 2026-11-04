# Create a BankAccount class with a constructor containing:

# 1.account_holder
# 2.account_number
# 3.balance

# Create methods:

# 1.deposit(amount)
# 2.withdraw(amount)
# 3.display_balance()

# Create one account and test all methods.
#---------------------------------------------------------------------------------

class bankaccount:
    def __init__(self,account_holder,account_number,balance,amount):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.amount = amount

    def deposit(self):
           self.balance =  self.balance + self.amount
   
    def withdraw(self):
           self.balance = self.amount - self.balance
   
    def display_balance(self):
           print(f'Account Holder Name = {self.account_holder}\nAccount Number ={self.account_number}\nBalance = {self.balance}')
   

obj = bankaccount('Sudhanshu Dhande',23046719997002,20000,5000)
obj.deposit()
obj.withdraw()
obj.display_balance()