# Create a DateUtility class with a static method is_leap_year(year).

# Return True if the year is a leap year and False otherwise.

# Test years such as 2024, 2025, 2000, and 1900

#----------------------------------------------------------------------------------------------------


class DateUtility:

    @staticmethod
    def is_leap_year(year):
         if year % 400 == 0:
            return True
         elif year % 100 == 0:
             return False
         elif year % 4 == 0:
             return True
         else:
             return False

kk = int(input('Enter The year ='))
r = DateUtility.is_leap_year(kk)
print(r)