# Create a parent class Bank with an interest_rate() method. Override it in SBI and HDFC.

#-----------------------------------------------------------------------------------------------------------------

class Bank:

    def interest_rate(Self):
        print(f'Bank Interest Rate ')

class SBI(Bank):
    def interest_rate(Self):
        super().interest_rate()
        print(f'SBI Bank Interast Rate 18 %')

class HDFC(SBI):

    def interest_rate(Self):
        super().interest_rate()
        print(f'HDFC Bank Interest Rate 20 %')


e = HDFC()
e.interest_rate()