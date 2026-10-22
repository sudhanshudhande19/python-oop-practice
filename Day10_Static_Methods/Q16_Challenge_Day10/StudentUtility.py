# Create these static methods:

    # calculate_discount(price, percent)
    # calculate_final_price(price, percent)

# Requirements:

    # Reject negative prices.
    # Accept percentages from 0 to 100.
    # Calculate the discount amount.
    # Calculate the final price after discount.
    # Test multiple products.

#-------------------------------------------------------------------------------------------------------
class StudentUtility:

    @staticmethod
    def calculate_total(marks):
        if len(marks) != 3:
            return "Exactly 3 marks are required"

        for mark in marks:
            if mark < 0 or mark > 100:
                return "Invalid marks"

        return sum(marks)

    @staticmethod
    def calculate_percentage(marks):
        total = StudentUtility.calculate_total(marks)

        if isinstance(total, str):
            return total

        return (total / 300) * 100

    @staticmethod
    def check_result(marks):
        if len(marks) != 3:
            return "Exactly 3 marks are required"

        for mark in marks:
            if mark < 0 or mark > 100:
                return "Invalid marks"

        for mark in marks:
            if mark < 35:
                return "Fail"

        return "Pass"


# Test Student 1
marks1 = [78, 85, 92]
print("Student 1")
print("Total:", StudentUtility.calculate_total(marks1))
print("Percentage:", StudentUtility.calculate_percentage(marks1))
print("Result:", StudentUtility.check_result(marks1))

print()

# Test Student 2
marks2 = [40, 35, 50]
print("Student 2")
print("Total:", StudentUtility.calculate_total(marks2))
print("Percentage:", StudentUtility.calculate_percentage(marks2))
print("Result:", StudentUtility.check_result(marks2))

print()

# Test Student 3
marks3 = [80, 25, 90]
print("Student 3")
print("Total:", StudentUtility.calculate_total(marks3))
print("Percentage:", StudentUtility.calculate_percentage(marks3))
print("Result:", StudentUtility.check_result(marks3))