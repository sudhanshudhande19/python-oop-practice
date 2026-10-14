# Create a parent class Payment with a method process_payment().
# Create child classes:

    # CreditCardPayment
    # UPIPayment
    # CashPayment

# Override process_payment() in each child class with a different message.
# Create objects and demonstrate the different payment methods.
#----------------------------------------------------------------------------------------------


class payment:
    def process_payment(self):
        print('Processing payment')

class CreditCardPayment(payment):
    def process_payment(self):
        print('Payment processed using Credit Card')

class UPIPayment(payment):
    def process_payment(self):
        print('Payment processed using UPI')

class CashPayment(payment):
    def process_payment(self):
        print('Payment processed using Cash')

e = payment()
e.process_payment()

e1 = CreditCardPayment()
e1.process_payment()

e2 = UPIPayment()
e2.process_payment()

e3 = CashPayment()
e3.process_payment()