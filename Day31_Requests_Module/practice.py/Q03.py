# Q3. Check HTTP Status Code

# Concept: response.status_code

# Requirements:

    # Send a GET request.
    # Display the status code.
    # Check whether the request was successful.

# Steps to Solve:

    # Send a GET request to a valid API endpoint.
    # Access the status code.
    # Check whether it is 200.
    # Display a success or failure message.

#------------------------------------------------------------------------------------------------------------
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url,timeout=10)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print('Request Seccessful')
else:
    print('Request Failed')