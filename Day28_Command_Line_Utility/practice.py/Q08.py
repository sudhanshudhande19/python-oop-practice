# Concept: argparse, numeric arguments

# Requirements:

    # Accept a temperature value.
    # Accept the conversion type.
    # Support Celsius to Fahrenheit.
    # Support Fahrenheit to Celsius.
    # Display the converted temperature.


#--------------------------------------------------------------------------------------

import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Temperature Converter"
)

# Add arguments
parser.add_argument(
    "--temp",
    type=float,
    required=True,
    help="Temperature value"
)

parser.add_argument(
    "--convert",
    required=True,
    choices=["c2f", "f2c"],
    help="Conversion type: c2f or f2c"
)

# Parse arguments
args = parser.parse_args()

# Perform conversion
if args.convert == "c2f":
    result = (args.temp * 9/5) + 32
    print(f"{args.temp}°C = {result:.2f}°F")

elif args.convert == "f2c":
    result = (args.temp - 32) * 5/9
    print(f"{args.temp}°F = {result:.2f}°C")
