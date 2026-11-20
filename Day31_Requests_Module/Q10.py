# not found.

# Q10. Send Data Using POST

# Concept: requests.post()

# Requirements:

    # Create a dictionary containing post information.
    # Send the data using POST.
    # Display the response status and returned JSON.

# Steps to Solve:

    # Create a dictionary with title, body, and user ID.
    # Send a POST request to the posts endpoint.
    # Pass the dictionary using the json parameter.
    # Display the status code.
    # Convert the response into JSON.
    # Display the returned information.

#--------------------------------------------------------------------------------------------

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"


data = {
    'id' : 101,
    'title' : 'python',
    'body' : 'Python oop function'

}

response = requests.post(url,json=data,timeout=10)
print(response.status_code)
print(data)
