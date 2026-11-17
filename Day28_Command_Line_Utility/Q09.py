# Concept: argparse, file handling

# Requirements:

    # Accept a filename from the terminal.
    # Check whether the file exists.
    # Display the filename.
    # Display whether the file exists.
    # Handle invalid file paths.



#-----------------------------------------------------------------------------------
import argparse
import os

# Create argument parser
parser = argparse.ArgumentParser(
    description="Check whether a file exists"
)

# Add filename argument
parser.add_argument(
    "--file",
    required=True,
    help="Path of the file to check"
)

# Parse arguments
args = parser.parse_args()

# Get filename
filename = args.file

# Check if file exists
if os.path.exists(filename):
    print(f"Filename : {filename}")
    print("Status   : File exists")
else:
    print(f"Filename : {filename}")
    print("Status   : File does not exist")