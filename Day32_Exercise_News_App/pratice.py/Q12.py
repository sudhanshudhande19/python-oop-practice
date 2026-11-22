# Q12. Build an API News Fetcher

# Concept: Requests, JSON, and exception handling

# Requirements:

    # Connect to a news API.
    # Fetch news articles.
    # Extract headlines and descriptions.
    # Display the original article links.
    # Handle API errors.

# Steps to Solve:

    # Choose a news API and read its documentation.
    # Register for an API key if required.
    # Store the endpoint and API parameters.
    # Keep the API key outside the source code.
    # Send a GET request using Requests.
    # Check the HTTP status.
    # Convert the response into JSON.
    # Extract the articles list.
    # Display title, description, and URL.
    # Handle missing data and request errors.



#----------------------------------------------------------------------------------------------------
import requests

API_KEY = "YOUR_API_KEY"

url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "apiKey": API_KEY
}

try:
    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        print("No news articles found.")

    else:
        for number, article in enumerate(articles, start=1):

            title = article.get("title") or "Title unavailable"
            description = article.get("description") or "Description unavailable"
            article_url = article.get("url") or "URL unavailable"

            print(f"\nArticle {number}")
            print("-" * 50)
            print(f"Title       : {title}")
            print(f"Description : {description}")
            print(f"URL         : {article_url}")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Internet connection problem.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")

except requests.exceptions.RequestException as error:
    print(f"Request Failed: {error}")