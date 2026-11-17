# oncept: argparse

# Requirements:

    # Accept name, age, and city.
    # Use named command-line arguments.
    # Display all information.
    # Make the name argument compulsory.


#------------------------------------------------------------------------------------

import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Display user information"
)

# Add arguments
parser.add_argument(
    "--name",
    required=True,
    help="Enter your name"
)

parser.add_argument(
    "--age",
    type=int,
    help="Enter your age"
)

parser.add_argument(
    "--city",
    help="Enter your city"
)

# Parse arguments
args = parser.parse_args()

# Display information
print("\nUser Information")
print("----------------")
print("Name :", args.name)
print("Age  :", args.age)
print("City :", args.city)