# Create a BankAccount class with:

    # account_holder
    # balance
    # display_balance()

# Create a SavingsAccount class with:

    # interest_rate

#------------------------------------------------------------------------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f'Name = {self.account_holder}')
        print(f'Balance = {self.balance}')


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate


e = SavingsAccount('Sudhanshu Dhande', 80000, 25)

e.display_balance()
print(f'Interest Rate = {e.interest_rate}%')