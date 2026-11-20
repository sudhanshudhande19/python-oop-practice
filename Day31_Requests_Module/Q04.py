# Q4. Display API Response as JSON

# Concept: response.json()

# Requirements:

    # Fetch data from an API.
    # Convert the response into Python data.
    # Display the returned data.

# Steps to Solve:

    # Send a GET request.
    # Receive the response.
    # Convert it using .json().
    # Display the result.
    # Identify whether the returned data is a dictionary or list.


# ------------------------------------------------------------------------------

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url, timeout=10)

print(response.json())