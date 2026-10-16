# Create a BankAccount class with:
    # Public attribute account_holder
    # Public attribute balance
    # Public method display_balance()

# Create an object and access its public members from outside the class.

#-----------------------------------------------------------------------------------

class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f'Account Holder Name ={self.account_holder}')
        print(f'Balance ={self.balance}')

obj = bankaccount('Sudhanshu Dhande',78000)

obj.display_balance()