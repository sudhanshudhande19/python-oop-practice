# Create an ATM class with:
# account_holder
# balance

# Create methods:
# deposit(amount)
# withdraw(amount)
# check_balance()

# Add these rules:
# Deposit must be greater than 0.
# Withdrawal must be greater than 0.
# Withdrawal cannot exceed balance.
# Minimum balance after withdrawal should be ₹500.
# Display appropriate messages.

# Test the program using multiple transactions.
#-----------------------------------------------------------------

class ATM:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} Deposited Successfully")
        else:
            print("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")

        elif amount > self.balance:
            print("Insufficient Balance")

        elif self.balance - amount < 500:
            print("Minimum balance of ₹500 must be maintained")

        else:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")

    def check_balance(self):
        print(f"\nAccount Holder : {self.account_holder}")
        print(f"Available Balance : ₹{self.balance}")
        print("-" * 40)


# Create ATM object
acc1 = ATM("Sudhanshu Dhande", 10000)

# Multiple Transactions
acc1.check_balance()

acc1.deposit(5000)
acc1.check_balance()

acc1.withdraw(3000)
acc1.check_balance()

acc1.withdraw(12000)  # Insufficient Balance
acc1.check_balance()

acc1.withdraw(9500)   # Minimum balance rule
acc1.check_balance()

acc1.deposit(-1000)   # Invalid deposit

acc1.withdraw(0)      # Invalid withdrawal