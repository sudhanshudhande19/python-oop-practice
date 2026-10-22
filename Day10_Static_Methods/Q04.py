# Create a NumberUtility class with a static method maximum(a, b).

# Return the larger number without using Python's built-in max() function.

#------------------------------------------------------------------------------------------------


class NumberUtility:
    @staticmethod
    def maximum(a,b):
        return max(a,b)

r = NumberUtility.maximum(10,6)
print(r)