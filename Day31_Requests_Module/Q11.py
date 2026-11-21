# Q11. API User Information Finder

# Concept: API data extraction

# Requirements:

    # Fetch a user from JSONPlaceholder.
    # Display the user's name.
    # Display username and email.
    # Display the user's address.

# Steps to Solve:

    # Use the endpoint https://jsonplaceholder.typicode.com/users/1.
    # Send a GET request.
    # Convert the response into JSON.
    # Extract the name.
    # Extract username and email.
    # Access the nested address information.
    # Display the details in a readable format.

#_----------------------------------------------------------------------------------------------------------------------------------


import requests

url = 'https://jsonplaceholder.typicode.com/users/1'

responest = requests.get(url,timeout=10)

data = responest.json()

print(f'Name = {data['name']}')
print(f'Username = {data['username']}')
print(f'Email = {data['email']}')

for key, value in data['address'].items():
    print(f'{key.title()} : {value}')