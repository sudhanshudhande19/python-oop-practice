# Create a BankAccount class with:

# account_holder
# balance
# deposit()
# withdraw()

# Use help(BankAccount) and understand the displayed information.

#-------------------------------------------------------------------------------------------------------


class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self):
        self.balance = self.balance  + 5000
        print(f'Deposit = {self.balance}')

    def withdraw(self):
        print(f'Withdraw = {self.balance - 2000}')

e = BankAccount('Sudhanshu Dhande',10000)

print(f'Name = {e.account_holder}')
print(f'Balance = {e.balance}')
e.deposit()
e.withdraw()
print(help(BankAccount))