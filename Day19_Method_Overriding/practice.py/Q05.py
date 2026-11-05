# Create a parent class Bank with an interest_rate() method. Override it in SBI and HDFC.

#-----------------------------------------------------------------------------------------------------------------

class Bank:

    def interest_rate(Self):
        print(f'Bank Interest Rate ')

class SBI(Bank):
    def interest_rate(Self):
        print(f'SBI Bank Interast Rate 18 %')

class HDFC(SBI):

    def interest_rate(Self):
        print(f'HDFC Bank Interest Rate 20 %')


c = Bank()
d = SBI()
e = HDFC()

c.interest_rate()
d.interest_rate()
e.interest_rate()