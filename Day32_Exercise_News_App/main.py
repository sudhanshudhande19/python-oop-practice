import requests

# Store your News API key here
API_KEY = "YOUR_API_KEY"

# News API endpoint
BASE_URL = "https://newsapi.org/v2/top-headlines"


# Function to fetch news from API
def fetch_news(keyword=None, category=None):

    # Default parameters
    params = {
        "country": "us",
        "apiKey": API_KEY
    }

    # Add category if provided
    if category:
        params["category"] = category

    # Add search keyword if provided
    if keyword:
        params["q"] = keyword

    try:
        # Send GET request with timeout
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Raise error for bad HTTP responses
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Return articles list
        return data.get("articles", [])

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Connection error. Check internet connection.")

    except requests.exceptions.HTTPError:

        if response.status_code == 401:
            print("Invalid API Key.")

        elif response.status_code == 403:
            print("Access forbidden.")

        elif response.status_code == 429:
            print("API request limit exceeded.")

        else:
            print(f"HTTP Error: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"Request Failed: {error}")

    return []


# Function to display articles
def display_articles(articles):

    # Handle empty results
    if not articles:
        print("No news articles found.")
        return

    # Loop through all articles
    for number, article in enumerate(articles, start=1):

        # Get article details safely
        title = article.get("title") or "Title unavailable"

        description = (
            article.get("description")
            or "Description unavailable"
        )

        source = (
            article.get("source", {}).get("name")
            or "Source unavailable"
        )

        date = (
            article.get("publishedAt")
            or "Date unavailable"
        )

        url = article.get("url") or "URL unavailable"

        # Display formatted article
        print("\n" + "=" * 60)
        print(f"ARTICLE {number}")
        print("=" * 60)

        print(f"Title       : {title}")
        print(f"Description : {description}")
        print(f"Source      : {source}")
        print(f"Published   : {date}")
        print(f"URL         : {url}")


# Display top headlines
def top_headlines():
    articles = fetch_news()
    display_articles(articles)


# Search news by keyword
def search_news():
    keyword = input("Enter keyword: ")
    articles = fetch_news(keyword=keyword)
    display_articles(articles)


# Display technology news
def technology_news():
    articles = fetch_news(category="technology")
    display_articles(articles)


# Display business news
def business_news():
    articles = fetch_news(category="business")
    display_articles(articles)


# Display sports news
def sports_news():
    articles = fetch_news(category="sports")
    display_articles(articles)


# Main menu function
def main():

    # Welcome Screen
    print("=" * 40)
    print("         PYTHON NEWS APP")
    print("=" * 40)

    while True:

        # Menu Options
        print("\n1. Top Headlines")
        print("2. Search News")
        print("3. Technology News")
        print("4. Business News")
        print("5. Sports News")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            top_headlines()

        elif choice == "2":
            search_news()

        elif choice == "3":
            technology_news()

        elif choice == "4":
            business_news()

        elif choice == "5":
            sports_news()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice. Try Again.")


# Start the application
main()