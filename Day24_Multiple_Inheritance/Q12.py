# Create a Customer class and an Account class. Inherit both into a BankAccount class.

# Concept: Multiple Inheritance in a Banking Application.

# Requirements:

    # Customer stores customer name and customer ID.
    # Account stores account number and balance.
    # BankAccount inherits both classes.
    # Add deposit and withdrawal methods.
    # Prevent withdrawal when balance is insufficient.
    # Display complete account details.

#----------------------------------------------------------------------------------------------------------


class Customer:

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Account:

    def __init__(self,account_no,balance):
        self.account_no = account_no
        if balance < 0:
            return ValueError
        self.balance = balance

class BankAccount(Customer,Account):

    def __init__(self,name,id,deposit):
        super().__init__(name, id)
        if deposit < 0:
            return ValueError
        self.deposit = deposit

    def withdrawal(self,amount):
        print(f'Withrawal  = {amount} ')


z = BankAccount('Sudhanshu',1012,5000)
a = Account(23046791997002,5000)
print(f'Name       = {z.name}')
print(f'ID         = {z.id}')
print(f'Account No = {a.account_no}')
print(f'Balance    = {a.balance}')
print(f'Deposit    = {z.deposit}')
z.withdrawal(2000)