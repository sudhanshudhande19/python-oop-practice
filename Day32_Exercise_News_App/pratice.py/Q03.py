# Q3. Display News Descriptions

# Concept: Dictionary values

# Requirements:

    # Store article titles and descriptions.
    # Display both fields.
    # Handle missing descriptions.

# Steps to Solve:

    # Create a list of article dictionaries.
    # Add titles and descriptions.
    # Access each article using a loop.
    # Use .get() to retrieve the description.
    # Display a default message if the description is missing.

#-----------------------------------------------------------------------------------------------------------------------------

import requests

news_response = {
        'Articles' : [
            {
                "title": "AI Changes Education",
                "description": "AI is transforming learning."
            },
            {
                "title": "India Wins Cricket Match",
                "description": "India defeated Australia."
            },
            {
                "title": "New Space Mission Launched"
            }
    ]
}


# for number, article in enumerate(news_response['Articles'], start=1):
#     title = article.get("title", "Title unavailable")
#     description = article.get("description") or "Description unavailable"
#     print(f"Article {number}: {title}")
#     print(f'Description  : {description}')


if news_response:
    for article in news_response['Articles']:
        title = article.get("title") or "Title unavailable"
        description = article.get("description") or "Description unavailable"

        print("Title:", title)
        print("Description:", description)
        print("-" * 40)
else:
    print("No news articles found.")