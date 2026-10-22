# Create a StudentUtility class with static methods:

    # calculate_total(maths, science, english)
    # calculate_percentage(maths, science, english)
    # is_pass(maths, science, english)

# Requirements:

    # Each subject is out of 100.
    # Validate that marks are between 0 and 100.
    # The student passes only if every subject mark is at least 35.
    # Test at least three students.

#----------------------------------------------------------------------------------------------------------------------
class StudentUtility:

    @staticmethod
    def calculate_total(maths, science, english):
        if (0 <= maths <= 100 and
            0 <= science <= 100 and
            0 <= english <= 100):
            return maths + science + english
        return "Invalid Marks"

    @staticmethod
    def calculate_percentage(maths, science, english):
        total = StudentUtility.calculate_total(
            maths, science, english
        )

        if total == "Invalid Marks":
            return "Invalid Marks"

        return (total / 300) * 100

    @staticmethod
    def is_pass(maths, science, english):
        if maths >= 35 and science >= 35 and english >= 35:
            return True
        return False


print('--------Student 1--------------------')
print('Total =',StudentUtility.calculate_total(63, 85, 96))
print('Percentage =',StudentUtility.calculate_percentage(63, 85, 96))
print('Result =',StudentUtility.is_pass(63, 85, 96))
print('------------------------------------------------')

print('---------Student 2-------------------------')
print('Total =',StudentUtility.calculate_total(40, 36, 50))
print('Percentage =',StudentUtility.calculate_percentage(40, 36, 50))
print('Result =',StudentUtility.is_pass(40, 36, 50))
print('------------------------------------------------')

print('----------Student 3-------------------------')
print('Total =',StudentUtility.calculate_total(80, 20, 90))
print('Percentage =',StudentUtility.calculate_percentage(80, 20, 90))
print('Result =',StudentUtility.is_pass(80, 20, 90))
print('------------------------------------------------')
