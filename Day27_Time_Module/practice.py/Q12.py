# Concept: time.sleep()

# Requirements:

    # Display a loading message.
    # Show multiple loading stages.
    # Pause briefly between stages.
    # Display a completion message
    # Create a list of loading stages.
    # Loop through the stages.
    # Display each stage.
    # Pause briefly using time.sleep().
    # Display a final success message.

#-----------------------------------------------------------------------------

import time

loading_messages = [
    "Loading...",
    "Please wait...",
    "Processing...",
    "Analyzing input...",
    "Fetching data...",
    "Working on it...",
    "Almost there...",
    "Finalizing...",
    "Done!"
]

for message in loading_messages:
    print(message)
    time.sleep(1)

print("Successfully displayed all loading messages.")