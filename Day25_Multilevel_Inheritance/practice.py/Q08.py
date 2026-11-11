# Concept: Multilevel Inheritance with customer information.

# Requirements:

    # Create User, Customer, and PremiumCustomer classes.
    # User stores username and email.
    # Customer stores customer ID.
    # PremiumCustomer stores discount percentage.
    # Create a method to calculate final price after discount.
    # Display all customer details.

#----------------------------------------------------------------------------------------------------------------

class User:

    def __init__(self,username,email):
        self.username = username
        self.email = email

class customer(User):

    def __init__(self, username, email,customer_id):
        super().__init__(username, email)
        self.customer_id = customer_id

class PremiumCustomer(customer):
    def __init__(self, username, email, customer_id, discount_per):
        super().__init__(username, email, customer_id)
        self.discount_per = discount_per

    def calculate_price(self, price):
        final_price = price - (price * self.discount_per / 100)
        return final_price

    def display_details(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Discount: {self.discount_per}%")
        

obj = PremiumCustomer(
    "Sudhanshu",
    "sudhanshu@gmail.com",
    101,
    20
)

obj.display_details()

price = 1000
print(f'Orifinal Price = {price}')
print("Final Price =", obj.calculate_price(price))