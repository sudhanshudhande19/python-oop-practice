# Concept: Multilevel Inheritance with calculations.

# Requirements:

    # Create Bank, Account, and SavingsAccount classes.
    # Bank stores bank name.
    # Account stores account number and balance.
    # SavingsAccount stores interest rate.
    # Create a method to calculate annual interest.
    # Display account details and interest.

#----------------------------------------------------------------------------------------------------------------


class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name

class Account(Bank):

    def __init__(self, bank_name,account_no,balance):
        super().__init__(bank_name)
        self.account_no = account_no
        self.balance = balance

class SavingAccount(Account):

    def __init__(self, bank_name, account_no, balance,interest_rate):
        super().__init__(bank_name, account_no, balance)
        self.interest_rate = interest_rate

    def calculate_annual_interest(self):
        print(f'Annual Interest = {(self.balance * self.interest_rate)/ 100}')

s = SavingAccount('SBI',12345,50000,5)
print(f'Bank = {s.bank_name}')
print(f'Account No = {s.account_no}')
print(f'Balance = {s.balance}')
print(f'Interest Rate = {s.interest_rate} %')
s.calculate_annual_interest()