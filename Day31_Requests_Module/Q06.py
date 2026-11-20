# Q6. Fetch Multiple Posts

# Concept: API list response and loops

# Requirements:

    # Fetch multiple posts.
    # Display the title of each post.
    # Display the total number of posts.

# Steps to Solve:

    # Send a GET request to https://jsonplaceholder.typicode.com/posts.
    # Convert the response into JSON.
    # Check the returned data type.
    # Use a loop to access each post.
    # Display the ID and title.
    # Count the total posts.

#---------------------------------------------------------------------------------------------------------------------

import requests

url = 'https://jsonplaceholder.typicode.com/posts'


response = requests.get(url, timeout=10)

data = response.json()
for post in data:
    print(f'ID = {post['id']}')
    print(f'Title = {post['title']}')

print(f'Total Posts = {len(data)}')