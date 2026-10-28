# Create a Date class with instance variables:

    # day
    # month
    # year

# Requirements:

    # Create a regular constructor that accepts day, month, and year.
    # Create a class method from_string(date_string).
    # Accept a date in the format DD-MM-YYYY.
    # Split the string and create a Date object.
    # Test both the regular constructor and the alternative constructor.

#-----------------------------------------------------------------------------------------------------------------------

class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month 
        self.year = year

    
    @classmethod
    def from_string(cls,date_string):
        day , month ,year = date_string.split('-')

        return cls(int(day),int(month),int(year))



d1 = Date(15, 8, 2026)
print("Regular Constructor:")
print(d1.day, d1.month, d1.year)



d2 = Date.from_string("26-10-2026")
print("\nAlternative Constructor:")
print(d2.day, d2.month, d2.year)