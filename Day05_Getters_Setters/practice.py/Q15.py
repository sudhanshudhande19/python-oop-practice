# Create a BankAccount class with:

    # _account_holder
    # _balance

# Requirements:

    # Account holder name cannot be empty.
    # Balance cannot be negative.
    # Use a property to read the balance.
    # Create a deposit(amount) method that accepts only positive amounts.
    # Create a withdraw(amount) method that rejects invalid amounts or insufficient funds.

# Test valid and invalid operations.
#--------------------------------------------------------------------------------------------------------------

class bankaccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
     

    @property
    def account_holder(self):
        return self._account_holder
    @account_holder.setter
    def account_holder(self,new_account_holder):
        if new_account_holder.strip():
            self._account_holder = new_account_holder
        else:
            print('Holder Name Canot Be Empty')
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print('Balance Cannote be Empty')
    

    def deposit(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print("Withdrawn:", amount)

    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print("Withdrawn:", amount)

    def info(self):
        print('Holder Name =',self.account_holder)
        print('Final Balance =',self.balance)
        print('------------------------------')

e1 =bankaccount('sudhanshu',1000)

e1.deposit(500)       # Valid deposit
e1.withdraw(200)      # Valid withdrawal
e1.deposit(-100)      # Invalid deposit
e1.withdraw(2000)     # Insufficient funds
e1.withdraw(0)        # Invalid withdrawal

e1.info()
