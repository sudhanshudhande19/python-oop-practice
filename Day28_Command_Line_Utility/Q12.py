# Concept: argparse, lists, calculations

# Requirements:

    # Accept a student name.
    # Accept marks for three subjects.
    # Calculate total marks.
    # Calculate percentage.
    # Display the student's result.

#-------------------------------------------------------------------------------------

import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Student Result Calculator"
)

# Add arguments
parser.add_argument(
    "--name",
    required=True,
    help="Enter student name"
)

parser.add_argument(
    "--mark1",
    type=float,
    required=True,
    help="Marks for Subject 1"
)

parser.add_argument(
    "--mark2",
    type=float,
    required=True,
    help="Marks for Subject 2"
)

parser.add_argument(
    "--mark3",
    type=float,
    required=True,
    help="Marks for Subject 3"
)

# Parse arguments
args = parser.parse_args()

# Calculate total and percentage
total = args.mark1 + args.mark2 + args.mark3
percentage = total / 3

# Display result
print("\nStudent Result")
print("-" * 25)
print(f"Name       : {args.name}")
print(f"Subject 1  : {args.mark1}")
print(f"Subject 2  : {args.mark2}")
print(f"Subject 3  : {args.mark3}")
print(f"Total Marks: {total}")
print(f"Percentage : {percentage:.2f}%")