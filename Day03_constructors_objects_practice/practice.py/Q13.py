# Create a Product class with:
# name
# price
# quantity

# Create methods:
# subtotal()
# discount()
# gst()
# final_bill()

# Rules:
# Subtotal >= ₹10,000 → 15% discount
# Subtotal >= ₹5,000  → 10% discount
# Otherwise            → No discount

# After applying the discount, calculate 18% GST.
# Display a complete bill.
#------------------------------------------------------------

class Product:
    def __init__(self,name,price,quantity):
        self.name = name   # Class Attribute
        self.price =price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity

    def discount(self):
        if self.subtotal() >= 10000:
            return  self.subtotal() * 0.15
        elif self.subtotal() >= 5000:
            return self.subtotal() * 0.10
        else:
            return 0

    def gst(self):
        dis = self.subtotal() - self.discount()
        gst_amount = dis * 0.18 
        return dis + gst_amount
    
    def final_bill(self):
        print('----Shopping Bill---------')
        print(f"Product Name = {self.name}")
        print(f"Total Price = {self.subtotal()}")
        print(f"Discount = {self.discount()}")
        print(f"Final Price With GST(18%)= {self.gst()}")
        print('--------------------------------------------')

s1 = Product('Iphone Mobile ',150000, 1)
s2 = Product('Asusu Laptop',225000,2)
s3 = Product ('Samsung Mobile',140000,3)

s1.final_bill()
s2.final_bill()
s3.final_bill()