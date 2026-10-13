# Create a parent class BankAccount with:
    # account_holder
    # balance
    # deposit(amount)
    # display_balance()

# Create a child class SavingsAccount with:

    # interest_rate
    # calculate_interest()

# Formula:
    # Interest = balance × interest_rate / 100
    # Use super() in the child constructor. Test the account with different balances.
#------------------------------------------------------------------------------------------------------

class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance =  balance

    def deposit(self,amount):
        return self.balance + amount

    def display_balance(self):
        print(f'Account Holder = {self.account_holder}')
        print(f'Balance        = {self.balance}')


class SavingsAccount(bankaccount):
    def __init__(self, account_holder, balance,inerset_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = inerset_rate


    def calculate_interest(self):
        interset = self.balance  * self.interest_rate / 100
        print(f'Interest Rate = {self.interest_rate} ')
        print(f'Interest  = {interset}')

e1 = SavingsAccount('Sudhanshu Dhande',10000,5)
e1.deposit(8500)
e1.display_balance()
e1.calculate_interest()