# create a BankAccount class.

# Requirements:

    # Store account holder and balance.
    # Implement __add__().
    # Add two account balances.
    # Return the combined amount as a number.
    # Do not modify either original account.

#--------------------------------------------------------------------------------------------------------------


class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)


e = BankAccount('Sudhanshu',5000)
f = BankAccount('Kunal',5000)

s = [e,f]
for i in s:
    print(f'Name = {i.account_holder}')
    print(f'Balance = {i.balance}')
    print('-------------------------------')
    
total = e.balance + f.balance

print(f'Total Balance = {total}')