# Create a Time class and overload +.

# Requirements:

    # Store hours and minutes.
    # Define __add__().
    # Add two time objects.
    # Convert excess minutes into hours.
    # Return a new Time object.
    # Display the final time.

#-----------------------------------------------------------------------------------


class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __add__(self, other):
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute

        new_hour += new_minute // 60
        new_minute = new_minute % 60

        return Time(new_hour, new_minute)

    def __str__(self):
        return f"{self.hour} hr {self.minute} min"


t1 = Time(2, 40)
t2 = Time(1, 35)

result = t1 + t2

print(result)