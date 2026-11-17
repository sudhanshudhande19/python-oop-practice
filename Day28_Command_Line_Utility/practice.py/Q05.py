# oncept: argparse.ArgumentParser()

# Requirements:

    # Import argparse.
    # Create an argument parser.
    # Add a named argument called --name.
    # Parse the arguments.
    # Access the value using args.name.
    # Display the result.


#--------------------------------------------------------------------------------------------



import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Welcome Program")

# Add --name argument
parser.add_argument("--name", help="Enter your name")

# Parse arguments
args = parser.parse_args()

# Display result
if args.name:
    print(f"Welcome, {args.name}!")
else:
    print("Please provide your name using --name")