# Concept: Advanced calculations and method overriding.

# Requirements:

    # Create Account, SavingsAccount, and PremiumSavingsAccount classes.
    # Account stores account holder and balance.
    # SavingsAccount stores normal interest rate.
    # PremiumSavingsAccount stores premium interest rate.
    # Create an interest calculation method.
    # Override the method in PremiumSavingsAccount.
    # Compare the interest earned by both accounts

#_-------------------------------------------------------------------------------------------------------------------------------

class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)


    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100



normal = SavingsAccount("Sudhanshu", 50000, 5)
premium = PremiumSavingsAccount("Sudhanshu", 50000, 8)

normal_interest = normal.calculate_interest()
premium_interest = premium.calculate_interest()

print("Normal Account Interest =", normal_interest)
print("Premium Account Interest =", premium_interest)
print("Difference =", premium_interest - normal_interest)