# Create a Date class with:

    # day
    # month
    # year

# Requirements:

    # Create a class method from_string(date_string).
    # Accept dates in the format "29-10-2026".
    # Convert the date components into integers.
    # Display the date in DD-MM-YYYY format.

#--------------------------------------------------------------------------------------------------------------


class Data:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls,data_string):
        day,month,year = data_string.split('-')
        return cls(int(day),int(month),int(year))

e = Data.from_string('29-10-2026')
print(f'{e.day}-{e.month}-{e.year}')