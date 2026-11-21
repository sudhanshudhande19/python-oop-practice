import requests

# Base URL of API
BASE_URL = "https://jsonplaceholder.typicode.com"


# Function to fetch a single post
def get_single_post():

    # Take post ID from user
    post_id = input("Enter Post ID: ")

    try:
        # Send GET request
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}",
            timeout=10
        )

        # Display status code
        print("Status Code:", response.status_code)

        # Check if post exists
        if response.status_code == 200:

            # Convert response to JSON
            data = response.json()

            print("\nPOST DETAILS")
            print("ID:", data["id"])
            print("Title:", data["title"])
            print("Body:", data["body"])

        else:
            print("Post not found!")

    except requests.RequestException as e:
        print("Network Error:", e)


# Function to fetch all posts
def get_all_posts():

    try:
        # Send GET request
        response = requests.get(
            f"{BASE_URL}/posts",
            timeout=10
        )

        # Display status code
        print("Status Code:", response.status_code)

        # Convert data to JSON
        posts = response.json()

        # Loop through all posts
        for post in posts:

            print(f"\nPost ID: {post['id']}")
            print("Title:", post["title"])

        # Display total posts
        print("\nTotal Posts:", len(posts))

    except requests.RequestException as e:
        print("Network Error:", e)


# Function to search posts by user ID
def search_by_user():

    # Take user ID from user
    user_id = input("Enter User ID: ")

    try:

        # Send GET request with query parameter
        response = requests.get(
            f"{BASE_URL}/posts",
            params={"userId": user_id},
            timeout=10
        )

        print("Status Code:", response.status_code)

        # Convert to JSON
        posts = response.json()

        # Check if posts exist
        if posts:

            print("\nMATCHING POSTS")

            # Display all matching post titles
            for post in posts:
                print(f"\nTitle: {post['title']}")

            print("\nTotal Posts:", len(posts))

        else:
            print("No posts found.")

    except requests.RequestException as e:
        print("Network Error:", e)


# Function to fetch user information
def get_user_info():

    # Take user ID
    user_id = input("Enter User ID: ")

    try:

        # Send GET request
        response = requests.get(
            f"{BASE_URL}/users/{user_id}",
            timeout=10
        )

        print("Status Code:", response.status_code)

        # Check status code
        if response.status_code == 200:

            # Convert JSON
            data = response.json()

            print("\nUSER DETAILS")
            print("Name:", data["name"])
            print("Username:", data["username"])
            print("Email:", data["email"])

            # Access nested address dictionary
            address = data["address"]

            print("\nADDRESS DETAILS")
            print("Street:", address["street"])
            print("Suite:", address["suite"])
            print("City:", address["city"])
            print("Zipcode:", address["zipcode"])

        else:
            print("User not found.")

    except requests.RequestException as e:
        print("Network Error:", e)


# ================= MAIN PROGRAM =================

while True:

    # Display menu
    print("\n" + "=" * 65)
    print("                 PYTHON API DATA EXPLORER")
    print("=" * 65)

    print("1. Get Single Post")
    print("2. Get All Posts")
    print("3. Search Posts by User ID")
    print("4. Get User Information")
    print("5. Exit")

    try:

        # Take user choice
        option = int(input("\nEnter Your Choice: "))

        # Menu handling
        if option == 1:
            get_single_post()

        elif option == 2:
            get_all_posts()

        elif option == 3:
            search_by_user()

        elif option == 4:
            get_user_info()

        elif option == 5:
            print("Program Closed Successfully.")
            break

        else:
            print("Invalid Choice! Please choose between 1 to 5.")

    except ValueError:
        print("Please enter only numeric values.")