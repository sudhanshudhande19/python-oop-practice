# Create a BankAccount class with:

    # Class variable: interest_rate = 5
    # Instance variables: account_holder, balance

# Requirements:

    # Create a class method change_interest_rate(new_rate).
    # Update the interest rate for all accounts.
    # Display the current interest rate.
    # Calculate simple yearly interest using the current rate.

#-----------------------------------------------------------------------------------------------------


class BankAccount:
    interest_rate = 5

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    @classmethod
    def chnage_interes_rate(cle,new_rate):
        cle.interest_rate = new_rate
        print(f'Interest Rate = {cle.interest_rate}')

    def calculate(Self):
        print(f'Name = {Self.account_holder}') 
        print(f'Balance = {Self.balance}')   
        print(f'Yearly Interest = ₹{(Self.balance * Self.interest_rate * 1)/ 100}')

e1 =BankAccount('Sudhanhsu Dhande',10000)
BankAccount.chnage_interes_rate(7)
e1.calculate()