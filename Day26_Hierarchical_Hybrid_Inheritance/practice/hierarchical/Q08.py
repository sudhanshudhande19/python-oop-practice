# Concept: Method overriding.

# Requirements:

    # Create Payment parent class.
    # Create CreditCard, UPI, and Cash child classes.
    # Add a pay() method in Payment.
    # Override pay() in each child class.
    # Give each child class a different payment message.
    # Create objects of all three classes.
    # Call their pay() methods.

#------------------------------------------------------------------------------------------------------

class Paymet:

    def pay(self):
        pass

class creaditCard(Paymet):

    def pay(self):
        super().pay()
        print('Payment using Credit Card')

class UPI(Paymet):

    def pay(self):
        super().pay()
        print('Payment using UPI')

class Cash(Paymet):

    def pay(self):
        super().pay()
        print('Payment using Cash')

s = creaditCard()
s2 = UPI()
s3 = Cash()

s.pay()
s2.pay()
s3.pay()