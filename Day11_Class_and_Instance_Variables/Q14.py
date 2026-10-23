# Create a Website class with a class variable visitor_count = 0.

# Requirements:

    # Increase the visitor count whenever a new visitor object is created.
    # Create five visitor objects.
    # Display the total visitors.

# For this exercise, count created visitor objects; do not count repeated visits by the same person.

#---------------------------------------------------------------------------------------------------------------------------------------

class Wedsite:
    visitor_count = 0

    def __init__(self):
        Wedsite.visitor_count += 1


e1 = Wedsite()
e2 = Wedsite()
e3 = Wedsite()
e4 = Wedsite()
e5 = Wedsite()

print('Total visitors = ',Wedsite.visitor_count)