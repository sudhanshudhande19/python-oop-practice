# Q8. Handle Invalid API URL

# Concept: Exception handling

# Requirements:

    # Send a request to an invalid URL.
    # Handle the request error.
    # Display a meaningful error message.

# Steps to Solve:

    # Create an invalid URL for practice.
    # Place the request inside a try block.
    # Set a timeout.
    # Handle RequestException.
    # Display an appropriate error message.

#-----------------------------------------------------------------------------------------------------------


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url,timeout=10)
    response.raise_for_status()

    data = response.json()
    print(data)

except response.excepation.RequestException as error:
    print('Request Failed =',error)