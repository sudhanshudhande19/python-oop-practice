# Create a Customer parent class and a PremiumCustomer child class.

# Concept: Inheritance and Polymorphism.

# Requirements:

    # Parent stores customer name and purchase amount.

    # Parent calculates a regular discount.

    # Child overrides the discount calculation.

    # Premium customers receive a different discount.

    # Display the final payable amount.

#--------------------------------------------------------------------------------------------------------------

class Customer:
    def __init__(self, name, purchase_amount):
        self.name = name
        self.purchase_amount = purchase_amount

    def calculate_discount(self):
        discount = self.purchase_amount * 0.10  # % discount
        final_amount = self.purchase_amount - discount
        return final_amount


class PremiumCustomer(Customer):
    def calculate_discount(self):
        discount = self.purchase_amount * 0.20  # % discount
        final_amount = self.purchase_amount - discount
        return final_amount


# Regular Customer
customer1 = Customer("Rahul", 5000)

# Premium Customer
customer2 = PremiumCustomer("Sudhanshu", 5000)

print("Regular Customer Payable Amount:", customer1.calculate_discount())
print("Premium Customer Payable Amount:", customer2.calculate_discount())


