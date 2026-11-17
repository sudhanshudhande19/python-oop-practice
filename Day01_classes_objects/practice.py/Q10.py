# Create a BankAccount class with:
# 1.account_holder
# 2.account_number
# 3.balance

# Create methods:
# 1.deposit(amount)
# 2.withdraw(amount)
# 3.display_balance()

# Create one object and test all methods.
#---------------------------------------------------------------
class BankAccount:
    account_holder  = ''
    account_number = 00
    balance = 00
    deposit_amount = 00
    withdraw_amount = 00


    def deposit(self):
        self.balance =  self.balance + self.deposit_amount

    def withdraw(self):
        self.balance = self.withdraw_amount - self.balance

    def display_balance(self):
        print(f'Account Holder Name = {self.account_holder}\nAccount Number ={self.account_number}\nBalance = {self.balance}')

obj = BankAccount()

obj.account_holder = 'Sudhanshu Dhande'
obj.account_number = 23046791997002
obj.balance = 10000
obj.deposit_amount = 5000
obj.withdraw_amount = 8000 

obj.deposit()
obj.withdraw()
obj.display_balance()