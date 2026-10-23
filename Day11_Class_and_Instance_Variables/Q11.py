# Create a BankAccount class with a class variable total_accounts = 0.

# Requirements:

    # Each object should have account_holder and balance.
    # Increase the total account count whenever an account is created.
    # Create at least four accounts.
    # Display the total number of accounts

#--------------------------------------------------------------------------------------------------------------

class BankAccount:
    total_accounts = 0

    def __init__(self,account_holder,balance):
        self.acount_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1


e1 = BankAccount('Sudhanshu Dhande',5000)
e2 = BankAccount('Pranay Dhande',6000)
e3 = BankAccount('Ayesha Ali',4000)
e4 = BankAccount('Yesh',1000)

print(f'Name = {e1.total_accounts}\nBalnce = {e1.balance}')
print('----------------------------------------------------')
print(f'Name = {e2.total_accounts}\nBalnce = {e2.balance}')
print('----------------------------------------------------')
print(f'Name = {e3.total_accounts}\nBalnce = {e3.balance}')
print('----------------------------------------------------')
print(f'Name = {e4.total_accounts}\nBalnce = {e4.balance}')
print('----------------------------------------------------')
print('total number of  account Holder =',e1.total_accounts)
    
