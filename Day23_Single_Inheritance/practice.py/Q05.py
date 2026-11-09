# Create a BankAccount class and inherit it into SavingsAccount.

# Concept: Real-World Inheritance.

# Requirements:

    # Parent stores account holder and balance.
    # Parent has deposit and withdraw methods.
    # Child stores interest rate.
    # Child has a method to calculate interest.
    # Display account information.

#----------------------------------------------------------------------------------------------

class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance =  balance

    def deposit(self,amount):
        return self.balance + amount

    def withdrw(self,amount):
        return self.balance - amount

class SavingsAccount(bankaccount):
    def __init__(self, account_holder, balance,inerset_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = inerset_rate


    def calculate_interest(self):
        return self.balance  * self.interest_rate / 100
        

    def display_balance(self):
        print(f'Account Holder = {self.account_holder}')
        print(f'Balance        = {self.balance}')
        print(f'Interest Rate = {self.interest_rate} ')
        print(f'Interest  = {self.calculate_interest()}')

e1 = SavingsAccount('Sudhanshu Dhande',10000,5)
e1.deposit(10000)
e1.withdrw(8000)
e1.display_balance()
e1.calculate_interest()