# Create an EligibilityChecker class with a static method is_adult(age).

# Requirements:
    # Return True if age is 18 or older.
    # Reject negative ages.
    # Test ages below 18, equal to 18, and above 18.

#-------------------------------------------------------------------------------------------------------------------------

class EligibilityChecker:
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return 'Your Eligibal Above 18 Age'
        elif age < 0:
            return 'Reject The Negative Age '
        else:
            return 'Your Age Below than 18 Not Eligibal'

kk = int(input("Enter The Age = "))

r = EligibilityChecker.is_adult(kk)
print(r)