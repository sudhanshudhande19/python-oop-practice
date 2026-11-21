import requests

try:
    user_id = input("Enter User ID: ")

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(
        url,
        params={"userId": user_id},
        timeout=10
    )

    data = response.json()

    if data:
        print(f"\nPosts of User {user_id}:\n")

        for post in data:
            print(post["title"])

        print("\nTotal Posts =", len(data))

    else:
        print("No matching posts found")

except requests.RequestException as e:
    print("Request Error:", e)