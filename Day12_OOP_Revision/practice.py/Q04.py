# Create a BankAccount class with:

#     account_holder
#     Private attribute __balance

# Methods:

#     deposit(amount)
#     withdraw(amount)
#     get_balance()

# Requirements:

#     Reject non-positive deposit amounts.
#     Prevent withdrawals greater than the available balance.
#     Test valid and invalid transactions.


#-------------------------------------------------------------------------------------------------

class BankAccount:

    def __init__(self,account_holder,privete_balance):
        self.account_holder = account_holder
        self.privete_balance = privete_balance

    def deposit(self,amount):
        if amount <= 0:
            print('Reject deposit The Amount')
        else:
            self.privete_balance = self.privete_balance + amount

    def withdraw(self,amount):
        if amount <= self.privete_balance:
            self.privete_balance = self.privete_balance - amount
        
        else:
            print('Unavailable withdraw Balance')

    def get_balance(self):
        print(f'Holder Name = {self.account_holder}')
        print(f'New Balance = {self.privete_balance}')

e1 = BankAccount('Sudhanshu',10000)

e1.deposit(5000)
e1.withdraw(4000)
e1.get_balance()