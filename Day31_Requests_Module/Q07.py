# Q7. Find Posts by User ID

# Concept: Query parameters

# Requirements:

    # Fetch posts belonging to a particular user.
    # Use query parameters.
    # Display the matching posts.

# Steps to Solve:

    # Select a user ID.
    # Create a dictionary containing the query parameter.
    # end a GET request with params.
    # Convert the response into JSON.
    # Display the matching post titles.
    # Display the total number of matching posts.

#---------------------------------------------------------------------------------------------------------------------------------


import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params, timeout=10)

data = response.json()

for post in data:
    print(f"ID = {post['id']}")
    print(f"Title = {post['title']}")
    print("-" * 40)

print(f"Total Matching Posts = {len(data)}")