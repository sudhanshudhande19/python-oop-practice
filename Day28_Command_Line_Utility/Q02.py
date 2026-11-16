# Concept: sys.argv

# Requirements:

    # Accept a name through the terminal.
    # Display a welcome message.
    # Handle the case when no name is provided.
    # Import sys.
    # Check whether a name argument exists.
    # Read the name from sys.argv.
    # Display a welcome message.
    # Display a helpful message if the argument is missing.


#----------------------------------------------------------------------------------------------------\

import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f'welcome, {name}')
else:
    print('No name provided')
    print('usage python program.py <name>')