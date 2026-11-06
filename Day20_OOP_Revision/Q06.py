# Create a BankAccount class with a private balance. Implement deposit and withdraw methods with validation.

#----------------------------------------------------------------------------------------------------------------------------------


class BankAccount:
    def __init__(self,balance):
        if balance < 0:
            return f'Invalid Amount'
        else:
            self.balance = balance
        
    def deposit(self,amount):
        if amount <= 0:
            return f'Invalid Amount'
        else:
            self.balance = self.balance + amount
            print(f'Deposit = {self.balance}')

    def withdraw(self,amount):
        if amount <= 0:
            return f'Invalid Amount'
        else:
            self.balance = self.balance - amount
            print(f'Withdraw = {self.balance}')

s = BankAccount(2)
print(f'Old Balance = {s.balance}')
s.deposit(5)
s.withdraw(1)
print(f'New Balance = {s.balance}')