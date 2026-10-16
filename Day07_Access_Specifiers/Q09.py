# Create a parent class BankAccount with:

    # account_holder
    # _balance

# Create a child class SavingsAccount.
# Add a method display_account() that displays the account holder and balance.
#---------------------------------------------------------------------------------------------------

class  BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self._balance = balance


class SavingsAccount(BankAccount):
    def display_account(self):
        print(f'Account Holder Name = {self.account_holder}')
        print(f'Balance = {self._balance}')

obj = SavingsAccount('Sudhanshu Dhande',85020)
obj.display_account()