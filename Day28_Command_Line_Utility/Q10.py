# Concept: argparse, default values

# Requirements:

    # Accept a name.
    # Accept a greeting message.
    # Provide a default greeting.
    # Display the final greeting.


#-------------------------------------------------------------------------------

import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Greeting Application"
)

# Add arguments
parser.add_argument(
    "--name",
    required=True,
    help="Enter your name"
)

parser.add_argument(
    "--greeting",
    default="Hello",
    help="Greeting message (default: Hello)"
)

# Parse arguments
args = parser.parse_args()

# Display greeting
print(f"{args.greeting}, {args.name}!")
