# Concept: Diamond Inheritance and MRO.

# Requirements:

    # Create Account as common parent.
    # SavingsAccount and CurrentAccount inherit from Account.
    # PremiumSavingsAccount inherits from SavingsAccount and CurrentAccount.
    # Account stores holder name and balance.
    # SavingsAccount defines an interest method.
    # CurrentAccount defines a transaction method.
    # PremiumSavingsAccount inherits from both.
    # Override the interest method if required.
    # Print PremiumSavingsAccount.mro().
    # Observe the method execution order.

#-------------------------------------------------------------------------------------------------


class Account:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_details(self):
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)

    def interest(self):
        print("Savings Interest: 5%")


class CurrentAccount(Account):
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)

    def transaction(self):
        print("Current Account Transaction Successful")


class PremiumSavingsAccount(SavingsAccount, CurrentAccount):
    def __init__(self, holder_name, balance):
        super().__init__(holder_name, balance)


    def interest(self):
        print("Premium Savings Interest: 8%")



acc = PremiumSavingsAccount("Rahul", 50000)


acc.show_details()
acc.interest()
acc.transaction()

print("\nMRO:")
print(PremiumSavingsAccount.mro())