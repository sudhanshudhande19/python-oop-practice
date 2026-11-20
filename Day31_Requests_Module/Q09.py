# Q9. Detect a 404 Error

# Concept: HTTP status codes and raise_for_status()

# Requirements:

    # Send a request to a nonexistent resource.
    # Check the status code.
    # Handle the HTTP error.

# Steps to Solve:

    # Use an invalid resource endpoint.
    # Send a GET request.
    # Display its status code.
    # Call raise_for_status().
    # Handle the exception.
    # Display a message explaining that the resource was not found.


#---------------------------------------------------------------------------------------------------------------------------------------


import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"
try:
    response = requests.get(url,timeout=10)

    print("Status Code:", response.status_code)
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Resource not found (404 Error)")