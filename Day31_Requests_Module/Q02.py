# Q2. Send Your First GET Request

# Concept: requests.get()

# Requirements:

    # Send a GET request to JSONPlaceholder.
    # Store the response.
    # Display the response text.

# Steps to Solve:

    # Import the Requests library.
    # Store this API URL: https://jsonplaceholder.typicode.com/posts/1.
    # Send a GET request.
    # Store the response in a variable.
    # Display the response text.

#-------------------------------------------------------------------------------------------------------------------------------


import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

reponse = requests.get(url,timeout=10)

print(reponse.text)