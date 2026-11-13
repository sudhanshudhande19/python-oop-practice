# Concept: Hierarchical Inheritance with calculations.

# Requirements:

    # Create BankAccount parent class.
    # Create SavingsAccount and CurrentAccount child classes.
    # Store account holder and balance in BankAccount.
    # SavingsAccount stores interest rate.
    # CurrentAccount stores overdraft limit.
    # Add a method to calculate savings interest.
    # Display the details of both accounts.

#-------------------------------------------------------------------------------------------------------------

class BankAccount:

    def __init__(self,name,balance):
        self.name = name 
        self.balance = balance

class SavingAccount(BankAccount):

    def __init__(self, name, balance,interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate(self):
        print(f'Interst = {(self.balance * self.interest_rate)/ 100}')

class CurrentAccount(BankAccount):

    def __init__(self, name, balance,overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

s = SavingAccount('Rahul',50000,5)
print(f'Saving Account = {s.name}')
print(f'Balance = {s.balance}')
s.calculate()

print()
c = CurrentAccount('Amit',80000,20000)
print(f'Current Acount = {c.name}')
print(f'Balance = {c.balance}')
print(f'Overdraft Limit = {c.overdraft_limit}')