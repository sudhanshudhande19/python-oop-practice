# Create a Printer class and a Scanner class. Inherit both into a MultiFunctionMachine class.

# Concept: Combining Device Functionalities.

# Requirements:

    # Printer should have a print_document() method.
    # Scanner should have a scan_document() method.
    # MultiFunctionMachine should inherit both.
    # Add a copy_document() method.
    # Test all three functionalities.

#--------------------------------------------------------------------------------------------------------------------------


class Printer:

    def print_document(self):
        print(f'Document')

class scanner:

    def scan_document(self):
        print('Sacnner')

class MultiFunctionMachine(Printer,scanner):

    def copy_document(self):
        print('copy')

s = MultiFunctionMachine()
s.print_document()
s.scan_document()
s.copy_document()