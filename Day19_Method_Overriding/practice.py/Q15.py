# Create a parent class Order with a calculate_total() method. Override it in RegularOrder and PremiumOrder with different discount rules.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Order:
    def calculate_total(self):
        return 1000


class RegularOrder(Order):
    def calculate_total(self):
        total = super().calculate_total()
        return total - 100


class PremiumOrder(Order):
    def calculate_total(self):
        total = super().calculate_total()
        return total - 200


r = RegularOrder()
p = PremiumOrder()

print("Regular Order Total:", r.calculate_total())
print("Premium Order Total:", p.calculate_total())