# Q5. Extract Article URLs

# Concept: List iteration

# Requirements:

    # Store at least five article URLs.
    # Display every URL.
    # Display the number of available URLs.

# Steps to Solve:

    # Create article dictionaries containing URLs.
    # Store them in a list.
    # Use a loop to access each article.
    # Extract the URL.
    # Skip missing or empty URLs.
    # Count the available URLs.

#----------------------------------------------------------------------------------------------------


news_response = {
    "articles": [
        {
            "url": "https://example.com/news1"
        },
        {
            "url": "https://example.com/news2"
        },
        {
            "url": ''
        },
        {
            "url": "https://example.com/news4"
        },
        {
            "url": None
        }
    ]
}

count = 1
for url in news_response['articles']:
    ok = url.get('url')

    if ok:
        print(ok)
        count += 1
print("\nTotal Available URLs:", count)