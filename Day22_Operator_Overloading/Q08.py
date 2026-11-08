# Create a Money class and overload +.

# Requirements:

    # Store an amount.
    # Store the currency.
    # Define __add__().
    # Allow addition only when currencies match.
    # Return a new Money object.
    # Handle different currencies safely.

#-------------------------------------------------------------------------------------------------------------

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            return "Error: Cannot add different currencies"

        return Money(
            self.amount + other.amount,
            self.currency
        )

    def __str__(self):
        return f"{self.amount} {self.currency}"


m1 = Money(100, "INR")
m2 = Money(200, "INR")

result = m1 + m2
print(result)


m3 = Money(50, "USD")

result2 = m1 + m3
print(result2)