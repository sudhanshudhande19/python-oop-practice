# Q5. Extract Specific Information

# Concept: Dictionary access

# Requirements:

    # Fetch a post from JSONPlaceholder.
    # Extract its ID.
    # Extract its title.
    # Extract its body.

# Steps to Solve:

    # Send a GET request to the first post endpoint.
    # Convert the response into JSON.
    # Access the id key.
    # Access the title key.
    # Access the body key.
    # Display each value separately.

#----------------------------------------------------------------------------------------------------


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url,timeout=10)

data = response.json()

print("ID:", data.get("id"))
print("Title:", data.get("title"))
print("Body:", data.get("body"))